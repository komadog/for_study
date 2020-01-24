#List Comprehensions
'''
整数x,y,z,nをそれぞれ入力
i,j,kが 0<i<x, 0<j<y, 0<k<zの関係にあり、かつi+j+k!=nとなる
[i,j,k]を網羅したリストを出力する
'''

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
print([ [i,j,k] for i in range( x + 1) for j in range( y + 1) for k in range( z + 1) if ( ( i + j + k ) != n )])


#スマートに書かないとこういう形になる
#出力結果は同じ
'''
x = int(input())
y = int(input())
z = int(input())
n = int(input())
ar = []
p = 0
for i in range ( x + 1 ) :
    for j in range( y + 1):
        for k in range( z + 1):
            if i+j+k != n:
                ar.append([])
                ar[p] = [ i, j, k ]
                p+=1
print(ar)
'''
