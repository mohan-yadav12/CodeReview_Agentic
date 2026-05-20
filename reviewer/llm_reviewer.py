import os
import json

from dotenv import load_dotenv
import google.generativeai as genai
from openai import OpenAI

load_dotenv()

API_KEY = os.getenv("API_KEY")

print(
    "KEY FOUND:",
    API_KEY is not None
)


if not API_KEY:

    raise Exception(
        """
Missing API_KEY
Create:
.env
API_KEY=YOUR_API_KEY
"""
    )

genai.configure(
    api_key=API_KEY
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

def review_code(
    code,
    meta
):

    prompt = f"""
You are a senior code reviewer.

Analyze Python code.

Return ONLY JSON.

Schema:

[
{{
"issue_type":"",
"severity":"",
"review_comment":"",
"suggested_fix":"",
"confidence_score":0
}}
]

FILE:
{meta}

CODE:
{code}
"""

    try:

        response = model.generate_content(
            prompt
        )

        text = response.text.strip()

        text = (
            text
            .replace(
                "```json",
                ""
            )
            .replace(
                "```",
                ""
            )
            .strip()
        )

        return json.loads(
            text
        )

    except Exception as e:

        return [

            {
                "issue_type":
                "LLM Error",

                "severity":
                "N/A",

                "review_comment":
                str(e),

                "suggested_fix":
                "Retry",

                "confidence_score":
                None
            }

        ]