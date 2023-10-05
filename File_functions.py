'''file = open('demofile.txt', 'r+')

try:
    file.write('\nnew line')
except:
    print('You dont have permissions to write file')
finally:
    print(file.readlines())
    file.close()
'''

file = open('myfile.py', 'r+')
file.write('print(\'this is a new file\', True)')