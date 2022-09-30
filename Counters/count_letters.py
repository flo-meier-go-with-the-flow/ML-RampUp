from collections import Counter
import matplotlib.pyplot as plt

def count_letters(filename):
    letter_counter = Counter()
    with open(filename) as file:
        for line in file:
            line_letters = [
                char for char in line.lower() if char.isalpha()
            ]
            letter_counter.update(Counter(line_letters))
    return letter_counter

if __name__=='__main__':
    letter_counter= count_letters('text.txt')
    print(letter_counter)


    x=[i for i in letter_counter.keys()]
    y=[i for i in letter_counter.values()]
    x,y = zip(*letter_counter.items())
    plt.bar(x,y)
    plt.show()