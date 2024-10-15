import sys 
import math
# 입력
n = int(sys.stdin.readline()) 
arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline()))

# 최대공약수 gcd 사용    
def gcd(arr):
    val = arr[0]
    for i in arr[1:]:
        val = math.gcd(i, val)
    return val
    
# 인접한 수의 차이 계산
diff = [abs(arr[i] - arr[i-1]) for i in range(1,n)]

diff_gcd = gcd(diff)

def find_divisors(n): 
    divisors = [] 
    for i in range(1, int(n**0.5) + 1): 
        if n % i == 0: 
            divisors.append(i) 
            if i != n // i: 
                divisors.append(n // i) 
    return sorted(divisors)
    
m = find_divisors(diff_gcd)
print(*m) 
