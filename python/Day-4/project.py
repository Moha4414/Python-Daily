# Day 4 Practice — Network port checker
# Checks what service is running based on port number



print('=== Port Service Identifier ===')
print('Enter a port number:')
port = int(input())

if port == 22:
    print('Port 22 — SSH (Secure Shell)')
    print('Used for: remote device management')
elif port == 23:
    print('Port 23 — Telnet')
    print('Warning: unencrypted — avoid using this')
elif port == 80:
    print('Port 80 — HTTP')
    print('Used for: web traffic unencrypted')
elif port == 443:
    print('Port 443 — HTTPS')
    print('Used for: secure web traffic')
elif port == 53:
    print('Port 53 — DNS')
    print('Used for: domain name resolution')
elif port >= 1 and port <= 1023:
    print('Port ' + str(port) + ' is a well-known port')
    print('Used for: system and network services')
elif port >= 1024 and port <= 49151:
    print('Port ' + str(port) + ' is a registered port')
    print('Used for: specific applications')
else:
    print('Port ' + str(port) + ' is a dynamic/private port')
    
    