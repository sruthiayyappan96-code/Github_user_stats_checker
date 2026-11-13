# GitHub User Stats Checker

A simple Python script that takes a GitHub username and prints the user's name, number of public repositories, and follower count using the [GitHub REST API](https://docs.github.com/en/rest/users/users).

## Requirements

- Python 3.6+
- [`requests`](https://pypi.org/project/requests/)

## Installation

```bash
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>
pip install requests
```

## Usage

```bash
python github_user_stats_checker.py
```

Enter a GitHub username when prompted.

### Example

```
Github username: torvalds
Name: Linus Torvalds
Public Repos: 7
Followers: 200000
```

## How it works

The script sends a `GET` request to `https://api.github.com/users/<username>`, parses the JSON response, and prints the `name`, `public_repos`, and `followers` fields.

## Notes

- The GitHub API allows about 60 unauthenticated requests per hour per IP address.
- If the username doesn't exist, the fields will show `None`.

## Possible improvements

- Handle invalid usernames and network errors
- Use a personal access token for higher rate limits
- Show more stats (following, bio, location, top repositories)

## License

This project is licensed under the MIT License. Feel free to use and modify it.
