# Day 4 — if, elif, else
# Network device status checker

print('Enter device status (up/down/unknown):')

status=input()

if status=="up":
    print("Device is online and reachable")
    print("No action needed")

elif status=="down":
    print("Warning: Device is ofline")
    print('Sending alert to network team')

elif status=="unknown":
    print("Status can not be determined")
    print("Runing diagnostic check")

else:
    print("Invalid status entered")
    print("pleas enter up,down or unknown")
    