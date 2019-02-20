Name= input("Enter your name: ")
print(" Hey,"+Name+", do you want to see something great?")
Answer = input("Type 1 for yes or type 2 for no: ")
if Answer == 2:
    print("Ok, it is your loss then.")
else:
    print("Great!!")
Mantle = input("Enter a sentence of your choice: ")
new_list = Mantle.split(' - ')
print(new_list)


for j in Mantle:
     if (j=='a' or j=='e' or j=='i' or j=='o' or j=='u'):
         print(j, end=" ")


