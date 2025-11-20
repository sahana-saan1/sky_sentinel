def calculate_score(inclination, eccentricity, altitude, drift):
    score = 0

    if inclination < 0.1 or inclination > 100:
        score += 20
    if eccentricity > 0.5:
        score += 20
    if altitude < 200 or altitude > 2000:
        score += 20
    if drift > 200:
        score += 20

    return score