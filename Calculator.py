def add(n1,n2):
  return n1 + n2

def substract(n1,n2):
  return n1 - n2

def multiply(n1,n2):
  return n1 * n2  

def divide(n1,n2):
  return n1 / n2  

operators={ 
  "+":add,
  "-":substract,
  "*":multiply,
  "/":divide
}

def calculator():
  num1 = float(input("What's the first number: "))
  for symbol in operators:
      print(symbol)
  new_number=True
  while  new_number:
    operations_symbol=input("Please enter an operating symbol: ")
    num2 = float(input("What's the next number: "))
    calculations=operators[operations_symbol]
    answer=calculations(num1,num2)
    print(f"{num1}{operations_symbol}{num2}={answer}")
    if input(f"Type 'y' to continue calculating with {answer}, type 'n' to start a new calculation : ")== 'y':
      num1=answer
    else:
      new_number=False
      calculator()

calculator()


