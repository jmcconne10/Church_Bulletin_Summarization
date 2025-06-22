# 📰 Church Bulletin Summarization

This project automatically downloads a weekly church bulletin (in PDF form), extracts the text, summarizes it using OpenAI, and emails the summary to a specified address. The script is written in Python and is ideal for automation via `cron` or other schedulers.

---

## 💡 Features

- Downloads the bulletin PDF from a URL that changes weekly
- Extracts readable text from the PDF
- Sends the content to OpenAI for summarization using a custom prompt
- Emails the summary with a link to the original PDF
- Easy to configure and extend

---

## 🔁 How It Works

```mermaid
graph TD
    A[Start Script] --> B[Construct PDF URL based on date]
    B --> C[Download PDF]
    C --> D[Extract Text using PyMuPDF]
    D --> E[Load Prompt from prompt.txt]
    E --> F[Call OpenAI API to summarize]
    F --> G[Append PDF URL to summary]
    G --> H[Send summary via email]
    H --> I[Done ✅]
```  <-- ✅ This closes the mermaid block!
## 🛠 Setup Instructions

Follow these steps to configure and run the Church Bulletin Summarization script.

```markdown
### 1. Install Dependencies

Make sure you have Python 3.7 or higher installed.

Create and activate a virtual environment (optional but recommended):

    python -m venv .venv
    source .venv/bin/activate  # On Windows use: .venv\Scripts\activate

Install the required libraries:

    pip install -r requirements.txt

---

### 2. Create the `.env` File

In the project root (where `fetch_and_summarize.py` lives), create a file named `.env`.

Add the following variables:

    EMAIL_USER=youremail@gmail.com
    EMAIL_TO=recipient@gmail.com
    EMAIL_PASSWORD=your_16_char_gmail_app_password
    OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    PDF_BASE_URL=https://container.parishesonline.com/bulletins/05/4108/

#### Variable Descriptions:
- `EMAIL_USER`: Your Gmail address used to send the summary  
- `EMAIL_TO`: Address to receive the summary  
- `EMAIL_PASSWORD`: Your [Gmail App Password](https://support.google.com/mail/answer/185833)  
- `OPENAI_API_KEY`: Your OpenAI API key  
- `PDF_BASE_URL`: Base URL to the bulletin location (excluding the date)

---

### 3. Customize Your Prompt

Open `prompt.txt` in the project root. Write instructions that tell the AI how to summarize the bulletin.

Example:

    Please summarize this church bulletin focusing on:
    - Upcoming events
    - Volunteer opportunities
    - Prayer requests and Mass intentions
    - Youth and adult education programs

---

### 4. Run the Script

With everything configured, run:

    python fetch_and_summarize.py

The script will:
- Download the bulletin for today’s date
- Extract text from the PDF
- Summarize the contents using OpenAI
- Send the summary to your configured email

---

### ✅ Done!

You’re now ready to use and automate the bulletin summarization process.
