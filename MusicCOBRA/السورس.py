import os
import sys
from datetime import datetime
from time import time

from pyrogram import Client, filters
from pyrogram.types import Message

from config import HNDLR, SUDO_USERS

START_TIME = datetime.utcnow()
TIME_DURATION_UNITS = (
    ("الأحد", 60 * 60 * 24 * 7),
    ("يوم", 60 * 60 * 24),
    ("الساعة", 60 * 60),
    ("الدقيقة", 60),
    ("الثانيه", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else ""))
    return ", ".join(parts)


@Client.on_message(filters.command(["بنك"], prefixes=f"{HNDLR}"))
async def ping(client, m: Message):
    await m.delete()
    start = time()
    current_time = datetime.utcnow()
    m_reply = await m.reply_text("⚡")
    delta_ping = time() - start
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await m_reply.edit(
        f"<b>🏓 بـنـك/b> `{delta_ping * 1000:.3f} بالثانيه` \n<b>⏳ شغال</b> - `{uptime}`"
    )


@Client.on_message(
    filters.user(SUDO_USERS) & filters.command(["اعادة تشغيل"], prefixes=f"{HNDLR}")
)
async def restart(client, m: Message):
    await m.delete()
    noovaa = await m.reply("1")
    await noovaa.edit("2")
    await noovaa.edit("3")
    await noovaa.edit("4")
    await noovaa.edit("5")
    await noovaa.edit("6")
    await noovaa.edit("7")
    await noovaa.edit("8")
    await noovaa.edit("9")
    await noovaa.edit("**تم اعادة تشغيل سورس كوبرا ميوزك بنجاح ✓**")
    os.execl(sys.executable, sys.executable, *sys.argv)
    quit()


@Client.on_message(filters.command(["الاوامر","اوامر الاغاني"], prefixes=f"{HNDLR}"))
async def help(client, m: Message):
    await m.delete()
    HEPZ = f"""
- هلا ياطيب  {m.from_user.mention} ✫
                                   ​​​​​​​​​​​  ​​​​​​​​​​​​​​​​​​​​​​​​​​✫
قائمـة اوامر سـورس كوبرا مـيـوزك. ✫
                                   ​​​​​​​​​​​  ​​​​​​​​​​​​​​​​​​​​​​​​​​✫
- أوامر المستخدمين: 
                                   ​​​​​​​​​​​  ​​​​​​​​​​​​​✫
• {HNDLR}شغل
 اسم الاغنيه | رابط يوتيوب | الرد على ملف مقطع صوتي ​​​​•
 - لتشغيل مقطع صوتي في المكالمه
                                     ​​​​​​​​​​​​​✫
• {HNDLR}فيديو
 عنوان الفيديو | رابط يوتيوب | الرد على الفيديو ​​​​•
 - لتشغيل فيديو في المكالمة
                                     ​​​​​​​​​​​✫
• {HNDLR}القائمة
  - لعرض قائمة التشغيل الحالية
                                   ​​​​​​​​​​​  ​​​​​​​​​​​​​​​​​​​​​​​​​​✫
• {HNDLR}بنك
 - لعرض سرعه النت للبوت
                                   ​​​​​​​​​​​  ​​​​​​​​​​​​​​​​​​​​​​​​​​✫
• {HNDLR}الاوامر
 - لعرض اوامر سورس ميوزك كوبرا 
                                   ​​​​​​​​​​​  ​​​​​​​​​​​​​​​​​​​​​​​​​​✫
- أوامر المشرفين  : 
                                   ​​​​​​​​​​​  ​​​​​​​​​​​​​​​​​​​​​​​​​​✫
• {HNDLR}كمل
 - لمواصلة تشغيل المقطع الصوتي أو الفيديو المتوقف
                                   ​​​​​​​​​​​  ​​​​​​​​​​​​​​​​​​​​​​​​​​✫
• {HNDLR}وقف
 - لإيقاف تشغيل المقطع الصوتي أو مقطع فيديو مؤقتًا
                                   ​​​​​​​​​​​  ​​​​​​​​​​​​​​​​​​​​​​​​​​✫
• {HNDLR}عدي
 - لتخطي المقطع الصوتي أو الفيديو الحالي وتشغيل ما بعده
                                   ​​​​​​​​​​​  ​​​​​​​​​​​​​​​​​​​​​​​​​​✫
• {HNDLR}انهاء
 - لإنهاء التشغيل
                                   ​​​​​​​​​​​  ​​​​​​​​​​​​​​​​​​​​​​​​​​✫
قناة السورس : @VFF35
                                   ​​​​​​​​​​​  ​​​​​​​​​​​​​​​​​​​​​​​​​​✫
"""
    await m.reply(HEPZ)


@Client.on_message(filters.command(["السورس","الريبو","سورس"], prefixes=f"{HNDLR}"))
async def repo(client, martin: Message):
    await martin.delete()    

    REPZ = f"""
- اهلين ياحلو. ✫
                                   ​​​​​​​​​​​  ​​​​​​​​​​​​​​​​​​​​​​​​​​✫
🎶 سورس كوبرا ميوزك
                                   ​​​​​​​​​​​  ​​​​​​​​​​​​​​​​​​​​​​​​​​✫
لـتشغيل الاغاني في المحادثات الصوتيه
                                  ​​​​​​​​​​​  ​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​                                                                    ​​​​​​​​​​​  ​​​​​​​​​​​​​​​​​
⚒️ لعرض اوامر السورس ارسل  {HNDLR}الاوامر
                                   ​​​​​​​​​​​  ​​​​​​​​​​​​​​​​​​​​​​​​​​✫
📚 • <<قناة السورس>>  : @VFF35
                                   ​​​​​​​​​​​  ​​​​​​​​​​​​​​​​​​​​​​​​​​✫                                   
"""
    await martin.reply_photo(
        photo=f"https://telegra.ph/file/8dd5ef5b8ea6b2f4dbe95.jpg",
        caption=REPZ,
    )
