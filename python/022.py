# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.
# 
# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.
# 
# What is the total of all the name scores in the file?

def alpha_value(s):
    return sum([ord(x) - 64 for x in s])

file_name = 'a.txt'
file_name = '022_names.txt'
a = open(file_name, 'r')
content = a.read()
a.close()

names = [x for x in content.split('"') if x != '' and x != ',' and x != '\n']
names.sort()

value = sum([(alpha_value(x) * (i+1)) for i,x in enumerate(names)])
print(value)
print(value == 871198282)
