dates = []

with open("bank_statement.txt", "r") as file:
    for line in file:
        date = line.split()[1]
        if date == "Date":
            continue
        dates.append(date)
        print(dates)



    

