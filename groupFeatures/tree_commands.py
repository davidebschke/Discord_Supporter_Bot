import json
import discord
from discord import app_commands
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)

class tree_commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="language", description="Change the Language from the bot,Wechselt die Sprache des bots")
    @app_commands.choices(language=[
        app_commands.Choice(name="Deutsch", value="de"),
        app_commands.Choice(name="English", value="en")
    ])
    async def language(self, interaction: discord.Interaction, language: app_commands.Choice[str]):

            try:
                with open('assets/settings.json', 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    data["settings"]["language"]=language.value
                    with open('assets/settings.json', 'w', encoding='utf-8') as f:
                        json.dump(data, f, indent=4, ensure_ascii=False)


                    if language.value == "de":
                        await interaction.response.send_message(f"✅ Sprache wurde in der JSON auf `['{language.value}']` aktualisiert.",ephemeral=True)
                    elif language.value == "en":
                        await interaction.response.send_message(f"✅ Language was set to in the JSON `['{language.value}']`",ephemeral=True)

            except Exception as e:
                await interaction.response.send_message(f"Fehler: {e}", ephemeral=True)
            except (json.JSONDecodeError, FileNotFoundError):
                if language.value == "de":
                    await interaction.response.send_message(f"Sprache auf {language.name} gesetzt!", ephemeral=True)
                elif language.value == "en":
                    await interaction.response.send_message(f"Language set to {language.name}!", ephemeral=True)

async def setup(bot):
    # Falls dein System in einer Klasse (Cog) ist:
    await bot.add_cog(tree_commands(bot))

