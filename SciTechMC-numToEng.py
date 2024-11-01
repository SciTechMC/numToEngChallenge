#V 1.0.0

def numToEng(number):
    import random
    """ When given an integer or string between 0 and 999 included, will return the number writen in plain english as a string"""
    
    if number == 0:
        return "zero"

    numberLst = [int(i) for i in str(number)]
    if len(numberLst) < 3:
        while(len(numberLst) < 3): numberLst = [0]+numberLst
    out_String = []

    def stringToList(text):
        nonlocal out_String
        out_String = out_String + [text]

    numbers = [0,1,2,3,4,5,6,7,8,9]
    single = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    doubles = ["", "", "twenty ", "thirty ", "fourty ", "fifty ", "sixty ", "seventy" , "eighty ", "ninety "]
    ten = ["","eleven", "twelve", "thirteen", "fourteen", "fifteen"]


    if numberLst[0] >= 1:
        stringToList(str(single[numberLst[0]]))
        stringToList(" hundred ")


    if numberLst[1] == 1:
        if numberLst[2] < 6:
            stringToList(ten[numberLst[2]])
        if numberLst[2] >= 6 or numberLst[2] == 4:
            stringToList(single[numberLst[2]])
            stringToList("teen")
    elif numberLst[1] != 1:
        stringToList(doubles[numberLst[1]])
        stringToList(single[numberLst[2]])

    cleared_string = []
    for i in out_String:
        if i != '':
            cleared_string = cleared_string + [i]
    out_String = cleared_string

    out_String = ''.join(out_String)
    return out_String


if __name__ == "__main__":
    choice = input("Type in  number from 0 to 999 included or type 'tests' to do automated tests: ")
    if choice == "tests":
        tests = [0,1,11,16,90,99,100,101,115,999]
        for i in range(len(tests)):
            print("Your number is: " + numToEng(tests[i]) + "!")
    try:
        choice = int(choice)
        if 0 <= choice <= 999:
            print("Your number is: " + numToEng(choice) + "!")
    except:
        print("Wrong choice, restart the application.")