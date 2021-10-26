def vowels_in_a_string(word):
    final_name =word.lower()
    list1 = list(word)
    list2 = []
    vowels = "aeiou"
    for i in list1:
        if i.lower() in vowels:
            if i in vowels:
                list2.append(i)
    vowels_ouput = ', '.join(list2)
    return vowels_ouput

