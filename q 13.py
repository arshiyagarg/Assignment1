import datetime as dt
yr = int(input("Enter the birth year: "))
curr = dt.datetime.now()
ans = curr.year - yr
print("Age: ", ans)