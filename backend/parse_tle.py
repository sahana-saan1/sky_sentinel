def parse_tle(tle_path):
    sat_data = {}

    with open(tle_path, "r") as f:
        lines = f.readlines()

    for i in range(0, len(lines), 3):
        name = lines[i].strip()
        line1 = lines[i + 1].strip()
        line2 = lines[i + 2].strip()

        sat_data[name] = (line1, line2)

    return sat_data
