#Python functions are blocks of reusable code designed to perform specific tasks. They enhance code organization, readability, and reusability, and are defined using the def keyword, followed by the function name and parentheses.
'''
def function_name(parameters):
    # Function body
    return value


python code----

def player(name, age, runs, matches):
    print(f"My name is {name}")
    print(f"And, I am {age} years old")
    print(f"I played {matches} matches")
    print(f"I scored {runs} runs")
    print()

player("Dhoni", 43, 10000, 300)
player("Virat", 38, 20000, 250)
player("Rohit", 37, 15000, 220)


code output ---

My name is Dhoni
And, I am 43 years old
I played 300 matches
I scored 10000 runs

My name is Virat
And, I am 38 years old
I played 250 matches
I scored 20000 runs

My name is Rohit
And, I am 37 years old
I played 220 matches
I scored 15000 runs

python code---

def display_invoice(username,amount,due_date):
    print(f"Hello {username}")
    print(f"your bill of ${amount:.2f} is due:{due_date}")

display_invoice("kamal haasan",102.20,"01/03")
    
code output ---

Hello kamal haasan
your bill of $102.2 is due:01/03

python code ---

def display_invoice(username, amount, due_date):
    print("="*30)
    print("        INVOICE")
    print("="*30)
    print(f"Name     : {username}")
    print(f"Amount   : ₹{amount:.2f}")
    print(f"Due Date : {due_date}")
    print("="*30)

display_invoice("Kamal Haasan", 102.20, "01/03")

output code ---

==============================
        INVOICE
==============================
Name     : Kamal Haasan
Amount   : ₹102.20
Due Date : 01/03
==============================

python code----

def add(x,y):
    return x+y
print(add(3,4))


def sub(x,y):
    return x-y
print(sub(3,4))


def mul(x,y):
    return x*y
print(mul(3,4))


def div(x,y):
    return x/y
print(div(3,4))


output code ---

7
-1
12
0.75

python code ---


def calculater(x, y):
    def add(x, y):
        return x + y

    def sub(x, y):
        return x - y

    def mul(x, y):
        return x * y

    def div(x, y):
        return x / y

    print(f"Addition: {add(x, y)}")
    print(f"Subtraction: {sub(x, y)}")
    print(f"Multiplication: {mul(x, y)}")
    print(f"Division: {div(x, y):.2f}")

calculater(2, 3)

code output ----

Addition: 5
Subtraction: -1
Multiplication: 6
Division: 0.67


