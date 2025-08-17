def main():
  for _ in range(5):
    time = input("what is the time? ")
    time = convert(time)
    decider(time)
    
def convert(time: str) -> float:
  hour, minutes = time.split(":", 1)
  hour, minutes = float(hour), float(minutes[:2]) / 60
  if time.endswith("p.m"):
    hour += 12
  return hour + minutes
        
def decider(time: float):
  if 7 <= time <= 8:
    print("Breakfast time!")
  elif 12 <= time <= 13:
    print("Lunch time.")
  elif 18 <= time <= 19:
    print("dinner time.")
        
        
if __name__ == "__main__":
  main()
        
