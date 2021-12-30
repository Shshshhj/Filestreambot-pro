# (c) Jigarvarma2005
from pyrogram.errors import RPCError
from pyrogram import filters
from Code_X_Mania.bot import StreamBot

@StreamBot.on_message(filters.channel & (filters.forwarded | filters.via_bot))
async def forward_channel_handler(client, message):
    try:
        jv_message = await message.copy(message.chat.id)
        await message.delete()
    except RPCError as lel:
        print(lel)
        return
    except:
        return
