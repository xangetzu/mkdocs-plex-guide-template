import os
from datetime import datetime

def define_env(env):
    """
    This hook is called when the config is loading.
    """
    username = os.getenv('GITHUB_REPOSITORY_OWNER', 'Ghost')
    repo_name = os.getenv('GITHUB_REPOSITORY', 'mkdocs-plex-guide-template').split('/')[-1]
    current_year = datetime.now().year

    env.variables.update({
        "username": username,
        "repo_name": repo_name,
        "year": current_year,
        "request_url": "request.example.com",
        "plex_url": "plex.example.com",
        "plex_libraries": "Movies and TV Shows"
        "noreply_email": "noreply@example.com",
    })
