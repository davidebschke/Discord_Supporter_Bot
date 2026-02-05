
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from utils.load_settings import load_language
from utils.normal_messages import changing_channel_message
from utils.load_jokes import load_welcome_jokes

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
        language= await load_language()
        random_joke=await load_welcome_jokes(language)

        # The first channel you enter
        if before.channel is None and after.channel is not None:
            channel = after.channel.guild.system_channel
            if channel:
                await channel.send(embed=embedded_messages.embedded_welcome_message(member,after.channel,random_joke))
        # When changing channels
        elif before.channel is not None and after.channel is not None and before.channel != after.channel:
            await changing_channel_message(member, before, after,language)

async def setup(bot):
    # Falls dein System in einer Klasse (Cog) ist:
    await bot.add_cog(member_join_system(bot))
