import discord
import datetime as dt
from discord.ext import tasks
import pytz
from os import getenv

intents = discord.Intents.default()
intents.messages = True

client = discord.Client(intents=intents)

utc = pytz.utc
aest = pytz.timezone("Australia/Sydney")
time = dt.datetime.now(aest).replace(hour=0, minute=0, second=0)
time = time.astimezone(utc).time()


async def get_channel():
    guild = await client.fetch_guild(getenv("GUILD_ID"))
    return await guild.fetch_channel(getenv("CHANNEL_ID"))


@client.event
async def on_ready():
    channel = await get_channel()
    await channel.send("Bot started")
    daily_check.start()


@tasks.loop(time=time)
async def daily_check():
    channel = await get_channel()
    await channel.send("eeee")


client.run(getenv("DISCORD_TOKEN"))
