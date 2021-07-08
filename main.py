import fileinput
import csv
import cProfile
import os
import psutil

def func():

    replace_texts = dict()   # dictionary for lookup for english words to replace with french words
    f = open("demo.csv")   # Given dictionary file  english,french
    for line in f:
        line = line.strip('\n')
        (key, val) = line.split(",")
        replace_texts[key] = val

    word_frequency = dict()  # dictionary to store frequency of replaced english words
    word_file = open("t8.shakespeare.txt", "r")
    content = word_file.read()
    word_list = content.split(" ")
    word_file.close()

    # ############# Frequency of Each word replaced #######################
    for i in replace_texts:
        word_frequency[i] = 0  # initialising frequency of each english word to zero '0'

    for search_text in replace_texts:
        for word in word_list:
            if search_text == word:
                word_frequency[search_text] += 1
            elif search_text + "\n" == word:
                word_frequency[search_text] += 1

    # ########################### Creating Frequency.csv ###############################

    # field names
    fields = ['English word', 'French word', 'Frequency']

    # data rows of csv file
    rows = []
    for text in replace_texts:
        if word_frequency[text] > 0:
            row = [text, replace_texts[text], word_frequency[text]]
            rows.append(row)

    # name of csv file
    filename = "frequency.csv"

    # writing to csv file
    with open(filename, 'w') as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)

        # writing the fields
        csvwriter.writerow(fields)
        # writing the data rows
        csvwriter.writerows(rows)

    # ##################################### Replacing english words to french ############################

    for line in fileinput.input('t8.shakespeare.txt', inplace=True):
        for search_text in replace_texts:
            replace_text = replace_texts[search_text]   # replacing english word with french
            line = line .replace(search_text, replace_text)

        print(line, end=' ')

    print("Success!")


func()
# function to calculate script run-time
cProfile.run('func()')
process = psutil.Process(os.getpid())
print(process.memory_info().rss/1024)  # in MBs

