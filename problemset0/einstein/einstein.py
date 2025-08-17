def main():
  mass = input("m: ")
	print("E:", calculate_energy(mass))

def calculate_energy(mass: str):
  c = 3 * 10 ** 8
	return int(mass) * c ** 2
						
if __name__ == "__main__":
  main()
