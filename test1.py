print("basic I/L programming")
print("*********************")
n = int(input("enter the no of processes:"))
print("no of processes:",n)
a_time = []
b_time = []
for x in range(n):
    print("enter the arrival time of the process P{}".format(x+1))
    a = int(input())
    a_time.append(a)
print("total no of arrival time",a_time)
for x in range(n):
    print("enter the burst time of the peocess p{}".format(x+1))
    a = int(input())
    b_time.append(a)
print("total no of burst time",b_time)
print("PNO \t\t AT \t\t BT")
for i in range(n):
    print("p{}".format(i+1),"\t\t",a_time[i],"\t\t",b_time[i])

      

