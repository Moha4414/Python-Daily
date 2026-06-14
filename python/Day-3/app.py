# Day 3 — First complete program
# Network device info collector

# Ask for device information

print("--Network-device-info")
print("Enter deive name")

device_name=input()

print("pleas inter ip address")

ip_address=input()

print("Enter number of open ports")

open_ports=input()

# Convert ports to integer so we can do math

open_ports=int(open_ports)


# Calculate and display results
print('')
print('--- Summary ---')

print("device name: " +device_name)
print("ip address:"+ip_address)
print("open ports"+ str(open_ports))
print('Closed ports from first 100: ' + str(100 -open_ports))
print("The lenght of the device "+ str(len(device_name))+"charecters") 