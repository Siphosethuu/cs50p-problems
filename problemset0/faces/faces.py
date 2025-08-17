def main():
  string = input().strip()
	new_string = faces(string)
	print(new_string)

def faces(string):
	dct = {":)": "😊", ":(": "🙁" }
	for face in dct:
    string = string.replace(face, dct[face])
	return string

if __name__ == "__main__":
	main()
