#!/usr/bin/env python
'''
Machine Learning homework 01 question 01
'''
'''
count a list of words
in: a list of str
out a tuple:
    list_of_count: a dictionary {word:count}
    list_of_words: a ordered list of str
'''

def cunt_fun(list_words):
    list_of_count = {}
    list_of_words = []
    for word in list_words:
        if word in  list_of_count:
            list_of_count[word] += 1
        else:
            list_of_count[word] = 1
            list_of_words.append(word)
    return list_of_count, list_of_words

'''
form to lines and output to a file
in: fw the opened file handle to hold the anser
    lst_cnt from cunt_fun
    lst_words from cunt_fun
    
out: None 
'''
def out_fun(fw,lst_cnt,lst_words):
    index = 0
    for word in lst_words:
        if index == 0:
            fw.writelines(word + " " + str(index) + " " + str(lst_cnt[word]))
        else:
            fw.writelines('\n' + word + " " + str(index) + " " + str(lst_cnt[word]))
        index += 1

if __name__ == '__main__':
    fwords = open('/Users/adam/WorkShop/machine learning/ML2017/hws/hw01/words.txt', 'r')
    fq1 = open('/Users/adam/WorkShop/machine learning/ML2017/hws/hw01/Q1.txt', 'w')
    str_of_words = fwords.read()
    str_strip_eol = str_of_words.strip('\n')
    list_of_words = str_strip_eol.split(" ")
    lst_cnt, lst_words = cunt_fun(list_of_words)
    out_fun(fq1,lst_cnt,lst_words)
    fwords.close()
    fq1.close()