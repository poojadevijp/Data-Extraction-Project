amounts = []

with open("bank_statement.txt", "r") as file:
    lines = file.readlines()


for line in lines[1:]:
    parts = line.split("\t")   
    amount = parts[3]          
    amounts.append(float(amount))

print("All transaction amounts:")
print(amounts)
