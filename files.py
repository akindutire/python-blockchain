
#modes, a=append, w=write, r+=read/write, b=read binary, r=read only

file_handle = open('data/heck.txt', mode='w')
file_handle.write("Hello here")
file_handle.close()    

file_handle = open('data/heck.txt', mode='r')
#All contents on different lines as a string
contents = file_handle.read()

#all contents on diff. lines as list
contents = file_handle.readlines()
print(contents)