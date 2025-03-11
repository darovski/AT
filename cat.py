import requests


def get_random_cat_image():
    """
    Получает URL случайного изображения кошки с TheCatAPI.

    Возвращает:
        str: URL изображения или None в случае ошибки.
    """
    url = "https://api.thecatapi.com/v1/images/search"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Проверка на HTTP-ошибки

        data = response.json()
        if data and isinstance(data, list):
            return data[0]['url']

    except (requests.ConnectionError, requests.Timeout) as e:
        print(f"Ошибка соединения: {e}")
    except requests.RequestException as e:
        print(f"Ошибка запроса: {e}")

    return None


# Пример использования
image_url = get_random_cat_image()
if image_url:
    print(f"Ссылка на котика: {image_url}")
else:
    print("Не удалось получить изображение")