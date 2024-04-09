words=input()

def thingy(words):
    list = words.split(' ')

    char=list[0]

    frag = list[1:]

    occur = frag.count()

    if char in frag == 1:
        print(occur, char)
    else:
        print(" ")
        
    