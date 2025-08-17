def main():
  string = input("Input: ")
  output  = twttr(string)
  print(f"Output: {output}")
						
def twttr(string: str)-> str:
  vowels = ("a", "e", "i", "o", "u")
  for vowel in vowels:
    string = string.replace(vowel, "").replace(vowel.upper(), "")
  return string
												
if __name__ == "__main__":
  main()
