import datetime
import discord

def embedded_welcome_message(welcome_member,channel,description_message):
    """
    Creates an embedded welcome message for the Discord channel

    Args:
        welcome_member: The member to be welcomed
        channel: The channel that was entered
        description_message: The description message

    Returns: Returns an embedded message from Discord.

    """
    embed = discord.Embed(
        title=str(welcome_member) +" hat gerade den Channel "+ str(channel)+" betreten",
        description=str(welcome_member)+" "+str(description_message),
        color=discord.Color.brand_green()
    )
    embed.timestamp=datetime.datetime.now(datetime.timezone.utc)
    return embed
