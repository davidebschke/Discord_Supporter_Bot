import json
from unittest.mock import patch, MagicMock, AsyncMock

import pytest

from utils.load_settings import load_language


class Test_load_settings:

    @pytest.mark.asyncio
    async def test_load_language_success(self):


        """Prüft, ob die Sprache korrekt aus der JSON extrahiert wird"""
        # 1. Fake-JSON-Struktur vorbereiten
        fake_settings = {
            "settings": {
                "language": "en"
            }
        }
        fake_json_content = json.dumps(fake_settings)

        # 2. Mocking von anyio.open_file
        with patch("anyio.open_file", new_callable=AsyncMock) as mocked_open:
            # Wir simulieren das Dateiobjekt, das zurückgegeben wird
            mock_file = MagicMock()
            # .read() muss ein Awaitable sein, daher AsyncMock
            mock_file.read = AsyncMock(return_value=fake_json_content)

            # Das 'async with' Handling (Context Manager)
            mocked_open.return_value.__aenter__.return_value = mock_file

            # 3. Funktion ausführen
            result = await load_language()

            # 4. Überprüfung
            assert result == "en"
            assert isinstance(result, str)

    @pytest.mark.asyncio
    async def test_load_language_key_error(self):
            """Prüft das Verhalten bei einer fehlerhaften JSON-Struktur"""
            invalid_json = json.dumps({"wrong_key": "empty"})

            with patch("anyio.open_file", new_callable=AsyncMock) as mocked_open:
                mock_file = MagicMock()
                mock_file.read = AsyncMock(return_value=invalid_json)
                mocked_open.return_value.__aenter__.return_value = mock_file

                # Hier erwarten wir einen KeyError, da 'settings' fehlt
                with pytest.raises(KeyError):
                    await load_language()