def value(colors):
    code = [
        "black", "brown", "red", "orange", "yellow",
        "green", "blue", "violet", "grey", "white"
    ]
    return code.index(colors[0]) * 10 + code.index(colors[1])