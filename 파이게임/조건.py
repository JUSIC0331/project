"""
a = bool(0)
b = bool(1)
c = bool(10 > 4)
print(a,b,c)

a = 100
b = 20
if a > b :
    print(a)
elif a < b :
    print(b)
else:
    print("같다")

m = 4000
if m > 5000 :
    print("택시를 타자")
else:
    print("대중교통을 이용하자")

a = ["a" , "c" , "e"]
if "c" in a:
    print("있다")
else:
    print("없다")

num = int(input())
print(num%2)
if num < 1 :
   print("홀수")
else:
   print("짝수")
"""
a = 20  
if a % 2 == 0 and a > 10 :
    print("참")
else:
    print("거짓")
