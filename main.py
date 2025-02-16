import os
from datetime import datetime

def define_env(env):
    """
    This hook is called when the config is loading.
    """
    # Fetch values from GitHub Actions environment variables, fallback to local defaults
    username = os.getenv('GITHUB_REPOSITORY_OWNER', env.variables.get("username", "Ghost"))
    repo_name = os.getenv('GITHUB_REPOSITORY', env.variables.get("repo_name", "mkdocs-plex-guide-template")).split('/')[-1]
    current_year = datetime.now().year

    env.variables.update({
        "username": username,
        "repo_name": repo_name,
        "year": current_year,
        "request_url": os.getenv("REQUEST_URL", env.variables.get("request_url", "request.example.com")),
        "plex_url": os.getenv("PLEX_URL", env.variables.get("plex_url", "plex.example.com")),
        "plex_libraries": os.getenv("PLEX_LIBRARIES", env.variables.get("plex_libraries", "Movies and TV Shows")),
        "noreply_email": os.getenv("NOREPLY_EMAIL", env.variables.get("noreply_email", "noreply@example.com")),
    })
