import sys

if len(sys.argv) < 2:
    print("erreur.")
    exit(1)

timestamp_parts=sys.argv[1].split(':')
if len(timestamp_parts) != 2:
    print("erreur.")
    exit(1)

hour=int(timestamp_parts[0])
minutes=int(timestamp_parts[1])
suffix="AM"

if hour < 0 or hour > 23 or minutes < 0 or minutes > 59:
    print("erreur.")
    exit(1)

if hour > 12:
    hour = hour % 12
    suffix="PM"
elif hour == 12:
    suffix="PM"
elif hour == 0:
    hour += 12

print(f"{hour}:{minutes}{suffix}")