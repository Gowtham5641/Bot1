from telethon import TelegramClient, events
import re
import asyncio

# Your API ID and API Hash from my.telegram.org
api_id = 26885611
api_hash = 'b35690cb29129d11f070995148cddb07'

# Your phone number
phone_number = '+923090916423'

# Group ID where the bot should reply and send messages
group_id = 2205452808

# Regular expression pattern to detect URLs
url_pattern = re.compile(r'https?://\S+|www\.\S+')

# Event handler for new messages
async def handler(event):
    message_text = event.message.message
    
    # Check if the message contains a URL
    if not url_pattern.search(message_text):
        # Reply to the message if it doesn't contain a URL
        await event.reply('You Just Won A Free Ton! Message me to claim.')

# Function to send a message to a specific group
async def send_message_to_group(client, group_id, message):
    # Fetch the entity (group)
    group_entity = await client.get_entity(group_id)
    await client.send_message(group_entity, message)

# Main function to start the client and manage events
async def main():
    client = TelegramClient('session_name', api_id, api_hash)
    await client.start(phone_number)
    print("Client is running...")

    # Send a message to the specific group
    await send_message_to_group(client, group_id, "Hello, this is a message from the bot.")

    # Listen for new messages and respond
    client.add_event_handler(handler, events.NewMessage(chats=group_id))
    
    await client.run_until_disconnected()

# Start the bot
if __name__ == '__main__':
    asyncio.run(main())
    
