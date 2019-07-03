#MASTER YODA: Given a sentence, return a sentence with the words reversed¶

def my_func(mytext):
    new_list = mytext.split()
    result = new_list[::-1]
    print (' '.join(result))

my_func('Hello the world, this is Kate')

