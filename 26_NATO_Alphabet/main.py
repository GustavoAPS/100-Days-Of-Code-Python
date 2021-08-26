import pandas


data = pandas.read_csv("nato_phonetic_alphabet.csv")

alphabet_dict = {}
for (index, row) in data.iterrows():
    alphabet_dict[row.letter] = row.code

name = (input("What is the word to receive in NATO?")).upper()

for letters in name:
    print(alphabet_dict[letters])
