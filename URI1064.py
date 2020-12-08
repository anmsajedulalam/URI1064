sum=float(0.0)
pos=int(0)
avg=float(0.0)
for i in range(1,7):
    x=float(input())
    if(x>0):
        pos=pos+1
        sum=sum+x
avg=sum/pos
print(str(pos)+" valores positivos")
print("%0.1f"%(avg))
