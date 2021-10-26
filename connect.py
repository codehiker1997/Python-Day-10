import requests

API = "0f6a756cb3deccf53598b1e855c5c191"

movie_id = 500


api_version = 4
api_base_url = "https://api.themoviedb.org/{api_version}"
end_point =f'/movie/{movie_id}'

endpoint = f"{api_base_url}{end_point}?api_key={API}"
# print(endpoint)
r = requests.get(endpoint)


print(r.status_code)
print(r.text)