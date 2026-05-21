def markdown_report(df):

    md = "# AI Code Review Report\n\n"

    for _, row in df.iterrows():

        md += (
            f"## {row['file']}\n\n"
        )

        md += (
            f"Object: {row['object']}\n\n"
        )

        md += (
            f"- Severity: {row['severity']}\n"
        )

        md += (
            f"- Issue: {row['issue_type']}\n"
        )

        md += (
            f"- Confidence: {row['confidence_label']}\n\n"
        )

        md += (
            f"{row['review_comment']}\n\n"
        )

        md += (
            f"Fix:\n"
        )

        md += (
            f"{row['suggested_fix']}\n\n"
        )

        md += "---\n"

    return md