test = int(input())
all = []
for i in range(test):
    carts = int(input())
    contain = []
    for x in range(carts):
        hold = int(input())
        contain.append(hold)
    all.append(contain)
def reverse(seq):
    hold = []
    for i in range(len(seq)):
        hold.append(seq[-i-1])
    return hold
for i in range(len(all)):
    all[i] = reverse(all[i])

def check(seq, hold,  num):
    side = []
    finished = []
    for i in seq:
        if i == num:
            finished.append(i)
            break
        else:
            side.append(i)
    if len(side) > 1:
        side = reverse(side)
    seq = set(seq).difference(side, finished)
    seq = list(seq)
    if len(hold) > 0:
        for i in hold:
            side.append(i)
    return [seq, side]

def here(hold, num):
    if hold[0] == num:
        hold.remove(num)
        return hold
    return False

def total(seq, holding, num):
    if num in holding:
        answer = here(holding, num)
        if answer == False:
            return False
        else:
            return [seq, answer]
    else:
        answer = check(seq, holding, num)
        return answer
control = []
for x in range(test):
    for i in range(len(all[x])):
        finding = total(all[x], control, i+1)
        if finding == False:
            print('N')
            break
        all[0] = finding[0]
        control = finding[1]
        if i == len(all[x]) -1:
            print('Y')

