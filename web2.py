import asyncio
from crawlee import PuppeteerCrawler

async def main():
    crawler = PuppeteerCrawler()

    @crawler.request_handler
    async def handle_request(context):
        await context.dataset.push_data({
            'url': context.request.url,
            'title': await context.page.title(),
        })
        await context.enqueue_links()

    await crawler.run(["https://crawlee.dev"])