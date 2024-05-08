# file = open("demo.txt", "w")
file = open("demo.txt", "a")
# file.write("I am learning python from youtube")  # overwrites the file content
file.write("\nCurrently I am learning File I/O operations")  # append data at the end
file.close()
