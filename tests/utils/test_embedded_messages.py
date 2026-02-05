from unittest.mock import MagicMock
import discord
import pytest

from utils.embedded_messages import embedded_welcome_message


class Test_embedded_welcome_messages:

    @pytest.fixture
    def mock_member(self):
        """Erstellt einen sauberen Member-Mock für jeden Test"""
        member = MagicMock(spec=discord.Member)
        member.__str__.return_value = "David#1234"
        return member

    @pytest.fixture
    def mock_channel(self):
        """Erstellt einen sauberen Channel-Mock"""
        channel = MagicMock(spec=discord.TextChannel)
        channel.__str__.return_value = "lobby"
        return channel

    def test_title_formatting(self, mock_member, mock_channel):
        """Prüft, ob der Titel die Namen korrekt kombiniert"""
        embed = embedded_welcome_message(mock_member, mock_channel, "Hi!")
        expected = "David#1234 hat gerade den Channel lobby betreten"
        assert embed.title == expected

    def test_embed_color_is_green(self, mock_member, mock_channel):
        """Stellt sicher, dass die Farbe immer Brand-Green ist"""
        embed = embedded_welcome_message(mock_member, mock_channel, "Hi!")
        assert embed.color == discord.Color.brand_green()

    def test_description_content(self, mock_member, mock_channel):
        """Prüft, ob die Beschreibung den Member und die Nachricht enthält"""
        msg = "willkommen im Team!"
        embed = embedded_welcome_message(mock_member, mock_channel, msg)
        assert "David#1234" in embed.description
        assert msg in embed.description
