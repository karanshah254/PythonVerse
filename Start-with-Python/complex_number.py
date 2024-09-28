x = int(input("Enter the real part of the first complex number: "))
y = int(input("Enter the imaginary part of the first complex number: "))

z = complex(x, y)

print(f"The complex number is: {z}")

print(f"The real part of the complex number is: {z.real}")
print(f"The imaginary part of the complex number is: {z.imag}")
