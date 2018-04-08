directions = ['north', 'south', 'west', 'east']
verbs = ['go', 'kill', 'eat']
stops = ['the', 'in', 'of']
nouns = ['bear', 'princess']


def scan(text):

    word_list = text.split()
    processed_tuples = []

    for word in word_list:

        if word in directions:
            processed_tuples.append(("direction", word))

        elif word in verbs:
                processed_tuples.append(("verb", word))

        elif word in stops:
                processed_tuples.append(("stop", word))

        elif word in nouns:
                processed_tuples.append(("noun", word))

        elif convert_numbers(word):
                processed_tuples.append(("number", int(word)))

        else:
            processed_tuples.append(("error", word))

    return processed_tuples


def convert_numbers(s):
    try:
        return int(s)
    except ValueError:
        return None
