# backend/detect_anomalies.py

from backend.parse_tle import parse_tle

# Fake known satellites (in real version you load from database or Celestrak)
KNOWN_SATELLITES = {
    "ISS",
    "HUBBLE",
    "NOAA 20",
    "LANDSAT 8",
    "SENTINEL-2A"
}

def detect_rogue_objects(tle_file_path):
    sats = parse_tle(tle_file_path)

    if not sats:
        return []   # always return list

    rogue = []

    for sat in sats:
        name = sat["name"].upper()

        # if satellite name NOT in known list → mark as rogue
        if name not in KNOWN_SATELLITES:
            rogue.append(name)

    return rogue