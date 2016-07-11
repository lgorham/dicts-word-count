import sys

def word_count(filename):
    """"
    Takes a file and parses each words and prints out how many times the word appears
    """

    file_data = open(filename)
    occurance = {}
    for line in file_data:
        line = line.rstrip().replace("--", " ").split(" ")
        for word in line:
            word = word.strip("?,!.;-\":_").lower()
            occurance[word] = occurance.get(word, 0) + 1
    for word, count in occurance.items():
        print word, count
        

word_count(sys.argv[1])