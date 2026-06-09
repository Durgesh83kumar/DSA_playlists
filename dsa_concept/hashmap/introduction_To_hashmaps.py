hashmap = {}

hashmap['one'] = 1

# Count frequency

def count_frequency(nums):
    ans = {}

    for eachNumber in nums:
        if(eachNumber in ans):
            ans[eachNumber] += 1

        else:
            ans[eachNumber] = 1

    return ans

nums = [1, 2, 2, 3, 3, 1, 1, 4, 2]
print(count_frequency(nums))



# Anagrams
def group_anagrams(words):
    anagrams = {}

    for eachWord in words:
        sorted_word = ''.join(sorted(eachWord))
        if(sorted_word in anagrams):
            anagrams[sorted_word].append(eachWord)

        else:
            anagrams[sorted_word] = [eachWord]

    # return anagrams
    return list(anagrams.values())

words = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
print(group_anagrams(words))