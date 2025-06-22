import os
import requests
import datetime
import smtplib
import fitz  # PyMuPDF
from email.message import EmailMessage
from dotenv import load_dotenv
from openai import OpenAI
from pathlib import Path

# Load environment variables
load_dotenv()

# Configuration
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_TO = os.getenv("EMAIL_TO")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")   # App password from .env
OPENAI_KEY = os.getenv("OPENAI_API_KEY")       # OpenAI API Key from .env
URL = os.getenv("URL")
OPENAI_MODEL = "gpt-4"

# Get current date (use fixed date for testing)
today = datetime.date.today()
date_str = today.strftime("%Y%m%d")
pdf_url = f"{URL}{date_str}B.pdf"
pdf_path = Path(f"bulletin_{date_str}.pdf")

# Step 1: Download the bulletin
print(f"📥 Downloading bulletin from: {pdf_url}")
response = requests.get(pdf_url)
if response.status_code != 200:
    raise Exception(f"❌ Failed to download PDF: Status code {response.status_code}")
with open(pdf_path, "wb") as f:
    f.write(response.content)
print(f"✅ PDF saved to {pdf_path}")

# Step 2: Extract text using PyMuPDF
print("🔍 Extracting text from PDF...")
doc = fitz.open(pdf_path)
full_text = "\n".join(page.get_text() for page in doc)
doc.close()

# Step 3: Load your custom prompt
with open("prompt.txt", "r", encoding="utf-8") as f:
    prompt = f.read()

# Step 4: Send to OpenAI for summarization
print("🤖 Generating summary with OpenAI...")
client = OpenAI(api_key=OPENAI_KEY)
response = client.chat.completions.create(
    model=OPENAI_MODEL,
    messages=[
        {"role": "system", "content": prompt},
        {"role": "user", "content": full_text}
    ]
)
summary = response.choices[0].message.content.strip()

summary += f"\n\n📎 Bulletin PDF: {pdf_url}"     # Add in the link to the pdf at the bottom of the message

# Step 5: Send summary via email
print("📧 Sending summary via email...")
msg = EmailMessage()
msg["Subject"] = f"📜 Church Bulletin Summary – {today.strftime('%B %d, %Y')}"
msg["From"] = EMAIL_USER
msg["To"] = EMAIL_TO
msg.set_content(summary)

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.starttls()
    smtp.login(EMAIL_USER, EMAIL_PASSWORD)
    smtp.send_message(msg)

print("✅ Summary emailed successfully.")
