import threading
import mysql.connector

from pytgbot.api_types.sendable.reply_markup import ReplyKeyboardMarkup, ReplyKeyboardRemove

from telegram.client import Telegram

from pytgbot import Bot

from netsec import utils2
import telethon

CHAT = '-870785248'
bot = Bot('6192637865:AAFhsFmA2Th-Bjk_kWdtNDMshd-wa-sU0mM')

# Set up Telegram client
tg = Telegram(
    api_id='25941753',
    api_hash='3adbdd2acb9a4ece85747a823a1c37c1',
    phone='+27609876288',
    database_encryption_key='tyutytuyj',
)


def send_authentication_request(name, email, mac, ip):
    message_text = f"New registration:\nName: {name}\nEmail: {email}\nMac Address: {mac}\nIP: {ip}\n\nAllow or deny access?"

    print("Authentication request message sent to Telegram bot")

    reply_keyboard = [
        [f"/allow {name} {email} {mac} {ip}", f"/deny"],
        ["", ""],
        ["Done"],
    ]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)

    # Send the message with the inline keyboard
    bot.send_message(chat_id=CHAT, text=message_text, reply_markup=markup)


def new_message_handler(update):
    message_content = update['message']['content'].get('text', {})
    message_text = message_content.get('text', '').lower()

    if message_text.startswith('/allow '):
        name = message_text.split()[1]  # Extract the IP address from the message text
        email = message_text.split()[2]  # Extract the interface from the message text
        mac = message_text.split()[3]  # Extract the MAC address from the message text
        ip = message_text.split()[4]  # Extract the IP from the message text
        try:
            result = f'Data updated in mikrotik router. Device with {mac} now has access to the network'
            print(result)
            response = f"User details: {result}"

            # Send the response to the chat where the command was invoked
            chat_id = update['message']['chat_id']
            tg.send_message(chat_id, response)
            print(response)
        except mysql.connector.Error as error:
            print("Error while connecting to MySQL:", error)


def start_telegram_bot():
    # Define the login process and add the message handler
    tg.login()
    tg.add_message_handler(new_message_handler)
    tg.idle()


def main():
    # Define the login process and add the message handler
    tg.login()
    tg.add_message_handler(new_message_handler)
    tg.idle()


if __name__ == '__main__':
    # Start the Telegram bot in a separate thread
    bot_thread = threading.Thread(target=main())
    bot_thread.start()
