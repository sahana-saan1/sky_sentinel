def simulate_rogue(altitude, drift, eccentricity):
    """
    Returns simulated rogue behavior based on user input.
    """
    risk = 0
    
    if altitude < 200 or altitude > 2000:
        risk += 30

    if drift > 100:
        risk += 40

    if eccentricity > 0.5:
        risk += 30

    if risk >= 70:
        return "HIGH RISK — Possible Rogue Object"
    elif risk >= 40:
        return "MODERATE RISK — Monitor Object"
    else:
        return "LOW RISK — Normal Satellite"