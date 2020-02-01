
#modes, a=append, w=write, r+=read/write, b=read binary, r=read only

with open('data/heck.txt', mode='w') as file_handle:
    file_handle.write("Hello here")


with open('data/heck.txt', mode='r') as file_handle:
    #All contents on different lines as a string
    contents = file_handle.read()

    #all contents on diff. lines as list
    contents = file_handle.readlines()
    print(contents)

    line = file_handle.readline()
    while line:
        print(line)
        line = file_handle.readline()