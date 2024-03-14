import requests
from your_information import username, token

def get_all_pages(url, headers):
    data = []
    while url:
        response = requests.get(url, headers=headers)
        response_data = response.json()
        data.extend(response_data)
        url = None
        if 'next' in response.links:
            url = response.links['next']['url']
    return data

# Authenticate with the GitHub API
headers = {
    'Authorization': f'token {token}',
    'Accept': 'application/vnd.github.v3+json'
}

# Retrieve followers and following
followers_url = f'https://api.github.com/users/{username}/followers'
following_url = f'https://api.github.com/users/{username}/following'

followers_data = get_all_pages(followers_url, headers)
following_data = get_all_pages(following_url, headers)

# Convert JSON responses to sets of usernames
followers = set([follower['login'] for follower in followers_data])
following = set([followed['login'] for followed in following_data])

# Identify users who don't follow you back
users_to_unfollow = following - followers

# Unfollow users who don't follow you back
for user in users_to_unfollow:
    response = requests.delete(f'https://api.github.com/user/following/{user}', headers=headers)
    if response.status_code == 204:
        print(f'Unfollowed: {user}')
    else:
        print(f'Error unfollowing {user}: {response.status_code}')
