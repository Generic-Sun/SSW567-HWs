import requests
import json

def get_repos(user_id):
    """Fetches a list of repository names for a given GitHub user ID."""
    response = requests.get(f"https://api.github.com/users/{user_id}/repos")
    
    if response.status_code != 200:
        return []
        
    # Explicitly using the json module to parse the text response
    repos_data = json.loads(response.text)
    return [repo.get("name") for repo in repos_data if isinstance(repo, dict)]

def get_commits(user_id, repo_name):
    """Fetches the number of commits for a specific repository."""
    response = requests.get(f"https://api.github.com/repos/{user_id}/{repo_name}/commits")
    
    if response.status_code != 200:
        return 0
        
    commits_data = json.loads(response.text)
    return len(commits_data) if isinstance(commits_data, list) else 0

def get_github_info(user_id):
    """Combines repo and commit data and formats it for output."""
    # Using a list comprehension to condense the loop into a single line
    return [f"Repo: {repo} Number of commits: {get_commits(user_id, repo)}" 
            for repo in get_repos(user_id)]

if __name__ == "__main__":
    for info in get_github_info("Generic-Sun"):
        print(info)