import aiohttp
import asyncio


def get_jobs(session, postal_code):
    url = "https://api.zippopotam.us/ca/{}"
    jobs = []
    for tag in postal_code:
        jobs.append(asyncio.create_task(session.get(url.format(tag), ssl=False)))
    return jobs


async def async_api_call(postal_code):
    data = []
    async with aiohttp.ClientSession() as session:
        jobs = get_jobs(session, postal_code)
        responses = await asyncio.gather(*jobs)
        for response in responses:
            data.append(await response.json())
        return data
