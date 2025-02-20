# Query GitHub User Repositories with GraphQL

## Objective
Fetch a list of repositories for a GitHub user using GraphQL.

## Requirements
- Python 3.8+
- Poetry
- GitHub personal access token

## Setup
1. Replace `your_github_token_here` in `github_graphql.py` with your actual GitHub token.
2. Install dependencies:
poetry install

## Usage
Run the script:
poetry run python github_graphql.py

Enter a GitHub username when prompted.


## Expected Output
Enter GitHub username: octocat
Repository: Hello-World - My first repository
Repository: SampleRepo - A simple test repository