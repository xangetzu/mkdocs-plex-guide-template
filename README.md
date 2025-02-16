# Plex Documentation Guide

A standardized documentation template for your Plex server, built with Material for MkDocs and deployed via GitHub Pages. This template includes pre-built pages covering common Plex topics like streaming quality, content requests, transcoding, and more.

## 🚀 Getting Started
> [!NOTE]
> When forking, you only need the main branch. The gh-pages branch will be created automatically by our workflow.

1. Fork this repository to your own GitHub account
2. Enable GitHub Actions:
   * Go to Actions tab (top of this page)
   * Click "I understand my workflows, go ahead and enable them"
3. Run the CI workflow to create the gh-pages branch:
   * Option 1: Modify and push a change (e.g., customize variables in [main.py](main.py))
   * Option 2: Manually trigger the workflow
     * Go to Actions tab
     * Select "ci" workflow from the left sidebar
     * Click "Run workflow" dropdown button
     * Select branch (main) and click "Run workflow"

Your site will be available at `https://yourusername.github.io/mkdocs-plex-guide-template` after the workflow completes.

The template will automatically use your GitHub username and repository name throughout the site. You can see this in action at my demo site: https://mistercalvin.github.io/mkdocs-plex-guide-template

### Automatic Deployment
The site is automatically built using GitHub Actions whenever changes are pushed to the main branch. After a successful build, the site is deployed to the `gh-pages` branch, which GitHub Pages then serves automatically. You can monitor the build and deployment process in the Actions tab of your repository.

## 📝 Customization

### Basic Configuration
The following values are automatically set via environment variables in [`ci.yml`](.github/workflows/ci.yml) and used in the header + footer of your MKDocs site:
- `username` - Your GitHub username (lowercase)
- `repo_name` - Repository name
- `year` - Current year

### Default Values
The following values can be set in [`main.py`](main.py) or in Settings (top of this page) > Security > Secrets and variables > Actions > Variables tab. These values are used throughout the rendered site pages:
- request_url: `request.example.com`
- plex_url: `plex.example.com`
- plex_libraries: `Movies and TV Shows`
- noreply_email: `noreply@example.com`

### Content Customization
Key files to modify:
- `docs/*.md` - Documentation pages
- `docs/stylesheets/extra.css` - [Custom admonitions](https://squidfunk.github.io/mkdocs-material/reference/admonitions/#custom-admonitions)
- `docs/assets/` - Images and video

## 📚 Resources

### Documentation / Plugins
- [Material for MkDocs - Getting started](https://squidfunk.github.io/mkdocs-material/getting-started/)
- [MkDocs Plugins Catalog](https://github.com/mkdocs/catalog)
- [MKDocs Pasword Encryption Plugin](https://github.com/unverbuggt/mkdocs-encryptcontent-plugin)

### Video Tutorials
- [Creating Documentation with MkDocs Material Theme](https://www.youtube.com/watch?v=Q-YA_dA8C20) - James Willett
- [Hosting MkDocs on Cloudflare Pages](https://www.youtube.com/watch?v=7-HhLascLuM) - Techdox
