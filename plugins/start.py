from pyrogram import Client, Filters, StopPropagation


@Client.on_message(Filters.command(["starttt"]), group=-2)
async def start(client, message):
    # return
    welcomed = f"**• مرحبا بك : <b>{message.from_user.first_name}</b>\n\n• يمديك تحميل من يوتيوب بأستخدام البوت .\n• ارسل رابط الاغنية بس -- -- -- -- -- -- -- -- -- -- -- -- -- --**"
    await message.reply_text(welcomed)
    raise StopPropagation
