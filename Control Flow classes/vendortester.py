vendor = str(input("Enter the vendor you want to automate: "))



if vendor == "cisco_ios":
    print("""
    show ip int br
    shot interface desc
    show ip bgp summ""")

elif vendor == "arista":
    print("""show mlag config-sanity""")

else:
    print("Por favor digite um vendor válido...")

