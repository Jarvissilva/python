num = int(input("Enter a number: "))
a = 0
b = 1
nums = [0,1]
isFound = False

for i in range(num):
    nums.append(a+b)
    ind = nums.index(a+b,2)
    if(nums[ind] == num):
        print(f"{num} is fibonacci")
        isFound = True
        break
    else:
        a = nums[ind]
        b = nums[ind - 1]

if(isFound == False):
    print("Not fibonacci")
