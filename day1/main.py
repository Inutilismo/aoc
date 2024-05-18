from io import TextIOWrapper

with open('day1/input.txt', 'r') as f:
    input = f.read().splitlines()

sum = 0
written_digits = {
    "zero":0,
    "one":1,
    "two":2,
    "three":3,
    "four":4,
    "five":5,
    "six":6,
    "seven":7,
    "eight":8,
    "nine":9,
}

def translate(string: str) -> str:
    for word, digit in written_digits.items():
        string = string.replace(word, word+str(digit)+word)
    return string
 
output1 = 0
output2 = 0
for string in input:
    
    digits = [digit for digit in string if digit.isnumeric()]
    if digits:
        output1 += int(digits[0]+digits[-1])
    
    digits = [digit for digit in translate(string) if digit.isnumeric()]
    if digits:
        output2 += int(digits[0]+digits[-1])

print(output1)
print(output2) 
