sentence = [int(i) for i in input().split()]

def has_33(sentence):
    for i in range(len(sentence)):
        if sentence[i] == 3 and sentence[i-1] == 3:
            print(True)
            break
        else:
            print(False)
            break

has_33(sentence)