

from django.shortcuts import render

from .telegram_bot_handler import send_authentication_request



import re
import uuid

def format_mac_address(mac_address):
    formatted_mac = ':'.join(re.findall('..', mac_address))
    return formatted_mac

def display_mac_address(request):
    # Get the client's IP address
    client_ip = request.META.get('REMOTE_ADDR')

    # Retrieve the MAC address using the IP address
    mac_address = None
    try:
        mac_address = uuid.UUID(int=uuid.getnode()).hex[-12:]
    except Exception as e:
        print(f"Failed to retrieve MAC address: {str(e)}")

    # Format the MAC address
    formatted_mac = format_mac_address(mac_address)

    # Pass the formatted MAC address to the template
    context = {'mac_address': formatted_mac, 'client_ip': client_ip}
    return render(request, 'redirect.html', context)

def registration(request):
    if request.method == 'POST':
        # Process the submitted details from the registration form
        name = request.POST.get('name')
        email = request.POST.get('email')
        # ...
        client_ip = request.META.get('REMOTE_ADDR')
        # Retrieve the MAC address
        mac_address = None
        try:
            mac_address = uuid.UUID(int=uuid.getnode()).hex[-12:]
        except Exception as e:
            print(f"Failed to retrieve MAC address: {str(e)}")

        # Format the MAC address
        formatted_mac = format_mac_address(mac_address)

        # Send the authentication request to Telegram bot
        send_authentication_request(name, email, formatted_mac, client_ip)

        return render(request, 'registration_success.html')

    return render(request, 'registration.html')

