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
