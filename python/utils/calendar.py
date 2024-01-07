def day_of_week(year, month, day):
    # Array of month adjustments
    t = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]

    # Adjust year for January and February
    if month < 3:
        year -= 1

    # Calculate day of the week
    return (year + year // 4 - year // 100 + year // 400 + t[month - 1] + day) % 7


def weekdays(day):
    return [
        "Sunday",
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
    ][day]


def print_date(year, month, day):
    weekday = day_of_week(year, month, day)
    print(f"The day of the week for {year}-{month}-{day} is {weekdays(weekday)}.")
