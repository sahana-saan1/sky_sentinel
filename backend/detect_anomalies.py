from .parse_tle import parse_tle

REGISTERED_SATS = {
    "ISS",
    "HUBBLE",
    "STARLINK-1001",
    "GPS-III",
    "INSAT-3D"
}

def detect_rogue_objects(tle_path):
    tle_data = parse_tle(tle_path)
    rogue_objects = []

    for sat_name in tle_data.keys():
        if sat_name not in REGISTERED_SATS:
            rogue_objects.append(sat_name)

    return rogue_objects
