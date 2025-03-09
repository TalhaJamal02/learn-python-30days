# Understanding Asynchronous Programming:

# Unlike threading and multiprocessing, async programming lets you handle multiple tasks concurrently without creating multiple threads or processes. It’s perfect for tasks like:

# Fetching data from APIs
# Reading/writing files
# Database queries

# Key Concepts
# - async / await → Define async functions and use await for non-blocking execution.
# - asyncio → Python's built-in library for asynchronous tasks.
# - Event Loop → Manages the execution of async tasks.

# Simple Async Example: Fetching Data
import asyncio
import aiohttp
import aiofiles
import json


async def fetch_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            print(f"Data from {url}: {data}")


async def main():
    urls = [
        "https://official-joke-api.appspot.com/random_joke",
        "https://api.agify.io?name=John"
    ]
    tasks = [fetch_data(url) for url in urls]
    await asyncio.gather(*tasks)  # Runs all tasks concurrently
if __name__ == "__main__":
    asyncio.run(main())

# ^ What’s Happening?
# async def defines an asynchronous function.
# await pauses execution until the function completes.
# asyncio.gather(*tasks) runs multiple async tasks concurrently.

# Practice Task:


async def fetch_data(url):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, timeout=5) as res:
                if res.status == 200:
                    data = await res.json()
                    print(f"Data from {url} : {data}")

                    async with aiofiles.open("output.json", "a") as file:
                        await file.write(json.dumps(data, indent=2) + "\n")
                else:
                    print(f"Error: {url} returned status {res.status}")
    except asyncio.TimeoutError:
        print(f"Timeout error: {url} took too long to respond!")
    except aiohttp.ClientError as e:
        print(f"Network error: {e}")


async def main():
    urls = [
        "https://api.nationalize.io?name=Talha",
        "https://catfact.ninja/fact",
        "https://invalid-url.com"  # This will trigger an error!
    ]
    tasks = [fetch_data(url) for url in urls]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())