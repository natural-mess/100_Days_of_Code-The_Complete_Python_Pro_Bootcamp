# Flask Blog Bootstrap

A simple blog web app built with Flask and Bootstrap (Clean Blog theme).

The app fetches blog posts from a remote JSON API and renders:
- A home page with post previews
- A post details page
- About and Contact pages

## Features

- Flask routing with dynamic post pages: `/post/<int:num>`
- Jinja templates with shared header/footer includes
- Static assets served with `url_for('static', ...)`
- Remote data source using `requests`

![alt text](demo/2026-07-10_19h35_01.gif)

## Project Structure

```text
Flask-Blog-Bootstrap/
├── main.py
├── blog_data.txt
├── templates/
│   ├── header.html
│   ├── footer.html
│   ├── index.html
│   ├── about.html
│   ├── contact.html
│   └── post.html
└── static/
    ├── assets/
    ├── css/
    │   └── styles.css
    └── js/
        └── scripts.js
```

## Requirements

- Python 3.10+
- pip

Python packages:
- Flask
- requests

## Setup

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd Flask-Blog-Bootstrap
```

### 2. Create and activate a virtual environment

Windows (PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Windows (CMD):

```bat
python -m venv .venv
.venv\Scripts\activate.bat
```

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install flask requests
```

## Run the App

```bash
python main.py
```

Open in browser:
- http://127.0.0.1:5000/

## Routes

- `/` -> Home page with all posts
- `/about` -> About page
- `/contact` -> Contact page
- `/post/<int:num>` -> Post details page (e.g. `/post/1`)

## Notes

- Blog data is fetched from:
  `https://api.npoint.io/6b78c3badded7def110f`
- The current code uses `verify=False` in `requests.get(...)` inside `main.py`.
  This suppresses SSL verification and is not recommended for production.

## Troubleshooting

### `url_for` not working

Common causes:
- Endpoint name does not match the Flask view function name.
  Example: use `url_for('home')` only if the function is `def home():`.
- Missing route for a linked page.
- Wrong static file path.
  Example: `css/styles.css` (not `css/style.css`).

### Post page returns 404

- Check the post id in URL. If `/post/<num>` exceeds available posts, the app returns `Post not found`.

## License

MIT. See `LICENSE`.
