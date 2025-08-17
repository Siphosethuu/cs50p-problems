def main():
	print("Hello, Guest!")
	file = input("File name: ").strip().lower()
	print(types(file))
						
def types(string: str)-> str:
	extensions = {
		(".txt", "text/plain"), (".jpg", "image/jpeg"),
		(".gif", "image/gif"), (".jpeg", "image/jpeg"), 
		(".png", "image/png"), (".pdf", "application/pdf"),
		(".zip", "application/zip")
	}
	for ext, typ in extensions:
		if string.endswith(ext):
			return f"{typ}"
	return "application/octet-stream"
						

if __name__ == "__main__":
	main()
