import datetime
import discord

def embedded_welcome_message(welcome_member,channel):
    embed = discord.Embed(
        title=str(welcome_member) +" hat gerade den Channel "+ str(channel)+" betreten",
        color=discord.Color.blue()
    )
    embed.timestamp=datetime.datetime.now(datetime.timezone.utc)
    return embed