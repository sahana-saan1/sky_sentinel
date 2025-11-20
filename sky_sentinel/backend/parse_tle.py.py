import pandas as pd

def load_tle(file_path):
    with open(file_path, "r") as f:
        lines = f.readlines()

    sats = []
    for i in range(0, len(lines), 3):
        if i+2 >= len(lines):
            break
        name = lines[i].strip()
        line1 = lines[i+1].strip()
        line2 = lines[i+2].strip()

        inc = float(line2[8:16])
        ecc = float("0." + line2[26:33])
        alt = float(line2[52:63])

        sats.append({
            "name": name,
            "inclination": inc,
            "eccentricity": ecc,
            "altitude": alt
        })

    return pd.DataFrame(sats)