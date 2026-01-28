import datetime
import discord

def embedded_welcome_message(welcome_member,channel,description_message):
    embed = discord.Embed(
        title=str(welcome_member) +" hat gerade den Channel "+ str(channel)+" betreten",
        description=str(welcome_member)+" "+description_message,
        color=discord.Color.brand_green()
    )
    embed.timestamp=datetime.datetime.now(datetime.timezone.utc)
    return embed