import os
from time import sleep


a="\033[91m"
b="\033[92m"
c="\033[93m"
d="\033[0m"
                  
def main():
      try:
            os.system("clear")
            print (b+"+"*40)
            print(c+"\tAuto NgOOntOOlin :v")
            print (a+"\t  Kusus Jomblo !!")
            print (b+"+"*40)
            print (d+"""program ini akan terus berjalan\nsaat enter dipencet\ndan terus-terusan bikin dosalu nambah.\ntekan ctrl+c untuk stop.""")
            print (b+"+"*40)
            kata=input(a+"\nMasukin nama temen/mantan yg mau lu kontolin !?\n> "+d)
            while True:
                  sleep(0.5)
                  print (c+"Dasar KontooooLLL kau "+kata+" !!")
      except KeyboardInterrupt:
            ask=input(a+"\nlagi y/n ? "+d)
            if ask == "y":
                  main()
            
            elif ask == "n":
                  os.system("clear")
                  print(b+"MMMMUaaach !! :*"+d)
                  exit()
            
try:
      main()
            
except KeyboardInterrupt:
      ask=input(a+"\nlagi y/n ? "+d)
      if ask == "y":
            main()
            
      elif ask == "n":
            os.system("clear")
            print(b+"MMMMUaaach !! :*"+d)
            exit()

