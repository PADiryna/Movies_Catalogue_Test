import requests
import json

API_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmYWI2MDlhOTkwMTFkMmE1MzAxYjY5ZjVlODY0NjZiYyIsInN1YiI6IjYzZmJmMDY5ODRmMjQ5MDBhOTQxZjI2NSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.ed_rAlbtavSLRvYBlFpfIdzrqLCH3SaujU_s_AKazYc"
api_key = "fab609a99011d2a5301b69f5e86466bc"


def get_popular_movies(how_many,list_type):
    endpoint = "https://api.themoviedb.org/3/movie/{list_type}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()


def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"


def get_movies(how_many, list_type):
    data = get_popular_movies(list_type)
    return data["results"][:how_many]


def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()


def get_single_movie_cast(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()["cast"]


def get_movie_images(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/images"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()


def get_movies_list(list_type):
    endpoint = f"https://api.themoviedb.org/3/movie/{list_type}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    return response.json()


def search(search_query):
   base_url = "https://api.themoviedb.org/3/"
   headers = {
       "Authorization": f"Bearer {API_TOKEN}"
   }
   endpoint = f"{base_url}search/movie/?query={search_query}"

   response = requests.get(endpoint, headers=headers)
   response = response.json()
   return response['results']


def get_airing_today():
    endpoint = f"https://api.themoviedb.org/3/tv/airing_today"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    response = response.json()
    return response['results']
