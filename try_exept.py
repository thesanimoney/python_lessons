try:
  f = open("myfile.txt", 'x')
  try:
    f.write('My file content bla bla bla')
  except:
    print("Something went wrong when writing to the file")
  finally:
    f = open('myfile.txt', 'r')
    print(f.read())
    f.close()
except:
  print("Something went wrong when opening the file")