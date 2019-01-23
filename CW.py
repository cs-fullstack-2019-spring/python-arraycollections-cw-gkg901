def main():

    # ex1()
    # ex2()
    # ex3()
    # ex4()
    ex5()
# Create a function with the variable below. After you create the variable do the instructions below that.
#
# arrayForProblem2 = ["Kenn", "Kevin", "Erin", "Meka"]
# a) Print the 3rd element of the numberList.
#
# b) Print the size of the array
#
# c) Delete the second element.
#
# d) Print the 3rd element.
def ex1():

    arrayForProblem2 = ["Kenn", "Kevin", "Erin", "Meka"]

    print(arrayForProblem2[2])
    print(arrayForProblem2.__len__())
    arrayForProblem2.remove("Kevin")
    print(arrayForProblem2)
    print(arrayForProblem2[2])


# Create a function that has a loop that quits with ‘q’.
# If the user doesn't enter 'q', ask them to input another string.
def ex2():
    while True:
        ask = input("Kenn is mean. do you agree? yes or no")
        if ask == "yes":
            break




# Create a function that contains a collection of information for the following.
# After you create the collection do the instructions below that.
def ex3():
    listofNames = {

        "Johnathan": "John",
        "Michael": "Mike",
        "William": "Bill",
        "Robert": "Rob"
    }

    print(listofNames)
    print(listofNames["William"])



# Create an array of 5 numbers.
# Using a loop, print the elements in the array reverse order.
# Do not use a function
def ex4():

    nums = list(range(1,6))
    print(nums)


    x=len(nums)
    while x >= 1:
        print(nums[x-1])
        x-=1

# Create a function that will have a hard coded array then ask the user for a number.
# Use the userInput to state how many numbers in an array are higher, lower, or equal to it.
def ex5():

    p5array = list(range(1,16))
    print(p5array)

    higher = 0
    lower = 0
    equal = 0

    ask = int(input("pick a number 1 - 15"))
    for x in p5array:
        x+=1
        if x > ask:
            higher +=1
            print("higher")

        elif x < ask:
            lower +=1
            print("lower")

        elif x == ask:
            equal +=1
            print("equal")





















if __name__ == '__main__':
    main()