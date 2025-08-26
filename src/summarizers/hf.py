from transformers import pipeline
from src.templates.prompts import BULLETS_PROMPT, EMAIL_PROMPT, TODO_PROMPT
from src.summarizers import hf
engine = hf
 
_summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def _sum(txt: str, maxlen=200, minlen=60) -> str:
    txt = txt.strip()
    chunks = [txt[i:i+3000] for i in range(0, len(txt),3000)] or [txt]
    outs = []
    for ch in chunks:
        outs.append(_summarize_chunk(ch, minlen, maxlen))
        merged = " ".join(outs)
        return _summarize_chunk(merged, minlen, maxlen) # final pass
    


def _summarize_chunk(ch, minlen, maxlen):
    out = _summarizer(ch, max_length=maxlen, min_length=minlen, do_sample=False)[0]["summary_text"]
    return out.strip()

def summarize_all(content: str) -> dict:
    bullets = _sum(BULLETS_PROMPT.format(content=content)).replace(". ", ".\n")
    if not bullets.startswith("."):
        bullets = ". " + bullets

    email = _sum(EMAIL_PROMPT.format(content=content))
    todo_raw = _sum(TODO_PROMPT.format(content=content))

    todos = "\n".join(f"[ ] {line.strip('-')}" for line in todo_raw.split("\n") if line.strip())
    return {"bullets": bullets, "email": email, "todo": todos}

    


