
def scan(text):

    word_list = text.split()
    processed_tuples = []

    for word in word_list:

        #  directions
        if word in ('north', 'south', 'west', 'east'):
            tuple = ("direction", word)
            processed_tuples.append(tuple)

        #  verbs
        if word in ('go', 'kill', 'eat'):
                tuple = ("verb", word)
                processed_tuples.append(tuple)

        #  stop
        if word in ('the', 'in', 'of'):
                tuple = ("stop", word)
                processed_tuples.append(tuple)

    return processed_tuples
