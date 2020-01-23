'''
Print Function

nの入力に対して
123・・・n
という結果を返す

stringは使用しない
'''
if __name__ == '__main__':
    n = int(input())
for i in range(n):
    print(i+1,end = "")

'''
他に試したもの

for i in range(3):
    print(i+1,end = "@")
>1@2@3@

for i in range(3):
    print(i+1,sep='')
>1
>2
>3

for i in range(3):
    print(i+1,end='\n')
>1
>2
>3
'''
