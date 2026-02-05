
from discord.ext import commands
import pytest
import discord
import discord.ext.test as dpytest
from unittest.mock import patch, mock_open, MagicMock, AsyncMock
from groupFeatures.tree_commands import tree_commands

@pytest.mark.asyncio
class Test_tree_commands:
    @pytest.mark.asyncio
    async def test_language_command_success(self):
        # 1. Bot & Cog Setup
        intents = discord.Intents.default()
        intents.message_content = True
        bot = commands.Bot(command_prefix='$', intents=intents)

        cog = tree_commands(bot)
        await bot.add_cog(cog)
        dpytest.configure(bot)

        fake_json_data = '{"settings": {"language": "en"}}'

        with patch("builtins.open", mock_open(read_data=fake_json_data)) as mocked_file:

            choice = discord.app_commands.Choice(name="Deutsch", value="de")

            mock_interaction = MagicMock(spec=discord.Interaction)
            mock_interaction.response = MagicMock()
            mock_interaction.response.send_message = AsyncMock()

            await cog.language.callback(cog, mock_interaction, choice)

            # 4. Überprüfen (Assertions)
            # Wurde die richtige Nachricht gesendet?
            args, kwargs = mock_interaction.response.send_message.call_args
            assert "Sprache wurde in der JSON auf `['de']` aktualisiert" in args[0]
            assert kwargs["ephemeral"] is True

            # Wurde die Datei theoretisch geschrieben?
            assert mocked_file.call_count >= 2  # Einmal lesen, einmal schreiben

