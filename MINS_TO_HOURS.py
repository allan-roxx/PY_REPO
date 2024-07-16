def minutes_to_hours(minutes):
    hours= minutes/60
    return hours

convert=minutes_to_hours(540)
int(convert)
print(f" that is {int(convert)} hours")