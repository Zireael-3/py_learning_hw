from hw4.hw4_tasks.task02 import count_dots_on_i
import pytest


from unittest.mock import MagicMock, patch


def test_count_dots_on_i_network_error():
    with patch('requests.get') as mock_get:
        mock_get.side_effect = ValueError("Unreachable https://example.com/")
        with pytest.raises(ValueError):
            count_dots_on_i('https://example.com/')
        mock_get.assert_called_once_with('https://example.com/')


def test_count_dots_on_i():
    with patch('requests.get') as mock_get:
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = 'This is a test string'
        mock_get.return_value = mock_response
        assert count_dots_on_i('https://example.com/') == 3
        mock_get.assert_called_once_with('https://example.com/')
