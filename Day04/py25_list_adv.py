# 리스트 고급 사용
# 1~1000까지 사이에서 3의 배수값 리스트

# 1번 방법
list_3rd = []
for n in range(1, 1000+1) : # 1부터 1000까지
    if n % 3 == 0 : # 3의 배수이면
        list_3rd.append(n)

#print (list_3rd)

# 2번 방법
list_3rd_2 = [n for n in range(3, 1000+1, 3)] # 3부터 1000까지 3씩 올라감
#print(list_3rd_2)

# 3번 방법
list_3rd.clear() # list_3rd 값 초기화
for n in range(3, 1000+1, 3) : 
    list_3rd.append(n)

#print (list_3rd)    

#print([2 * x for x in range(1, 10+1)]) # 1부터 10까지의 값의 2배수
#print([3 * x for x in range(1, 333+1)]) # 1부터 333까지의 값의 3배수

# 4번 방법
list_3rd = []
for n in range(1, 1000+1):
    if n % 3 == 0 : # 3의 배수이면
        list_3rd.append(n)

#print([x for x in range(1,101) if x % 3 == 0]) # for문 if문 전부 처리

# 2중 for문
# zip하고 유사
#print([(x, y) for x in ['광어', '고등어', '참치'] for y in['한돈', '한우', '한계']])

l1=[]
for x in ['광어', '고등어', '참치'] :
    for y in ['한돈', '한우', '한계'] :
        l1.append((x,y))
#print(l1)
l1.clear()

# 2중 if문
print([x for x in range(10+1) if x < 5 if x % 2 == 0]) # 10까지의 숫자 중에서 5보다 작은 짝수 (0포함)

for x in range(10+1):
    if x < 5:
        if x % 2 == 0:
            l1.append(x)
print(l1)

print(tuple([x * 2 for x in range(1, 5+1)]))