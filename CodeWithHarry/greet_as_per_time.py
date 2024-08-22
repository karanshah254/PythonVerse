import time

t = time.strftime("%H:%M:%S")

hour = int(time.strftime("%H"))
# hour = int(input("Enter the hour: "))


# conditions has been put in such a way that it will work for 24 hours
if 0 <= hour < 12:
    print("Good Morning")
elif 12 <= hour < 18:
    print("Good Afternoon")
else:
    print("Good Evening")
