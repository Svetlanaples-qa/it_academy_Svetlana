

x = 100  # Global

def outer():
    x = 50  # Enclosed
    print("")

    def inner():
        x = 10  # Local
        print(x)

    inner()

outer()


x = 10  # Global

def outer():
    x = 100  # Local
    print("Внутри функции:", x)




a = [2, 4, 6, 7, 2, 1]
print(min(a))

b = [2, 4, 6, 7, 2, 1]
print(max(b))

c = [2, 4, 6, 7, 2, 1]
print(sorted(c))

d = [2, 4, 6, 7, 2, 1]
print(sum(d))

e = 'vnfjndfknkdyfjmykfv'
print(len(e))

for i in range(56, 171):
    if i % 2 == 0:
        print(i)

j = 'dndjfndkfjvkfvdfv'
print(type(j))

s, n = int(input()), int(input())
for _ in range(s,n+1,1):
    print(_)


