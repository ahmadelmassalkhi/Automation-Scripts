import requests
from your_information import username, token

# Authenticate with the GitHub API
headers = {
    'Authorization': f'token {token}',
    'Accept': 'application/vnd.github.v3+json'
}

# Retrieve followers and following
followers_response = requests.get(f'https://api.github.com/users/{username}/followers', headers=headers)
following_response = requests.get(f'https://api.github.com/users/{username}/following', headers=headers)

# Convert JSON responses to sets of usernames
followers = set([follower['login'] for follower in followers_response.json()])
following = set([followed['login'] for followed in following_response.json()])

# Identify users who you don't follow back
users_to_follow = followers-following

# follow users who follow you
for user in users_to_follow:
    response = requests.put(f'https://api.github.com/user/following/{user}', headers=headers)
    if response.status_code == 204:
        print(f'Followed: {user}')
    else:
        print(f'Error following {user}: {response.status_code}')
