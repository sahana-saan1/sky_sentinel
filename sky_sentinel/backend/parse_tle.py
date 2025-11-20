# backend/parse_tle.py

def parse_tle(tle_file_path):
    satellites = []

    try:
        with open(tle_file_path, 'r') as file:
            lines = file.readlines()

        # Ensure TLE lines are in sets of 3
        i = 0
        while i < len(lines) - 2:
            name = lines[i].strip()
            line1 = lines[i+1].strip()
            line2 = lines[i+2].strip()

            # Validate basic format of TLE lines
            if not (line1.startswith("1 ") and line2.startswith("2 ")):
                i += 1
                continue

            satellites.append({
                "name": name,
                "line1": line1,
                "line2": line2
            })

            i += 3

        return satellites

    except Exception as e:
        print("Error parsing TLE:", e)
        return []