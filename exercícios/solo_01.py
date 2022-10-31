"""
Criação de ranking de 1 a 9
"""

"""text = 'This is awesome'
text_words = text.split()
word = input()

if word in text_words:
    print('Word found')
else:
    print('Word not found')"""

text = input()
word = input()

def search(text, word):
    if word in text:
        print('Word found')
    else:
        print('Word not found')

search(text, word)