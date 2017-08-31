import random
def go(count,n):

    if count <3:

        try:
            user_input = int(input("Guess the number please: "))
        except ValueError:
            print("Please enter a number.")
            exit()

        if user_input == n: #checks if the guess is correct
            print("That's correct! you are awesome!!!")
            exit()
        elif user_input == n+1 or user_input == n-1:
            print("hot")
            count += 1
            go(count,n)
        elif user_input == n + 2 or user_input == n - 2:
            print("warm")
            count += 1
            go(count,n)
        else:
            print("cold")
            count += 1
            go(count,n)
    else:
        exit()

nums = [i for i in range(1, 11)] #creates random numbers from 1 to 10
random.shuffle(nums)
print(nums[0])
n=nums[0]
count=0
go(count,n)


