
file_open = open('sample.ini','r')
data = file_open.read()

for vowels in data:
    if vowels in ["a","e","i","o","u"]:
        count = 0
        count += 1
        print(f"vowel count {count}")

for letter in data:
    count1 = 0
    count1 += 1
    print(f"letter count {count1}")

for num in data:
    if num.isdigit():
        count2 = 0
        count2 += 1
        print(f"number count {count2}")


#with open("counts.txt","w") as fileWriter:
   # fileWriter.write(str(a))
