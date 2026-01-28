import unittest

import unittest
from unittest.mock import MagicMock
import discord
import datetime

from utils import embedded_messages

class TestWelcomeEmbed(unittest.TestCase):

    def test_embedded_welcome_message_content(self):
        # 1. Setup: Fake-Objekte erstellen
        mock_member = MagicMock()
        mock_member.__str__.return_value = "TestUser#1234"

        mock_channel = MagicMock()
        mock_channel.__str__.return_value = "Lounge"

        test_msg = "ist gerade gelandet!"

        # 2. Aktion: Funktion ausführen
        embed = embedded_messages.embedded_welcome_message(mock_member, mock_channel, test_msg)

        # 3. Assert: Prüfen, ob alles stimmt
        self.assertIsInstance(embed, discord.Embed)

        # Prüfen, ob der Titel den User und Channel enthält
        expected_title = "TestUser#1234 hat gerade den Channel Lounge betreten"
        self.assertEqual(embed.title, expected_title)

        # Prüfen, ob die Beschreibung korrekt zusammengebaut wurde
        expected_desc = "TestUser#1234 ist gerade gelandet!"
        self.assertEqual(embed.description, expected_desc)

        # Prüfen, ob die Farbe stimmt
        self.assertEqual(embed.color, discord.Color.brand_green())


if __name__ == '__main__':
    unittest.main()
