f = open('WgetRDA_URLs.txt', 'a')
i = 25001

while i:
  f.write('\nhttps://www.rd-alliance.org/user/' +str(i))
  if i == 30000:
    break
  i = i + 1


f.close()
