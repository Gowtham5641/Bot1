from telethon import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.errors import UserAlreadyParticipantError, ChatAdminRequiredError, ChannelPrivateError, ChannelInvalidError
import asyncio
import time

# Your API ID and API Hash from my.telegram.org
api_id = 26885611
api_hash = 'b35690cb29129d11f070995148cddb07'

# Your phone number
phone_number = '+923090916423'

# List of group usernames to join
group_usernames = [
    '@BuYeRssAnDsElLeRss',
    '@chatting_girls_boys_and',
    '@Tamilhotchattingg1',
    '@BHABHI_FREE_GIRLS_GRUOP',
    '@INDIAN_SINGING_GRUOP',
    '@spamm_link',
    '@Bhabhi_chatting_Group_Interfaith',
    '@FREE_COUPALE_SHOW',
    '@SHARE_GRUOP_LINK',
    '@Chatting_Group_Adultt',
    '@Cum_world_tributer',
    '@share_link1',
    '@and_boys_girls_chatting',
    '@GIRLS_AND_BOYS_CHATTING_GRUOP',
    '@GIRLFRAIND_WIFE_INDIAA_SWAPPING',
    '@ice_shirajmolla',
    '@freelinksharegroups',
    '@EXCHANGELINKS_SHARE',
    '@BHABHI_GRUOP_TINDER',
    '@indian_gay_chat_group',
    '@freepromos480',
    '@WIFE_SWAPPING_INDIA_COUPLES',
    '@combochatdaily',
    '@Web3FarmAirdrop',
    '@airdrophub_chat01',
    '@BHABHI_GIRLS_CHATTING_GRUOP',
    '@habitcommunitychat3',
    '@cryptoz_chat',
    '@configsetup1',
    '@BlockchainSage',
    '@CryptoChatting1',
    '@Crackerspace'
]

# Function to join groups with a delay
async def join_groups(client):
    for username in group_usernames:
        try:
            await client(JoinChannelRequest(username))
            print(f"Joined group: {username}")
        except UserAlreadyParticipantError:
            print(f"Already a member of group: {username}")
        except (ChatAdminRequiredError, ChannelPrivateError, ChannelInvalidError) as e:
            print(f"Failed to join {username}: {str(e)}")
        except Exception as e:
            print(f"Unexpected error for {username}: {str(e)}")
        # Wait for 2 seconds before joining the next group
        time.sleep(15)

# Main function to start the client and join groups
async def main():
    client = TelegramClient('session_name', api_id, api_hash)
    await client.start(phone_number)
    print("Client is running...")

    await join_groups(client)
    await client.run_until_disconnected()

# Start the bot
if __name__ == '__main__':
    asyncio.run(main())
    
