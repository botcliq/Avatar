word_list = ['cat','dog','rabbit']
letter_list = [ ]
for a_word in word_list:
    for a_letter in a_word:
        if a_letter not in letter_list:
            letter_list.append(a_letter)
#ter_list = list(set(letter_list))
print(letter_list)

print("List Comprehension !!")
[[letter_list.append(a_letter) for a_letter in a_word] for a_word in word_list]
print(letter_list)
