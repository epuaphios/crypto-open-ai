import unittest
import pytest
import requests
import datetime
# import requests_mock
from unittest.mock import patch, MagicMock
import matplotlib.pyplot as plt
from modules.historical_getter import get_historical_data
from modules.current_price import get_current_price
from rich.console import Console
from modules.option import user_option


class TestFunctionExistence(unittest.TestCase):
    def test_get_prices_exists(self):
        # Assert that the function exists
        self.assertTrue(callable(get_current_price))

def test_get_historical_data():
    product_id = "SOL-USD"
    api_url = "https://api.pro.coinbase.com/products"
    start_date = datetime.datetime(2023, 7, 1)
    end_date = datetime.datetime(2023, 7, 10)

    # Mock the requests library response
    expected_data = [{"timestamp": 1640995200, "open": 35000, "high": 36000, "low": 34000, "close": 35500}]
    with patch("modules.historical_getter.requests.get") as mock_get:
        mock_get.return_value.json.return_value = expected_data

        # Call the function
        data = get_historical_data(product_id, api_url, start_date, end_date)

    # Check the result
    assert data == expected_data


