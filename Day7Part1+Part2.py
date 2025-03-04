from itertools import product

def evaluate(numbers, operators):
    res = numbers[0]
    
    for i, op in enumerate(operators):
        if op == '+':
            res += numbers[i + 1]
        elif op == '*':
            res *= numbers[i + 1]
        elif op == '||':  #for part 2
            res = str(res) + str(numbers[i + 1])  
            res = int(res)  

    return res




def validEquation(result, numbers):
    num = len(numbers) - 1

    
    for ops in product(['+', '*', '||'], repeat=num): #for part 1 only: "for ops in product(['+', '*'], repeat=num):"
        if evaluate(numbers, ops) == result:
            return True
    
    return False


def totalResult(input):
    totalRes = 0

    
    for line in input.strip().split("\n"):
        result, numbers = parse_line(line)

        if validEquation(result, numbers):
            totalRes += result

    return totalRes


def read(filename):
    with open(filename, "r") as file:
        return file.read()



def parse_line(line):
    
    target, nums = line.split(": ")
    numbers = list(map(int, nums.split()))
    return int(target), numbers



input = read("input1.txt")

result = totalResult(input)
print("Total Result:", result)
