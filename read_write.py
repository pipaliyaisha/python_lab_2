def write_to_file(filename,content):
    with open(filename,'w')as file:
        file.write(content)
    print(f"content written to {filename}")
def read_from_file(filename):
    with open(filename,'r')as file:
        content=file.read()
    return content
content="Hello, this is a test file.\nwelcome to the file operations in python!"
filename="readwrite.txt"
write_to_file(filename,content)
file_content=read_from_file(filename)
print(f"content read from {filename}:\n{file_content}")        