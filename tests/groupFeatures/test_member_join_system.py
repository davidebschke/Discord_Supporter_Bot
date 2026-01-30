import json
import unittest
from unittest.mock import AsyncMock, MagicMock, patch
import discord
from discord.ext import commands
from groupFeatures.member_join_system import on_voice_state_update


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

    async def test_join_first_channel(mock_print):
        """Test: Member betritt zum ersten Mal einen Channel (before.channel is None)"""

        # 1. Setup Mocks
        member = MagicMock(spec=discord.Member)
        member.display_name = "TestUser"

        before = MagicMock()
        before.channel = None  # Er war vorher in keinem Channel

        after = MagicMock()
        after.channel = MagicMock(spec=discord.VoiceChannel)
        after.channel.name = "Lounge"

        # System Channel simulieren, an den die Nachricht geht
        system_channel = AsyncMock()
        after.channel.guild.system_channel = system_channel

        # 2. Ausführung
        # Vorbereitung der Mock-Daten
        mock_data = {"jokes": {"welcome": ["Witz"]}}
        mock_content = json.dumps(mock_data)

        # Der Test-Block
        with patch('os.path.exists', return_value=True), \
                patch('anyio.open_file', new_callable=AsyncMock) as mock_anyio_open, \
                patch('utils.embedded_messages.embedded_welcome_message', return_value=discord.Embed(title="Test")):
            # Wir erstellen einen asynchronen Context Manager Mock für das File-Objekt
            mock_file = AsyncMock()
            mock_file.read.return_value = mock_content
            mock_anyio_open.return_value.__aenter__.return_value = mock_file

            await on_voice_state_update(member, before, after)



        system_channel.send.assert_called_once()


        # 3. Prüfung (Assertion)
        system_channel.send.assert_called_once()  # Wurde eine Nachricht gesendet?

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
        await on_voice_state_update(member, before, after)

        # Prüfung: Die Wechsel-Nachricht sollte gesendet worden sein
        system_channel.send.assert_called_with("🔄 TestUser, ist von `Alt` zu `Neu` gewechselt.")
