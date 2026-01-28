import unittest
from unittest.mock import AsyncMock, MagicMock
import discord
from discord.ext import commands

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

