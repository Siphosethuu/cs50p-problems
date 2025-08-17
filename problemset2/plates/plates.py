def main():
  plate = input("Plate: ")
  if is_valid(plate):
    print("Valid")
  else:
    print("Invalid")
						
def is_valid(plate: str)-> bool:
  if not (2 <= len(plate) <= 6 and all(x.isalpha() for x in plate[:2])):
    return False
  plate = plate[2:]
  for index, char in enumerate(plate):
    if char.isalpha():
      continue
    elif char.isdigit():
      return all(x.isdigit() for x in plate[index:]) and "0" != char
		else:
      return False
  return True												

if __name__ == "__main__":
  main()
