import os
from openai import OpenAI
from src.templates.prompts import SYSTEM_ROLE, BULLETS_PROMPT, EMAIL_PROMPT, TODO_PROMPT

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def _chat(prompt: str) -> str:
    resp = client.chat.completions.create(
        model="gpt-4o-mini",

        messages=[
            {"role": "system", "content": SYSTEM_ROLE},
            {"role": "user", "content": prompt},
            ],
            
            temperature=0.2,
    )
    return resp.choices[0].message.content.strip()


def summarize_all(content: str) -> dict:
    return {
        "bullets": _chat(BULLETS_PROMPT.format(content=content)),
        "email": _chat(EMAIL_PROMPT.format(content=content)),
        "todo": _chat(TODO_PROMPT.format(content=content)),

    }

        
    