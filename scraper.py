import requests
from bs4 import BeautifulSoup

def scrape_article(url):
    try:
        print("⏳ Fetching URL...")
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers)
        print(f"✅ Status Code: {response.status_code}")

        if response.status_code != 200:
            return f"Failed to load page: {response.status_code}"

        soup = BeautifulSoup(response.content, 'html.parser')
        print("🔍 Extracting paragraphs...")
        paragraphs = soup.find_all('p')

        if not paragraphs:
            return "❌ No paragraphs found. The website layout may be different."

        article_text = '\n'.join([p.get_text() for p in paragraphs])
        return article_text

    except Exception as e:
        return f"🚨 Error: {e}"

if __name__ == "__main__":
    test_url = "https://www.coindesk.com/markets/2025/07/16/xrp-prints-bullish-reversal-volume-confirms-recovery-toward-3"

    print("🚀 Starting scraper...\n")
    article = scrape_article(test_url)
    print("\n📄 Article Output:\n")
    print(article[:2000])  # Print first 2000 characters
    print("\n✅ Done.")
