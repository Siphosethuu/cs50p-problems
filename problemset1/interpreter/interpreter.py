def main():
  ans = input("Expression:").strip().replace(" ", "")
  res = calculate(ans)
  print(f"{ans} = {res}")															
						
						
def calculate(expr: str):
  operations = {("+", lambda x, y: x + y), ("-", lambda  x, y: x - y),("*", lambda x, y: x * y),("/", lambda x, y: x / y),("^", lambda x, y: x ** y)}
  for operator, funct in operations:
    if operator in expr:
      try:
        first, second = expr.split(operator)
        return funct(float(first), float(second))
      except (ValueError, ZeroDivisionError) as e:
        return (f"{str(e).capitalize()}")
    return "Use format: a + b"
						
if __name__  == "__main__":
  main()						
