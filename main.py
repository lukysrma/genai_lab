from fastapi import FastAPI
from fastapi.responses import RedirectResponse, HTMLResponse

app = FastAPI()

BASE = "https://raw.githubusercontent.com/lukysrma/genai_lab/main/programs"

# ── Short URLs: /p1 to /p10 ──
@app.get("/p{num}")
def load_program(num: int):
    return RedirectResponse(url=f"{BASE}/p{num}.py")

# ── Home page ──
@app.get("/", response_class=HTMLResponse)
def home():
    links = "".join([
        f'<li><a href="/p{i}">%load https://genai-lab-08wy.onrender.com/p{i}</a></li>'
        for i in range(1, 11)
    ])
    return f"""<!DOCTYPE html>
<html>
<head>
    <title>VTU BAIL657C</title>
    <style>
        body {{ font-family: Arial, sans-serif; max-width: 700px; margin: 60px auto;
                background: #1e1e1e; color: #d4d4d4; padding: 0 20px; }}
        h1   {{ color: #569cd6; }}
        p    {{ color: #808080; font-size: 13px; }}
        ul   {{ list-style: none; padding: 0; }}
        li   {{ margin: 10px 0; }}
        a    {{ display: block; padding: 12px 20px; background: #252526;
                border: 1px solid #3a3a3a; border-radius: 8px;
                color: #4ec9b0; text-decoration: none; font-size: 14px;
                font-family: monospace; }}
        a:hover {{ background: #2d2d2d; border-color: #569cd6; }}
    </style>
</head>
<body>
    <h1>VTU GenAI Lab — BAIL657C</h1>
    <p>Copy any line below and paste it into Jupyter Notebook to load that program</p>
    <ul>{links}</ul>
</body>
</html>"""