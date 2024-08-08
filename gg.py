from telethon import TelegramClient, events
import random

# Your API ID and API Hash from my.telegram.org
api_id = 22858464
api_hash = '2a15cab706be6999c037a49f3e430188'

# Your phone number
phone_number = '+91 6374025998'

# The group ID you want to monitor
group_id = 2226019478  # Group IDs are usually negative

# Create the client and connect
client = TelegramClient('session_name', api_id, api_hash)

messages = [
    "🎉 **Get Free TON Tokens!** 🎉\nMessage me to receive your free TON tokens!",
    "🚀 **Claim Your Free TON Tokens Now!** 🚀\nMessage me to get started!",
    "🎊 **Free TON Tokens Available!** 🎊\nMessage me to claim yours!",
    "★ **Free TON Tokens for You!** ★\nMessage me to get your tokens!",
    "✨ **Exclusive: Free TON Tokens!** ✨\nMessage me to find out more!",
    "🌟 **Don't Miss Out on Free TON Tokens!** 🌟\nMessage me now!",
    "🎁 **Special Offer: Free TON Tokens!** 🎁\nMessage me to claim yours!",
    "🔥 **Hot Deal: Free TON Tokens!** 🔥\nMessage me to get yours now!",
    "💎 **Free TON Tokens Just for You!** 💎\nMessage me to receive them!",
    "📣 **Free TON Tokens Available!** 📣\nMessage me to claim your tokens!",
    "🎉 **Celebrate with Free TON Tokens!** 🎉\nMessage me to get yours!",
    "🎁 **Surprise: Free TON Tokens!** 🎁\nMessage me to claim your reward!",
    "⭐ **Free TON Tokens Offer!** ⭐\nMessage me to get your tokens!",
    "🚀 **Get Your Free TON Tokens!** 🚀\nMessage me to find out how!",
    "🎊 **Join the Free TON Tokens Giveaway!** 🎊\nMessage me to participate!"
]

@client.on(events.NewMessage(chats=group_id))
async def handler(event):
    # Check if the sender is not the bot itself
    if event.sender_id != (await client.get_me()).id:
        # Select a random message
        reply_message = random.choice(messages)
        await event.reply(reply_message, parse_mode='markdown')

async def main():
    await client.start(phone_number)
    print("Bot is running...")
    await client.run_until_disconnected()

if __name__ == '__main__':
    asyncio.run(main())
