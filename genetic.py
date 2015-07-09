import random

from pangrams import PangramFinder


# Get initial pangram
pg = PangramFinder()
results = pg.run_search(10, 1, 10, False)[0]["pangram"]

def optimize(pangram, iterations):
    """

    """
    if iterations > 0:
        num_copies = len(pangram) # one set for swapping, one for removing
        copies = list()

        copies.append(pangram)

        for index in range(num_copies):
            copies.append(swap(pangram, index))
            copies.append(remove(pangram, index))

        scored = pg.score(copies)
        return optimize(pg.get_top_scores(1, scored))
    else:
        return pangram

def swap(pangram, index):
    """
    Swaps a word in a pangram at [index]
    """
    words = pangram.split()
    words[index] = pg.words[random.randrange(0, len(pg.words))].lower()
    return words

# Test code
swap(results, 1)

def remove(pangram, index):
    #TODO: This
