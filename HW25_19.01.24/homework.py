import aiohttp
import asyncio
import time

async def fetch_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def load_data(links):
    tasks = [fetch_data(url) for url in links]
    return await asyncio.gather(*tasks)

urls = ['http://www.twitch.tv'] * 100

start = time.time()
asyncio.run(load_data(urls))
end = time.time()

elapsed_time = end - start
print(elapsed_time)