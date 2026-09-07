fruits = ["pineapple","peach","apple","strawberry","blueberry"]

file= open("fruits.txt", "w")
for fruit in fruits:
    file.write(fruit+"\n")
file.close()

print("fruits written successfuly!")

file= open("fruits.txt","r")
contents = file.read()
file.close()

print("fruits in file:")
print(contents)



