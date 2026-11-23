while True:
    print("1.add the marks")
    print("2.modify the marks")
    print("3.display the marks")
    print("4.exit")

    choice=int(input("Enter your choice: "))
    if choice==1:
        m1=int(input("Enter marks of subject 1: "))
        m2=int(input("Enter marks of subject 2: "))
        m3=int(input("Enter marks of subject 3: "))
        m4=int(input("Enter marks of subject 4: "))
        A=[m1,m2,m3,m4]
    elif choice==2:
        print("1.modify marks of subject 1")
        print("2.modify marks of subject 2")
        print("3.modify marks of subject 3")
        print("4.modify marks of subject 4")
        sub=int(input("Enter your choice: "))
        if sub==1:
            A[0]=int(input("Enter new marks of subject 1: "))
        elif sub==2:
            A[1]=int(input("Enter new marks of subject 2: "))
        elif sub==3:
            A[2]=int(input("Enter new marks of subject 3: "))
        elif sub==4:
            A[3]=int(input("Enter new marks of subject 4: "))
    elif choice==3:
        print("Marks of subject 1: ",A[0])
        print("Marks of subject 2: ",A[1])
        print("Marks of subject 3: ",A[2])
        print("Marks of subject 4: ",A[3])
    elif choice==4:
        break
    