import json
import os
import random

import anyio
import discord
from discord.ext import commands
from dotenv import load_dotenv

from utils import embedded_messages

intents = discord.Intents.default()
intents.members = True       # Um zu sehen, wer dem Server beitritt
intents.voice_states = True  # Um zu sehen, wer in den Voice-Channel geht
intents.message_content = True



bot = commands.Bot(command_prefix="!", intents=intents)
load_dotenv()
DiscordToken=os.getenv('DISCORD_BOT_TOKEN')


@bot.event
async def on_ready():
    """

    Returns:

    """
    print(f'Bot ist online als {bot.user.name}')
    await bot.tree.sync()


@bot.event
async def on_voice_state_update(member, before, after):
    """

    This checks whether the member is changing channels
    or joining a new one. In addition, a joke is displayed when a new member joins.

    Args:
        member: The Channel Member
        before: The previous channel
        after: The future channel

    Returns: None

    """
    if os.path.exists('assets/welcome_jokes.json'):
        async with await anyio.open_file('assets/welcome_jokes.json', 'r', encoding='utf-8') as file:
            content = await file.read()
            data_welcome_jokes = json.loads(content)
        random_joke = random.choice(data_welcome_jokes['jokes']['welcome'])
    else:
        random_joke = None
        print("der pfad existiert nicht")
    # The first channel you enter
    if before.channel is None and after.channel is not None:
        channel = after.channel.guild.system_channel
        if channel:
            await channel.send(embed=embedded_messages.embedded_welcome_message(member,after.channel,random_joke))

    # When changing channels
    elif before.channel is not None and after.channel is not None and before.channel != after.channel:
        channel = after.channel.guild.system_channel
        await channel.send(f"🔄 {member.display_name}, ist von `{before.channel.name}` zu `{after.channel.name}` gewechselt.")



