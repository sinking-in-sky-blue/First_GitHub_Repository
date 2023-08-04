# 2023/08/04 14:42
print("Calculator:")
operator = input("請輸入+-*/:")
numA = int(input)
numB = int(input())
result = 0
if(operator == "+"):
    result = numA + numB
elif(operator == "-"):
    result = numA - numB
elif(operator == "*"):
    result = numA * numB
elif(operator == "/"):
    result = numA / numB
else:
    print("您輸入錯誤")

print(f" {numA} {operator} {numB} = {result}")