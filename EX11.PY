print("Takshashila university")
print("Ongur tindivanam")
print("-----------------")
print("Student marklist")
print("----------------")
m1=int(input("Enter the Python Mark:"))
m2=int(input("Enter the dbms Mark:"))
m3=int(input("Enter the Industry Mark:"))
total=m1+m2+m3
print("Totalmark:",total)
avg=total/3
print("Average:",avg)
if(m1>=40,m2>=40,m3>=40):
    print("Result:pass")
else:
    print("Result:Fail")
if(total>=240):
    print("Grade:o Grade")
elif(total>=200):
    print("Grade:a+ Grade")
elif(total>=150):
    print("Grade:a Grade")
else:
    print("Grade:b Grade")
