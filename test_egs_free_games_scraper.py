import json
import pytest
from egs_free_games_scraper import EpicGamesStoreScraper

def test_valid_json():
	'''
	Validation test for JSON value
	'''
	try:
		json.loads(EpicGamesStoreScraper().get_free_games_json())
	except json.JSONDecodeError as e:
		pytest.fail(f'JSON is invalid. Error: {e}')
	except Exception as e:
		pytest.fail(f'The program is invalid. Error: {e}')
