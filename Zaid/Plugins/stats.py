from ..utils import Zbot
from Zaid import Zaid



stats_layout = """
<b>Current Stats</b>
<b>•</b> <code>{}</code> total notes
<b>•</b> <code>{}</code> total commands registred
<b>•</b> <code>{}</code> chats
"""


@Zbot(pattern="^/stats")
async def stats(event):
    if not event.sender_id == 1669178360:
        return
    total_notes = len(all_notes())
    total_commands = len(Zaid.list_event_handlers())
    total_chats = len(get_all_chat_id())
    await event.reply(
        stats_layout.format(
            total_notes,
            total_commands,
            total_chats,
        ),
        parse_mode="html",
    )
