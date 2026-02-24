#Lecture 5 finger exercise

my_str = "abcdefg"
even_index = ""

for i, s in enumerate(my_str):
    if i%2 == 0:
        even_index += s
    
print(even_index)