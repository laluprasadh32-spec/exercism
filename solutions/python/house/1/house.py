def recite(start_verse, end_verse):
    parts = [
        ("house that Jack built.", ""),
        ("malt", "lay in"),
        ("rat", "ate"),
        ("cat", "killed"),
        ("dog", "worried"),
        ("cow with the crumpled horn", "tossed"),
        ("maiden all forlorn", "milked"),
        ("man all tattered and torn", "kissed"),
        ("priest all shaven and shorn", "married"),
        ("rooster that crowed in the morn", "woke"),
        ("farmer sowing his corn", "kept"),
        ("horse and the hound and the horn", "belonged to"),
    ]

    result = []

    for i in range(start_verse - 1, end_verse):
        verse = "This is the " + parts[i][0]

        for j in range(i, 0, -1):
            verse += " that " + parts[j][1] + " the " + parts[j - 1][0]

        result.append(verse)

    return result