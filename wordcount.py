import sys
import collections

def word_count(filename):
    """"
    Takes a file and parses each words and prints out how many times the word appears
    """

    file_data = open(filename)
    occurance = collections.Counter()
    for line in file_data:
        line = line.rstrip().replace("--", " ").split(" ")
        occurance.update(line)
    print occurance
        ###for word in line:
           ### word = word.strip("?,!.;-\":_").lower()
            ###print word
            ###occurance.update(word)
            #print occurance
    #for word, count in occurance:
        #print occurance
        

word_count(sys.argv[1])