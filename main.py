## Yusuf & sons
p = float(input("Enter the principal interest rate: "))
r = float(input("Enter the annual interest rate: "))
time = int(input("Enter the time in years: "))
n = int(input("Enter the number of times an interest is applied per time period: "))
si = p * (1 + (r*time))
ci = p * (1 + (r/n))**(n * time)

print(f'The Simple interest is {si}')
print(f'The Compound interest is {ci}')