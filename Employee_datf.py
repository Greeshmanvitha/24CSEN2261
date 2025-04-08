import pickle
f=open("Employee.dat","wb")
L=[]
n=int(input("Enter No.of Employees:"))
for i in range(n):
    code=int(input("Enter code:"))
    name=input("Enter name:")
    salary=int(input("Enter salary:"))
    L=[code,name,salary]
    pickle.dump(L,f)
f.close()


f=open("Employee.dat","rb")
try:
    while True:
        L=pickle.load(f)
        print(L)
except:
    f.close()

    
OUTPUT:
Enter No.of Employees:3
Enter code:101
Enter name:suraj
Enter salary:100000
Enter code:102
Enter name:Bheeshma Pratap Singh
Enter salary:100000
Enter code:103
Enter name:Surendra
Enter salary:100000
[101, 'suraj', 100000]
[102, 'Bheeshma Pratap Singh', 100000]
[103, 'Surendra', 100000]
