from telebot import types, TeleBot
import random
from time import sleep
bot = TeleBot('TOKEN')


games = {}


@bot.message_handler(commands = ['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    btn1 = types.KeyboardButton("New game!")
    btn2 = types.KeyboardButton("About game!")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, "Hello " + message.from_user.username + '!\nWelcome to our Reversi_bot!', reply_markup = markup)


class game():

    def __init__(self, id1, id2, username1, username2, table, whoseturn, score1, score2):
        self.id1 = id1;
        self.id2 = id2;
        self.table = table;
        self.whoseturn = whoseturn;
        self.username1 = username1;
        self.username2 = username2;
        self.score1 = score1;
        self.score2 = score2;

    def get_count_balls(self):
        countwhite = 0
        countblack = 0
        table = self.table
        for i in range(1,9):
            for j in range(1, 9):
                if table[i][j] == '⚪️':
                    countwhite += 1
                elif table[i][j] == "⚫️":
                    countblack += 1
        return [countwhite, countblack]

    def get_table_title(self):
        x = self.wholose()
        if not x:
            t1 = ''
            if self.id1 == self.whoseturn:
                t1 = 'Your turn'
            t2 = ''
            if self.id2 == self.whoseturn:
                t2 = 'Your turn'

            count = self.get_count_balls()
            return [0, f"Reversi!  \n{self.username1} ⚪️ {count[0]} {t1}\n{self.username2} ⚫️ {count[1]} {t2}"]
        else:
            verdikt = ''
            uname = ""
            ball = ''
            count = self.get_count_balls()
            if 1 <= x <=3:
                if x == 1:
                    uname = self.username1
                    verdikt = 'WON!!!'
                    ball = '⚪️'
                    self.score1 += 1
                elif x == 3:
                    uname = ''
                    verdikt = "DRAW!!!"
                else:
                    uname = self.username2
                    verdikt = 'WON!!!'
                    ball = '⚫️'
                    self.score2 += 1
                return [1, f"Reversi!\n{self.username1} ⚪️ {count[0]}\n{self.username2} ⚫️ {count[1]}\n{uname} {ball} {verdikt}\n{self.username1}'s score = {self.score1}\n{self.username2}'s score = {self.score2}"]
            else:
                if self.whoseturn != self.id1:
                    self.whoseturn = self.id1
                else:
                    self.whoseturn = self.id2
                t1 = ''
                if self.id1 == self.whoseturn:
                    t1 = 'Your turn'
                t2 = ''
                if self.id2 == self.whoseturn:
                    t2 = 'Your turn'

                return [0, f"Reversi!  \n{self.username1} ⚪️ {count[0]} {t1}\n{self.username2} ⚫️ {count[1]} {t2}"]

    def filltable(self):
        table = [[' ']*10 for i in range(10)]
        table[4][4] = "⚪️"
        table[4][5] = "⚫️"
        table[5][4] = "⚫️"
        table[5][5] = "⚪️"

        self.table = table

    def generatewhoseturn(self):
        id = random.choice([self.id1, self.id2])
        self.whoseturn = id

    def wholose(self):
        ch = ''
        tch = ''
        if self.whoseturn == self.id1:
            ch = "⚫️"
            tch = '⚪️'
        else:
            ch = "⚪️"
            tch = "⚫️"


        yes = False
        for i in range(1, 9):
            if yes == True:
                break
            for j in range(1, 9):
                if self.table[i][j] == ' ':
                    #chap yuqoriga diagonalga yurish
                    x, y = i - 1, j - 1
                    while x >= 1 and y >= 1 and self.table[x][y] == ch:
                        x -= 1
                        y -= 1
                    if self.table[x][y] != ' ' and x != i - 1:
                        yes = True
                        break

                    # o'ng yuqori diagonalga yurish
                    x, y = i - 1, j + 1
                    while x >= 1 and y <= 8 and self.table[x][y] == ch:
                        x -= 1
                        y += 1
                    if self.table[x][y] != ' ' and x != i - 1:
                        yes = True
                        break

                    #chap pastki diagonalga yurish
                    x, y = i + 1, j - 1
                    while x <= 8 and y >= 1 and self.table[x][y] == ch:
                        x += 1
                        y -= 1
                    if self.table[x][y] != ' ' and x != i + 1:
                        yes = True
                        break

                    #ong pastki diagonalga yurish
                    x, y = i + 1, j + 1
                    while x <= 8 and y <= 8 and self.table[x][y] == ch:
                        x += 1
                        y += 1
                    if self.table[x][y] != ' ' and x != i + 1:
                        yes = True
                        break
                    #yuqoriga yurish
                    x, y = i - 1, j
                    while x >= 1 and self.table[x][y] == ch:
                        x -= 1
                    if self.table[x][y] != ' ' and x != i - 1:
                        yes = True
                        break

                    #ongga yurish
                    x, y = i, j + 1
                    while y <= 8 and self.table[x][y] == ch:
                        y += 1
                    if self.table[x][y] != ' ' and y != j + 1:
                        yes = True
                        break
                    #chapga yurish
                    x, y = i, j - 1
                    while y >= 1 and self.table[x][y] == ch:
                        y -= 1
                    if self.table[x][y] != ' ' and y != j - 1:
                        yes = True
                        break
                    #pastga yurish
                    x, y = i + 1, j
                    while x <= 8 and self.table[x][y] == ch:
                        x += 1
                    if self.table[x][y] != ' ' and x != i + 1:
                        yes = True
                        break
        if not yes:
            x = self.get_count_balls()
            if x[0] + x[1] == 64:
                if x[0] > x[1]:
                    return 1
                elif x[0] == x[1]:
                    return 3
                else:
                    return 2
            else:
                return 4
        else:
            return 0


    def step(self, ka):
        x1 = int(ka[0])
        y1 = int(ka[1])
        if self.table[x1][y1] != ' ':
            return 0
        ch = ''
        tch = ''
        if self.whoseturn == self.id1:
            ch = "⚫️"
            tch = '⚪️'
        else:
            ch = "⚪️"
            tch = "⚫️"

        yes = 0
        #chap yuqoriga diagonalga yurish
        x, y = x1 - 1, y1 - 1
        while x >= 1 and y >= 1 and self.table[x][y] == ch:
            x -= 1
            y -= 1
        if self.table[x][y] != ' ' and x != x1 -1:
            yes = 1
            while x <= x1 and y <= y1:
                self.table[x][y] = tch
                x += 1
                y += 1

        # o'ng yuqori diagonalga yurish
        x, y = x1 - 1, y1 + 1
        while x >= 1 and y <= 8 and self.table[x][y] == ch:
            x -= 1
            y += 1
        if self.table[x][y] != ' ' and x != x1 - 1:
            yes = 1
            while x <= x1 and y >= y1:
                self.table[x][y] = tch
                x += 1
                y -= 1


        #chap pastki diagonalga yurish
        x, y = x1 + 1, y1 - 1
        while x <= 8 and y >= 1 and self.table[x][y] == ch:
            x += 1
            y -= 1
        if self.table[x][y] != ' ' and x != x1 + 1:
            yes = 1
            while x >= x1 and y <= y1:
                self.table[x][y] = tch
                x -= 1
                y += 1

        #ong pastki diagonalga yurish
        x, y = x1 + 1, y1 + 1
        while x <= 8 and y <= 8 and self.table[x][y] == ch:
            x += 1
            y += 1
        if self.table[x][y] != ' ' and x != x1 + 1:
            yes = 1
            while x >= x1 and y >= y1:
                self.table[x][y] = tch
                x -= 1
                y -= 1

        #yuqoriga yurish
        x, y = x1 - 1, y1
        while x >= 1 and self.table[x][y] == ch:
            x -= 1
        if self.table[x][y] != ' ' and x != x1 - 1:
            yes = 1
            while x <= x1:
                self.table[x][y] = tch
                x += 1

        #ongga yurish
        x, y = x1, y1 + 1
        while y <= 8 and self.table[x][y] == ch:
            y += 1
        if self.table[x][y] != ' ' and y != y1 + 1:
            yes = 1
            while y >= y1:
                self.table[x][y] = tch
                y -= 1

        #chapga yurish
        x, y = x1, y1 - 1
        while y >= 1 and self.table[x][y] == ch:
            y -= 1
        if self.table[x][y] != ' ' and y != y1 - 1:
            yes = 1
            while y <= y1:
                self.table[x][y] = tch
                y += 1
        #pastga yurish
        x, y = x1 + 1, y1
        while x <= 8 and self.table[x][y] == ch:
            x += 1
        if self.table[x][y] != ' ' and x != x1 + 1:
            yes = 1
            while x >= x1:
                self.table[x][y] = tch
                x -= 1

        if yes:
            if self.whoseturn != self.id1:
                self.whoseturn = self.id1
            else:
                self.whoseturn = self.id2
        return yes


def startgame(chatid, mid):
    table = games[chatid][mid].table
    markup = types.InlineKeyboardMarkup()
    for i in range(1, 9):
        rowq = []
        for j in range(1, 9):
            rowq.append(types.InlineKeyboardButton(table[i][j], callback_data=str(i)+str(j)))
        markup.row(rowq[0], rowq[1], rowq[2], rowq[3], rowq[4], rowq[5], rowq[6], rowq[7])
    txt = games[chatid][mid].get_table_title()
    if txt[0]:
        markup.row(types.InlineKeyboardButton("New game!", callback_data="start1"))
    bot.edit_message_text(chat_id = chatid, text = txt[1], message_id = mid, reply_markup = markup)

def send_authorize_table(chatid, button1, button2, mid):
    markup = types.InlineKeyboardMarkup()
    # buttons = []
    if button1:
        markup.add(types.InlineKeyboardButton("⚪️", callback_data = "id1"))
    if button2:
        markup.add(types.InlineKeyboardButton("⚫️", callback_data = 'id2'))
    if button1 == button2 == 0:
        markup.add(types.InlineKeyboardButton("Start game!", callback_data = 'start'))
        games[chatid][mid].generatewhoseturn()
        games[chatid][mid].filltable()
        txt = games[chatid][mid].get_table_title()[1]
        bot.edit_message_text(chat_id = chatid, text = txt, message_id = mid, reply_markup = markup)
    else:
        if button1 == button2 == 1:
            bot.send_message(chatid, "Reversi!".center(50), reply_markup = markup)
        else:
            bot.edit_message_text(chat_id = chatid, text = f"Reversi! + \n{games[chatid][mid].username1} \n{games[chatid][mid].username2}", message_id = mid, reply_markup = markup)


@bot.callback_query_handler(func = lambda call: True)
def callanswer(call):
    chatid = call.message.json['chat']['id']
    mid = call.message.message_id
    uid = call.from_user.id
    uname = call.from_user.username
    try:
        if call.data == 'id1':
            if chatid not in games.keys():
                games[chatid] = {}
            if mid not in games[chatid].keys():
                games[chatid][mid] = game(uid, 0, uname, '', [],  0, 0, 0)
                send_authorize_table(chatid, 0, 1, mid)
            else:
                if uid != games[chatid][mid].id2:
                    games[chatid][mid].id1 = uid
                    games[chatid][mid].username1 = uname
                    send_authorize_table(chatid, 0, 0, mid)
        elif call.data == 'id2':
            if chatid not in games.keys():
                    games[chatid] = {}
            if mid not in games[chatid].keys():
                games[chatid][mid] = game(0, uid, '', uname, [], 0, 0, 0)
                send_authorize_table(chatid, 1, 0, mid)
            elif uid != games[chatid][mid].id1:
                    games[chatid][mid].id2 = uid
                    games[chatid][mid].username2 = uname
                    send_authorize_table(chatid, 0, 0, mid)

        elif call.data == 'start' and uid in [games[chatid][mid].id1, games[chatid][mid].id2]:
            startgame(chatid, mid)
        elif len(call.data) == 2:
            if games[chatid][mid].whoseturn == uid:
                yes = games[chatid][mid].step(call.data)
                if yes:
                    startgame(chatid, mid)
        elif call.data == 'start1':
            games[chatid][mid].generatewhoseturn()
            games[chatid][mid].filltable()
            startgame(chatid, mid)
    except:
        pass


@bot.message_handler(content_types = ['text'])
def new_game(message):
    if message.chat.type in ['group', 'supergroup']:
        if message.text == 'New game!':
            send_authorize_table(message.chat.id, 1, 1, 0)
        elif message.text == 'About game!':
            bot.send_message(message.chat.id, "https://en.wikipedia.org/wiki/Reversi")
    else:
        bot.send_message(message.chat.id, "Sorry! This bot don't work in chat! Please, add it to any group!")


def main():
    bot.polling()


if __name__ == '__main__':
    main()
