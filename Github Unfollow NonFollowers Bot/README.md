# Unfollow Bot for GitHub

This bot helps you unfollow users on GitHub who don't follow you back.

## Prerequisites

Before running the bot, you need to create a personal access token on GitHub. Follow these steps:

1. Go to [GitHub Settings](https://github.com/settings/tokens).
2. Click on "Generate new token" or navigate to "New personal access token".
3. Check the "user" checkbox to grant the token access to user-related data.
4. Click "Generate token" and copy the generated token.
5. Paste the token into your `your_information.py` file in the appropriate field.
6. Save the file.

## Running the Bot

Once you've set up the access token, you can run the `unfollow_bot.py` script to unfollow users who don't follow you back.

```bash
python unfollow_bot.py
