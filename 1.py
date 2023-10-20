count = 0
count1 = 0
count2 = 0
file_open = open('sample.ini')
data = file_open.read()

for vowels in data:
    if vowels in ["a","e","i","o","u"]:
        count += 1
        print(f"vowel count {count}")
for letter in data:
    count1 += 1
    print(f"{count1}")
for num in data:
    if num.isdigit():
        count2 += 1
        print(count2)