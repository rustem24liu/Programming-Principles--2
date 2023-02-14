sentence = [str(i) for i in input().split()]
result = []
def reverse(sentence):
    res = sentence[::-1]
    # print(res)
    for i in range(len(res)):
        print(res[i], end = ' ')
reverse(sentence)