# def count_word_frequency(sentence):
#     # Your code goes here
#     dic = {}
#     word = ""
#     lst = []
#     for i in range(len(sentence)):
#         if(sentence[i]==' '):
#             lst.append(word)
#             word = ""
#         else:
#             word += sentence[i]
#     lst.append(word)
#     # return lst

#     for word in lst:
#         if(word not in dic):
#             dic[word] = 1
#         else:
#             dic[word] += 1

#     return dic
    
#     # lst = sentence.split()
#     # for word in lst:
#     #     if(word not in dic):
#     #         dic[word] = 1
#     #     else:
#     #         dic[word] += 1

#     # return dic

def count_word_frequency(sentence):
    # Your code goes here
    dic = {}
    word = ""
    for x in range(len(sentence)):
        if(sentence[x]==" "):
            if(word not in dic):
                dic[word] = 1
                word = ""
            else:
                dic[word]+=1
        else:
            word += sentence[x]

    # if(word not in dic):
    #     dic[word] = 1
    #     word = ""
    # else:
    #     dic[word]+=1

    # _____________________ instead of this code we can use following code________________________________________
    dic[word] = dic.get(word,0) + 1
    return dic
    
sent = "hello world hello"
print(count_word_frequency(sent))
