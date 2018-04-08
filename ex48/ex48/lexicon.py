
def scan(text):

    word_list = text.split()
    processed_tuples = []

    for word in word_list:

        #  directions
        if word in ('north', 'south', 'west', 'east'):
            processed_tuples.append(("direction", word))

        #  verbs
        if word in ('go', 'kill', 'eat'):
                processed_tuples.append(("verb", word))

        #  stop
        if word in ('the', 'in', 'of'):
                processed_tuples.append(("stop", word))

        #  noun
        if word in ('bear', 'princess'):
                processed_tuples.append(("noun", word))

        #  number
        if convert_numbers(word):
                processed_tuples.append(("number", int(word)))

    return processed_tuples


def convert_numbers(s):
    try:
        return int(s)
    except ValueError:
        return None
