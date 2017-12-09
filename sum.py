import  math

#1+2+3+....+100
# sum=0
# n=1
# while n<=100:
#     sum=sum+n
#     n=n+1
# print(sum)

def func(num):
    val=0
    n=1
    while n<=num:
        val=val+n
        n=n+1
    return val

print("func(100):", func(100))
print("func(200):", func(200))

print(math.sqrt(2))

# 1+3+7+15+31
# 2 4  8 16 32
# sum=(1+2^n)!
# 1+2^1+2^2+2^3+....2^n=
def sum(num):
    val=1
    n=1
    while n<=num:
        val=val+2**n
        n=n+1
    return val
n=int(input("请输入数值（１００－２００）:"))
while True:
    if n>=100 and n<=200:
        print(sum(n))
        break
    else:
        print("输入的必须在100-200之间")
        n=int(input("请输入数值（１００－２００）:"))
    







