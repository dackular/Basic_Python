import netmiko

connection = netmiko.ConnectHandler(ip="10.0.253.238", device_type="cisco_ios", username="ait", password="ait1234")

print(connection.send_command("show ip inter brief"))

connection.disconnect()

