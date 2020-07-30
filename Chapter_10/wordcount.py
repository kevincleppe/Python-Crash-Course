def word_count(filename):
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print("Sorry we cant't find the file")
        pass
    else:
        words= contents.split()
        num_words=len(words)
        print(num_words)

filename=['million.txt','nothere.txt', 'red.txt','alice.txt','notreal.txt']
for files in filename:
    word_count(files)