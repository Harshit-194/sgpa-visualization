import matplotlib.pyplot as plt
n=int(input("enter number of semesters:"))
sgpa=[]
semester=[]
i=0
while i<n:
    a=float(input(f"enter marks for {i+1}th semester:"))
    sgpa.append(a)
    semester.append(i+1)
    i+=1
plt.plot(semester,sgpa)
plt.xlabel("semester")
plt.ylabel("sgpa")
plt.title("sem wise sgpa")
plt.show()