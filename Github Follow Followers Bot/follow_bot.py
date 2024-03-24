import requests
from your_information import username, token

def get_all_pages(url, headers):
    data = []
    while url:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            try:
                response_data = response.json()
                data.extend(response_data)
                url = response.links.get('next', {}).get('url')
            except ValueError:
                print(f'Error: Expected JSON response, got {response.text}')
                break
        else:
            print(f'HTTP Error {response.status_code}: {response.text}')
            break
    return data

# Authenticate with the GitHub API
headers = {
    'Authorization': f'token {token}',
    'Accept': 'application/vnd.github.v3+json'
}

# Retrieve followers and following
followers_url = f'https://api.github.com/users/{username}/followers'
following_url = f'https://api.github.com/users/{username}/following'

# Since Github API uses pagination, we need to get all pages
followers_data = get_all_pages(followers_url, headers)
following_data = get_all_pages(following_url, headers)

# Convert JSON responses to sets of usernames
followers = set([follower['login'] for follower in followers_data])
following = set([followed['login'] for followed in following_data])

# Identify users who you don't follow back
users_to_follow = followers - following

# Follow users who follow you
for user in users_to_follow:
    response = requests.put(f'https://api.github.com/user/following/{user}', headers=headers)
    if response.status_code == 204:
        print(f'Followed: {user}')
    else:
        print(f'Error following {user}: {response.status_code}')
