class script(object):
    START_TXT = """<i>𝖧i {}, <b>𝖭𝗂𝖼𝖾 𝗍𝗈 𝗆𝖾𝖾𝗍 𝗒𝗈𝗎 🙌<\b>
 𝖨'𝗆 𝗃𝗎𝗌𝗍 𝖺 𝗌𝗂𝗆𝗉𝗅𝖾 𝗉𝗋𝖾 - 𝖿𝗎𝗇𝖼𝗍𝗂𝗈𝗇𝖾𝖽 𝖺𝗎𝗍𝗈𝖿𝗂𝗅𝗍𝖾𝗋 𝖻𝗈𝗍
 i𝗍𝗌 𝖾𝖺𝗌𝗒 𝗍𝗈 𝗎𝗌𝖾 𝗆𝖾; 𝗃𝗎𝗌𝗍 𝖺𝖽𝖽 𝗆𝖾 𝗍𝗈 𝗒𝗈𝗎𝗋 𝗀𝗋𝗈𝗎𝗉 𝖺𝗌 𝖺𝖽𝗆𝗂n,𝖨 𝖶𝗂𝗅𝗅 𝖬𝖺𝗇𝖺𝗀𝖾 𝖨𝗇𝗍𝗈 𝖳𝗁𝖾 𝖱𝖾𝗌𝗍😌🔥</i>"""
    HELP_TXT = """<b><i>𝖧𝖾𝗅𝗅𝗈 𝖬𝗋. {} 𝖨𝗍'𝗌 𝖬𝗒 𝖧𝖾𝗅𝗉 𝖬𝗈𝖽𝗎𝗅𝖾</b>"""
    ABOUT_TXT = """<b><i>• 𝖬𝗒 𝖭𝖺𝗆𝖾: <a href=https://t.me/cvEva_Bot><b>Wᴀᴢᴇᴇᴍ ⚡</b></a>\n
• 𝖬𝗒 𝖵𝖾𝗋𝗌𝗂𝗈𝗇 : 𝖵2.1
• 𝖣𝖾𝗏𝗈𝗅𝖾𝗉𝖾𝗋 : <a href=https://t.me/humen_tg><b>Hᴜᴍᴇɴ ⛔</b></a>\n
• 𝖫𝖺𝗇𝗀𝗎𝖺𝗀𝖾 : 𝖯𝗒𝗋𝗈𝗀𝗋𝖺𝗆\n
• 𝖥𝗋𝖺𝗆𝖾𝖶𝗈𝗋𝗄 : 𝖯𝗒𝗍𝗁𝗈𝗇 3\n
• 𝖧𝗈𝗌𝗍𝖾𝖽 𝖮𝗇 : 𝖧𝖾𝗋𝗈𝗄𝗎\n
• 𝖣𝖺𝗍𝖺𝖡𝖺𝗌𝖾 : 𝖬𝗈𝗇𝗀𝗈 𝖣𝖡\n
📖 𝖭𝗈𝗍𝖾 : ആരും പേടിക്കേണ്ട എല്ലാവർക്കും  ബോട്ട്  ഉപയോഗിക്കാം</i>"""
    SOURCE_TXT = """<b>NOTE:</b>
- Unfortunately This Bot is an Closed source project. 
-   

<b>But Base Repo Open Source:</b>
- <a href=https://github.com/EvamariaTG/EvaMaria>Eva Maria</a>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and EvaMaria will respond whenever a keyword is found the message

<b>NOTE:</b>
1. eva maria should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    FILTERMENU_TXT = """Currently I Have 2 Filter Options!!!
 Here Is It"""
    
    BUTTON_TXT = """Help: <b>Buttons</b>

- Wazeem Bot Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Wazeem Bot supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/Cinemaveed)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of Eva Maria

<b>Commands and Usage:</b>
• /id - <code>get id of a specified user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """<u>Cᴜʀʀᴇɴᴛ Dᴀᴛᴀʙᴀsᴇ Sᴛᴀᴛᴜs</u>

📑 ғɪʟᴇs sᴀᴠᴇᴅ: <code>{}</code>
👩🏻‍💻 ᴜsᴇʀs: <code>{}</code>
👥 ɢʀᴏᴜᴘs: <code>{}</code>
🗂️ ᴏᴄᴄᴜᴘɪᴇᴅ: <code>{}</code> 𝙼𝚒𝙱
🛒 ғʀᴇᴇ sᴛᴏʀᴀɢᴇ: <code>{}</code> 𝙼𝚒𝙱
"""
    CPU_TXT = """<i><u>𝖬𝗒 𝖲𝖾𝗋𝗏𝖾𝗋 𝖲𝗍𝖺𝗍𝗎𝗌📡</u></i>
"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
