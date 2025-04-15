import asyncio
from crawl4ai import AsyncWebCrawler

async def main():
    async with AsyncWebCrawler() as crawler:
        url = "https://example.com"
        res = await crawler.arun(url)

        print(res.markdown)
    
asyncio.run(main())
