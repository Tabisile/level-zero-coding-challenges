def common(string1,string2):
    common_letters_list = []
    for a in string1:
        if(a in string2):
            common_letters_list.append((a) + ',')
    print('Common letters: ', *common_letters_list)

