import math

class Block:

    def __init__(self, i, n, size):
        self.i = i
        self.n = n
        self.size = size


def get_words():
    with open("words.txt", encoding="utf8") as file:
        return file.read().lower().split('\n')[:-1]


def set_equal_length(w1, w2):
    w1len = len(w1)
    w2len = len(w2)
    if w1len > w2len:
        neww2 = w2
        for i in range(w1len - w2len):
            neww2 += ' '
        return [(w1, neww2)]

    neww1 = w1
    for i in range(w2len - w1len):
        neww1 += ' '
    return [(neww1, w2)]


def get_score(w1, w2):
    (word_1, word_2) = set_equal_length(w1, w2).pop()
    counter, n, size = 0, 0, 1

    word_1 += ' '
    word_2 += '_'
    blocks = []
    for i in range(len(word_1)):
        if word_1[i] == word_2[i]:
            if word_1[i] == ' ' or word_2[i] == ' ':
                continue
            n += 1
            size += 1
        if word_1[i] == ' ' or word_2[i] == ' ':
            blocks.append(Block(counter, n, 1))
            n += 1
            counter = n + 1

        if word_1[i] != word_2[i]:
            blocks.append(Block(counter, n, size))
            size = 0
            n += 1
            counter = n + 1

    for index, block in enumerate(blocks):
        if not block or block.size == 0:
            blocks[index] = Block(0, 0, 0)

    return list(filter(lambda x: (x.i != 0 or x.n != 0 or x.size != 0), blocks))

def calculate_score(w1, w2, blocks):
    score = 0
    for b in blocks:
        score += b.size

    return  2.0 * score / (abs(len(w1) -  len(w2)) + 1)


def generate_subsitutions(input_word):
    rules = {}
    for word in get_words():
        rules[word] = calculate_score(input_word, word, get_score(input_word, word))  # Closeness value
    return sorted(rules, key=lambda x: rules[x], reverse=True)[:10]






if __name__ == "__main__":
    #input_word = input("Word: ").split(' ')[0]
        
    print("***WORD CHECK***")
    subs = generate_subsitutions(input("\nEnter Word -> "))
    print("\n***GENERATED WORDS ARE***")
    for sub in subs:
        print('\t' + sub)

    while input("***GENERATE AGAIN*** (y/n)") == 'y':
        subs = generate_subsitutions(input("Enter Word -> "))
        print("\n***GENERATED WORDS ARE***")
        for sub in subs:
            print('\t' + sub)
