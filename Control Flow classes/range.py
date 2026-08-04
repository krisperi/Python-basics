
for int in range(1,11):
    print(f""" 
    interface GigabitEthernet1/{int}
     shutdown
     no cdp enable
     no ip address
     switchport
    """)
