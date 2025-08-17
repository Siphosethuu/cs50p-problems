def main():
  camel = input("camelCase: ")
  snake = to_snake(camel)
  print(f"{snake}")
						
#siphosethu_somagagu == siphosethuSomagagu
def to_snake(camel: str)->str:
  snake = ""
  for char in camel:
    if char.isupper():
      snake += "_"
    snake += char
  return snake.lower()
						
if __name__ == "__main__":
  main()
