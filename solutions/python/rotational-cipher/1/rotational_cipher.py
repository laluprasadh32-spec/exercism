def rotate(text, key):
    result = ""

    for char in text:
        if char.isalpha():
            shift = key % 26

            if char.islower():
                start = ord('a')
            else:
                start = ord('A')

            rotated = chr((ord(char) - start + shift) % 26 + start)
            result += rotated
        else:
            result += char

    return result