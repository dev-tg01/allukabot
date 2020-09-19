from telegram import Update, Bot, ParseMode
from telegram.ext import run_async

from alluka.modules.disable import DisableAbleCommandHandler
from alluka import dispatcher

from requests import get

@run_async
def ud(bot: Bot, update: Update):
  message = update.effective_message
  text = message.text[len('/familylist '):]
  
  Divuvideo = "https://telegra.ph/file/cae30f13d93b4c24f9fd8.mp4"
  Divu = """[Mr.Divu」](https://telegram.dog/imDivu) As *Itachi Uchiha*.\n\nDon't Be So Quick To Judge Me.\nAfter All, You Only See 👀 \nWhat I Choose To Show You.\n\nTo Get More About Him Do `/info @imDivu`"""

  Ayanokojiimg = "https://telegra.ph/file/1cf42dcd39ff264f5a2f1.jpg"
  Ayanokoji = """[Ayanokōji](https://telegram.dog/Ayanokoji_op) As Ayanokōji Kiyotaka.\n To Get More About Him Do `/info @Ayanokoji_op`"""


 

  message.reply_photo(Ayanokojiimg, Ayanokoji, parse_mode=ParseMode.MARKDOWN)
  message.reply_video(Divuvideo, Divu, parse_mode=ParseMode.MARKDOWN)  


  
ud_handle = DisableAbleCommandHandler("familylist", ud)

dispatcher.add_handler(ud_handle)
