months = [ 
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    date = input("Date: ")

    if "/" in date:

        try:

            month, day, year = date.split("/")

            month = int(month)
            day = int(day)
            year = int(year)

        except ValueError:
            pass
        else:
            if month <= 12 and day <= 31:
                break
    else:
        try:
            month_day, year = date.split(", ")
            month, day = month_day.split(" ")
            month = months.index(month) + 1
            day = int(day)
            year = int(year)
        except ValueError:
            pass
        else:
            if day <= 31:
                break

print(f"{year}-{month:02}-{day:02}")