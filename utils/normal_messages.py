
async def changing_channel_message(changingmember, before_channel, after_channel,language):
    channel = after_channel.channel.guild.system_channel
    if language == "de":
        await channel.send(
            f"{changingmember.display_name}, ist von `{before_channel.channel.name}` zu `{after_channel.channel.name}` gewechselt.")
    elif language == "en":
        await channel.send(
            f"The User: {changingmember.display_name} has switched from `{before_channel.channel.name}` to `{after_channel.channel.name}`")


