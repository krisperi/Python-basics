from getpass import getpass
from netmiko import ConnectHandler
from netmiko import NetmikoTimeoutException, NetmikoAuthenticationException

devices = ["192.168.0.1", "192.168.0.2", "192.168.0.3"]

'''
Para redes inteiras usar :

devices = []

for octeto in range(2, 254):
    devices.append(f"192.168.0.{octeto}")

'''

print("Devices to onboard: {}".format(devices))


username=input("Enter username: ")
password=getpass("Enter password: ")

for device in devices:
    try:
        connection = ConnectHandler(
            device_type="cisco_ios",
            host=device,
            username=username,
            password=password
        )
        print(""""
        ###################################
        #Successfully connected to {}#
        ###################################
        """.format(device))

        connection.send_config_from_file("commands.txt")

        print(connection.send_command("show running-config"))

        connection.disconnect()

    except NetmikoTimeoutException:
        print("Timeout no {}".format(device))

    except NetmikoAuthenticationException:
        print("Problema de autenticação {}".format(device))

    except Exception as e:
        print("Erro esquisito, verifique a vanilla no equip {}: {}".format(device, e))
