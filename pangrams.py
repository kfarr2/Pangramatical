import collections
import os, sys, json
import random
from datetime import datetime

SCORE = 234

class PangramFinder:
    """
        This class finds pangrams.
        A pangram is defined (for the purpose of this program) as a semantically correct phrase
        that uses all 26 characters in the english alphabet, in as few words as possible.

        Pangrams are useful for testing typefaces and ensuring that all characters are output correctly.

        This program will follow an algorithm similar to the following pseudocode.


            1. Initialize everything.
                a. load the dictionary.
                b. initialize the empty list of pangrams.

            // Get the pangram list.
            2. While there is still time left:
                a. start with a list containing each character in the alphabet.
                b. while there are still characters in the list:
                    1. find a random word in the dictionary.
                    2. make sure that word hasn't been used yet.
                    3. add it to the phrase.
                    4. remove the characters in the word from the alphabet list.
                c. add the phrase to the list of phrases.

            // Then analyze the list.
            3. Look through each item in the list.
                a. Score each entry
                -   +9 pts for each unique alphabet character.
                -   -1 point for each repeated character.
                -   -1 point per word.

    """
    def __init__(self):
        """ Initialize everything """

        # load the standard dictionary
        dictionary = open("dictionary.json", 'r').read()
        words = list(json.loads(dictionary))
        self.words = list()
        for word in words:
            if len(word) >= 2:
                self.words.append(word)
        self.dictlength = len(self.words)

    def all_chars(self):
        return list(chr(i + 97) for i in range(26))

    def search(self, seconds, words):
        """ Looks for all the pangrams for <seconds> number of seconds """
        # grab the alphabet
        alphabet = self.all_chars()
        pangrams = []

        # start the clock
        start_time = datetime.now()
        difference = (datetime.now() - start_time).total_seconds()

        # while we still have time left.
        while difference <= seconds:
            alphabet = self.all_chars()
            # and there are still characters left to check
            pangram = ""
            while len(alphabet) > 0:
                word = words[random.randrange(0,len(words))]
                pangram += " " + str(word)
                for c in word.lower():
                    if c in alphabet:
                        alphabet.remove(c)
                    else:
                        pass

            pangrams.append(pangram)
            difference = (datetime.now() - start_time).total_seconds()
        return pangrams

    def get_score(self, pangram):
        """
        Get the score for 1 single pangram
        """
        current_score = SCORE + 20
        # -1pt per word
        current_score -= pangram.count(" ")
        alphabet = self.all_chars()
        # -1pt for duplicate characters
        for c in alphabet:
            count = pangram.count(c)
            if count > 1:
                current_score = current_score - count + 1
            if count == 0:
                current_score = 0
        count = pangram.count('-')
        current_score -= (count * 50)

        return { "pangram": pangram, "current_score": current_score }


    def score(self, pangrams):
        """
            Score the pangrams based on the following criteria
                - 9 * 26 = 234 (+9pts per unique character. Each character had to get used once)
                - -1pt for each duplicate character
                - -1pt per word
                - -5pts per punctuation mark
        """
        scored = []
        # Initialize the score
        for pangram in pangrams:
            scored.append(self.get_score(pangram))
        return scored



    def get_top_scores(self, num_scores, scored):
        scores = []
        # look through each entry of the list.
        for score in scored:
            if len(scores) < num_scores:
               scores.append(score)
            else:
                # hoooo crap this here's a funky algorithm.
                temp = dict()
                for item in scores:
                    if score["current_score"] > item["current_score"]:
                        temp["current_score"] = item["current_score"] # should be pass by reference
                        temp["pangram"] = item["pangram"]
                        item["current_score"] = score["current_score"]
                        item["pangram"] = score["pangram"]
                        score = temp
        return scores


    def run_search(self, time, num_scores, max_wordlength, verbose):
        new_words = []
        for word in self.words:
            if len(word) < max_wordlength:
                    new_words.append(word.lower())

        self.dictlength = len(new_words)

        if verbose is True:
            print('\n'*100)
            print("Running...\n")
            print("Please wait " + str(time) + " seconds\n")

        pangrams = self.search(time, new_words)

        if verbose is True:
            print("\nSearch complete. ", str(len(pangrams)), " pangrams found.\nScoring...\n")

        scored = self.score(pangrams)
        top_scores = self.get_top_scores(num_scores, scored)

        if verbose is True:
            print('\n'*3)
            print("RESULTS\n=======\n")
            print("Total\t\tScore\t\tPangram")

        for score in top_scores:
            if verbose is True:
                print(str(score['current_score']) + "\t\t" + str(int((score['current_score'] / SCORE)*100)) + '%\t\t' + str(score["pangram"]) + '\n')

        return top_scores


