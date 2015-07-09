from pangrams import PangramFinder

# Get initial pangram
pg = PangramFinder()
results = pg.run_search(10, 1, 10, False)[0]["pangram"]

def optimize(pangram):
    """
    
    """
    num_copies = len(pangram) # one set for swapping, one for removing
    copies = list()
    
    for index in range(num_copies):
        copy = swap(pangram, index)
        copies.append(copy)

    


def swap(pangram, index):
    # TODO: All this shit

def remove(pangram, index):
    # TODO: All this shit

