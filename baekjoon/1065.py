x = int(input())
# 1. int로 받았을때
# 2. str로 받았을때의 경우가 있다.
# cnt = 0
# n은 1000보다 작거나 같은 자연수
def find_hansu(x):
    # i의 자리수 파악해서 한자리수를 저장
    # 1000의 자리수
    thou = (x // 1000)
    # 100의 자리수
    hund = int((x - thou * 1000) // 100)
    # 10의 자리수
    ten = int((x - (thou * 1000 + hund * 100)) // 10)
    # 1의 자리수
    one = x - (thou * 1000 + hund * 100 + ten * 10)
    
    if thou ==0:
        # 백의 자리수일때만 계산하면 됌
        if hund - ten == ten - one:
            # cnt += 1
            return 1
        # 두자리수 이하 일때 무조건 +1
        if hund == 0:
            return 1
    if thou != 0:
        if thou - hund == hund - ten and hund - ten == ten - one:
            # cnt += 1
            return 1
    return 0
sum = 0
# 등차수열인지 확인
for i in range(1, x+1):
    sum += find_hansu(i)
print(sum)