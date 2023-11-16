k = int(input())
f = 0 
for i in range(2,k):
    if k%i ==0:
        f+=1
if f == 0:
    print("{} is prime number".format(k))
else:
    print("{} is not a prime number".format(k))

