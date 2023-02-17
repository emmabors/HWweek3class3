# Excercise 1

words = ['this' , 'is', 'a', 'sentence', '.']
#inplace**
#dont hardcode it to 5 indecies, make it so you can put in any list at all and reverse it

def swap(words):
    words[0], words[1], words[2], words[3], words[4] = words[4], words[3], words[2], words[1], words[0]
    return words

print(swap(words))

# Excercise 2

a_text = 'In computing, a hash table hash map is a data structure which implements an associative array abstract data type, a structure that can map keys to values. A hash table uses a hash function to compute an index into an array of buckets or slots from which the desired value can be found'

# to find the word count in our string, create an empty dictionary called amount and split our string so every word is an indvidual element in the string
# for every word in the split string, if the word appears once, then the key becomes the word and the value is equal to 1.
# if the words appears twice then the key becomes that word, the value is equal to 2 and so on...
# when the loop ends, the dictinary is formed and we can call the defined function

def word_count(a_text):
    amount = dict()
    words = a_text.split()
    
    for word in words:
        if word in amount:
            amount[word] += 1
        else:
            amount[word] = 1
            
    return amount

print(word_count(a_text))

# Excercise 3


list1 = [2,7,56,24,98,100]


def linear_search(list1, target):
    for i in range(len(list1)):
        num = list1[i]
        if num == target:
            return f'{target} found at index: {i}'
    return -1

print(linear_search([2,7,56,24,98,100], 56))