import os

def define_env(env):
    """
    This hook is called when the config is loading.
    """
    # Get environment variables with fallbacks
    username = os.getenv('GITHUB_REPOSITORY_OWNER', 'Ghost')
    repo_name = os.getenv('GITHUB_REPOSITORY', 'mkdocs-plex-guide-template').split('/')[-1]

    # Add them to the macros environment
    env.variables.update({
        "username": username,
        "repo_name": repo_name,
        "request_url": "request.example.com",
        "domain": "example.com"
    })
