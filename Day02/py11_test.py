# 1번
hong = {'국어' : 80, '영어': 75, '수학' : 55}
print(hong.values())
sum = 0
for item in hong.values():
    sum += item
print(f'홍길동의 평균점수는 {sum / 3} 입니다')

# 2번
print(bool(13%2))

# 3번
pin = "881120-1068234"
yyyymmdd = pin.split('-')[0]
num = pin.split('-')[1]
# yyyymmdd=('19' + pin[0:6])
# num =(pin[7:])
print(yyyymmdd)
print(num)

# 6번
a = [1, 3, 5, 4, 2]
a.sort()
print(a)
a.reverse()
print(a)

# 11번
b = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
bSet = set(b)
c = list(bSet)
print(c)