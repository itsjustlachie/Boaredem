created_file = open("Gay.txt", "x")

print(open("Gay.txt", "r").read() == False)

my_file = open("Gay.txt", "w")
my_file.write("Open This For Free V-Bucks and $19 Fortnite Card\n")
my_file.write("VVVVVVVVV\n")
my_file.write("bit.ly/3oalbB7")
my_file.close()

my_file = open("Gay.txt", "r")
print(my_file.read())
