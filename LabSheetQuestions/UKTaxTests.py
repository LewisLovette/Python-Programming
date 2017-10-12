print("%"*50)
print("Running Personal Allowance tests")
print("%"*50)
try:
    from UKTax import personalAllowance
    numbers = [0, 9000,    36000, 100000,  100001, 115000, 121100, 122905, 123000, 1000000]
    answers = [11500, 11500,   11500, 11500,   11500,  4000,   950,    48,     0,      0]
    n = len(numbers)
    count=0
    for i in range(n):
        num = numbers[i]
        ans = personalAllowance(num)
        if ans!=answers[i]:
            print("Personal Allowance test for salary £" + str(num) + " failed")
            count = count+1
    print(str(n-count) + "/" + str(n) + " personal allowance tests passed")
except ImportError:
    print("The function personalAllowance was not present in the module UKTax")
print("%"*50)
print("End of Personal Allowance tests")
print("%"*50)


print("\n")


print("%"*50)
print("Running Income Tax tests")
print("%"*50)
try:
    from UKTax import incomeTax
    numbers = [9000, 11000, 16000, 31785, 36000, 42385, 60000, 100000, 110000, 1000000]
    answers = [0,0,900,4057,4900,6177,13000,29000,35000,436100]   
    n = len(numbers)
    count=0
    for i in range(n):
        num = numbers[i]
        ans = incomeTax(num)
        if ans!=answers[i]:
            print("Income tax test for salary £" + str(num) + " failed")
            count = count+1
    print(str(n-count) + "/" + str(n) + " income tax tests passed")
except ImportError:
    print("The function incomeTax was not present in the module UKTax")
print("%"*50)
print("End of Income Tax tests")
print("%"*50)


print("\n")


print("%"*50)
print("Running National Insurance tests")
print("%"*50)
try:
    from UKTax import nationalInsurance
    numbers = [0, 100, 157, 200, 550, 700, 800, 866, 1000, 20000]
    answers = [0, 0, 0, 5, 47, 65, 77, 85, 88, 468]
    n = len(numbers)
    count=0
    for i in range(n):
        num = numbers[i]
        ans = nationalInsurance(num)
        if ans!=answers[i]:
            print("National Insurance test for salary £" + str(num) + " failed")
            print(ans, answers[i])
            count = count+1
    print(str(n-count) + "/" + str(n) + " National Insurance tests passed")
except ImportError:
    print("The function nationalInsurance was not present in the module UKTax")
print("%"*50)
print("End of National Insurance tests")
print("%"*50)


