# Day 06 — Full Chapter 2 review
# Network port scanner simulator

import random 

print("== Port Scanner Simulater ==")

print("scanning ports 20 to 25")
print("")

open_ports=[]

for port in range(20,26):
    
    # simulate a random scann
    
    is_open=random.randint(1,2)
    
    if is_open==1:
        print("port"+ str(port)+":Open")
        
        open_ports.append(port)
        
    else :
        print("port"+ str(port)+":closed")
        
print ('')

print('Scan Compplete.')
print('Total open ports found'+str(len(open_ports)))
if len(open_ports) == 0:
    print('No open ports detected. Device may be fully secured.')
elif len(open_ports) > 3:
    print('WARNING: Many open ports detected. Review firewall rules.')
else:
    print('Normal number of open ports detected.')