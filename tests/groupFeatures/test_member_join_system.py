import json
import unittest
from unittest.mock import AsyncMock, MagicMock, patch
import discord
import pytest
from discord.ext import commands
from groupFeatures.member_join_system import member_join_system


class test_member_join_system(unittest.IsolatedAsyncioTestCase):
    async def test_tree_sync_called(self):
        # 1. Setup: Wir bauen einen "Fake" Bot
        intents = discord.Intents.default()
        bot = commands.Bot(command_prefix="!", intents=intents)

        # 2. Wir ersetzen die echte sync-Methode durch einen Mock (Platzhalter)
        bot.tree.sync = AsyncMock(return_value=[])

        # 3. Aktion: Wir rufen die Synchronisation auf (wie in deinem on_ready)
        synced = await bot.tree.sync()

        # 4. Assert: Prüfen, ob die Methode wirklich aufgerufen wurde
        bot.tree.sync.assert_called_once()
        self.assertIsInstance(synced, list, "Sync sollte eine Liste von Commands zurückgeben")

    @pytest.mark.asyncio
    async def test_join_first_channel(self):
        # 1. Mocks für Discord-Objekte
        member = MagicMock()
        before = MagicMock()
        after = MagicMock()

        # Status: User tritt Channel bei
        before.channel = None
        after.channel = MagicMock()

        # Mock für den System-Channel, in den die Willkommensnachricht geht
        system_channel_mock = AsyncMock()
        after.channel.guild.system_channel = system_channel_mock

        # 2. Cog instanziieren
        from groupFeatures.member_join_system import member_join_system
        bot_mock = MagicMock()
        cog = member_join_system(bot_mock)

        # 3. Den Datei-Zugriff simulieren (Mocking)
        # Wir fangen die anyio-Dateizugriffe ab, damit der KeyError verschwindet
        mock_settings = json.dumps({"settings": {"language": ["de"]}})
        mock_jokes = json.dumps({"jokes": {"welcome_DE": ["Test-Witz"], "welcome_EN": ["Test-Joke"]}})

        # Wir "patchen" die open_file Funktion von anyio
        with patch("anyio.open_file") as mocked_open:
            # Wir simulieren das Lesen der Dateien
            mocked_file = AsyncMock()
            # Beim ersten Aufruf (Witze) geben wir jokes zurück, beim zweiten (Settings) settings
            mocked_file.read.side_effect = [mock_jokes, mock_settings]
            mocked_open.return_value.__aenter__.return_value = mocked_file

            # 4. Die Funktion ausführen
            await cog.on_voice_state_update(member, before, after)

        # 5. Überprüfung: Wurde eine Nachricht gesendet?
        system_channel_mock.send.assert_called()
        print("✅ Test erfolgreich: Nachricht wurde gesendet!")

    async def test_change_channel(self):
        """Test: Member wechselt von einem Channel in einen anderen"""

        member = MagicMock(spec=discord.Member)
        member.display_name = "TestUser"

        # Vorheriger Channel
        before = MagicMock()
        before.channel = MagicMock(spec=discord.VoiceChannel)
        before.channel.name = "Alt"

        # Neuer Channel
        after = MagicMock()
        after.channel = MagicMock(spec=discord.VoiceChannel)
        after.channel.name = "Neu"

        system_channel = AsyncMock()
        after.channel.guild.system_channel = system_channel

        # Ausführung
        await member_join_system.on_voice_state_update(self,member, before, after)

        # Prüfung: Die Wechsel-Nachricht sollte gesendet worden sein
        system_channel.send.assert_called_with("🔄 TestUser, ist von `Alt` zu `Neu` gewechselt.")
