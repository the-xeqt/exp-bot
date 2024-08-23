from telethon import TelegramClient as Tc, events,Button
import yfinance as yf

# Replace with your own values
api_id = ''
api_hash = ''
bot_token = ''

# Create the Telegram client and connect
client = Tc('stock_bot', api_id, api_hash)

async def main():
    await client.start(bot_token=bot_token)

    @client.on(events.NewMessage(pattern='/start'))
    async def start(event):
        buttons = [
            [Button.url("🔰 Read Me 🔰", "https://telegra.ph/How-to-Use-Me-08-22")],
          [Button.url("➕Add me to Group➕",f"https://t.me/stock342bot?startgroup=true")] 
       ]
        await event.reply(''' Hello ! I am alive , 
    Which Stock do you want to get to know
    You can Use /s <stock_symbol>
    For more info Click on below Button''', buttons=buttons)
       
    @client.on(events.NewMessage(pattern='/s'))
    async def stock(event):
        try:
            # Extract stock symbol from message
            command = event.text.split()
            if len(command) < 2:
                return
            
            symbol = command[1]
            stock = yf.Ticker(symbol)
            info = stock.info

            # Format response
            response = (
                f"🌐**{info.get('longName', 'No name available')} ({symbol})**\n"
                f"❗Current Price: ₹{info.get('currentPrice', 'N/A')}\n"
                f"〽️Previous Close: ₹{info.get('regularMarketPreviousClose', 'N/A')}\n"
                f"🕛Day's Range: ₹{info.get('dayLow', 'N/A')} - ₹{info.get('dayHigh', 'N/A')}\n"
                f"❇️52 Week Range: ₹{info.get('fiftyTwoWeekLow', 'N/A')} - ₹{info.get('fiftyTwoWeekHigh', 'N/A')}\n"
                f"⏫Market Cap: ₹{info.get('marketCap', 'N/A')}\n"
                f"↪️PE Ratio: {info.get('trailingPE', 'N/A')}\n"
                f"↪️Dividend Yield: {info.get('dividendYield', 'N/A')}"
            )
            await event.reply(response)
        except Exception as e:
            await event.reply(f"Error fetching stock data: {str(e)}")

    print("Bot is running...")
    await client.run_until_disconnected()

# Run the client
with client:
    client.loop.run_until_complete(main())
