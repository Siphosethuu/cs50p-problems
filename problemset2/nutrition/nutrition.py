def main():
  inp = input("Item: ").lower()
  calories = get_calories(inp)
  if calories:
    print(f"Calories: {calories}")
												
def get_calories(fruit: str)-> str:
  #I am sorry, in my mind, the only way it worked without a dict
  #tuple or list of tuples would have been parallel lists (too much work)
  fruits = { "apple": 130, "avocado": 50, "banana": 110, "cantaloupe": 50, "grapefruit": 60, "grapes": 90, "honeydew melon": 50, "kiwifruit": 90, "lemon": 15, "lime": 20, "nectarine": 60, "orange": 80, "peach": 60, "pear": 100, "pineapple": 50, "plums": 70, "strawberries": 50, "sweet cherries": 100, "tangerine": 50, "watermelon": 80 }
  if fruit in fruits:
    return f"{fruits[fruit]}"
  return ""



if __name__ == "__main__":
  main()
