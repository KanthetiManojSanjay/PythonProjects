f = open("sample.txt", "r")
print(f.read())  # f.read(noofChar) then it will read mentioned no of characters only
f.seek(0)  # To move the file cursor
print(f.readline())  # Above mentioned noOfChar read is there for readLine as well
f.seek(0)
print(f.readlines())
f.close()
