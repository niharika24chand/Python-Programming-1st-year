class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    # To display complex number
    def display(self):
        print(f"{self.real} + {self.imag}i")

    # To add two complex numbers
    def add(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    # To subtract two complex numbers
    def subtract(self, other):
        return ComplexNumber(self.real - other.real, self.imag - other.imag)

    # To multiply two complex numbers
    def multiply(self, other):
        real_part = (self.real * other.real) - (self.imag * other.imag)
        imag_part = (self.real * other.imag) + (self.imag * other.real)
        return ComplexNumber(real_part, imag_part)

# Get first complex number from user
r1 = int(input("Enter real part of first complex number: "))
i1 = int(input("Enter imaginary part of first complex number: "))
num1 = ComplexNumber(r1, i1)

# Set second complex number manually
num2 = ComplexNumber(4, 3)  # You can change this to anything

print("\nFirst complex number:")
num1.display()

print("Second complex number:")
num2.display()

# Perform operations
sum_result = num1.add(num2)
diff_result = num1.subtract(num2)
mul_result = num1.multiply(num2)

# Display results
print("\n--- Results ---")
print("Sum:")
sum_result.display()

print("Difference:")
diff_result.display()

print("Multiplication:")
mul_result.display()
