
device_list = ["Gi0","Gi1", "Gi2", "Loopback1", "Loopback2"]

for device in device_list:
    if device.startswith("L"):
        continue
    print(device)
print ("Hello world")