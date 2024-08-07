from utils.utils import *
from utils.dcview import *
from utils.loggg import *
import os

import json
import functools
import typing
import asyncio



import os

from utils.dcdb import * 



def to_thread(func: typing.Callable) -> typing.Coroutine:
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        return await asyncio.to_thread(func, *args, **kwargs)
    return wrapper



command_data = {
    'name': 'blog',
    'description': 'chat with any blog'
}

async def discuss(message, url,bot=None):
    query = message.content
    text = get_content_url(url,stored=True)
    answer,all_answer = await blog_retrieve(query,text,bot=bot)
    await send_long_message(message.channel,answer)
    await message.channel.send(view=blog_view(answer))

async def execute(message, bot, debug=False):
    url = message.content.split(" ")[1]
    if debug:
        logger.info(f"Blog query {url}")
    if url == "l":
        urls = get_all_urls()
        print(urls)
        answer = ""
        for i in range(len(urls)):
            answer += f"{i}. {urls[i]}\n" 
        chunk_size = 2000
        chunks = [answer[i:i + chunk_size] for i in range(0, len(answer), chunk_size)]
        for chunk in chunks:
            await message.channel.send(chunk, reference=message)
        return
    

    elif url[0] == "i":
        urls = get_all_urls()
        print(urls)
        url = urls[int(url[1:])]
    
    else:
        url = extract_urls(message.content)[0]

    logger.info(f"DEBUG: URL: {url}")
    text = get_content_url(url, stored=True)
    try:
        # logger.info(f"DEBUG: text: {text}")
        if text:
            query = " ".join(message.content.split(" ")[2:])
            logger.info(f"DEBUG: Blog query {url} {query}")
            thread = await message.create_thread(name=url[:60])
            logger.info(f"DEBUG: Thread created {url}")
            if query == "full":
                answer = text
            else:
                if len(query.strip()) == 0:
                    query = "Summary the content and  after summarizing, please also suggest appropriate hashtags (less than 6) that would help in categorizing and highlighting the key topics discussed in the blog."
                answer,all_answer = await blog_retrieve(query,text,bot=bot)
                
            print(url + " " + query)
    
            insert_thread_to_db(thread.id, 1, url, message)
            await send_long_message(thread, answer)
            await thread.send(view=blog_view(answer))
        else:
            await send_long_message(thread, "No content found for this url")
    except Exception as e:
        logger.error("An error occurred at execute func: {}".format(e))
        raise e
