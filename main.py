import discord
from os import getenv

intents = discord.Intents.default()
intents.messages = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    guild = await client.fetch_guild(getenv("GUILD_ID"))
    channel = await guild.fetch_channel(getenv("CHANNEL_ID"))
    await channel.send("Bot started")


client.run(getenv("DISCORD_TOKEN"))
