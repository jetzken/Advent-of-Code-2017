# task guide:
# review sequence of digits
# sum of all digits that match NEXT digit
# list is circular (first is next digit for last)
# use recursion to loop through list?

testList1 = [1,1,2,2] # return 3
testList2 = [1,1,1,1] # return 4
testList3 = [1,2,3,4] # return 0
testList4 = [9,1,2,1,2,1,2,9] # return 9

""" def CompareDigits(num1, num2):
    if num1 == num2:
        return num1
    return 0
"""

def Captcha (digits):
    total = 0
    for i in range(len(digits)):
        if digits[i] == digits[(i+1)%len(digits)]: total += int(digits[i]) # % returns 0 to len-1, guaranteed to loop back
    return total

""" print (Captcha(testList1))
print (Captcha(testList2))
print (Captcha(testList3))
print (Captcha(testList4)) """

#print (Captcha(input()))

# part 2
# sum of digits half way around

testList5 = [1,2,1,2] # return 6
testList6 = [1,2,2,1] # return 0
testList7 = [1,2,3,4,2,5] # return 4
testList8 = [1,2,3,1,2,3] # return 12

def CaptchaHalf (digits):
    total = 0
    step = int(len(digits)/2)
    for i in range(len(digits)):
        if digits[i] == digits[(i+step)%len(digits)]: total += int(digits[i])
    return total

""" print (CaptchaHalf(testList5))
print (CaptchaHalf(testList6))
print (CaptchaHalf(testList7))
print (CaptchaHalf(testList8)) """

print (CaptchaHalf(input()))