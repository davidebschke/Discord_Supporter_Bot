import os

import discord
from discord.ext import commands
from dotenv import load_dotenv
from utils import embeddedMessages

intents = discord.Intents.default()
intents.members = True       # Um zu sehen, wer dem Server beitritt
intents.voice_states = True  # Um zu sehen, wer in den Voice-Channel geht
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)
load_dotenv()
DiscordToken=os.getenv('DISCORD_BOT_TOKEN')

@bot.event
async def on_ready():
    print(f'Bot ist online als {bot.user.name}')
    await bot.tree.sync()


@bot.event
async def on_voice_state_update(member, before, after):


   # The first channel you enter
    if before.channel is None and after.channel is not None:
        channel = after.channel.guild.system_channel
        if channel:
            await channel.send(embed=embeddedMessages.embedded_welcome_message(member,after.channel))

    # When changing channels
    elif before.channel is not None and after.channel is not None and before.channel != after.channel:
        channel = after.channel.guild.system_channel
        await channel.send(f"🔄 {member.display_name}, ist von `{before.channel.name}` zu `{after.channel.name}` gewechselt.")
        print(f"Log: {member.name} hat gewechselt.")

# --- 3. START ---
if __name__ == "__main__":
   if DiscordToken:
       bot.run(DiscordToken)
   else:
       print("FEHLER: Kein Token in der .env Datei gefunden!")
