import string

def disemvowel_2(sentence):
    vowel_list = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    cleaned_sentence = ''
    for s in sentence:
        if not s in vowel_list:
            cleaned_sentence += s

    return cleaned_sentence

def disemvowel(sentence):
    translator = str.maketrans({key: '' for key in 'aeiouAEIOU'})
    print(translator)
    return sentence.translate(translator)

sentence = "This website is for losers LOL!"
disemvowel(sentence)
