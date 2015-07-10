import random

from pangrams import PangramFinder


# Get initial pangram
pg = PangramFinder()
results = pg.run_search(10, 1, 10, True)[0]["pangram"]

def optimize(pangram, iterations):
    """

    """
    if iterations > 0:
        num_copies = len(pangram.split()) # one set for swapping, one for removing
        copies = list()
        copies.append(pangram)
        for index in range(0, num_copies - 1):
            copies.append(swap(pangram, index))
            #copies.append(remove(pangram, index))

        scored = pg.score(copies)
        return optimize(pg.get_top_scores(1, scored)[0]["pangram"], iterations - 1)
    else:
        return pangram

def swap(pangram, index):
    """
    Swaps a word in a pangram at [index]
    """
    words = pangram.split()
    words[index] = pg.words[random.randrange(0, len(pg.words))].lower()

    return " ".join(words)

def remove(pangram, index):
    words = pangram.split()
    words.remove(index)
    return " ".join(words)

# Test code
optimized = optimize(results, 100)
score = int(pg.get_score(optimized)["current_score"])
print("\nOPTIMIZED\n=========\nTotal\t\tScore\t\tGenetically Modified Pangram\n",score,"\t\t",int(score / 234 * 100),"%\t\t",optimized)
