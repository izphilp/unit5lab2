count = 0
count1 = 0 
count2= 0
file_open = open('sample.ini','r')
data = file_open.read()

for vowels in data:
    if vowels in ["a","e","i","o","u"]:
        count += 1
        c =(f" vowel count {count}")

for letter in data:
    count1 += 1
    b =(f" letter count {count1}")

for num in data:
    if num.isdigit():
        count2 += 1
        a =(f" number count {count2}")
d = a + b + c
print(d)

with open("counts.txt","w") as fileWriter:
    fileWriter.write(d)
