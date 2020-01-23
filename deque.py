from collections import deque
d = deque()
for i in range(int(input(""))): #操作回数の受付
    s = input("").split() #dequeに対する操作の受付とそれを操作と数字に分ける
    if s[0] == 'append':
            d.append(s[1])
    elif s[0] == 'appendleft':
            d.appendleft(s[1])
    elif s[0] == 'pop':
            d.pop()
    elif s[0] == 'popleft':
            d.popleft()
    else:
            print("その操作は無効です") #想定していない操作を受け付けた際の分岐
print(' '.join(d))

'''
過程を自分用にわかりやすくしたやつ

from collections import deque
d = deque()
for i in range(int(input("操作回数を入力してください"))): #操作回数の受付
    s = input("dequeへの操作を入力してください").split() #dequeに対する操作の受付とそれを操作と数字に分ける
    if s[0] == 'append':
            d.append(s[1])
            print(d)
    elif s[0] == 'appendleft':
            d.appendleft(s[1])
            print(d)
    elif s[0] == 'pop':
            d.pop()
            print(d)
    elif s[0] == 'popleft':
            d.popleft()
            print(d)
    else:
            print("その操作は無効です") #想定していない操作を受け付けた際の分岐
#print(d)
print(' '.join(d))
'''
