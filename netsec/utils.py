import json
import urllib.parse
import uuid

import requests
import routeros_api

from ros import Ros
from werkzeug.exceptions import InternalServerError
import urllib3
from urllib3.exceptions import InsecureRequestWarning

urllib3.disable_warnings(InsecureRequestWarning)
port = '8729'
host = '192.168.4.1'
username = 'ajswa'
password = '840bia'

ros = Ros("https://192.168.4.1/", "ajswa", "840bia")


def connect(host, username, password, port):
    connection = routeros_api.RouterOsApiPool(host='192.168.4.1', username='ajswa', password='840bia',
                                              plaintext_login=True,
                                              use_ssl=True,
                                              ssl_verify=False,
                                              ssl_verify_hostname=False,
                                              port='8729'
                                              )
    return connection


def get_interface_data():
    ros = Ros(f"https://192.168.4.1/", "ajswa", "840bia")
    # Connect to the RouterOS device

    # Retrieve the interfaces data

    # Process the interfaces data further
    for _ in ros.interface():
        print(ros.interface)
        print(ros.ip)

def get_interface_data1(host, username, password, port, loop):
    # Connect to the RouterOS device
    api = connect(host=host, username=username, password=password, port=port).get_api()

    # Retrieve the interface data using the /interface/print command
    response = api.get_binary_resource('/').call('/interface/print')

    # Convert the response to a list of dictionaries
    #    data = list(response)
    #    for d in data:
    #        d['actual_mtu'] = d.pop('actual-mtu')
    #        d['mac_address'] = d.pop('mac-address')
    #        d['link_downs'] = d.pop('link-downs')
    #        d['rx_byte'] = d.pop('rx-byte')
    #        d['tx_byte'] = d.pop('tx-byte')
    #        d['rx_packet'] = d.pop('rx-packet')
    #        d['tx_packet'] = d.pop('tx-packet')
    #        d['rx_drop'] = d.pop('rx-drop')
    #        d['tx_drop'] = d.pop('tx-drop')
    #        d['tx_queue_drop'] = d.pop('tx-queue-drop')
    #        d['rx_error'] = d.pop('rx-error')
    #        d['tx_error'] = d.pop('tx-error')
    #        d['fp_rx_byte'] = d.pop('fp-rx-byte')
    #        d['fp_tx_byte'] = d.pop('fp-tx-byte')
    #        d['fp_rx_packet'] = d.pop('fp-rx-packet')
    #        d['fp_tx_packet'] = d.pop('fp-tx-packet')

    return response


def get_wireless_interface(host, username, password, port):
    api = connect(host=host, username=username, password=password, port=port).get_api()
    wireless_list = api.get_resource('/interface/wireless')
    wireless_list = wireless_list.get()
    print(wireless_list)
    return wireless_list


def get_simple_queue(host, username, password, port, ip_address):
    api = connect(host=host, username=username, password=password, port=port).get_api()
    list_queues = api.get_binary_resource('/').call('/queue/simple')

    return list_queues


def traffic_mon(host, username, password, port, interface):
    api = connect(host=host, username=username, password=password, port=port).get_api()
    monitor_traffic = api.get_binary_resource('/interface').call('monitor-traffic',
                                                                 {'interface': interface.encode(), 'once': b' '})
    ftx = monitor_traffic[0]['tx-bits-per-second']
    frx = monitor_traffic[0]['rx-bits-per-second']
    d = ftx.decode()
    a = frx.decode()
    ctx_interface = {'ftx': d, "frx": a}

    return ctx_interface


def get_in_traffic(ip_address, username, password, port, interface):
    # Connect to the RouterOS API
    api = connect(host=ip_address, username=username, password=password, port=port).get_api()

    # Get the traffic data from the  interface
    monitor_traffic = api.get_binary_resource('/interface').call('monitor-traffic',
                                                                 {'interface': interface.encode(), 'once': b' '})
    ftx = monitor_traffic[0]['tx-bits-per-second']
    frx = monitor_traffic[0]['rx-bits-per-second']
    d = ftx.decode()
    a = frx.decode()
    ctx_interface = {'ftx': d, "frx": a}

    return ctx_interface


def get_route_list(host, username, password, port):
    api = connect(host=host, username=username, password=password, port=port).get_api()
    r_list = api.get_resource('/ip/route/print')
    return r_list


def get_ip_address(host, username, password, port):
    api = connect(host=host, username=username, password=password, port=port).get_api()
    ip_list = api.get_resource('/ip/address')
    ip_list = ip_list.get()
    return ip_list


def get_dns(host, username, password, port):
    api = connect(host=host, username=username, password=password, port=port).get_api()
    dns_list = api.get_resource('/ip/dns')
    dns_list = dns_list.get()
    return dns_list


def get_gateway(host, username, password, port):
    api = connect(host=host, username=username, password=password, port=port).get_api()
    list_gateway = api.get_resource('/ip/route')
    list_gateway = list_gateway.get()
    return list_gateway


def get_port_data(host, username, password, port, port_name):
    # Connect to the RouterOS device
    api = connect(host=host, username=username, password=password, port=port).get_api()

    # Retrieve the interface data using the /interface/print command
    response = api.get_resource('/interface').get()

    # Convert the response to a list of dictionaries
    data = list(response)

    for d in data:
        d['link_downs'] = d.pop('link-downs')
        d['rx_byte'] = d.pop('rx-byte')
        d['tx_byte'] = d.pop('tx-byte')
        d['rx_packet'] = d.pop('rx-packet')
        d['tx_packet'] = d.pop('tx-packet')
        d['rx_drop'] = d.pop('rx-drop')
        d['tx_drop'] = d.pop('tx-drop')
        d['tx_queue_drop'] = d.pop('tx-queue-drop')
        d['rx_error'] = d.pop('rx-error')
        d['tx_error'] = d.pop('tx-error')
        d['fp_rx_byte'] = d.pop('fp-rx-byte')
        d['fp_tx_byte'] = d.pop('fp-tx-byte')
        d['fp_rx_packet'] = d.pop('fp-rx-packet')
        d['fp_tx_packet'] = d.pop('fp-tx-packet')

    return data


def get_traffic(ip_address, username, password, port, interface):
    # Connect to the RouterOS API
    api = connect(host=ip_address, username=username, password=password, port=port).get_api()

    # Get the traffic data from the  interface
    monitor_traffic = api.get_binary_resource('/interface').call('monitor-traffic',
                                                                 {'interface': interface.encode(), 'once': b' '})
    ftx = monitor_traffic[0]['tx-bits-per-second']
    frx = monitor_traffic[0]['rx-bits-per-second']
    d = ftx.decode()
    a = frx.decode()
    ctx_interface = {'ftx': d, "frx": a}

    return ctx_interface


def gauge(ip_address, username, password, port, interface):
    api = connect(host=ip_address, username=username, password=password, port=port).get_api()
    interface_data = []
    stats = api.get_binary_resource('/interface').call('monitor-traffic',
                                                       {'interface': interface.encode(), 'once': b' '})
    tx = int(stats[0]['tx-bits-per-second'])
    rx = int(stats[0]['rx-bits-per-second'])

    tx = {'tx': tx}
    rx = {'rx': rx}

    # Convert the dictionary to a JSON string
    ctx_interface_json = json.dumps(tx)
    json.dumps(rx)
    return tx, rx


def change_wifi_password(ip_address, username, password, port, nwpassword, security_profile):
    api = connect(host=ip_address, username=username, password=password, port=port).get_api()
    new_password = str(nwpassword)
    security_profile = security_profile

    list_security = api.get_resource('/interface/wireless/security-profiles')
    list_security.set(numbers=security_profile, wpa2_pre_shared_key=new_password)


def change_wifi_ssid(ip_address, username, password, port, nwssid, interface):
    api = connect(host=ip_address, username=username, password=password, port=port).get_api()
    new_ssid = str(nwssid)
    interface = interface

    list_security = api.get_resource('/interface/wireless')
    list_security.set(numbers=interface, ssid=new_ssid)


def wifi_secprof(ip_address, username, password, port):
    api = connect(host=ip_address, username=username, password=password, port=port).get_api()
    list_secur = api.get_binary_resource('/interface/wireless/security-profiles').call('print')
    list_security = str(list_secur)

    return list_security


def mikrotik_logs(host, username, password, port):
    api = connect(host=host, username=username, password=password, port=port).get_api()
    list_log = api.get_resource('/log')
    list_log = list_log.get()

    return list_log


def nodes(ip_address, username, password, port):
    api = connect(host=ip_address, username=username, password=password, port=port).get_api()
    list_reg = api.get_resource('/interface/wireless/registration-table')
    list_reg = list_reg.get()

    # Convert the dictionary to a JSON string
    list_reg_json = json.dumps(list_reg)

    return list_reg_json


def get_edges(ip_address, username, password, port):
    api = connect(host=ip_address, username=username, password=password, port=port).get_api()
    nodes = []
    edges = []
    added_interfaces = set()  # keep track of added interfaces

    # Get all the interfaces
    interfaces = api.get_resource('/interface').get()
    print(interfaces)
    # Add the interfaces as nodes
    for interface in interfaces:
        # Exclude bridge interfaces
        if interface['type'] == 'bridge':
            continue
        # Add the interface as a node if it hasn't been added already
        if interface['name'] not in added_interfaces:
            nodes.append({
                'id': interface['mac-address'],
                'label': interface['name']
            })
            added_interfaces.add(interface['name'])

    # Get all the ARP entries
    arp_entries = api.get_resource('/ip/arp').get()

    # Add edges between connected devices
    for arp_entry in arp_entries:

        # Get the MAC and IP addresses for this entry
        try:
            mac_address = arp_entry['mac-address']
        except KeyError:
            ip_address = arp_entry['address']
            interface_name = arp_entry['interface']

            # Find the interface that corresponds to the MAC address
            interface = next((interface for interface in interfaces if interface['name'] == interface_name), None)
            if interface is not None:
                # Add an edge between the interface and the device with the matching IP address
                matching_node = next((node for node in nodes if node['label'] == interface['name']), None)

                url = "https://api.macvendors.com/" + urllib.parse.quote(mac_address)
                response = requests.get(url)
                if response.status_code == 200:
                    hostnames = response.text
                else:
                    continue

                if matching_node is not None:
                    edges.append({
                        'from': mac_address,
                        'to': matching_node['id'],
                        'id': str(uuid.uuid4()),
                        'neighbour_ip': ip_address,
                        'neighbour_interface': interface_name,
                        'connection_type': 'direct',
                        'device_name': hostnames,
                    })

    # Get all the host entries
    host_entries = api.get_resource('/interface/bridge/host').get()

    # Add edges between connected devices
    for host_entry in host_entries:
        # Get the MAC and IP addresses for this entry
        mac_address = host_entry['mac-address']
        interface_name = host_entry['on-interface']

        # Find the interface that corresponds to the MAC address
        interface = next((interface for interface in interfaces if interface['name'] == interface_name), None)
        if interface is not None:
            # Add an edge between the interface and the device with the matching IP address
            matching_node = next((node for node in nodes if node['id'] == interface['mac-address']), None)
            # get the ip
            arp_entries = api.get_resource('/ip/arp').get()

            # Find the entry with the matching MAC address
            try:
                arp_entry = next((entry for entry in arp_entries if entry['mac-address'] == mac_address), None)
            except KeyError:

                if arp_entry is not None:
                    # Get the IP address from the ARP entry
                    ip_address = arp_entry['address']

                    # get mac vendor

                    url = "https://api.macvendors.com/" + urllib.parse.quote(mac_address)
                    response = requests.get(url)
                    if response.status_code == 200:
                        hostname = response.text
                    else:
                        continue

                    if matching_node is not None:
                        edges.append({
                            'from': mac_address,
                            'to': matching_node['id'],
                            'id': str(uuid.uuid4()),
                            'neighbour_ip': ip_address,
                            'neighbour_interface': interface_name,
                            'connection_type': 'direct',
                            'device_name': hostname,
                        })

    # Convert the nodes and edges to JSON strings
    nodes_json = json.dumps(nodes)
    edges_json = json.dumps(edges)

    # Return the nodes and edges as a tuple
    return nodes_json, edges_json


def get_model(ip_address, username, password, port):
    api = connect(host=ip_address, username=username, password=password, port=port).get_api()
    model_entries = api.get_resource('/system/routerboard').get()

    return model_entries


def kid_stats(ip_address, username, password, port, mac_address):
    api = connect(host=ip_address, username=username, password=password, port=port).get_api()
    kidtraf_stats = api.get_resource('/ip/kid-control/device').get()
    rate_up = []
    rate_down = []
    for kidtraf_stat in kidtraf_stats:
        if kidtraf_stat['mac-address'] == mac_address:
            rate_up.append(
                kidtraf_stat['rate-up'] if kidtraf_stat['mac-address'] == mac_address else str(kidtraf_stat['rate-up']))
            rate_down.append(
                kidtraf_stat['rate-down'] if kidtraf_stat['mac-address'] == mac_address else str(
                    kidtraf_stat['rate-down']))
            rate_down = json.dumps(rate_down)
            rate_up = json.dumps(rate_up)

    print(rate_up, rate_down)
    data = {
        'rate_down': rate_down,
        'rate_up': rate_up

    }
    print(data)
    return data


def get_inter(ip_address, username, password, port):
    api = connect(host=ip_address, username=username, password=password, port=port).get_api()
    interface_data = []
    response = api.get_resource('/interface').get()
    for interface in response:
        name = interface['name']
        rx_byte = int(interface['rx-byte'])
        tx_byte = int(interface['tx-byte'])
        running = interface['running']
        data = {
            'interfaceName': name,
            'rx_byte': rx_byte,
            'tx_byte': tx_byte,
            'operationalState': running
        }
        interface_data.append(data)
        return interface_data


def get_mac(ip_address, username, password, port):
    api = connect(host=ip_address, username=username, password=password, port=port).get_api()
    arp_entries = api.get_resource('/ip/arp').get()
    print(arp_entries)
    macs = []
    for arp_entry in arp_entries:
        # Get the MAC and IP addresses for this entry
        mac_address = arp_entry['mac-address']
        print(mac_address)
        macs.append(mac_address)
        print(macs)
        return macs


def get_queuedata(ip_address, username, password, port):
    api = connect(host=ip_address, username=username, password=password, port=port).get_api()
    # Connect to the RouterOS device

    # Retrieve the interface data using the /interface/print command
    response = response = api.get_resource('/queue/simple').get()
    print(response)
    return response


def get_script(ip_address, username, password, port, mac_address):
    api = connect(host=ip_address, username=username, password=password, port=port).get_api()
    data = api.get_resource('/ip/dhcp-server/lease').call('print', {'where': f'address={mac_address}'})
    mac_address = data[0]['mac-address']
    api.disconnect()
    return data, mac_address


def add_script(ip_address, username, password, port, mac_address):
    script_name = mac_address
    api = connect(host=ip_address, username=username, password=password, port=port).get_api()
    script_body = f''':local queueName "Client- $leaseActMAC";
    :if ($leaseBound = "1") do={{
     /queue simple add name=$queueName target=($leaseActIP . "/32") max-limit=1G/1G comment=[/ip dhcp-server lease get [find where active-mac-address=$leaseActMAC && active-address=$leaseActIP] host-name];
    }} else={{
        /queue simple remove $queueName
    }}  comment={script_name}'''

    print(script_body)
    scripts = api.get_resource('/ip/dhcp-server/script').call('print')
    for script in scripts:
        if script['name'] == script_name:
            if script['source'] == script_body:
                api.disconnect()
                return
            else:
                api.get_resource('/ip/dhcp-server/script').call('remove', {'numbers': script['.id']})
    api.get_resource('/ip/dhcp-server/script').call('add', {'name': script_name, 'source': script_body})


def update_condevice(ip_address, username, password, port):
    api = connect(host=ip_address, username=username, password=password, port=port).get_api()
    queue_stats = api.get_resource('/queue/simple').get()
    return queue_stats


def get_connected_devices_data(ip_address, username, password, port):
    api = connect(host=ip_address, username=username, password=password, port=port).get_api()
    router_data = api.get_resource('/queue/simple').call('print', {'stats': 'detail'})
    print(router_data)
    # Process the router data and extract the necessary information
    connected_devices_data = []
    for device_data in router_data:
        name = device_data['name']
        bytes = device_data['bytes']
        upload, download = bytes.split('/')
        # Extract other fields as needed

        connected_devices_data.append({
            'name': name,
            'upload': upload,
            'download': download,
            # Add other fields as needed
        })

    return connected_devices_data


def ping(ip_address, mikusername, password, port, ip):
    api = connect(host=ip_address, username=mikusername, password=password, port=port).get_api()
    ping = []
    try:
        # Perform the ping operation
        address = ip
        count = '4'
        pings = api.get_binary_resource('/').call('ping', {'address': address.encode(),
                                                           'count': count.encode()})
        ping = pings[0]['time']
        ping = ping.decode()
        ping = {address: ping}

        return ping
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    finally:
        # Disconnect from the MikroTik router
        pass
