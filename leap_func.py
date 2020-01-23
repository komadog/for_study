#Write a function
#関数を定義する
'''
うるう年の判定関数
基本４年ごとに発生
例外として100年毎から400年毎を覗いた年はうるう年ではない
ex)2100年や1900年は非うるう年。2000年はうるう年。
'''
def is_leap(year):
    leap = False
    if year%4 != 0:
        return leap
    elif year%100 == 0 and year%400 != 0:
        return leap
    else:
        return True
year = int(input("うるう年か確認したい年を半角で入力してください"))
print(is_leap(year))
