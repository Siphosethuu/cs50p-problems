def main():
  amount = 50
  while True:
    print(f"Amount Due: {amount}")
    coin = input("Insert coin: ")
    amount = insert_coin(amount, coin)
    if 0 >= amount:
      print(f"Change owed: {amount}")
      break
																																	
def insert_coin(amount: int, coin: str)-> int:
  match coin:
    case "25" | "10" | "5":
      return amount - int(coin)
    case _:
      return amount
      
if __name__ == "__main__":
  main()
