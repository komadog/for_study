'''
生徒数N、その後に生徒名、各教科の点数%(Marks)をあたえられる。
最後に平均%を取得したい生徒名があたえられる。
2 <= N <= 10
0 <= Marks <= 100

入力に対して辞書型を活用し、小数点二桁で特定生徒の平均%を返す。
'''

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
query_scores = student_marks[query_name]
total = float(0.00)
for i in range(len(query_scores)):
    total = total + query_scores[i]
average = total/len(query_scores)
print("{0:.2f}".format(average))


# "{0:.2f}".format()
#という小数点整形があるので覚える（この場合は0.00 小数点2桁）
#2を別の数字に帰ると小数点何桁か変更可能
