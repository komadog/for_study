'''
テストの結果をインプット
入力人数を入力後、名前、点数の順で入力していく。

・縛り
人数は2<=n<=5
常に下から二番目の人は存在する（全員同率1位はない）

下から2位の点数の人の名前を出力する
同率2位がいる場合は名前をA-Z順で改行して出力

'''
marksheet = []
for _ in range(0,int(input())):
    marksheet.append([input(), float(input())])
set_score = set([marks for name, marks in marksheet]) #setで重複を排除して、得点のみにする
list_score = list(set_score) #再list化
list_sort = sorted(list_score) #ソート
second_score = list_sort[1] #２位のスコアを取得
second_score_names = ('\n'.join([a for a,b in sorted(marksheet) if b == second_score]))
print(second_score_names)

'''
set化とlistの中のlistから指定して取り出す方法などのメモ

marksheet = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41.0], ['Harsh', 39.0]]
list_name = [a for a,b in marksheet]
list_name_sorted = sorted([a for a,b in marksheet])
list_score = [b for a,b in marksheet]
list_score_sorted = sorted([b for a,b in marksheet])
print(list_name)
#['Harry', 'Berry', 'Tina', 'Akriti', 'Harsh']
print(list_name_sorted)
#['Akriti', 'Berry', 'Harry', 'Harsh', 'Tina']
print(list_score)
#[37.21, 37.21, 37.2, 41.0, 39.0]
print(list_score_sorted)
#[37.2, 37.21, 37.21, 39.0, 41.0]

#ここからはlist→setへの変換もあり(スコアのみ重複なのでスコアのみでテスト)
set_score = set([b for a,b in marksheet])
set_score_sorted = sorted(set([b for a,b in marksheet]))
print(set_score)
#{41.0, 37.2, 37.21, 39.0}
#重複要素が排除される
print(set_score_sorted)
#[37.2, 37.21, 39.0, 41.0]
#sortedのタイミングで再リスト化される
#setを後からすると下記のようになる
set_score_sorted_set = set(sorted([b for a,b in marksheet]))
print(set_score_sorted_set)
#{41.0, 37.21, 37.2, 39.0}
'''
