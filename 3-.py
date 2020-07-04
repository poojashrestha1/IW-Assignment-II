'''Write code that will print out the anagrams (words that use the same
letters) from a paragraph of text.'''

from collections import defaultdict

def anagram_checker(paragraph):

    #converting to lower case and removing special characters
    paragraph = paragraph.lower()
    words = paragraph.replace('.', '')

    words = words.split()

    #initializing empty dictionary of list
    anagram = defaultdict(list)

    for word in words:
        
        sorted1 = sorted(word)
        k = ''.join(sorted1)

        if k in anagram:
            continue

        for i in range(0, len(words)):
            sorted2 = sorted(words[i])
            if sorted1 == sorted2:
                anagram[k].append(words[i])

    return anagram


para = "Tired tried but not tub ton fried fired rifed"
anagram = anagram_checker(para)
for keywords in anagram:
    print(f"The anagram of {anagram[keywords][0]} are {anagram[keywords]}")