import requests

username = input ("Github uername:")

url = f"https://api.github.com/users/1{username}"

data = requests.get(url).json()

print(f"Name: {data.get('name')}")
print(f"Public Repos: {data.get('public_repos')}")
print(f"Followers: {data.get('followers')}")
