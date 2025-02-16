# Plex Documentation Guide

[![Build and Deploy MkDocs Site](https://github.com/MisterCalvin/mkdocs-plex-guide-template/actions/workflows/ci.yml/badge.svg)](https://github.com/MisterCalvin/mkdocs-plex-guide-template/actions/workflows/ci.yml)
[![pages-build-deployment](https://github.com/MisterCalvin/mkdocs-plex-guide-template/actions/workflows/pages/pages-build-deployment/badge.svg)](https://github.com/MisterCalvin/mkdocs-plex-guide-template/actions/workflows/pages/pages-build-deployment)

A standardized documentation template for your Plex server, built with Material for MkDocs and deployed via GitHub Pages. This template includes pre-built pages covering common Plex topics like streaming quality, content requests, transcoding, and more.

## ✨ Features
- 📚 Pre-built pages for common Plex topics
- 🔄 Automatic deployment via GitHub Actions
- 🎨 Material for MkDocs theme with custom styling
- 🔧 Easy configuration through environment variables

## 🚀 Getting Started
> [!IMPORTANT]
> Complete all steps below to ensure your site deploys correctly. Missing any step will cause the deployment to fail.

1. Fork this repository to your own GitHub account

2. Enable GitHub Pages:
   * Go to [Settings > Pages](../../settings/pages)
   * Under "Build and deployment", change Source to "GitHub Actions"
   * Click Save and wait for the blue success message "GitHub Pages source saved"

3. Enable GitHub Actions:
   * Go to [Actions tab](../../actions)
   * Click "I understand my workflows, go ahead and enable them"

4. Run the workflow:
   * Option 1: Modify and push a change (e.g., customize variables in [main.py](main.py))
   * Option 2: Manually trigger the workflow
     * Go to [Build and Deploy MkDocs Site](../../actions/workflows/ci.yml) in the Actions tab
     * Click "Run workflow" dropdown button
     * Select branch (main) and click "Run workflow"

Your site will be available at `https://yourusername.github.io/mkdocs-plex-guide-template` after the workflow completes.

The template will automatically use your GitHub username and repository name throughout the site. You can see this in action at my demo site: https://mistercalvin.github.io/mkdocs-plex-guide-template

## 📝 Customization

### Basic Configuration
The following values are automatically set via environment variables in [`ci.yml`](.github/workflows/ci.yml) and used in the header + footer of your MKDocs site:
- `username` - Your GitHub username (lowercase)
- `repo_name` - Repository name
- `year` - Current year

### Required Variables and Default Values
> [!NOTE]
> These can also be set in [Settings > Security > Secrets and variables > Actions > Variables](../../settings/variables/actions)

The following values can be set in [`main.py`](main.py). These values are used throughout the rendered site pages:
- `request_url` - `request.example.com`
- `plex_url` - `plex.example.com`
- `plex_libraries` - `Movies and TV Shows`
- `noreply_email` - `noreply@example.com`

### Content Customization
Key files to modify:
- `docs/*.md` - Documentation pages
- `docs/stylesheets/extra.css` - [Custom admonitions](https://squidfunk.github.io/mkdocs-material/reference/admonitions/#custom-admonitions)
- `docs/assets/` - Images and video

## 🔧 Troubleshooting

If your deployment fails, check:
1. [GitHub Pages](../../settings/pages) is enabled and set to "GitHub Actions" as the source
2. [GitHub Actions](../../actions) is enabled for your repository

If you have an older fork and are encountering persistent issues:
> [!TIP]
> As a last resort (if you don't have many custom changes), you can try deleting and re-forking the repository. This template is actively maintained in the main branch since [GitHub Pages currently doesn't support multiple branch deployments](https://github.com/orgs/community/discussions/7730#discussioncomment-7603270). While this feature is planned, for now all development happens in the main branch, which might occasionally lead to breaking changes.

## 📚 Resources

### Documentation / Plugins
- [Material for MkDocs - Getting started](https://squidfunk.github.io/mkdocs-material/getting-started/)
- [MkDocs Plugins Catalog](https://github.com/mkdocs/catalog)
- [MKDocs Password Encryption Plugin](https://github.com/unverbuggt/mkdocs-encryptcontent-plugin)

### Video Tutorials
- [Creating Documentation with MkDocs Material Theme](https://www.youtube.com/watch?v=Q-YA_dA8C20) - James Willett
- [Hosting MkDocs on Cloudflare Pages](https://www.youtube.com/watch?v=7-HhLascLuM) - Techdox
