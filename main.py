from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
import os

app = FastAPI(
    title="VTU GenAI Lab - BAIL657C",
    description="View all 10 lab programs from anywhere",
    version="1.0.0"
)

# Works both locally and on Render
PROGRAMS_DIR = os.path.join(os.path.dirname(__file__), "programs")

PROGRAMS = {
    "p1":  "Program 1 — Pre-trained Word Vectors",
    "p2":  "Program 2 — Vector Arithmetic",
    "p3":  "Program 3 — Visualize Embeddings",
    "p4":  "Program 4 — Semantically Similar Words",
    "p5":  "Program 5 — Train Word2Vec",
    "p6":  "Program 6 — Enrich GenAI Prompt",
    "p7":  "Program 7 — Creative Sentence Generation",
    "p8":  "Program 8 — Sentiment Analysis",
    "p9":  "Program 9 — Text Summarization",
    "p10": "Program 10 — FastAPI Demo",
}

def base_html(title: str, body: str) -> str:
    return f"""<!DOCTYPE html>
<html>
<head>
    <title>{title}</title>
    <style>
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{ font-family: 'Segoe UI', Arial, sans-serif; background: #1e1e1e; color: #d4d4d4; }}
        header {{ background: #252526; padding: 16px 32px; border-bottom: 1px solid #3a3a3a;
                  display: flex; align-items: center; justify-content: space-between; }}
        header h1 {{ color: #569cd6; font-size: 18px; font-weight: 600; }}
        header a  {{ color: #9cdcfe; font-size: 13px; text-decoration: none; }}
        header a:hover {{ color: #4ec9b0; }}
        .container {{ max-width: 860px; margin: 40px auto; padding: 0 24px; }}
        {body_css()}
    </style>
</head>
<body>
    <header>
        <h1>VTU GenAI Lab — BAIL657C</h1>
        <a href="/">← All Programs</a>
    </header>
    <div class="container">
        {body}
    </div>
</body>
</html>"""

def body_css():
    return """
        h2   { color: #4ec9b0; margin-bottom: 6px; font-size: 16px; font-weight: 600; }
        p    { color: #808080; font-size: 13px; margin-bottom: 28px; }
        ul   { list-style: none; padding: 0; }
        li   { margin: 10px 0; }
        .card { display: block; padding: 14px 20px; background: #252526;
                border: 1px solid #3a3a3a; border-radius: 8px;
                color: #4ec9b0; text-decoration: none; font-size: 15px;
                transition: all 0.15s ease; }
        .card:hover { background: #2d2d2d; border-color: #569cd6; color: #9cdcfe; }
        .card span  { color: #569cd6; font-size: 12px; float: right; margin-top: 2px; }
        .code-header { display: flex; justify-content: space-between; align-items: center;
                        background: #2d2d2d; border: 1px solid #3a3a3a;
                        border-bottom: none; border-radius: 8px 8px 0 0; padding: 10px 16px; }
        .code-header h2 { color: #9cdcfe; font-size: 14px; margin: 0; }
        .copy-btn { background: #0e639c; color: #fff; border: none; padding: 6px 14px;
                    border-radius: 4px; cursor: pointer; font-size: 12px; }
        .copy-btn:hover { background: #1177bb; }
        pre  { background: #1e1e1e; border: 1px solid #3a3a3a; border-radius: 0 0 8px 8px;
               padding: 24px; overflow-x: auto; font-size: 13px; line-height: 1.6;
               font-family: 'Cascadia Code', 'Consolas', monospace; white-space: pre; }
        .tag { display: inline-block; background: #0e639c; color: #fff;
               font-size: 11px; padding: 2px 8px; border-radius: 4px; margin-left: 8px; }
    """


# ── Home page ──────────────────────────────────────────────────────────────────

@app.get("/", response_class=HTMLResponse)
def home():
    cards = ""
    for key, label in PROGRAMS.items():
        num = key.replace("p", "")
        cards += f"""
        <li>
            <a class="card" href="/view/{key}">
                {label}
                <span>Program {num} →</span>
            </a>
        </li>"""

    body = f"""
        <h2 style="margin-top:32px">6th Sem CSE — Generative AI Lab</h2>
        <p style="margin-top:6px;margin-bottom:28px">Select a program to view its code</p>
        <ul>{cards}</ul>
    """
    return base_html("VTU BAIL657C Lab", body)


# ── View program code ──────────────────────────────────────────────────────────

@app.get("/view/{program}", response_class=HTMLResponse)
def view_program(program: str):
    if program not in PROGRAMS:
        raise HTTPException(status_code=404, detail="Program not found")

    filepath = os.path.join(PROGRAMS_DIR, f"{program}.py")

    if not os.path.exists(filepath):
        raise HTTPException(status_code=404, detail=f"{program}.py not found on server")

    with open(filepath, "r") as f:
        code = f.read()

    # Escape HTML special characters
    code_escaped = (
        code.replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
    )

    label = PROGRAMS[program]

    body = f"""
        <div style="margin-top:32px">
            <div class="code-header">
                <h2>{label} &nbsp;<span class="tag">{program}.py</span></h2>
                <button class="copy-btn" onclick="copyCode()">Copy Code</button>
            </div>
            <pre id="code-block">{code_escaped}</pre>
        </div>
        <script>
            function copyCode() {{
                const code = document.getElementById('code-block').innerText;
                navigator.clipboard.writeText(code).then(() => {{
                    const btn = document.querySelector('.copy-btn');
                    btn.textContent = 'Copied!';
                    btn.style.background = '#16825d';
                    setTimeout(() => {{
                        btn.textContent = 'Copy Code';
                        btn.style.background = '#0e639c';
                    }}, 2000);
                }});
            }}
        </script>
    """
    return base_html(label, body)