import re
m = re.search("output_(\d{4})", "output_1986.txt")
print(m.group(1))

m = re.search("output_(?P<year>\d{4})", "output_1986.txt")   #(?P<name>...) 为group命名
print(m.group("year"))