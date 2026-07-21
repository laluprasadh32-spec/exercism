def commands(binary_str):
    actions = [
        "wink",
        "double blink",
        "close your eyes",
        "jump"
    ]

    n = int(binary_str, 2)
    result = []

    for i in range(4):
        if n & (1 << i):
            result.append(actions[i])

    if n & 16:
        result.reverse()

    return result