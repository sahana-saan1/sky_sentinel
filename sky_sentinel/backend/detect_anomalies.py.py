import pandas as pd
from backend.parse_tle import parse_tle

# --- Step 1: Load rogue objects ---
rogue_df = pd.read_csv("data/rogue_objects.csv")

# --- Step 2: Load registered satellite TLE ---
with open("data/registered_tle.txt", "r") as f:
    tle_text = f.read()

registered_sats = parse_tle(tle_text)

# Convert TLE parsed data into DataFrame
inc = []
ecc = []
alt = []

for sat in registered_sats:
    inc.append(sat["inclination"])
    ecc.append(sat["eccentricity"])
    alt.append(sat["altitude"])

registered_df = pd.DataFrame({
    "inclination": inc,
    "eccentricity": ecc,
    "altitude": alt
})

# --- Step 3: Define normal ranges ---
inc_min, inc_max = registered_df["inclination"].min(), registered_df["inclination"].max()
ecc_min, ecc_max = registered_df["eccentricity"].min(), registered_df["eccentricity"].max()
alt_min, alt_max = registered_df["altitude"].min(), registered_df["altitude"].max()

print("\nNormal Ranges from Registered Satellites:")
print(f"Inclination: {inc_min} - {inc_max}")
print(f"Eccentricity: {ecc_min} - {ecc_max}")
print(f"Altitude: {alt_min} - {alt_max}")

# --- Step 4: Check rogue objects ---
def is_anomalous(row):
    anomaly = False
    reasons = []

    if not (inc_min <= row["inclination"] <= inc_max):
        anomaly = True
        reasons.append("Inclination out of range")

    if not (ecc_min <= row["eccentricity"] <= ecc_max):
        anomaly = True
        reasons.append("Eccentricity out of range")

    if not (alt_min <= row["altitude"] <= alt_max):
        anomaly = True
        reasons.append("Altitude out of range")

    return anomaly, reasons

rogue_df["Anomaly"], rogue_df["Reasons"] = zip(*rogue_df.apply(is_anomalous, axis=1))

print("\nRogue Object Analysis:\n")
print(rogue_df)