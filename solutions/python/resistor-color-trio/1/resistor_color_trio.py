def label(colors):
    color = [
        "black", "brown", "red", "orange", "yellow",
        "green", "blue", "violet", "grey", "white"
    ]

    value = (color.index(colors[0]) * 10 + color.index(colors[1])) * (10 ** color.index(colors[2]))

    units = ["ohms", "kiloohms", "megaohms", "gigaohms"]
    unit = 0

    while value % 1000 == 0 and value >= 1000:
        value //= 1000
        unit += 1

    return f"{value} {units[unit]}"