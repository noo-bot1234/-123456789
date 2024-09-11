from pyrogram import Client, idle
from config import API_ID, API_HASH, BOT_TOKEN
from pyromod import listen



bot = Client(
    "mo",
    api_id="15837209",
    api_hash="fe081df6989a4d79c1004903bb4f23e6",
    bot_token="7405964158:AAGVWeBOq2G8YJ-OKYN81_J5oM3eDTBOy1k",
    plugins=dict(root="Maker")
    )

async def start_bot():
    print("[INFO]: STARTING BOT CLIENT")
    await bot.start()
    AFROTOO = "nor_o"
    await bot.send_message(AFROTOO, "**تم تشغيل ال صانع بنجاح عزيزي المطور ...🥀،**")
    print("[INFO]: تم تشغيل الصانع وارسال رسالة للمطور⚡🚦.")
    await idle()
