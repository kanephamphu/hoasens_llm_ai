import json

with open("scraped_data/24h_articles.json", encoding="utf-8") as f:
    articles = json.load(f)

with open("news_dataset.jsonl", "w", encoding="utf-8") as out:
    for art in articles:
        if not art["content"].strip():
            continue
        prompt = f"title: {art['title']}\n\ncontent: {art['content']}"
        json.dump({"text": prompt}, out, ensure_ascii=False)
        out.write("\n")
