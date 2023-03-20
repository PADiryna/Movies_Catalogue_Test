import pytest
import tmdb_client
import requests
from unittest.mock import Mock


def test_get_poster_url_uses_default_size():
   # Підготовка даних
   poster_api_path = "some-poster-path"
   expected_default_size = 'w342'
   # Виклик коду, який ми тестуємо
   poster_url = tmdb_client.get_poster_url(poster_api_path=poster_api_path)
   # Порівняння результатів
   assert expected_default_size in poster_url


def test_get_movies_list_type_popular():
   movies_list = tmdb_client.get_movies_list(list_type="popular")
   assert movies_list is not None


def test_get_single_movie():
   single_movie = tmdb_client.get_single_movie(1077280)
   assert single_movie is not None


def test_get_single_movie_cast():
   single_movie_cast = tmdb_client.get_single_movie_cast(1077280)
   assert single_movie_cast is not None


def test_get_movies_list(monkeypatch):
   # Список, який поверне прихований "запит до API".
   mock_movies_list = ['Movie 1', 'Movie 2']

   requests_mock = Mock()
   # Результат запиту до API
   response = requests_mock.return_value
   # Ми перевизначаємо результат виклику методу json().
   response.json.return_value = mock_movies_list
   monkeypatch.setattr("tmdb_client.requests.get", requests_mock)

   movies_list = tmdb_client.get_movies_list(list_type="popular")
   assert movies_list == mock_movies_list


def test_get_single_movie_mock(monkeypatch):
   mock_single_movie = ['Movie 1']
   requests_mock = Mock()
   response = requests_mock.return_value
   response.json.return_value = mock_single_movie
   monkeypatch.setattr("tmdb_client.requests.get", requests_mock)
   movies_list = tmdb_client.get_single_movie(1077280)
   assert movies_list == mock_single_movie


def call_tmdb_api(endpoint):
   full_url = f"https://api.themoviedb.org/3/{endpoint}"
   headers = {
       "Authorization": f"Bearer {API_TOKEN}"
   }
   response = requests.get(full_url, headers=headers)
   response.raise_for_status()
   return response.json()

def get_movies_list(list_type):
   return call_tmdb_api(f"movie/{list_type}")