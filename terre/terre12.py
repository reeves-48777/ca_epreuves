import sys
if len(sys.argv) > 2 or len(sys.argv[1]) > 7 or len(sys.argv[1]) < 6:
    print("erreur.")
    exit(1)

timestamp=sys.argv[1]
hour_parts=timestamp[:-2].split(':')
hour=int(hour_parts[0])
minutes=int(hour_parts[1])
suffix=timestamp[-2:]

if hour < 0 or hour > 12 or minutes < 0 or minutes > 59:
    print("erreur.")
    exit(1)

match suffix:
    case "AM":
        if hour == 12:
            hour = 0
    case "PM":
        if hour != 12:
            hour += 12
print(f"{hour}:{minutes}")