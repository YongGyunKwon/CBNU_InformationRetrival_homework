import os
from nltk.stem import PorterStemmer
from nltk.tokenize import TweetTokenizer
from natsort import natsorted
from nltk.corpus import stopwords
import string
import wikipediaapi
import requests


#stopword setting 
stop_words=set(stopwords.words('english'))
# stemming setting
ps=PorterStemmer()


#make 10 document
wiki=wikipediaapi.Wikipedia('en')

words=['Newcastle','Judge','Customer','Market','summary','summer','winter','trust','union','response']

for i in words:
    #print("i is",i)
    page_1=wiki.page(i)
    filen= i+'.txt'
    print(page_1.summary[0:100])
    with open(filen,"w",-1,"utf-8") as f:
        f.write(page_1.summary)


def read_file(filename):
    with open(filename, 'r', encoding="ascii", errors="surrogateescape") as f:
        stuff = f.read()

    f.close()

    return stuff

def preprocessing(final_string):
    # Tokenize.
    tokenizer = TweetTokenizer()
    token_list = tokenizer.tokenize(final_string)

    # Remove punctuations.
    table = str.maketrans('', '', '\t')
    token_list = [word.translate(table) for word in token_list]
    punctuations = (string.punctuation).replace("'", "")
    trans_table = str.maketrans('', '', punctuations)
    stripped_words = [word.translate(trans_table) for word in token_list]
    token_list = [str for str in stripped_words if str]

    # Change to lowercase.
    token_list = [word.lower() for word in token_list]
    return token_list


# In this example, we create the positional index for only 1 folder.
folder_names = ["Users/ygkwo/Desktop/informationretrival/quiz6_doc2"]

# Initialize the stemmer.
stemmer = PorterStemmer()

# Initialize the file no.
fileno = 0

# Initialize the vocabulary.
pos_index = {}

# Initialize the file mapping (fileno -> file name).
file_map = {}

for folder_name in folder_names:

    # Open files.
    file_names = natsorted(os.listdir("C:/" + folder_name))

    # For every file.
    for file_name in file_names:

        # Read file contents.
        stuff = read_file("C:/" + folder_name + "/" + file_name)

        # This is the list of words in order of the text.
        # We need to preserve the order because we require positions.
        # 'preprocessing' function does some basic punctuation removal,
        # stopword removal etc.
        final_token_list = preprocessing(stuff)
        
        #print token
        print("token")
        print(final_token_list)

        #stopword, print stopword

        final_token_list=[w for w in final_token_list if not w in stop_words]

        print("stopword")
        print(final_token_list)


        # For position and term in the tokens.
        for pos, term in enumerate(final_token_list):

            # First stem the term.
            term = stemmer.stem(term)

            # If term already exists in the positional index dictionary.
            if term in pos_index:

                # Increment total freq by 1.
                pos_index[term][0] = pos_index[term][0] + 1

                # Check if the term has existed in that DocID before.
                if fileno in pos_index[term][1]:
                    pos_index[term][1][fileno].append(pos)

                else:
                    pos_index[term][1][fileno] = [pos]

            # If term does not exist in the positional index dictionary
            # (first encounter).
            else:

                # Initialize the list.
                pos_index[term] = []
                # The total frequency is 1.
                pos_index[term].append(1)
                # The postings list is initially empty.
                pos_index[term].append({})
                # Add doc ID to postings list.
                pos_index[term][1][fileno] = [pos]

                # Map the file no. to the file name.
        file_map[fileno] = "C:/" + folder_name + "/" + file_name

        # Increment the file no. counter for document ID mapping
        fileno += 1

print("-------------------------------------------------------------------------")
print(pos_index)
print("-------------------------------------------------------------------------")

for key in pos_index.keys():
    print(key, ":", pos_index[key])




# Sample positional index to test the code.
'''
sample_pos_idx = pos_index["a"]
print("Positional Index")
print(sample_pos_idx)

file_list = sample_pos_idx[1]
print("Filename, [Positions]")
for fileno, positions in file_list.items():
    print(file_map[fileno], positions)

'''