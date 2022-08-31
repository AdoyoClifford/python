def replace_word():
    str = 'Hi guys Iam Clifford and these are my beginner projects'
    word_to_replace = input('Enter word to replace:')
    word_replacement = input('Enter word replacement:') 
    print(str.replace(word_to_replace, word_replacement))

replace_word()