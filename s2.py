students = int(input())
line1 = input()
line2 = input()
line1 = line1.split(' ')
line2 = line2.split(' ')
def createDic(seq1, seq2):
    start = {}
    for key in seq1:
        for value in seq2:
            start[key] = value
            seq2.remove(value)
            break
    return start

all = createDic(line1,line2)

def check(look):
    for key,value in look.items():
        if key == value:
            return "bad"
        else:
            for i , x in look.items():
                if key == x:
                    if value != i:
                        return "bad"
    return "good"
if students % 2 != 0:
    print('bad')
else:
    print(check(all))