def main():
    path='/home/howard/Documents/nvim/python/CISP71_Files_OS_Examples/CISP71_Files_Examples/data/'
    f= open(path+"myFile.txt","w+")
    f=open(path+"myFile.txt","a+")
    for i in range(10):
         f.write("\nThis is line %d\r\n" % (i+1))
    f.close()   
     #Open the file back and read the contents
    #f=open(path+"myFile.txt", "r")
    # if f.mode == 'r': 
    #      contents =f.read()
    #      print (contents)
     #or, readlines reads the individual line into a list
    # fl =f.readlines()
    # for x in fl:
    #  print (x)
if __name__== "__main__":
  main()
 



