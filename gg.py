from telethon import TelegramClient, events
import asyncio

# Your API ID and API Hash from my.telegram.org
api_id = 22858464
api_hash = '2a15cab706be6999c037a49f3e430188'

# Your phone number
phone_number = '+91 6374025998'

# The group ID you want to monitor
group_id = 2226019478  # Group IDs are usually negative

# Create the client and connect
client = TelegramClient('session_name', api_id, api_hash)

@client.on(events.NewMessage(chats=group_id))
async def handler(event):
    # Check if the sender is not the bot itself
    if event.sender_id != (await client.get_me()).id:
        # Wait for 30 seconds before replying
        await asyncio.sleep(30)
        await event.reply("Message me For Free Ton\nYou're eligible for free TON")

async def main():
    await client.start(phone_number)
    print("Bot is running...")
    await client.run_until_disconnected()

if __name__ == '__main__':
    asyncio.run(main())
    
