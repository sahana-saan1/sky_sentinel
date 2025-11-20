def predict_orbit(altitude, velocity):
    """
    Very simple orbit prediction model for demonstration.
    """
    next_altitude = altitude + (velocity * 0.1)
    status = "Stable"

    if next_altitude > 2000:
        status = "Orbit Increasing — Possible Drift"
    elif next_altitude < 200:
        status = "Orbit Decay Warning"

    return next_altitude, status