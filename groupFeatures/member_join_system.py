import json
import os
import random
import anyio
import discord
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv
from utils import embedded_messages

intents = discord.Intents.default()
intents.members = True
intents.voice_states = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)
load_dotenv()
DiscordToken=os.getenv('DISCORD_BOT_TOKEN')

class member_join_system(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @bot.event
    async def on_ready(self):
        """

        Returns:

        """
        print(f'Bot ist online als {bot.user.name}')
        try:
            synced = await bot.tree.sync(guild=discord.Object(id=os.getenv('SERVER_ID')))
            print(f"Synchronisiert: {len(synced)} Befehle.")
        except Exception as e:
            print(f"Fehler beim Sync: {e}")


    @bot.event
    async def on_voice_state_update(self,member, before, after):
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
            async with await anyio.open_file('assets/settings.json', 'r', encoding='utf-8') as f:
                content = await f.read()
                language_file = json.loads(content)
                language_data = language_file['settings']['language']
                local_server_language=language_data
            if local_server_language == "de":
                random_joke = random.choice(data_welcome_jokes['jokes']['welcome_DE'])
            else:
                random_joke = random.choice(data_welcome_jokes['jokes']['welcome_EN'])

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
            if local_server_language == "de":
                await channel.send(f"🔄 {member.display_name}, ist von `{before.channel.name}` zu `{after.channel.name}` gewechselt.")
            elif local_server_language == "en":
                await channel.send(
                    f"🔄 The User: {member.display_name} has switched from `{before.channel.name}` to `{after.channel.name}`")

async def setup(bot):
    # Falls dein System in einer Klasse (Cog) ist:
    await bot.add_cog(member_join_system(bot))


    # Falls es nur Funktionen sind, reicht der Import oben in der main.
    pass