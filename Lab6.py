def simple_calculator(string):
    try:
        return eval(string, {}, {})
    except:
        return 'ERR'

def main():
    equation = input()
    while equation:
        print(simple_calculator(equation))
        equation = input()

def subtract(a: int, b: int) -> int:
    return a - b

def multiply(a: int, b: int) -> int:
    return a * b

def divide(a: int, b: int) -> float:
    if(a != 0) and (b != 0): return a / b
    else: return 'Error'