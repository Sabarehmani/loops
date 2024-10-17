i = 1
while i <= 5:
    print(i)
    if(i==  3):
        break
    i += 1

    print("end of loop")



nums = (1, 3, 5, 8, 23, 45, 67, 89, 100)

x = 45

i = 0
while i < len(nums):
    if(nums[i] == x):
        print("FOUND at idx", i)
        break
    else:
        print("finding....")
    i += 1
    print("end of loop")
