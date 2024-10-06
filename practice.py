i = 1
while i <= 100:
    print(i)
    i += 1

i = 100
while i >= 1:
    print(i)
    i -= 1

n = int(input("enter number : "))
i = 1
while i <= 10:
    print(4*i)
    i += 1


nums = [1, 23, 45, 6, 90, 34, 5, 100]
idx = 0
while idx < len(nums):
    print(nums[idx])
    idx += 1

heros = ["ironman", "batman", "spiderman"]
idx = 0
while idx < len(heros):
    print(heros[idx])
    idx += 1

nums = (1, 3, 5, 8, 23, 45, 67, 89, 100)

x = 45

i = 0
while i < len(nums):
    if(nums[i] == x):
        print("FOUND")

    i += 1
