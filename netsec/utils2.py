import urllib3
from urllib3.exceptions import InsecureRequestWarning

from ros import Ros
import traceback
from ros.inteface.ethernet import InterfaceEthernet

urllib3.disable_warnings(InsecureRequestWarning)


def get_interface_data(ip):
    try:
        ros = Ros(f"https://{ip}/", "ajswa", "840bia")

        # Retrieve list of interfaces
        interfaces = ros.interface()

        # Find the desired interface by name (e.g., "eth0")
        for interface in interfaces:
            pass
            # Print the id attribute
            return interface

        else:
            pass

    except Exception as e:
        print("An error occurred:")
        traceback.print_exc()


# Usage example
ip_address = "192.168.4.1"
# inter = "ether1"
get_interface_data(ip_address)
