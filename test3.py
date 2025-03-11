import pytest
import requests
from cat import get_random_cat_image  # замените your_module на имя вашего файла


def test_successful_request(requests_mock):
    # Мокируем успешный ответ API
    mock_url = "https://example.com/cat.jpg"
    requests_mock.get(
        "https://api.thecatapi.com/v1/images/search",
        json=[{"url": mock_url}],
        status_code=200
    )

    result = get_random_cat_image()
    assert result == mock_url


def test_failed_request(requests_mock):
    # Мокируем ответ с ошибкой 404
    requests_mock.get(
        "https://api.thecatapi.com/v1/images/search",
        status_code=404
    )

    result = get_random_cat_image()
    assert result is None


def test_connection_error(requests_mock):
    # Мокируем ошибку соединения
    requests_mock.get(
        "https://api.thecatapi.com/v1/images/search",
        exc=requests.ConnectionError
    )

    result = get_random_cat_image()
    assert result is None


def test_invalid_response_format(requests_mock):
    # Мокируем некорректный формат ответа
    requests_mock.get(
        "https://api.thecatapi.com/v1/images/search",
        json={"invalid": "format"},
        status_code=200
    )

    result = get_random_cat_image()
    assert result is None