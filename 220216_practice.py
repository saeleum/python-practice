### 백준 10872 (재귀함수) 
### 성공
num = int(input())

def factorial(num):
    if num == 0 :
        return 1
    else :
        mul = num * factorial(num-1)
        return mul
         
print(factorial(num))

### 백준 2798 (브루트포스)
### 코드 길이로 실패?

arr = []
def blackJack(counts, target, numbers):
    
    for i in numbers:
        for j in numbers:
            for k in numbers:
                if (i != j) & (j != k) & (i != k):
                      if (i + j + k) <= target:
                            arr.append(i+j+k)
                            
    return max(arr)                   

input1 = input().replace(" ", ",").split(",")
counts = int(input1[0])
target = int(input1[1])

input2 = input().replace(" ", ",").split(",")
numbers = list(map(int, input2))

blackJack(counts, target, numbers)

