import requests
import xml.etree.ElementTree as ET
from goose3 import Goose
import json
import os

# Initialize Goose
g = Goose()

# Output directory
OUTPUT_FILE = "24h_articles.json"

# Step 1: Fetch sitemap
sitemap_url = "https://nypost.com/news-sitemap.xml"
print(f"Fetching sitemap from: {sitemap_url}")
sitemap_response = requests.get(sitemap_url)
sitemap_response.raise_for_status()

# Step 2: Parse XML
root = ET.fromstring(sitemap_response.content)
namespace = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}

# Step 3: Extract article URLs
urls = [url.find('ns:loc', namespace).text for url in root.findall('ns:url', namespace)]
print(f"Found {len(urls)} URLs in sitemap.")

# Optional: limit for testing
urls = urls[:20]  # remove this line to crawl full list

# Step 4: Extract data from each article
def extract_article(url):
    try:
        print(f"Extracting: {url}")
        article = g.extract(url=url)

        return {
            "url": url,
            "title": article.title or "",
            "sapo": article.meta_description or "",
            "content": article.cleaned_text or "",
        }
    except Exception as e:
        print(f"❌ Error extracting {url}: {e}")
        return None

# Step 5: Collect all articles
articles = []
for url in urls:
    data = extract_article(url)
    if data:
        articles.append(data)

# Step 6: Save to JSON
os.makedirs("scraped_data", exist_ok=True)
with open(f"scraped_data/{OUTPUT_FILE}", "w", encoding="utf-8") as f:
    json.dump(articles, f, ensure_ascii=False, indent=2)

print(f"\n✅ Done. Saved {len(articles)} articles to scraped_data/{OUTPUT_FILE}")
