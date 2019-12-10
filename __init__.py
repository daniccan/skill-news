from opsdroid.matchers import match_regex

import random
import aiohttp
import ssl
import certifi


async def get_headlines(config, query):
    base_url = "https://newsapi.org/v2/"
    api_url = "top-headlines?pageSize={}&apiKey={}".format(
        config["result-count"], config["api-key"]
    )

    if query is not None:
        api_url = "{}&q={}".format(api_url, query)

    async with aiohttp.ClientSession() as session:
        response = await session.get(
            base_url + api_url, ssl=ssl.create_default_context(cafile=certifi.where())
        )

    return await response.json()


@match_regex(
    r"what(?:\'s|s| is) the (?:news|headlines)(\s*(?:about|with|on)\s*(?P<query>.*))?",
    case_sensitive=False,
)
async def tell_weather(opsdroid, config, message):

    query = message.regex.group("query")

    headlines = await get_headlines(config, query)

    articles = headlines["articles"]
    if len(articles) != 0:
        result = ""
        for article in articles:
            url = article["url"]

            result = result + "\n" + url

        await message.respond(
            "The top {} is: {}".format(random.choice(["news", "headlines"]), result)
        )
    else:
        await message.respond("I can't seem to find any news on your query.")
