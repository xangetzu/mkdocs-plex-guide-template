# Plex Documentation Guide

A standardized documentation template for your Plex server, built with Material for MkDocs and deployed via GitHub Pages. This template includes pre-built pages covering common Plex topics like streaming quality, content requests, transcoding, and more.

## 🚀 Getting Started

1. Fork this repository to your own GitHub account
2. Configure GitHub Pages:
  - Go to Settings > Pages
  - Set "Source" to "Deploy from a branch"
  - Select "gh-pages" branch and "/" (root) folder
  - Click Save

Your site will be available at `https://yourusername.github.io/mkdocs-plex-guide-template`

The template will automatically use your GitHub username and repository name throughout the site. You can see this in action at my demo site: https://mistercalvin.github.io/mkdocs-plex-guide-template

## 📝 Customization

### Basic Configuration
The following values are automatically set via environment variables:
- `username` - Your GitHub username (lowercase)
- `repo_name` - Repository name
- `year` - Current year

### Content Customization
Key files to modify:
- `docs/*.md` - Documentation pages
- `docs/stylesheets/extra.css` - [Custom admonitions](https://squidfunk.github.io/mkdocs-material/reference/admonitions/#custom-admonitions)
- `docs/assets/images/` - Images and video

### Default Values
You can customize default values for:
- Request URL: `request.example.com`
- Domain name: `example.com`

Edit these in [`main.py`](main.py) in the project root. These values are used throughout the rendered markdown pages.

## 📚 Resources

### Documentation
- [Material for MkDocs Customization](https://squidfunk.github.io/mkdocs-material/customization/)
- [Publishing Your Site](https://squidfunk.github.io/mkdocs-material/publishing-your-site/#github-pages)
- [MkDocs Plugins Catalog](https://github.com/mkdocs/catalog)

### Video Tutorials
- [Creating Documentation with MkDocs Material Theme](https://www.youtube.com/watch?v=Q-YA_dA8C20) - James Willett
- [Hosting MkDocs on Cloudflare Pages](https://www.youtube.com/watch?v=7-HhLascLuM) - Techdox
