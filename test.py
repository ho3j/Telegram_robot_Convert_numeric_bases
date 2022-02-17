"""
Hossein Jalili
feb-17-2022
version 1.0.0
Telegram_robot_Convert_numeric_bases 

"""

from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import CallbackContext
from telegram.ext.filters import Filters
from telegram import Update
from telegram.chataction import ChatAction
from telegram.ext.messagehandler import MessageHandler
import string
from random import *
from datetime import datetime
from datetime import timedelta
 

letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation
token = "5195180425:AAGS8nq3fj77sVEePIM1HL0Hin5An6dlPAw"
messages = {
    "msg_start": "Hi {0} {1}, \nwelcome to Convert numeric bases robot.\n#ho3j",
    "msg_help": "Available Commands :-\n/b - Binary\n/d - Decimal\n/o - Octal\n/h - Hexadecimal\n/b2 value on 2cmp\n",
    "msg_d":"your 'Decimal' number  : \t\t{0}\n------------------------------------------------ \nin Binary : \t\t{1}\nin Octal : \t\t{2}\nin Decimal : \t\t{3}\nin Hexadecimal : \t{4}",  
    "msg_b":"your 'Binary' number  : \t{0}\n------------------------------------------------ \nin Binary : \t\t{1}\nin Octal : \t\t{2}\nin Decimal : \t\t{3}\nin Hexadecimal : \t{4}",
    "msg_o":"your 'Octal' number  : \t\t{0}\n------------------------------------------------ \nin Binary : \t\t{1}\nin Octal : \t\t{2}\nin Decimal : \t\t{3}\nin Hexadecimal : \t{4}",
    "msg_h":"your 'Hexadecimal' number  : \t{0}\n------------------------------------------------ \nin Binary : \t\t{1}\nin Octal : \t\t{2}\nin Decimal : \t\t{3}\nin decimal : \t\t{4}",

}

def twos_comp(val, bits):
    """compute the 2's complement of int value val"""
    if (val & (1 << (bits - 1))) != 0: # if sign bit is set e.g., 8bit: 128-255
        val = val - (1 << bits)        # compute negative value
    return val 

def write_operation(x):
    file_name = "save_time.txt"
    file = open( file_name, "a+" )
    file.write(x+"\n")
    file.close()

def inffo(update):
    update_="update_id: \t\t\t"+str(update.update_id)
    message_id="message_id: \t\t"+str(update.message.message_id)
    from_user="from_user: \t\t\t"+str(update.message.from_user.id)
    is_bot="is_bot: \t\t\t"+str(update.message.from_user.is_bot)
    first_name_from="first_name_from: \t"+str(update.message.from_user.first_name)
    last_name_from="last_name_from: \t"+str(update.message.from_user.last_name)
    username_from="username_from: \t\t"+str(update.message.from_user.username)
    language_code="language_code: \t\t"+str(update.message.from_user.language_code)
    chat_id = "chat_id: \t\t\t"+str(update.message.chat_id)
    first_name ="first_name_chat: \t"+ str(update.message.chat.first_name)
    last_name = "last_name_chat: \t"+str(update.message.chat.last_name)
    username = "username_chat: \t\t"+str(update.message.chat.username)
    type_ = "type_: \t\t\t\t"+str(update.message.chat.type)

    date="date: \t\t\t\t"+str((update.message.date)+timedelta(hours=3,minutes=30))
    text="text: \t\t\t\t"+str(update.message.text)

    length="length: \t\t\t"+str(len(update.message.text))

    write_operation("\n"+str(update_)+"\n"+str(message_id)+"\n"+str(from_user)+"\n"+str(is_bot)+"\n"+str(first_name_from)+"\n"+str(last_name_from)+"\n"+str(username_from)+"\n"+str(language_code)+"\n"+str(chat_id)+"\n"+str(first_name)+"\n"+str(last_name)+"\n"+str(username)+"\n"+str(type_)+"\n"+str(date)+"\n"+str(text)+"\n"+str(length)+"\n")

    # print("update_id: \t\t",update_)
    # print("message_id: \t\t",message_id)
    # print("from_user: \t\t",from_user)
    # print("is_bot: \t\t",is_bot)
    # print("first_name_from: \t",first_name_from)
    # print("last_name_from: \t",last_name_from)
    # print("username_from: \t\t",username_from)
    # print("language_code: \t\t",language_code)
    # print("chat_id: \t\t", chat_id)
    # print("first_name_chat: \t", first_name)
    # print("last_name_chat: \t", last_name)
    # print("username_chat: \t\t", username)
    # print("type_: \t\t\t", type_)
    # print("date: \t", date)
    # print("text: \t\t\t", text)
    # print("length: \t\t", length)



def start_handler(update: Update, context: CallbackContext):
    # when a user start the bot.

    # import pdb; pdb.set_trace()
    write_operation("==================")
    inffo(update)
    write_operation("/start")
    write_operation("==================")
    first_name = update.message.chat.first_name
    last_name = update.message.chat.last_name
    chat_id = update.message.chat_id

    context.bot.send_chat_action(chat_id, ChatAction.TYPING)
    update.message.reply_text(text=messages["msg_start"].format(first_name, last_name))

def help(update: Update, context: CallbackContext):
    write_operation("==================")
    inffo(update)
    write_operation("/help")
    write_operation("==================")
    chat_id = update.message.chat_id
    context.bot.send_chat_action(chat_id, ChatAction.TYPING)
    update.message.reply_text(messages["msg_help"])


#--------------------------
def d(update: Update, context: CallbackContext):
    write_operation("==================")
    inffo(update)
    if context.args==[] or context.args[0].startswith('-') :
        txt="Please enter a Decimal_number whithout sign (-)"
        chat_id = update.message.chat_id
        context.bot.send_chat_action(chat_id, ChatAction.TYPING)
        update.message.reply_text(text=txt)
        
    elif len(context.args[0])>10 :
        txt="number is too long/we can't convert it"
        chat_id = update.message.chat_id
        context.bot.send_chat_action(chat_id, ChatAction.TYPING)
        update.message.reply_text(text=txt)
    else :
        try:
            num=context.args[0]
            num=int(str(num), 10)
            Binary=str(bin(num)).lstrip('0b')
            Octal=str(oct(num)).lstrip('0o')
            Decimal=str(int(num))
            Hexadecimal=str(hex(num)).lstrip('0x')
            chat_id = update.message.chat_id
            context.bot.send_chat_action(chat_id, ChatAction.TYPING)
            update.message.reply_text(text=messages["msg_d"].format(num,Binary,Octal,Decimal,Hexadecimal))
            write_operation(messages["msg_d"].format(num,Binary,Octal,Decimal,Hexadecimal))
        except:
            chat_id = update.message.chat_id
            context.bot.send_chat_action(chat_id, ChatAction.TYPING)
            update.message.reply_text(text="Please enter a Decimal_number")
    
    write_operation("==================")

def b(update: Update, context: CallbackContext):
    write_operation("==================")
    inffo(update)
    if context.args==[] or context.args[0].startswith('-') :
        txt="Please enter a Binary_number whithout sign (-)"
        chat_id = update.message.chat_id
        context.bot.send_chat_action(chat_id, ChatAction.TYPING)
        update.message.reply_text(text=txt)
    elif len(context.args[0])>125 :
        txt="number is too long/we can't convert it"
        chat_id = update.message.chat_id
        context.bot.send_chat_action(chat_id, ChatAction.TYPING)
        update.message.reply_text(text=txt)
    else :
        try:
            num=context.args[0]
            num=int(str(num), 2)
            Binary=str(bin(num)).lstrip('0b')
            Octal=str(oct(num)).lstrip('0o')
            Decimal=str(int(num))
            Hexadecimal=str(hex(num)).lstrip('0x')
            chat_id = update.message.chat_id



            context.bot.send_chat_action(chat_id, ChatAction.TYPING)
            update.message.reply_text(text=messages["msg_b"].format(Binary,Binary,Octal,Decimal,Hexadecimal))
            write_operation(messages["msg_b"].format(Binary,Binary,Octal,Decimal,Hexadecimal))
        except:
            chat_id = update.message.chat_id
            context.bot.send_chat_action(chat_id, ChatAction.TYPING)
            update.message.reply_text(text="Please enter a Binary_number")
    
    write_operation("==================")

def b2(update: Update, context: CallbackContext):
    write_operation("==================")
    inffo(update)
    if context.args==[] or context.args[0].startswith('-') :
        txt="Please enter a Binary_number_2complement whithout sign (-)"
        chat_id = update.message.chat_id
        context.bot.send_chat_action(chat_id, ChatAction.TYPING)
        update.message.reply_text(text=txt)
    elif len(context.args[0])>125 :
        txt="number is too long/we can't convert it"
        chat_id = update.message.chat_id
        context.bot.send_chat_action(chat_id, ChatAction.TYPING)
        update.message.reply_text(text=txt)
    else :
        try:
            from bitstring import Bits
            Binary=str(context.args[0])
            num="0b"+str(context.args[0])
            # print(num)
            num=Bits(bin=num)
            # Hexadecimal=num
            # print(Hexadecimal)  #16

            Decimal=num.int
            value2=str(Decimal)
            
            # print(Decimal) #10

            # Hexadecimal=str(hex(num)).lstrip('0x')
            # Binary=str(bin(num)).lstrip('0b')
            # Octal=(int(str(Decimal), 8))
            # print(Octal) #8
 

            chat_id = update.message.chat_id

            context.bot.send_chat_action(chat_id, ChatAction.TYPING)
            update.message.reply_text(text="value on 2cmp= \t"+value2)
            write_operation("value on 2cmp= \t"+value2)
        except:
            chat_id = update.message.chat_id
            context.bot.send_chat_action(chat_id, ChatAction.TYPING)
            update.message.reply_text(text="Please enter a Binary_number")
    
    write_operation("==================")


def o(update: Update, context: CallbackContext):
    write_operation("==================")
    inffo(update)
    if context.args==[] or context.args[0].startswith('-') :
        txt="Please enter a Octal_number whithout sign (-)"
        chat_id = update.message.chat_id
        context.bot.send_chat_action(chat_id, ChatAction.TYPING)
        update.message.reply_text(text=txt)
    elif len(context.args[0])>10 :
        txt="number is too long/we can't convert it"
        chat_id = update.message.chat_id
        context.bot.send_chat_action(chat_id, ChatAction.TYPING)
        update.message.reply_text(text=txt)
    else :
        try:
            num=context.args[0]
            num=int(str(num), 8)
            Binary=str(bin(num)).lstrip('0b')
            Octal=str(oct(num)).lstrip('0o')
            Decimal=str(int(num))
            Hexadecimal=str(hex(num)).lstrip('0x')
            chat_id = update.message.chat_id
            context.bot.send_chat_action(chat_id, ChatAction.TYPING)
            update.message.reply_text(text=messages["msg_o"].format(Octal,Binary,Octal,Decimal,Hexadecimal))
            write_operation(messages["msg_o"].format(Octal,Binary,Octal,Decimal,Hexadecimal))
        except:
            chat_id = update.message.chat_id
            context.bot.send_chat_action(chat_id, ChatAction.TYPING)
            update.message.reply_text(text="Please enter a Octal_number")
    
    write_operation("==================")

def h(update: Update, context: CallbackContext):
    write_operation("==================")
    inffo(update)
    if context.args==[] or context.args[0].startswith('-') :
        txt="Please enter a Hexadecimal_number whithout sign (-)"
        
        chat_id = update.message.chat_id
        context.bot.send_chat_action(chat_id, ChatAction.TYPING)
        update.message.reply_text(text=txt)
    elif len(context.args[0])>10 :
        txt="number is too long/we can't convert it"
        
        chat_id = update.message.chat_id
        context.bot.send_chat_action(chat_id, ChatAction.TYPING)
        update.message.reply_text(text=txt)
    else :
        try:
            num=context.args[0]
            num=int(str(num), 16)
            Binary=str(bin(num)).lstrip('0b')
            Octal=str(oct(num)).lstrip('0o')
            Decimal=str(int(num))
            Hexadecimal=str(hex(num)).lstrip('0x')
            chat_id = update.message.chat_id
            context.bot.send_chat_action(chat_id, ChatAction.TYPING)
            update.message.reply_text(text=messages["msg_h"].format(Hexadecimal,Binary,Octal,Decimal,Hexadecimal))
            write_operation(messages["msg_h"].format(Hexadecimal,Binary,Octal,Decimal,Hexadecimal))
        except:
            chat_id = update.message.chat_id
            context.bot.send_chat_action(chat_id, ChatAction.TYPING)
            update.message.reply_text(text="Please enter a Hexadecimal_number")
    
    write_operation("==================")


def unknown(update: Update, context: CallbackContext):
    write_operation("==================")
    inffo(update)
    chat_id = update.message.chat_id
    context.bot.send_chat_action(chat_id, ChatAction.TYPING)
    write_operation(update.message.text)
    write_operation("==================")
    
    update.message.reply_text(
        "Sorry '%s' is not a valid command" % update.message.text)
  
def unknown_text(update: Update, context: CallbackContext):
    write_operation("==================")
    inffo(update)
    chat_id = update.message.chat_id
    context.bot.send_chat_action(chat_id, ChatAction.TYPING)
    write_operation(update.message.text)
    write_operation("==================")
    
    update.message.reply_text(
        "Sorry I can't recognize you , you said '%s'" % update.message.text)




def main():
    updater = Updater(token, use_context=True)

    updater.dispatcher.add_handler(CommandHandler("start", start_handler))
    updater.dispatcher.add_handler(CommandHandler('help', help))

    updater.dispatcher.add_handler(CommandHandler('d', d, pass_args=True))
    updater.dispatcher.add_handler(CommandHandler('b', b, pass_args=True))
    updater.dispatcher.add_handler(CommandHandler('o', o, pass_args=True))
    updater.dispatcher.add_handler(CommandHandler('h', h, pass_args=True))
    updater.dispatcher.add_handler(CommandHandler('b2', b2, pass_args=True))



    updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown)) 
    updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text)) 

    updater.start_polling()
    # updater.idle()


main()