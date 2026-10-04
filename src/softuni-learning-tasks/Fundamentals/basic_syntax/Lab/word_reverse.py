
def word_reverse(word:str):
    reversed_str = ""
    for i in range(len(word) - 1, -1, -1):
        reversed_str += word[i]
    print(reversed_str)
        
word_reverse("Python")
word_reverse("banana")