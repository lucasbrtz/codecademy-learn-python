def substring_between_letters(word, start, end):
    if start in word and end in word:
        return (word[word.find(start)+1:word.find(end)])
    else:
        return word


print(substring_between_letters("apple", "p", "e"))
print(substring_between_letters("apple", "p", "c"))
