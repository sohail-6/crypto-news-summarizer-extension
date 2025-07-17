from transformers import pipeline
import requests
from bs4 import BeautifulSoup
import torch

# Set device
device = 0 if torch.cuda.is_available() else -1
print(f"Device set to use {'cuda' if device == 0 else 'cpu'}")

# Load summarization pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn", device=device)

# Article URL
url = "https://www.coindesk.com/markets/2025/07/16/xrp-prints-bullish-reversal-volume-confirms-recovery-toward-3"

# Scrape article
print("📰 Scraping article...")
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}
response = requests.get(url, headers=headers)
if response.status_code != 200:
    print(f"❌ Failed to load page: {response.status_code}")
    exit()


soup = BeautifulSoup(response.content, "html.parser")
paragraphs = soup.find_all("p")
article_text = "\n".join([p.get_text() for p in paragraphs])

# Clean long text (limited tokens for BART)
if len(article_text.split()) > 1024:
    article_text = " ".join(article_text.split()[:1024])

# Summarize
print("\n🔎 Summary:\n")
summary = summarizer(article_text, max_length=130, min_length=30, do_sample=False)
print(summary[0]['summary_text'])
