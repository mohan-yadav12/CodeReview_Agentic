def label(score):
    if score is None:
        return "Not Reviewed"
    if isinstance(score, str):
        try:
            score = float(score)
        except:
            return "Not Reviewed"

    if score <= 1:
        score *= 100

    score = round(score)
    if score >= 80:
        return "High"
    if score >= 50:
        return "Medium"
    return "Verify This"