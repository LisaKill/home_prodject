from telebot import types
def keyboard_m(mought,N):
    keyboards = types.ReplyKeyboardMarkup(row_width= N, resize_keyboard=True)
    btn_list = [types.KeyboardButton(text=x) for x in mought]
    keyboards.add(*btn_list)
    return keyboards

list1 = ["Январь","Февраль","Март","Апрель","Май", "Июнь", "Июль", "Август" ,"Сентябрь" ,"Октябрь", "Ноябрь" ,"Декабрь"]
Junn= {a:"-" for a in range(1,31)}
Feb= {a:"-" for a in range(28)}
Mar= {a:"-" for a in range(31)}
Apr= {a:"-" for a in range(30)}
May= {a:"-"for a in range(31)}
Jun={a:"-" for a in range(1,30)}
Jul= {a:"-" for a in range(31)}
Aug= {a:"-" for a in range(31)}
Sen= {a:"-" for a in range(30)}
Oct= {a:"-" for a in range(31)}
Nov= {a:"-" for a in range(30)}
Dec= {a:"-" for a in range(31)}

planss ={1:Junn,2:Feb,3:Mar,4:Apr,5:May,6:Jun,7:Jul,8:Aug,9:Sen,10:Oct,11:Nov,12:Dec}

creatt = {}

celebrate ={1:" Всемирный день модерна (World Art Nouveau Day).",2:"День мебельщика",3:"День России",4:"Праздник Сошествия Святого Духа",5:"День работников миграционной службы"}