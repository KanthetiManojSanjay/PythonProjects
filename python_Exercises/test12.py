import os.path

# w-writing , a- appending , r- reading r+ reading/writing

"""
file=open("./data.csv","w+")
file.write("id,name,email\n")
file.write("1,Vivek,vivek123@gmail.com\n")
file.write("2,Sharan,sharan23@gmail.com\n")
file.write("3,Mahesh,mahirocks7@gmail.com\n")
file.close()
"""

""""
file=open("./data.csv","r")
#print(file.read())  // reads entire file at once
# for line in file:  // reads line by line
#     print(line)
print(file.readlines())   // gives data in list
file.close()
"""

file_name="data.csv"
if os.path.isfile(file_name):
    with open(file_name,"r") as file:
        print(file.read())
else:
    print(f"file {file_name} does not exist!")


