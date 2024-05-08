count = 0

with open("practice.txt","r") as f:
    data = f.read()

    number = data.split(",")
    for value in number:
        if(int(value) % 2 ==0):
            count+=1

print("Even numbers are",count)