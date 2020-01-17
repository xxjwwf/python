
# _*_ coding:utf-8 _*_

import time
import datetime

with open('sample.txt') as S:
  word_dict={}
  for line in S:
    for word in line:
      if word not in word_dict:
        word_dict[word] = 1
      else:
        word_dict[word] += 1
print(word_dict)
dict_sort = sorted(word_dict.items,key=lambda x:x[1],reverse=True)
print(dict_sort)
