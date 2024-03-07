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

# Identify users who don't follow you back
users_to_unfollow = following - followers

# Unfollow users who don't follow you back
for user in users_to_unfollow:
    response = requests.delete(f'https://api.github.com/user/following/{user}', headers=headers)
    if response.status_code == 204:
        print(f'Unfollowed: {user}')
    else:
        print(f'Error unfollowing {user}: {response.status_code}')
