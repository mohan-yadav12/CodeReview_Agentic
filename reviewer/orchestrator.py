from parser.ast_parser import (parse_file)
from reviewer.llm_reviewer import (review_code)
from reviewer.confidence import (label)

def run_review(files):
    results = []
    for file in files:
        chunks = (parse_file(file))
        for c in chunks:
            reviews = (review_code(c["code"],f"""
{file}
{c["name"]}
"""
                )
            )
            for r in reviews:
                r["file"] = file
                r["object"] = c["name"]
                from reviewer.confidence import (normalize,label)
                r["confidence_score"] = normalize(r.get("confidence_score"))
                r["confidence_label"] = label(r["confidence_score"])
                results.append(r)

    return results