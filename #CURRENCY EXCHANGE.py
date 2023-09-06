#CURRENCY EXCHANGE 
a = int(input(('''Choose which currency you want to Exchange
              1.INR
              2.EURO
              3.DOLLAR
              4.POUNDS
              ''')))
if a==1:
    INR=int(input("ENTER THE CURRENCY IN INR:"))
    EURO=INR*.011
    DOLL=INR*.012
    POUNDS=INR*.0096
    print(f"In Euro:{EURO}")
    print(f"In dollar:{DOLL}")
    print(f"In Pounds:{POUNDS}")
if a==2:
    EURO=int(input("Enter the Amount in EURO "))
    INR=EURO*89.32
    DOLL=EURO*1.08
    POUNDS=EURO*0.86
    print(f"in INR:{INR}")
    print(f"In dollar:{DOLL}")
    print(f"In Pounds:{POUNDS}")
if a==3:
    DOLL=int(input("Enter the Amount in DOLLAR "))
    INR=DOLL*82.72
    EURO=DOLL*.93
    POUNDS=DOLL*.79
    print(f"in INR:{INR}")
    print(f"In EURO:{EURO}")
    print(f"In Pounds:{POUNDS}")
if a==4:
    POUNDS=int(input("Enter the Amount in POUNDS "))
    INR=POUNDS*104.
    EURO=POUNDS*1.17
    DOLL=POUNDS*1.26
    print(f"in INR:{INR}")
    print(f"In EURO:{EURO}")
    print(f"In DOLLAR:{DOLL}")
else:
    print("invalid input")