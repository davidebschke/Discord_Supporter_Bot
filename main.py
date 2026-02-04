
import discord
import os
from dotenv import load_dotenv
# WICHTIG: Importiere nur das Bot-Objekt, aber starte es noch nicht!
from groupFeatures.member_join_system import bot, DiscordToken


# Wir definieren den setup_hook direkt am bot-Objekt
async def my_setup():

    await bot.load_extension('groupFeatures.console_commands')
    await bot.load_extension('groupFeatures.member_join_system')
    print("Cogs geladen!"+ str(bot.cogs.keys()))


# Wir weisen dem Bot die Funktion zu, damit er sie VOR dem Sync ausführt
bot.setup_hook = my_setup


@bot.event
async def on_ready():
    print(f'Bot ist online als {bot.user.name}')
    try:
        # Lade die ID aus der .env (os.getenv statt load_dotenv hier)
        server_id = int(os.getenv('SERVER_ID'))
        MY_GUILD = discord.Object(id=server_id)

        # WICHTIG: Damit Befehle aus anderen Dateien erscheinen:
        bot.tree.copy_global_to(guild=MY_GUILD)
        await bot.tree.sync(guild=MY_GUILD)
    except Exception as e:
        print(f"Fehler beim Sync: {e}")


if __name__ == "__main__":
    if DiscordToken:
        bot.run(DiscordToken)
    else:
        print("FEHLER: Kein Token gefunden!")