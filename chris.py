import sys
print(sys.version)
import discord
import asyncio
import random

client = discord.Client()

async def background_loop():
    await client.wait_until_ready()
    while not client.is_closed:
        channel = client.get_channel("260599782676889602")
        messages = ["Hello!", "How are you doing?", "Howdy!"]
        await client.send_message(channel, random.choice(messages))
        await asyncio.sleep(120)

client.loop.create_task(background_loop())
client.run("NDQ3NTE4ODA2OTAzMDk1MzA2.DeIwMQ.U0miI1ljr3xffWDwKGGYqWV2ERM")
