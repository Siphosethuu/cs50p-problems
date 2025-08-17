def main():
  while True:
    greeting = input("Greeting: ").strip().lower()
		if greeting:
      print(f"You get R{reward(greeting)}")
      break
												
def reward(string: str)-> int:
  if "h" != string[0]:
    return 100
  elif 5 > len(string):
    return 20
  else:
    if string[:5] != "hello":
      return 20
		return 0																								
												
												
if __name__ == "__main__":
  main()						
