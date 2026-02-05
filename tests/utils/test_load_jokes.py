import pytest
import json
from unittest.mock import patch, MagicMock, AsyncMock
from utils.load_jokes import load_welcome_jokes  # Pfad anpassen

class Test_loadJokes():
    def test_load_welcome_jokes(self):


        @pytest.mark.asyncio
        async def test_load_welcome_jokes_success():
            # 1. Fake-Daten vorbereiten
            fake_data = {
                "jokes": {
                    "welcome_DE": ["Ein deutscher Witz"],
                    "welcome_EN": ["An english joke"]
                }
            }
            fake_json = json.dumps(fake_data)

            # 2. Mocks für os.path und anyio setzen
            # Wir tun so, als ob die Datei existiert und geben den fake_json Inhalt zurück
            with patch("os.path.exists", return_value=True), \
                    patch("anyio.open_file", new_callable=AsyncMock) as mocked_open:
                # anyio Dateihandling simulieren
                mock_file = MagicMock()
                mock_file.read = AsyncMock(return_value=fake_json)

                # Das 'async with' Konstrukt simulieren
                mocked_open.return_value.__aenter__.return_value = mock_file

                # 3. Funktion aufrufen (Deutsch)
                joke_de = await load_welcome_jokes("de")
                assert joke_de == "Ein deutscher Witz"

                # 4. Funktion aufrufen (Englisch)
                joke_en = await load_welcome_jokes("en")
                assert joke_en == "An english joke"

        @pytest.mark.asyncio
        async def test_load_welcome_jokes_no_file():
            """Testet das Verhalten, wenn die Datei fehlt"""
            with patch("os.path.exists", return_value=False):
                joke = await load_welcome_jokes("de")
                assert joke is None