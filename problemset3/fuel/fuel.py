def main():
  while True:
    fraction = input("Fraction: ")
    try:
      percent = get_percent(fraction)
    except (ValueError, ZeroDivisionError):
      percent = None
    if percent:
      print(percent)
      break
																								
																								
def get_percent(fraction: str)-> str:
  x, y = fraction.split("/")
  x = float(x)
  y = float(y)
  match (x, y):
    case (x, y) if x > y:
      return None
    case (x, y) if not (0 != x % 1 or 0 != y % 1 or 0 > x):
      percent = int(x / y * 100)
      if percent >= 99:
        return "F"
      elif percent <= 1:
        return "E"
      return f"{percent}%"
    case _:
      raise ValueError

						
						
						
if __name__ == "__main__":
  main()
