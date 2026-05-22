def normalize(score):
    if score is None:
        return None
    if isinstance(score,str):
        try:
            score = float(score)
        except:
            return None
    if score <= 1:
        score *= 100
    return round(score)

def label(score):
    score = normalize(score)
    if score is None:
        return "Not Reviewed"

    if score >= 80:
        return "High"

    if score >= 50:
        return "Medium"

    return "Verify This"