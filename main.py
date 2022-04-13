f = open("myfile.txt", "r")

text = f.readlines()
text_str2 = ' '.join(map(str, text))
text_str2 = text_str2.upper()

text_lst = text_str2.split()

for  item in text_lst:
   if item == "AND":
      text_lst[text_lst.index(item)]= "44"

for  item2 in text_lst:
   if item2 == "OR":
      text_lst[text_lst.index(item2)]= "45"

for  item3 in text_lst:
   if item3 == "I":
      text_lst[text_lst.index(item3)]= "46"


text_str = ' '.join(map(str, text_lst))

new = text_str.replace ('44', '\n44')
new2 = new.replace('45', '\n45')
new3 = new2.replace('46', '\n46')


g = open("newfile.txt", "w")

g.write(new3)

g.close()
f.close()