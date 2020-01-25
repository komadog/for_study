'''
・インプット内容
スコアの個数をnとして入力
スコアの内訳をスペース区切りで入力

・出力内容
二番目にスコアが大きい数字を出力
2,3,6,6,5なら同率1位を省いて次点取得必要あり
'''
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
#print(list(arr))
#print(max(arr))
arr = sorted(list(arr),reverse=True)
#print(list(arr))
for i in range(n-1):
    if arr[i] != arr[i+1]:
        print(arr[i+1])
        break
    i+=1
'''
ディスカッションに記載のあったスマートな式
最大値がなくなるまで取り除いてその後改めて最大値を出す形式

i = int(input())
lis = list(map(int,input().strip().split()))[:i]
z = max(lis)
while max(lis) == z:
    lis.remove(max(lis))
print(max(lis))
'''
