def build_prompt(code, meta):

    return f"""
You are a senior code reviewer.
Analyze this Python code.
FILE:
{meta}
CODE:
{code}

Find:
1. Bugs
2. Security issues
3. Performance issues
4. Maintainability issues

Return STRICT JSON.
Schema:
[
 {{
   "issue_type":"Bug",
   "severity":"Low|Medium|High",
   "review_comment":"string",
   "suggested_fix":"string",
   "confidence_score":0
 }}
]
Rules:
- Output JSON only
- confidence_score 0–100
- No markdown
- No explanations
"""