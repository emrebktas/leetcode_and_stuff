def get_binary(binary):
    binary = binary[::-1] #to calculate the binary value we reverse the string so we can iterate it with for loop.
    result = 0
    for i in range(4):
        if binary[i] == "0":
            pass
        if binary[i] == "1":
            result += 2**i
    return result

x = input().split(",")

for i in x:
    if get_binary(i) % 5 == 0:
        print(i)











