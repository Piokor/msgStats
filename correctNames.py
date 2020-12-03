def correctNamess(names):
    letters = {
        "Å\x86": "Ć",
        "Å\x98": "Ę",
        "Å\x81": "Ł",
        "Å\x83": "Ń",
        "Å\x93": "Ó",
        "Å\x9a": "Ś",
        "Å\xb9": "Ź",
        "Å\xbb": "Ż",
        "Ä\x85": "ą",
        "Å\x87": "ć",
        "Å\x99": "ę",
        "Å\x82": "ł",
        "Å\x84": "ń",
        "Å\xb3": "ó",
        "Å\x9b": "ś",
        "Å\xba": "ź",
        "Å\xbc": "ż"
    }
    for i in range(len(names)):
        for letter in list(letters.keys()):
            names[i] = names[i].replace(letter, letters[letter])
    return names
