file= open('geek.txt', 'r')
data=file.readline()
count= 0
for i in data:
    count += 1
    if not data:
        break
    print(data)
file.close()