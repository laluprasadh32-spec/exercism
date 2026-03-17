def response(hey_bob):
    msg = hey_bob.strip()

    if not msg:
        return "Fine. Be that way!"
    if msg.isupper() and any(c.isalpha() for c in msg) and msg.endswith("?"):
        return "Calm down, I know what I'm doing!"
    if msg.isupper() and any(c.isalpha() for c in msg):
        return "Whoa, chill out!"
    if msg.endswith("?"):
        return "Sure."
    return "Whatever."