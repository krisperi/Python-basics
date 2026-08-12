from getpass import getpass
from netmiko import ConnectHandler
from netmiko import NetmikoTimeoutException, NetmikoAuthenticationException

devices = ["192.168.0.20", "192.168.0.21", "192.168.0.22"]

'''
Para redes inteiras usar :

devices = []

for octeto in range(2, 254):
    devices.append(f"192.168.0.{octeto}")

'''

print(f"Devices to onboard: {devices}")


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
        print(f""""
        ###################################
        #Successfully connected to {device}#
        ###################################
        """)

        connection.send_config_from_file("commands.txt")

        print(connection.send_command("show running-config"))

        connection.disconnect()

    except NetmikoTimeoutException:
        print(f"Timeout no {device}")

    except NetmikoAuthenticationException:
        print(f"Problema de autenticação {device}")

    except Exception as e:
        print(f"Erro esquisito, verifique a vanilla no equip {device}: {e}")
