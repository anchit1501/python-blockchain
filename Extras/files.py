# f = open('demo.txt', mode='w')
# f.write('Add this content!\n')

f = open('demo.txt', mode='r')    
# file_content = f.readlines()
# f.close()

# for line in file_content:
#     print(line[:-1])


f = open('demo.txt', mode='r') 
line = f.readline()
while line:
    print(line)
    line = f.readline()
f.close()