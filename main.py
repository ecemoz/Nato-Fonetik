import pandas

data = pandas.read_csv("eglenfonetik.csv")
phonetic_dict = {row.Harf: row.Kelime for(index, row) in data.iterrows()}

word = input("Kelimeyi girin: ").upper()
output_list = [phonetic_dict[letter] for letter in word]

print(output_list)