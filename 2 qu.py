
min=int(input("min"))
max=int(input("max"))
        i=min
        s=0
        while i <=max:
            if i % 2==0:
                s+=i
                i+=1
                print(s)
