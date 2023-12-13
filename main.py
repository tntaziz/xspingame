import logging

import time
import random

import database as db
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import DiceEmoji
from config import 

from text import *
from buttons import *
from int_to_str import top_str_to_int
from limit import get_max_limit

# Configure logging
logging.basicConfig(level=logging.INFO)

# Bot and Dispatcher
bot = Bot(6528588867:AAFeX0rsX_QXHQ4OFBwGG6fJAztDlb3-j0k)
dp = Dispatcher(bot)


# Command 'start'
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await db.create_table()
    await db.add_user(message.from_user.id, 2000, 0, 0, message.from_user.full_name)
    await db.add_prig_u
    ser(message.from_id)
    await db.add_user_stat(message.from_id, 0)
    await db.add_lang_user(message.from_id, f"@{message.from_user.username}", 'ru')
    await db.add_user_limit_lvl(str(message.from_id), 1)
    db.update_name(message.from_id, message.from_user.first_name)
    if db.get_lang(message.from_id) == 'ru':
        if message.chat.id == message.from_id:
            await message.answer(f"""<b>Привет. Это бот для игры в виртуальное казино🎰</b>

Для просмотра доступных команд - /help

Правила игры — FAQ

Чат для игры — @xSpinGame

<i>А если ты и так все прекрасно знаешь, добавь меня в свою группу 👇</i>""", parse_mode='html',
                                 reply_markup=add_to_group_btn)
        else:
            await message.answer("Привет!")
    else:
        if message.chat.id == message.from_id:
            await message.answer("""<b>Salom. Bu virtual kazino bot🎰</b>

Mavjud buyruqlarni ko'rish uchun - /help

O'yin qoidalari — FAQ

O'yin uchun chat — @xSpinuzbbot

<i>Va agar siz allaqachon hamma narsani mukammal bilsangiz, meni guruhingizga qo'shing👇</i>""", parse_mode='html',
                                 reply_markup=add_to_group_btn_uz)
        else:
            await message.answer("Salom!")


# Command 'help'
@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    try:
        await db.add_lang_user(message.from_id, f"@{message.from_user.username}", 'ru')
        await db.add_user_stat(message.from_id, 0)
        if db.get_lang(message.from_id) == 'uz':
            db.update_name(message.from_id, message.from_user.first_name)
            await message.answer("<b>Tanlang👇</b>", parse_mode='html', reply_markup=help_button_uz)
        else:
            db.update_name(message.from_id, message.from_user.first_name)
            await message.answer("<b>Выберите👇</b>", parse_mode='html', reply_markup=help_button)
    except:
        pass


# Command 'top'
@dp.message_handler(commands=['top'])
async def top(message: types.Message):
    try:
        await db.add_lang_user(message.from_id, f"@{message.from_user.username}", 'ru')
        await db.add_prig_user(message.from_id)
        await db.add_user_stat(message.from_id, 0)
        balance = int(db.get_balance(message.from_id))
        bonus = db.get_bonus(message.from_user.id)
        db.update_name(message.from_id, message.from_user.first_name)
    except:
        pass

    try:
        if db.get_lang(message.from_id) == 'ru':
            if balance <= 0:
                user_id = db.get_top_id()
                await db.add_user_limit_lvl(str(message.from_id), 1)
                index_user = user_id.index((str(message.from_id),))
                index_user_id = index_user + 1
                top = db.get_top()
                top_balance = db.get_top_balance()
                await message.answer(f"""<b>1. {top[0][0]}  —  {top_str_to_int(int(top_balance[0][0]))}💰
2. {top[1][0]}  —  {top_str_to_int(int(top_balance[1][0]))}💰
3. {top[2][0]}  —  {top_str_to_int(int(top_balance[2][0]))}💰
4. {top[3][0]}  —  {top_str_to_int(int(top_balance[3][0]))}💰
5. {top[4][0]}  —  {top_str_to_int(int(top_balance[4][0]))}💰
6. {top[5][0]}  —  {top_str_to_int(int(top_balance[5][0]))}💰
7. {top[6][0]}  —  {top_str_to_int(int(top_balance[6][0]))}💰
8. {top[7][0]}  —  {top_str_to_int(int(top_balance[7][0]))}💰 
9. {top[8][0]}  —  {top_str_to_int(int(top_balance[8][0]))}💰
10. {top[9][0]}  —  {top_str_to_int(int(top_balance[9][0]))} 💰

Чтобы узнать свое место в топе, ваш баланс должен быть больше 0.

Количество пользователей бота — {int(len(user_id))}</b>""", parse_mode='html')
            else:
                user_id = db.get_top_id()
                index_user = user_id.index((str(message.from_id),))
                index_user_id = index_user + 1
                top = db.get_top()
                top_balance = db.get_top_balance()
                await message.answer(f"""<b>1. {top[0][0]}  —  {top_str_to_int(int(top_balance[0][0]))}💰
2. {top[1][0]}  —  {top_str_to_int(int(top_balance[1][0]))}💰
3. {top[2][0]}  —  {top_str_to_int(int(top_balance[2][0]))}💰
4. {top[3][0]}  —  {top_str_to_int(int(top_balance[3][0]))}💰
5. {top[4][0]}  —  {top_str_to_int(int(top_balance[4][0]))}💰
6. {top[5][0]}  —  {top_str_to_int(int(top_balance[5][0]))}💰
7. {top[6][0]}  —  {top_str_to_int(int(top_balance[6][0]))}💰
8. {top[7][0]}  —  {top_str_to_int(int(top_balance[7][0]))}💰 
9. {top[8][0]}  —  {top_str_to_int(int(top_balance[8][0]))}💰
10. {top[9][0]}  —  {top_str_to_int(int(top_balance[9][0]))} 💰

Ваше место в топе — {index_user_id}
Количество пользователей бота — {int(len(user_id))}</b>""", parse_mode='html')
        else:
            if balance <= 0:
                user_id = db.get_top_id()
                await db.add_user_limit_lvl(str(message.from_id), 1)
                index_user = user_id.index((str(message.from_id),))
                index_user_id = index_user + 1
                top = db.get_top()
                top_balance = db.get_top_balance()
                await message.answer(f"""<b>1. {top[0][0]}  —  {top_str_to_int(int(top_balance[0][0]))}💰
2. {top[1][0]}  —  {top_str_to_int(int(top_balance[1][0]))}💰
3. {top[2][0]}  —  {top_str_to_int(int(top_balance[2][0]))}💰
4. {top[3][0]}  —  {top_str_to_int(int(top_balance[3][0]))}💰
5. {top[4][0]}  —  {top_str_to_int(int(top_balance[4][0]))}💰
6. {top[5][0]}  —  {top_str_to_int(int(top_balance[5][0]))}💰
7. {top[6][0]}  —  {top_str_to_int(int(top_balance[6][0]))}💰
8. {top[7][0]}  —  {top_str_to_int(int(top_balance[7][0]))}💰 
9. {top[8][0]}  —  {top_str_to_int(int(top_balance[8][0]))}💰
10. {top[9][0]}  —  {top_str_to_int(int(top_balance[9][0]))} 💰

Yuqoridagi o'rningizni bilish uchun balansingiz 0 dan katta bo'lishi kerak.

Bot foydalanuvchilar soni — {int(len(user_id))}</b>""", parse_mode='html')
            else:
                user_id = db.get_top_id()
                index_user = user_id.index((str(message.from_id),))
                index_user_id = index_user + 1
                top = db.get_top()
                top_balance = db.get_top_balance()
                await message.answer(f"""<b>1. {top[0][0]}  —  {top_str_to_int(int(top_balance[0][0]))}💰
2. {top[1][0]}  —  {top_str_to_int(int(top_balance[1][0]))}💰
3. {top[2][0]}  —  {top_str_to_int(int(top_balance[2][0]))}💰
4. {top[3][0]}  —  {top_str_to_int(int(top_balance[3][0]))}💰
5. {top[4][0]}  —  {top_str_to_int(int(top_balance[4][0]))}💰
6. {top[5][0]}  —  {top_str_to_int(int(top_balance[5][0]))}💰
7. {top[6][0]}  —  {top_str_to_int(int(top_balance[6][0]))}💰
8. {top[7][0]}  —  {top_str_to_int(int(top_balance[7][0]))}💰 
9. {top[8][0]}  —  {top_str_to_int(int(top_balance[8][0]))}💰
10. {top[9][0]}  —  {top_str_to_int(int(top_balance[9][0]))} 💰

Sizning topdagi o'rningiz — {index_user_id}
Bot foydalanuvchilar soni — {int(len(user_id))}</b>""", parse_mode='html')
    except:
        pass


# Command 'balance'
@dp.message_handler(commands=['balance'])
async def balance(message: types.Message):
    name = message.from_user.first_name
    id = message.from_id
    try:
        await db.create_table()
        await db.add_user(id, 2000, 0, 0, name)
        await db.add_prig_user(message.from_id)
        await db.add_lang_user(message.from_id, f"@{message.from_user.username}", 'ru')
        await db.add_user_limit_lvl(str(message.from_id), 1)
        await db.add_user_stat(message.from_id, 0)
        db.update_name(message.from_id, message.from_user.first_name)
        balance = int(db.get_balance(message.from_id))
        if db.get_lang(message.from_id) == 'ru':
            if int(balance) == 0:
                await message.reply(f"<b>Ваш баланс: <code>{int(balance)}</code>💰</b>", parse_mode='html')
                await message.answer(f"<b>Задонатить всегда можно тут - @xSpinAdmin</b>", parse_mode='html')
            else:
                await message.reply(f"<b>Ваш баланс: <code>{int(balance)}</code>💰</b>", parse_mode='html')
        else:
            if int(balance) == 0:
                await message.reply(f"<b>Sizning balansingiz: <code>{int(balance)}</code>💰</b>", parse_mode='html')
                await message.answer(f"<b>Bu yerda har doim donat qilishingiz mumkin - @xSpinAdmin</b>",
                                     parse_mode='html')
            else:
                await message.reply(f"<b>Sizning balansingiz: <code>{int(balance)}</code>💰</b>", parse_mode='html')
    except Exception as exc:
        print(exc)
        pass


#  Command 'active_limit_set_null'
@dp.message_handler(commands=['active_limit_set_null'])
async def active_limit(message: types.Message):
    try:
        id = str(message.from_id)
        if id == ADMIN_ISMOIL or id == ADMIN_ABDULLOH or id == ADMIN_KABULOV or id == ADMIN_KARMP:
            db.update_limit_null()
            db.set_bonus_null()
            await message.reply("<b>✅Все лимиты установлены на 0</b>", parse_mode='HTML')
        else:
            await message.reply("<b>❌Лимиты не установлены на 0</b>", parse_mode='HTML')
    except:
        pass


@dp.message_handler(commands=['about'])
async def about_user(message: types.Message):
    for admins_list in ADMIN_LIST:
        if str(message.from_id) == admins_list:
            try:
                replied_user_id = message.reply_to_message.from_id

                await db.add_user(replied_user_id, 2000, 0, 0, message.reply_to_message.from_user.first_name)
                await db.add_prig_user(message.from_id)
                await db.add_user_stat(replied_user_id, 0)
                await db.add_lang_user(replied_user_id, f"@{message.reply_to_message.from_user.username}", 'ru')
                await db.add_user_limit_lvl(str(replied_user_id), 1)
                db.update_name(replied_user_id, message.reply_to_message.from_user.first_name)

                top = db.get_top_id()
                replied_user_name = message.reply_to_message.from_user.first_name
                replied_user_username = message.reply_to_message.from_user.username
                replied_user_balance = db.get_balance(replied_user_id)
                replied_user_limit = db.get_limit(replied_user_id)
                replied_user_limit_lvl = db.get_limit_lvl(replied_user_id)
                replied_user_bank_balance = db.get_bank(replied_user_id)
                replid_user_bonus = db.get_bonus(replied_user_id)
                lang = db.get_lang(replied_user_id)
                user_id = db.get_top_id()
                index_user = user_id.index((str(replied_user_id),))
                stat = db.get_stat_user(replied_user_id)
                index_user_id = index_user + 1

                if replid_user_bonus == '1':
                    bonus_time = "Used"
                elif replid_user_bonus == '0':
                    bonus_time = "Not used"

                if replied_user_balance == 0:
                    rank_top = 0
                else:
                    rank_top = index_user_id

                if lang == 'uz':
                    language = "O'zbekcha🇺🇿"
                else:
                    language = "Russcha🇷🇺"

                await message.answer(f"""<b>User ID: <code>{replied_user_id}</code>
Username: @{replied_user_username}
Firstname: {replied_user_name}
Balance: <code>{int(replied_user_balance)}</code>
Balance Bank: {int(replied_user_bank_balance)}
Daily Limit: {int(replied_user_limit)}/{get_max_limit(replied_user_limit_lvl)}
Rank TOP: {rank_top}
Limit Level: {replied_user_limit_lvl}
Bonus: {bonus_time}
Played: {stat}
Language: {language}</b>""", parse_mode='html')
            except Exception as exc:
                print(exc)
                pass


# Command 'top'
@dp.message_handler(commands=['top_about'])
async def top(message: types.Message):
    try:
        await db.add_lang_user(message.from_id, f"@{message.from_user.username}", 'ru')
        balance = int(db.get_balance(message.from_id))
        bonus = db.get_bonus(message.from_user.id)
        db.update_name(message.from_id, message.from_user.first_name)
    except:
        pass

    try:
        for admin_list in ADMIN_LIST:
            if int(admin_list) == message.from_id:
                user_id = db.get_top_id()
                await db.add_user_limit_lvl(str(message.from_id), 1)
                index_user = user_id.index((str(message.from_id),))
                index_user_id = index_user + 1
                top = db.get_top()
                top_user = db.get_top_id()
                top_balance = db.get_top_balance()
                await message.answer(f"""<b>1. {top[0][0]}  —  {top_str_to_int(int(top_balance[0][0]))}💰
2. {top[1][0]}  —  {top_str_to_int(int(top_balance[1][0]))}💰
3. {top[2][0]}  —  {top_str_to_int(int(top_balance[2][0]))}💰
4. {top[3][0]}  —  {top_str_to_int(int(top_balance[3][0]))}💰
5. {top[4][0]}  —  {top_str_to_int(int(top_balance[4][0]))}💰
6. {top[5][0]}  —  {top_str_to_int(int(top_balance[5][0]))}💰
7. {top[6][0]}  —  {top_str_to_int(int(top_balance[6][0]))}💰
8. {top[7][0]}  —  {top_str_to_int(int(top_balance[7][0]))}💰 
9. {top[8][0]}  —  {top_str_to_int(int(top_balance[8][0]))}💰
10. {top[9][0]}  —  {top_str_to_int(int(top_balance[9][0]))} 💰


Количество пользователей бота — {int(len(user_id))}</b>""", parse_mode='html', reply_markup=top_about_btn)

    except Exception as exc:
        pass


@dp.message_handler(commands=['set_balance'])
async def set_balance(message: types.Message):
    msg = message.text
    id = str(message.from_id)
    split_msg = msg.split()
    try:
        if id == ADMIN_ABDULLOH or id == ADMIN_ISMOIL or id == ADMIN_JONY or id == ADMIN_KABULOV or id == ADMIN_KARMP:
            if len(split_msg) == 2:
                if split_msg[1].isdigit():
                    replied_user_id = message.reply_to_message.from_id
                    db.update_balance(replied_user_id, int(split_msg[1]))
                    await message.reply(f"Баланс установлен на {split_msg[1]}")
                    await bot.send_message(chat_id=-1001830374842, text=f"""<b>#SET_BALANCE

Admin: <a href="tg://user?id={int(id)}">{message.from_user.first_name}</a>
Qabul qiluvchi: <a href="tg://user?id={replied_user_id}">{message.reply_to_message.from_user.first_name}</a>
Balance: {int(split_msg[1])}</b>""", parse_mode='html')
    except:
        pass


# All
@dp.message_handler()
async def games(message: types.Message):
    msg_all = message.text
    msg = msg_all.lower()
    splitted_msg = msg.split()
    promo_split = msg_all.split()
    try:
        await db.create_table()
        await db.add_user(message.from_id, 2000, 0, 0, message.from_user.first_name)
        await db.add_user_stat(message.from_id, 0)
        await db.add_prig_user(message.from_id)
        await db.add_user_bank(message.from_id, 0, 1)
        get_bank = int(db.get_bank(message.from_id))
        get_bank_lvl = int(db.get_bank_lvl(message.from_id))
        await db.add_user_limit_lvl(str(message.from_id), 1)
        await db.add_lang_user(message.from_id, f"@{message.from_user.username}", 'ru')
        stat = db.get_stat_user(message.from_id)
        clan_stat = db.get_plays_clan(message.from_id)
        clan_id = db.get_clan_user(message.from_id)
        clan_plays = db.get_clan_plays(clan_id)

    except:
        pass

    try:
        if not message.chat.id == message.from_id:
            group_id = message.chat.id
            clan_id_user = db.get_clan_user(message.from_id)
            group_name = message.chat.title
            group_admin = await bot.get_chat_administrators(chat_id=group_id)
            await db.add_clan_user(message.from_id, message.from_user.first_name, 0, 'NoneClan.clanNone.clan.clan.None')
            for admins in group_admin:
                if admins['status'] == 'creator':
                    creator_id = admins['user']['id']
                    await db.add_clan(str(group_id), str(creator_id), 0, group_name)
    except Exception as exc:
        # print(exc)
        pass

    try:
        balance = int(db.get_balance(message.from_id))
        bonus = db.get_bonus(message.from_user.id)
        limit_lvl = db.get_limit_lvl(message.from_id)
        lang = db.get_lang(message.from_id)
        db.update_name(message.from_id, message.from_user.first_name)

    except Exception as exc:
        # print(exc)
        pass

    try:
        await db.create_table()
        await db.add_user(id, 2000, 0, 0, message.from_user.first_name)
        balance = db.get_balance(message.from_id)
    except:
        pass

    try:
        if (msg.startswith("!б ") or msg.startswith('!b ')) and (len(msg) >= 4) and (len(splitted_msg) >= 2) and not (
                splitted_msg[1] == 0) and not message.chat.id == message.from_id:
            if lang == 'ru':
                if splitted_msg[1].isdigit() and not int(splitted_msg[1]) == 0:
                    if int(splitted_msg[1]) <= balance:
                        db.update_clan_plays_count(str(message.from_id), str(clan_id), int(clan_stat) + 1)
                        if not clan_plays == None:
                            db.update_clan_plays(clan_id, int(clan_plays) + 1)
                        db.update_stat(message.from_id, stat + 1)
                        split_basket = int(splitted_msg[1])
                        basket = DiceEmoji.BASKETBALL
                        response = await message.reply_dice(basket)
                        value = response.dice.value
                        time.sleep(3.5)
                        response_asjson = response
                        if response_asjson['dice']['value'] == 5:
                            basket_balance = split_basket * 2
                            db.update_balance(message.from_id, balance + basket_balance)
                            await message.reply(f"""<b>{YOU_WIN(split_basket * 3)}</b>""", parse_mode='html')


                        elif response_asjson['dice']['value'] == 4:
                            basket_balance = split_basket * 1
                            db.update_balance(message.from_id, balance + basket_balance)
                            await message.reply(f"""<b>{YOU_WIN(split_basket * 2)}</b>""", parse_mode='html')

                        else:
                            await message.reply(f"<b>{YOU_LOSED}</b>", parse_mode='html')
                            basket_balance = split_basket
                            db.update_balance(message.from_id, balance - basket_balance)
                    else:
                        await message.reply(f"{NOT_ENOUGH_MONEY(balance)}")
            else:
                if splitted_msg[1].isdigit() and not int(splitted_msg[1]) == 0:
                    if int(splitted_msg[1]) <= balance:
                        db.update_clan_plays_count(str(message.from_id), str(clan_id), int(clan_stat) + 1)
                        if not clan_plays == None:
                            db.update_clan_plays(clan_id, int(clan_plays) + 1)
                        db.update_stat(message.from_id, stat + 1)
                        split_basket = int(splitted_msg[1])
                        basket = DiceEmoji.BASKETBALL
                        response = await message.reply_dice(basket)
                        value = response.dice.value
                        time.sleep(3.5)
                        response_asjson = response
                        if response_asjson['dice']['value'] == 5:
                            basket_balance = split_basket * 2
                            db.update_balance(message.from_id, balance + basket_balance)
                            await message.reply(f"""<b>{YOU_WIN_UZ(split_basket * 3)}</b>""", parse_mode='html')


                        elif response_asjson['dice']['value'] == 4:
                            basket_balance = split_basket * 1
                            db.update_balance(message.from_id, balance + basket_balance)
                            await message.reply(f"""<b>{YOU_WIN_UZ(split_basket * 2)}</b>""", parse_mode='html')

                        else:
                            await message.reply(f"<b>{YOU_LOSED_UZ}</b>", parse_mode='html')
                            basket_balance = split_basket
                            db.update_balance(message.from_id, balance - basket_balance)
                    else:
                        await message.reply(f"{NOT_ENOUGH_MONEY_UZ(balance)}")


        elif (msg.startswith("!боул ") or msg.startswith('!boul ')) and (len(msg) >= 7) and (
                len(splitted_msg) == 2) and (not splitted_msg[1] == 0) and not message.chat.id == message.from_id:
            if lang == 'ru':
                if splitted_msg[1].isdigit() and not int(splitted_msg[1]) == 0:
                    if balance >= int(splitted_msg[1]):
                        db.update_clan_plays_count(str(message.from_id), str(clan_id), int(clan_stat) + 1)
                        if not clan_plays == None:
                            db.update_clan_plays(clan_id, int(clan_plays) + 1)
                        db.update_stat(message.from_id, stat + 1)
                        splitted_boul = int(splitted_msg[1])
                        response = await message.reply_dice(DiceEmoji.BOWLING)
                        time.sleep(3.5)
                        response_asjson = response['dice']['value']
                        if response_asjson == 6:
                            new_balance = balance + splitted_boul * 2
                            db.update_balance(message.from_id, new_balance)
                            await message.reply(f"""<b>{YOU_WIN(splitted_boul * 3)}</b>""", parse_mode='html')
                        elif response_asjson == 5:
                            new_balance = balance + splitted_boul * 1
                            db.update_balance(message.from_id, new_balance)
                            await message.reply(f"""<b>{YOU_WIN(splitted_boul * 2)}</b>""", parse_mode='html')
                        else:
                            db.update_balance(message.from_id, balance - splitted_boul)
                            await message.reply(f"<b>{YOU_LOSED}</b>", parse_mode='html')
                    else:
                        await message.reply(f"<b>{NOT_ENOUGH_MONEY(balance)}</b>", parse_mode='html')
            else:
                if splitted_msg[1].isdigit() and not int(splitted_msg[1]) == 0:
                    if balance >= int(splitted_msg[1]):
                        db.update_clan_plays_count(str(message.from_id), str(clan_id), int(clan_stat) + 1)
                        if not clan_plays == None:
                            db.update_clan_plays(clan_id, int(clan_plays) + 1)
                        db.update_stat(message.from_id, stat + 1)
                        splitted_boul = int(splitted_msg[1])
                        response = await message.reply_dice(DiceEmoji.BOWLING)
                        time.sleep(3.5)
                        response_asjson = response['dice']['value']
                        if response_asjson == 6:
                            new_balance = balance + splitted_boul * 2
                            db.update_balance(message.from_id, new_balance)
                            await message.reply(f"""<b>{YOU_WIN_UZ(splitted_boul * 3)}</b>""", parse_mode='html')
                        elif response_asjson == 5:
                            new_balance = balance + splitted_boul * 1
                            db.update_balance(message.from_id, new_balance)
                            await message.reply(f"""<b>{YOU_WIN_UZ(splitted_boul * 2)}</b>""", parse_mode='html')
                        else:
                            db.update_balance(message.from_id, balance - splitted_boul)
                            await message.reply(f"<b>{YOU_LOSED_UZ}</b>", parse_mode='html')
                    else:
                        await message.reply(f"<b>{NOT_ENOUGH_MONEY_UZ(balance)}</b>", parse_mode='html')



        elif (msg.startswith("!слот ") or msg.startswith('!slot ')) and (len(msg) >= 7) and (
                len(splitted_msg) == 2) and (not splitted_msg[1] == 0) and not message.chat.id == message.from_id:
            if lang == 'ru':
                if splitted_msg[1].isdigit() and not int(splitted_msg[1]) == 0:
                    if balance >= int(splitted_msg[1]):
                        if int(splitted_msg[1]) >= 100:
                            db.update_clan_plays_count(str(message.from_id), str(clan_id), int(clan_stat) + 1)
                            if not clan_plays == None:
                                db.update_clan_plays(clan_id, int(clan_plays) + 1)
                            db.update_stat(message.from_id, stat + 1)
                            splitted_slot = int(splitted_msg[1])
                            response = await message.reply_dice(DiceEmoji.SLOT_MACHINE)
                            response_asjson = response['dice']['value']
                            time.sleep(2)
                            if response_asjson == 1:
                                rocket_balance = int(splitted_slot * 4.5)
                                new_rocket = rocket_balance - splitted_slot
                                new_balance = balance + new_rocket
                                db.update_balance(message.from_id, new_balance)
                                await message.reply(f"""<b>{YOU_WIN(rocket_balance)}</b>""", parse_mode='html')
                            elif response_asjson == 3:
                                rocket_balance = int(splitted_slot * 1.5)
                                new_rocket = rocket_balance - splitted_slot
                                new_balance = balance + new_rocket
                                db.update_balance(message.from_id, new_balance)
                                await message.reply(f"""<b>{YOU_WIN(rocket_balance)}</b>""", parse_mode='html')
                            elif response_asjson == 61:
                                rocket_balance = int(splitted_slot * 2)
                                new_rocket = rocket_balance - splitted_slot
                                new_balance = balance + new_rocket
                                db.update_balance(message.from_id, new_balance)
                                await message.reply(f"""<b>{YOU_WIN(rocket_balance)}</b>""", parse_mode='html')
                            elif response_asjson == 22:
                                rocket_balance = int(splitted_slot * 3)
                                new_rocket = rocket_balance - splitted_slot
                                new_balance = balance + new_rocket
                                db.update_balance(message.from_id, new_balance)
                                await message.reply(f"""<b>{YOU_WIN(rocket_balance)}</b>""", parse_mode='html')
                            elif response_asjson == 63:
                                rocket_balance = int(splitted_slot * 2)
                                new_rocket = rocket_balance - splitted_slot
                                new_balance = balance + new_rocket
                                db.update_balance(message.from_id, new_balance)
                                await message.reply(f"""<b>{YOU_WIN(rocket_balance)}</b>""", parse_mode='html')
                            elif response_asjson == 49:
                                rocket_balance = int(splitted_slot * 1.5)
                                new_rocket = rocket_balance - splitted_slot
                                new_balance = balance + new_rocket
                                db.update_balance(message.from_id, new_balance)
                                await message.reply(f"""<b>{YOU_WIN(rocket_balance)}</b>""", parse_mode='html')
                            elif response_asjson == 54:
                                rocket_balance = int(splitted_slot * 1.25)
                                new_rocket = rocket_balance - splitted_slot
                                new_balance = balance + new_rocket
                                db.update_balance(message.from_id, new_balance)
                                await message.reply(f"""<b>{YOU_WIN(rocket_balance)}</b>""", parse_mode='html')
                            elif response_asjson == 38:
                                rocket_balance = int(splitted_slot * 1.25)
                                new_rocket = rocket_balance - splitted_slot
                                new_balance = balance + new_rocket
                                db.update_balance(message.from_id, new_balance)
                                await message.reply(f"""<b>{YOU_WIN(rocket_balance)}</b>""", parse_mode='html')
                            elif response_asjson == 27:
                                rocket_balance = int(splitted_slot * 1.5)
                                new_rocket = rocket_balance - splitted_slot
                                new_balance = balance + new_rocket
                                db.update_balance(message.from_id, new_balance)
                                await message.reply(f"""<b>{YOU_WIN(rocket_balance)}</b>""", parse_mode='html')
                            elif response_asjson == 24:
                                rocket_balance = int(splitted_slot * 1.25)
                                new_rocket = rocket_balance - splitted_slot
                                new_balance = balance + new_rocket
                                db.update_balance(message.from_id, new_balance)
                                await message.reply(f"""<b>{YOU_WIN(rocket_balance)}</b>""", parse_mode='html')
                            elif response_asjson == 64:
                                rocket_balance = int(splitted_slot * 6)
                                new_rocket = rocket_balance - splitted_slot
                                new_balance = balance + new_rocket
                                db.update_balance(message.from_id, new_balance)
                                await message.reply(f"""<b>{YOU_WIN(rocket_balance)}</b>""", parse_mode='html')
                            elif response_asjson == 41:
                                rocket_balance = int(splitted_slot * 1.25)
                                new_rocket = rocket_balance - splitted_slot
                                new_balance = balance + new_rocket
                                db.update_balance(message.from_id, new_balance)
                                await message.reply(f"""<b>{YOU_WIN(rocket_balance)}</b>""", parse_mode='html')
                            elif response_asjson == 54:
                                rocket_balance = int(splitted_slot * 1.25)
                                new_rocket = rocket_balance - splitted_slot
                                new_balance = balance + new_rocket
                                db.update_balance(message.from_id, new_balance)
                                await message.reply(f"""<b>{YOU_WIN(rocket_balance)}</b>""", parse_mode='html')
                            elif response_asjson == 21:
                                rocket_balance = int(splitted_slot * 1.25)
                                new_rocket = rocket_balance - splitted_slot
                                new_balance = balance + new_rocket
                                db.update_balance(message.from_id, new_balance)
                                await message.reply(f"""<b>{YOU_WIN(rocket_balance)}</b>""", parse_mode='html')
                            elif response_asjson == 22:
                                rocket_balance = int(splitted_slot * 3)
                                new_rocket = rocket_balance - splitted_slot
                                new_balance = balance + new_rocket
                                db.update_balance(message.from_id, new_balance)
                                await message.reply(f"""<b>{YOU_WIN(rocket_balance)}</b>""", parse_mode='html')
                            elif response_asjson == 21:
                                rocket_balance = int(splitted_slot * 1.25)
                                new_rocket = rocket_balance - splitted_slot
                                new_balance = balance + new_rocket
                                db.update_balance(message.from_id, new_balance)
                                await message.reply(f"""<b>{YOU_WIN(rocket_balance)}</b>""", parse_mode='html')
                            elif response_asjson == 41:
                                rocket_balance = int(splitted_slot * 1.25)
                                new_rocket = rocket_balance - splitted_slot
                                new_balance = balance + new_rocket
                                db.update_balance(message.from_id, new_balance)
                                await message.reply(f"""<b>{YOU_WIN(rocket_balance)}</b>""", parse_mode='html')
                            elif response_asjson == 32:
                                rocket_balance = int(splitted_slot * 2)
                                new_rocket = rocket_balance - splitted_slot
                                new_balance = balance + new_rocket
                                db.update_balance(message.from_id, new_balance)
                                await message.reply(f"""<b>{YOU_WIN(rocket_balance)}</b>""", parse_mode='html')
                            elif response_asjson == 6:
                                rocket_balance = int(splitted_slot * 1.25)
                                new_rocket = rocket_balance - splitted_slot
                                new_balance = balance + new_rocket
                                db.update_balance(message.from_id, new_balance)
                                await message.reply(f"""<b>{YOU_WIN(rocket_balance)}</b>""", parse_mode='html')
                            elif response_asjson == 33:
                                rocket_balance = int(splitted_slot * 1.5)
                                new_rocket = rocket_balance - splitted_slot
                                new_balance = balance + new_rocket
                                db.update_balance(message.from_id, new_balance)
                                await message.reply(f"""<b>{YOU_WIN(rocket_balance)}</b>""", parse_mode='html')
                            elif response_asjson == 43:
                                rocket_balance = int(splitted_slot * 3)
                                new_rocket = rocket_balance - splitted_slot
                                new_balance = balance + new_rocket
                                db.update_balance(message.from_id, new_balance)
                                await message.reply(f"""<b>{YOU_WIN(rocket_balance)}</b>""", parse_mode='html')
                            elif response_asjson == 62 or response_asjson == 48:
                                rocket_balance = int(splitted_slot * 2)
                                new_rocket = rocket_balance - splitted_slot
                                new_balance = balance + new_rocket
                                db.update_balance(message.from_id, new_balance)
                                await message.reply(f"""<b>{YOU_WIN(rocket_balance)}</b>""", parse_mode='html')
                            elif response_asjson == 59:
                                rocket_balance = int(splitted_slot * 1.5)
                                new_rocket = rocket_balance - splitted_slot
                                new_balance = balance + new_rocket
                                db.update_balance(message.from_id, new_balance)
                                await message.reply(f"""<b>{YOU_WIN(rocket_balance)}</b>""", parse_mode='html')
                            elif response_asjson == 23:
                                rocket_balance = int(splitted_slot * 1.25)
                                new_rocket = rocket_balance - splitted_slot
                                new_balance = balance + new_rocket
                                db.update_balance(message.from_id, new_balance)
                                await message.reply(f"""<b>{YOU_WIN(rocket_balance)}</b>""", parse_mode='html')
                            elif response_asjson == 11:
                                rocket_balance = int(splitted_slot * 1.5)
                                new_rocket = rocket_balance - splitted_slot
                                new_balance = balance + new_rocket
                                db.update_balance(message.from_id, new_balance)
                                await message.reply(f"""<b>{YOU_WIN(rocket_balance)}</b>""", parse_mode='html')
                            elif response_asjson == 16:
                                rocket_balance = int(splitted_slot * 1.5)
                                new_rocket = rocket_balance - splitted_slot
                                new_balance = balance + new_rocket
                                db.update_balance(message.from_id, new_balance)
                                await message.reply(f"""<b>{YOU_WIN(rocket_balance)}</b>""", parse_mode='html')
                            elif response_asjson == 2:
                                rocket_balance = int(splitted_slot * 1.5)
                                new_rocket = rocket_balance - splitted_slot
                                new_balance = balance + new_rocket
                                db.update_balance(message.from_id, new_balance)
                                await message.reply(f"""<b>{YOU_WIN(rocket_balance)}</b>""", parse_mode='html')
                            elif response_asjson == 17 or response_asjson == 4:
                                rocket_balance = int(splitted_slot * 1.5)
                                new_rocket = rocket_balance - splitted_slot
                                new_balance = balance + new_rocket
                                db.update_balance(message.from_id, new_balance)
                                await message.reply(f"""<b>{YOU_WIN(rocket_balance)}</b>""", parse_mode='html')
                            elif response_asjson == 44 or response_asjson == 42:
                                rocket_balance = int(splitted_slot * 1.25)
                                new_rocket = rocket_balance - splitted_slot
                                new_balance = balance + new_rocket
                                db.update_balance(message.from_id, new_balance)
                                await message.reply(f"""<b>{YOU_WIN(rocket_balance)}</b>""", parse_mode='html')

                            else:
                                db.update_balance(message.from_id, balance - splitted_slot)
                                await message.reply(YOU_LOSED)
                        else:
                            await message.reply("<b>Сумма должна быть не менее 100 монет💰.</b>", parse_mode='HTML')
                    else:
                        await message.reply(f"<b>{NOT_ENOUGH_MONEY(balance)}</b>", parse_mode='html')
            else:
                if splitted_msg[1].isdigit() and not int(splitted_msg[1]) == 0:
                    if balance >= int(splitted_msg[1]):
                        if int(splitted_msg[1]) >= 100:
                            if not clan_plays == None:
                                db.update_clan_plays(clan_id, int(clan_plays) + 1)
                            db.update_stat(message.from_id, stat + 1)
                            db.update_stat(message.from_id, stat + 1)
                            splitted_slot = int(splitted_msg[1])
                            response = await message.reply_dice(DiceEmoji.SLOT_MACHINE)
                            response_asjson = response['dice']['value']
                            time.sleep(2)
                            if response_asjson == 1:
                                rocket_balance = int(splitted_slot * 4.5)
                                new_rocket = rocket_balance - splitted_slot
                                new_balance = balance + new_rocket
                                db.update_balance(message.from_id, new_balance)
                                await message.reply(f"""<b>{YOU_WIN_UZ(rocket_balance)}</b>""", parse_mode='html')
                            elif response_asjson == 3:
                                rocket_balance = int(splitted_slot * 1.5)
                                new_rocket = rocket_balance - splitted_slot
                                new_balance = balance + new_rocket
                                db.update_balance(message.from_id, new_balance)
                                await message.reply(f"""<b>{YOU_WIN_UZ(rocket_balance)}</b>""", parse_mode='html')
                            elif response_asjson == 61:
                                rocket_balance = int(splitted_slot * 2)
                                new_rocket = rocket_balance - splitted_slot
                                new_balance = balance + new_rocket
                                db.update_balance(message.from_id, new_balance)
                                await message.reply(f"""<b>{YOU_WIN_UZ(rocket_balance)}</b>""", parse_mode='html')
                            elif response_asjson == 22:
                                rocket_balance = int(splitted_slot * 3)
                                new_rocket = rocket_balance - splitted_slot
                                new_balance = balance + new_rocket
                                db.update_balance(message.from_id, new_balance)
                                await message.reply(f"""<b>{YOU_WIN_UZ(rocket_balance)}</b>""", parse_mode='html')
                            elif response_asjson == 63:
                                rocket_balance = int(splitted_slot * 2)
                                new_rocket = rocket_balance - splitted_slot
                                new_balance = balance + new_rocket
                                db.update_balance(message.from_id, new_balance)
                                await message.reply(f"""<b>{YOU_WIN_UZ(rocket_balance)}</b>""", parse_mode='html')
                            elif response_asjson == 49:
                                rocket_balance = int(splitted_slot * 1.5)
                                new_rocket = rocket_balance - splitted_slot
                                new_balance = balance + new_rocket
                                db.update_balance(message.from_id, new_balance)
                                await message.reply(f"""<b>{YOU_WIN_UZ(rocket_balance)}</b>""", parse_mode='html')
                            elif response_asjson == 54:
                                rocket_balance = int(splitted_slot * 1.25)
                                new_rocket = rocket_balance - splitted_slot
                                new_balance = balance + new_rocket
                                db.update_balance(message.from_id, new_balance)
                                await message.reply(f"""<b>{YOU_WIN_UZ(rocket_balance)}</b>""", parse_mode='html')
                            elif response_asjson == 38:
                                rocket_balance = int(splitted_slot * 1.25)
                                new_rocket = rocket_balance - splitted_slot
                                new_balance = balance + new_rocket
                                db.update_balance(message.from_id, new_balance)
                                await message.reply(f"""<b>{YOU_WIN_UZ(rocket_balance)}</b>""", parse_mode='html')
                            elif response_asjson == 27:
                                rocket_balance = int(splitted_slot * 1.5)
                                new_rocket = rocket_balance - splitted_slot
                                new_balance = balance + new_rocket
                                db.update_balance(message.from_id, new_balance)
                                await message.reply(f"""<b>{YOU_WIN_UZ(rocket_balance)}</b>""", parse_mode='html')
                            elif response_asjson == 24:
                                rocket_balance = int(splitted_slot * 1.25)
                                new_rocket = rocket_balance - splitted_slot
                                new_balance = balance + new_rocket
                                db.update_balance(message.from_id, new_balance)
                                await message.reply(f"""<b>{YOU_WIN_UZ(rocket_balance)}</b>""", parse_mode='html')
                            elif response_asjson == 64:
                                rocket_balance = int(splitted_slot * 6)
                                new_rocket = rocket_balance - splitted_slot
                                new_balance = balance + new_rocket
                                db.update_balance(message.from_id, new_balance)
                                await message.reply(f"""<b>{YOU_WIN_UZ(rocket_balance)}</b>""", parse_mode='html')
                            elif response_asjson == 41:
                                rocket_balance = int(splitted_slot * 1.25)
                                new_rocket = rocket_balance - splitted_slot
                                new_balance = balance + new_rocket
                                db.update_balance(message.from_id, new_balance)
                                await message.reply(f"""<b>{YOU_WIN_UZ(rocket_balance)}</b>""", parse_mode='html')
                            elif response_asjson == 54:
                                rocket_balance = int(splitted_slot * 1.25)
                                new_rocket = rocket_balance - splitted_slot
                                new_balance = balance + new_rocket
                                db.update_balance(message.from_id, new_balance)
                                await message.reply(f"""<b>{YOU_WIN_UZ(rocket_balance)}</b>""", parse_mode='html')
                            elif response_asjson == 21:
                                rocket_balance = int(splitted_slot * 1.25)
                                new_rocket = rocket_balance - splitted_slot
                                new_balance = balance + new_rocket
                                db.update_balance(message.from_id, new_balance)
                                await message.reply(f"""<b>{YOU_WIN_UZ(rocket_balance)}</b>""", parse_mode='html')
                            elif response_asjson == 22:
                                rocket_balance = int(splitted_slot * 3)
                                new_rocket = rocket_balance - splitted_slot
                                new_balance = balance + new_rocket
                                db.update_balance(message.from_id, new_balance)
                                await message.reply(f"""<b>{YOU_WIN_UZ(rocket_balance)}</b>""", parse_mode='html')
                            elif response_asjson == 21:
                                rocket_balance = int(splitted_slot * 1.25)
                                new_rocket = rocket_balance - splitted_slot
                                new_balance = balance + new_rocket
                                db.update_balance(message.from_id, new_balance)
                                await message.reply(f"""<b>{YOU_WIN_UZ(rocket_balance)}</b>""", parse_mode='html')
                            elif response_asjson == 41:
                                rocket_balance = int(splitted_slot * 1.25)
                                new_rocket = rocket_balance - splitted_slot
                                new_balance = balance + new_rocket
                                db.update_balance(message.from_id, new_balance)
                                await message.reply(f"""<b>{YOU_WIN_UZ(rocket_balance)}</b>""", parse_mode='html')
                            elif response_asjson == 32:
                                rocket_balance = int(splitted_slot * 2)
                                new_rocket = rocket_balance - splitted_slot
                                new_balance = balance + new_rocket
                                db.update_balance(message.from_id, new_balance)
                                await message.reply(f"""<b>{YOU_WIN_UZ(rocket_balance)}</b>""", parse_mode='html')
                            elif response_asjson == 6:
                                rocket_balance = int(splitted_slot * 1.25)
                                new_rocket = rocket_balance - splitted_slot
                                new_balance = balance + new_rocket
                                db.update_balance(message.from_id, new_balance)
                                await message.reply(f"""<b>{YOU_WIN_UZ(rocket_balance)}</b>""", parse_mode='html')
                            elif response_asjson == 33:
                                rocket_balance = int(splitted_slot * 1.5)
                                new_rocket = rocket_balance - splitted_slot
                                new_balance = balance + new_rocket
                                db.update_balance(message.from_id, new_balance)
                                await message.reply(f"""<b>{YOU_WIN_UZ(rocket_balance)}</b>""", parse_mode='html')
                            elif response_asjson == 43:
                                rocket_balance = int(splitted_slot * 3)
                                new_rocket = rocket_balance - splitted_slot
                                new_balance = balance + new_rocket
                                db.update_balance(message.from_id, new_balance)
                                await message.reply(f"""<b>{YOU_WIN_UZ(rocket_balance)}</b>""", parse_mode='html')
                            elif response_asjson == 62 or response_asjson == 48:
                                rocket_balance = int(splitted_slot * 2)
                                new_rocket = rocket_balance - splitted_slot
                                new_balance = balance + new_rocket
                                db.update_balance(message.from_id, new_balance)
                                await message.reply(f"""<b>{YOU_WIN_UZ(rocket_balance)}</b>""", parse_mode='html')
                            elif response_asjson == 59:
                                rocket_balance = int(splitted_slot * 1.5)
                                new_rocket = rocket_balance - splitted_slot
                                new_balance = balance + new_rocket
                                db.update_balance(message.from_id, new_balance)
                                await message.reply(f"""<b>{YOU_WIN_UZ(rocket_balance)}</b>""", parse_mode='html')
                            elif response_asjson == 23:
                                rocket_balance = int(splitted_slot * 1.25)
                                new_rocket = rocket_balance - splitted_slot
                                new_balance = balance + new_rocket
                                db.update_balance(message.from_id, new_balance)
                                await message.reply(f"""<b>{YOU_WIN_UZ(rocket_balance)}</b>""", parse_mode='html')
                            elif response_asjson == 11:
                                rocket_balance = int(splitted_slot * 1.5)
                                new_rocket = rocket_balance - splitted_slot
                                new_balance = balance + new_rocket
                                db.update_balance(message.from_id, new_balance)
                                await message.reply(f"""<b>{YOU_WIN_UZ(rocket_balance)}</b>""", parse_mode='html')
                            elif response_asjson == 16:
                                rocket_balance = int(splitted_slot * 1.5)
                                new_rocket = rocket_balance - splitted_slot
                                new_balance = balance + new_rocket
                                db.update_balance(message.from_id, new_balance)
                                await message.reply(f"""<b>{YOU_WIN_UZ(rocket_balance)}</b>""", parse_mode='html')
                            elif response_asjson == 2:
                                rocket_balance = int(splitted_slot * 1.5)
                                new_rocket = rocket_balance - splitted_slot
                                new_balance = balance + new_rocket
                                db.update_balance(message.from_id, new_balance)
                                await message.reply(f"""<b>{YOU_WIN_UZ(rocket_balance)}</b>""", parse_mode='html')
                            elif response_asjson == 17 or response_asjson == 4:
                                rocket_balance = int(splitted_slot * 1.5)
                                new_rocket = rocket_balance - splitted_slot
                                new_balance = balance + new_rocket
                                db.update_balance(message.from_id, new_balance)
                                await message.reply(f"""<b>{YOU_WIN_UZ(rocket_balance)}</b>""", parse_mode='html')
                            elif response_asjson == 44 or response_asjson == 42:
                                rocket_balance = int(splitted_slot * 1.25)
                                new_rocket = rocket_balance - splitted_slot
                                new_balance = balance + new_rocket
                                db.update_balance(message.from_id, new_balance)
                                await message.reply(f"""<b>{YOU_WIN_UZ(rocket_balance)}</b>""", parse_mode='html')

                            else:
                                db.update_balance(message.from_id, balance - splitted_slot)
                                await message.reply(YOU_LOSED_UZ)
                        else:
                            await message.reply("<b>Summa kamida 100 coin bo'lishi kerak💰.</b>", parse_mode='HTML')
                    else:
                        await message.reply(f"<b>{NOT_ENOUGH_MONEY_UZ(balance)}</b>", parse_mode='html')





        elif (msg.startswith("!р ") or msg.startswith('!r ')) and (len(splitted_msg) == 3) and (
                not splitted_msg[1] == 0 and not splitted_msg[2] == 0) and not message.chat.id == message.from_id:

            rand1 = [1, 1, 1, 1, 2, 3, 4, 1, 5, 2, 1, 2, 1, 1, 1, 9, 8, 7, 6, 1, 1, 1, 1, 1, 2, 2, 1, 3, 1, 1, 2, 2, 3,
                     1, 2, 1, 1, 2, 2, 2, 3, 1, 2, 1, 1, 2, 1, 2, 1, 4, 5, 6, 1, 1, 1, 1, 2, 1, 2, 1, 3]
            random_num1 = random.choice(rand1)
            random2 = [0, 0, 0, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 7, 2, 1, 3, 4, 1, 1, 1, 2, 1, 2, 3, 1, 5, 6, 7, 8, 9,
                       0, 0, 0, 0, 0, 1, 1, 2, 3, 4, 5, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 2, 1,
                       1, 3, 4, 4, 2, 2, 7, 6, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 7, 7, 7, 7, 8, 8, 8, 9, 9, 9, 1, 1,
                       1, 2, 2, 2, 3, 3, 0, 0, 6, 7, 8, 9, 5]
            rand2 = random.choice(random2)
            random3 = [0, 0, 0, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 7, 2, 1, 3, 4, 0, 0, 0, 0, 1, 1, 2, 4, 1, 1, 1, 2]
            rand3 = random.choice(random3)
            random_res = f"{random_num1}.{rand2}{rand3}"
            random_result = float(random_res)
            try:
                if lang == 'ru':
                    if splitted_msg[1].isdigit() and not int(splitted_msg[1]) == 0:
                        if int(splitted_msg[1]) >= 100:
                            if balance >= int(splitted_msg[1]):
                                if not clan_plays == None:
                                    db.update_clan_plays(clan_id, int(clan_plays) + 1)
                                db.update_stat(message.from_id, stat + 1)
                                db.update_stat(message.from_id, stat + 1)
                                splitted_rocket_summa = int(splitted_msg[1])
                                splitted_rocket_koefitsent = float(splitted_msg[2])
                                await message.reply("🚀")
                                time.sleep(2)
                                if splitted_msg[2] == 2 and random_result == 2.0:
                                    rocket_balance = splitted_rocket_summa * splitted_rocket_koefitsent
                                    rocket_minus = rocket_balance - splitted_rocket_summa
                                    db.update_balance(message.from_id, balance + rocket_minus)
                                    await message.reply(
                                        f"""<b>{YOU_WIN_ROCKET(random_result, int(rocket_balance))}</b>""",
                                        parse_mode='html')

                                elif splitted_msg[2] == 3 and random_result == 3.0:
                                    rocket_balance = splitted_rocket_summa * splitted_rocket_koefitsent
                                    rocket_minus = rocket_balance - splitted_rocket_summa
                                    db.update_balance(message.from_id, balance + rocket_minus)
                                    await message.reply(
                                        f"""<b>{YOU_WIN_ROCKET(random_result, int(rocket_balance))}</b>""",
                                        parse_mode='html')

                                elif splitted_msg[2] == 4 and random_result == 4.0:
                                    rocket_balance = splitted_rocket_summa * splitted_rocket_koefitsent
                                    rocket_minus = rocket_balance - splitted_rocket_summa
                                    db.update_balance(message.from_id, balance + rocket_minus)
                                    await message.reply(
                                        f"""<b>{YOU_WIN_ROCKET(random_result, int(rocket_balance))}</b>""",
                                        parse_mode='html')


                                elif splitted_msg[2] == 1 and random_result == 1.0:
                                    rocket_balance = splitted_rocket_summa * splitted_rocket_koefitsent
                                    rocket_minus = rocket_balance - splitted_rocket_summa
                                    db.update_balance(message.from_id, balance + rocket_minus)
                                    await message.reply(
                                        f"""<b>{YOU_WIN_ROCKET(random_result, int(rocket_balance))}</b>""",
                                        parse_mode='html')

                                elif splitted_rocket_koefitsent <= random_result:
                                    rocket_balance = splitted_rocket_summa * splitted_rocket_koefitsent
                                    rocket_minus = rocket_balance - splitted_rocket_summa
                                    db.update_balance(message.from_id, balance + rocket_minus)
                                    await message.reply(
                                        f"""<b>{YOU_WIN_ROCKET(random_result, int(rocket_balance))}</b>""",
                                        parse_mode='html')


                                elif splitted_rocket_koefitsent > random_result:
                                    rocket_balance = splitted_rocket_summa * splitted_rocket_koefitsent
                                    rocket_minus = rocket_balance - splitted_rocket_summa
                                    db.update_balance(message.from_id, balance - splitted_rocket_summa)
                                    await message.reply(f"""<b>{YOU_LOSED_ROCKET(random_result)}</b>""",
                                                        parse_mode='html')

                            else:
                                await message.reply(f"{NOT_ENOUGH_MONEY(balance)}")
                        else:
                            await message.reply("<b>Сумма должна быть не менее 100 монет💰.</b>", parse_mode='html')
                else:
                    if splitted_msg[1].isdigit() and not int(splitted_msg[1]) == 0:
                        if int(splitted_msg[1]) >= 100:
                            if balance >= int(splitted_msg[1]):
                                db.update_stat(message.from_id, stat + 1)
                                if not clan_plays == None:
                                    db.update_clan_plays(clan_id, int(clan_plays) + 1)
                                db.update_stat(message.from_id, stat + 1)
                                splitted_rocket_summa = int(splitted_msg[1])
                                splitted_rocket_koefitsent = float(splitted_msg[2])
                                await message.reply("🚀")
                                time.sleep(2)
                                if splitted_msg[2] == 2 and random_result == 2.0:
                                    rocket_balance = splitted_rocket_summa * splitted_rocket_koefitsent
                                    rocket_minus = rocket_balance - splitted_rocket_summa
                                    db.update_balance(message.from_id, balance + rocket_minus)
                                    await message.reply(
                                        f"""<b>{YOU_WIN_ROCKET_UZ(random_result, int(rocket_balance))}</b>""",
                                        parse_mode='html')

                                elif splitted_msg[2] == 3 and random_result == 3.0:
                                    rocket_balance = splitted_rocket_summa * splitted_rocket_koefitsent
                                    rocket_minus = rocket_balance - splitted_rocket_summa
                                    db.update_balance(message.from_id, balance + rocket_minus)
                                    await message.reply(
                                        f"""<b>{YOU_WIN_ROCKET_UZ(random_result, int(rocket_balance))}</b>""",
                                        parse_mode='html')

                                elif splitted_msg[2] == 4 and random_result == 4.0:
                                    rocket_balance = splitted_rocket_summa * splitted_rocket_koefitsent
                                    rocket_minus = rocket_balance - splitted_rocket_summa
                                    db.update_balance(message.from_id, balance + rocket_minus)
                                    await message.reply(
                                        f"""<b>{YOU_WIN_ROCKET_UZ(random_result, int(rocket_balance))}</b>""",
                                        parse_mode='html')


                                elif splitted_msg[2] == 1 and random_result == 1.0:
                                    rocket_balance = splitted_rocket_summa * splitted_rocket_koefitsent
                                    rocket_minus = rocket_balance - splitted_rocket_summa
                                    db.update_balance(message.from_id, balance + rocket_minus)
                                    await message.reply(
                                        f"""<b>{YOU_WIN_ROCKET_UZ(random_result, int(rocket_balance))}</b>""",
                                        parse_mode='html')

                                elif splitted_rocket_koefitsent <= random_result:
                                    rocket_balance = splitted_rocket_summa * splitted_rocket_koefitsent
                                    rocket_minus = rocket_balance - splitted_rocket_summa
                                    db.update_balance(message.from_id, balance + rocket_minus)
                                    await message.reply(
                                        f"""<b>{YOU_WIN_ROCKET_UZ(random_result, int(rocket_balance))}</b>""",
                                        parse_mode='html')


                                elif splitted_rocket_koefitsent > random_result:
                                    rocket_balance = splitted_rocket_summa * splitted_rocket_koefitsent
                                    rocket_minus = rocket_balance - splitted_rocket_summa
                                    db.update_balance(message.from_id, balance - splitted_rocket_summa)
                                    await message.reply(f"""<b>{YOU_LOSED_ROCKET_UZ(random_result)}</b>""",
                                                        parse_mode='html')

                            else:
                                await message.reply(f"{NOT_ENOUGH_MONEY_UZ(balance)}")
                        else:
                            await message.reply("<b>Summa kamida 100 coin bo'lishi kerak💰.</b>", parse_mode='html')

            except:
                pass

        elif (msg.startswith("!дартс ") or msg.startswith('!darts ')) and (len(msg) >= 8) and (
                len(splitted_msg) >= 2) and not (splitted_msg[1] == 0) and not message.chat.id == message.from_id:
            if splitted_msg[1].isdigit() and not int(splitted_msg[1]) == 0:
                if int(splitted_msg[1]) <= balance:
                    db.update_stat(message.from_id, stat + 1)
                    if not clan_plays == None:
                        db.update_clan_plays(clan_id, int(clan_plays) + 1)
                    db.update_stat(message.from_id, stat + 1)
                    split_dart = int(splitted_msg[1])
                    dart = DiceEmoji.DART
                    response = await message.reply_dice(dart)
                    time.sleep(2)
                    response_asjson = response
                    if response_asjson['dice']['value'] == 6:
                        basket_balance = int(split_dart * 3)
                        db.update_balance(message.from_id, balance + basket_balance)
                        await message.reply(f"""<b>{YOU_WIN(value=split_dart * 4)}</b>""", parse_mode='html')

                    else:
                        await message.reply(f"<b>{YOU_LOSED}</b>", parse_mode='html')
                        db.update_balance(message.from_id, balance - split_dart)
                else:
                    await message.reply(NOT_ENOUGH_MONEY(balance))


        elif (msg.startswith('!kubik ') or msg.startswith('!кубик ')) and not message.chat.id == message.from_id:
            if splitted_msg[1].isdigit() and splitted_msg[2].isdigit() and not int(splitted_msg[1]) == 0 and not int(
                    splitted_msg[2]) == 0 and int(splitted_msg[1]) <= 6:
                split_kubik_num = int(splitted_msg[1])
                split_kubik = int(splitted_msg[2])
                if lang == 'ru':
                    if split_kubik <= balance:
                        if not clan_plays == None:
                            db.update_clan_plays(clan_id, int(clan_plays) + 1)
                        db.update_stat(message.from_id, stat + 1)
                        db.update_stat(message.from_id, stat + 1)
                        dice = DiceEmoji.DICE
                        response = await message.reply_dice(dice)
                        time.sleep(2)
                        value = response.dice.value
                        if int(value) == int(split_kubik_num):
                            kubik_balance = int(split_kubik * 3)
                            db.update_balance(message.from_id, balance + kubik_balance)
                            await message.reply(f"""<b>{YOU_WIN(int(kubik_balance * 4))}</b>""", parse_mode='html')
                        else:
                            db.update_balance(message.from_id, balance - split_kubik)
                            await message.reply(f"""<b>{YOU_LOSED}</b>""", parse_mode='html')
                    else:
                        await message.reply(f"""<b>{NOT_ENOUGH_MONEY(balance)}</b>""", parse_mode='html')
                else:
                    if split_kubik <= balance:
                        if not clan_plays == None:
                            db.update_clan_plays(clan_id, int(clan_plays) + 1)
                        db.update_stat(message.from_id, stat + 1)
                        db.update_stat(message.from_id, stat + 1)
                        dice = DiceEmoji.DICE
                        response = await message.reply_dice(dice)
                        time.sleep(2)
                        value = response.dice.value
                        if int(value) == int(split_kubik_num):
                            kubik_balance = int(split_kubik * 3)
                            db.update_balance(message.from_id, balance + kubik_balance)
                            await message.reply(f"""<b>{YOU_WIN_UZ(int(kubik_balance * 4))}</b>""", parse_mode='html')
                        else:
                            db.update_balance(message.from_id, balance - split_kubik)
                            await message.reply(f"""<b>{YOU_LOSED_UZ}</b>""", parse_mode='html')
                    else:
                        await message.reply(f"""<b>{NOT_ENOUGH_MONEY_UZ(balance)}</b>""", parse_mode='html')


        elif (msg.startswith("!ф ") or msg.startswith("!f ")) and not message.chat.id == message.from_id:
            if splitted_msg[1].isdigit() and not int(splitted_msg[1]) == 0:
                split_basket = int(splitted_msg[1])
                if split_basket <= balance:
                    db.update_stat(message.from_id, stat + 1)
                    if not clan_plays == None:
                        db.update_clan_plays(clan_id, int(clan_plays) + 1)
                    db.update_stat(message.from_id, stat + 1)
                    dart = DiceEmoji.FOOTBALL
                    response = await message.reply_dice(dart)
                    time.sleep(2)
                    response_asjson = response
                    if response_asjson['dice']['value'] == 5:
                        basket_balance = int(split_basket * 2)
                        db.update_balance(message.from_id, balance + basket_balance)
                        await message.reply(f"""<b>{YOU_WIN(int(split_basket * 3))}</b>""", parse_mode='html')


                    elif response_asjson['dice']['value'] == 4:
                        basket_balance = int(split_basket * 1)
                        db.update_balance(message.from_id, balance + basket_balance)
                        await message.reply(f"""<b>{YOU_WIN(int(split_basket * 2))}</b>""", parse_mode='html')

                    else:
                        await message.reply(f"<b>{YOU_LOSED}</b>", parse_mode='html')
                        basket_balance = split_basket
                        db.update_balance(message.from_id, balance - basket_balance)

                else:
                    await message.reply(f"{NOT_ENOUGH_MONEY(balance)}")


        elif (msg.startswith('!активпромо ') or msg.startswith("!aktivpromo ")) and len(promo_split) == 4 and (
                str(message.from_id) == ADMIN_ABDULLOH or str(message.from_id) == ADMIN_KABULOV or str(
                message.from_id) == ADMIN_ISMOIL or str(message.from_id) == ADMIN_JONY or str(
                message.from_id) == ADMIN_KARMP) and message.chat.id == message.from_id:
            if promo_split[2].isdigit() and promo_split[3].isdigit():
                try:
                    promo_name_index = db.get_promo_name()
                    promo_index_name = promo_name_index.index((str(promo_split[1]),))
                    await message.reply("<b>Такой промокод уже имеется!</b>", parse_mode='html')
                except:
                    new_promo_name = promo_split[1]
                    new_promo_value = int(promo_split[2])
                    new_promo_max_user = int(promo_split[3])
                    db.add_new_promo(new_promo_name, new_promo_value, new_promo_max_user)
                    await message.reply(
                        f"<b>{ADD_PROMO(new_promo_name, new_promo_value, new_promo_max_user, message.from_user.username)}</b>",
                        parse_mode='html')
                    await bot.send_message(chat_id=-1001830374842,
                                           text=f"<b>{ADD_PROMO(new_promo_name, new_promo_value, new_promo_max_user, message.from_user.username)}</b>",
                                           parse_mode='html')

        elif (msg.startswith('!промокод ') or msg.startswith('!promokod ')) and len(
                promo_split) >= 2 and message.chat.id == message.from_id:
            for promo_name in db.get_promo_name():
                promo_index = db.get_used_promo(message.from_id)
                if lang == 'ru':
                    if promo_name == (promo_split[1],):
                        index_promo = db.get_promo_name().index((promo_split[1],))
                        balance_promo = db.get_promo_price()[index_promo][0]
                        if int(db.get_promo_max_user()[index_promo][0]) > int(db.get_promo_used_user()[index_promo][0]):
                            try:
                                index_promo_name = promo_index.index((str(message.from_id), promo_split[1]))
                                await message.reply("<b>Вы уже использовали этот промокод!</b>", parse_mode='html')
                            except:
                                await db.add_promo(message.from_id, promo_split[1])
                                db.update_max_user(promo_split[1], int(db.get_promo_used_user()[index_promo][0]) + 1)
                                db.update_balance(message.from_id, balance + balance_promo)
                                await message.reply(f"""<b>Вы успешно использовали промокод ✅.

Баланс пополнен на {balance_promo}💰</b>""", parse_mode='html')
                                await bot.send_message(chat_id=-1001830374842,
                                                       text=f"""#USED_PROMO\n\nPromokod: #{promo_split[1]}
User: <a href='tg://user?id={message.from_id}'>{message.from_user.first_name}</a>""", parse_mode='html')


                        else:
                            await message.reply("""<b>Этот промокод уже не действителен</b>""", parse_mode='html')
                else:
                    if promo_name == (promo_split[1],):
                        index_promo = db.get_promo_name().index((promo_split[1],))
                        balance_promo = db.get_promo_price()[index_promo][0]
                        if int(db.get_promo_max_user()[index_promo][0]) > int(
                                db.get_promo_used_user()[index_promo][0]):
                            try:
                                promo_index = db.get_used_promo(message.from_id)
                                index_promo_name = promo_index.index((str(message.from_id), promo_split[1]))
                                await message.reply("<b>Siz bu promo-kodni avval ishlatgansiz!</b>", parse_mode='html')
                            except:
                                await db.add_promo(message.from_id, promo_split[1])
                                db.update_max_user(promo_split[1],
                                                   int(db.get_promo_used_user()[index_promo][0]) + 1)
                                db.update_balance(message.from_id, balance + balance_promo)
                                await message.reply(f"""<b>Siz bu promo-koddan muvvafaqiyatli foydalandingiz ✅.

Balans to'ldirildi: {balance_promo}💰</b>""", parse_mode='html')
                                await bot.send_message(chat_id=-1001830374842,
                                                       text=f"""#USED_PROMO\n\nPromokod: #{promo_split[1]}
User: <a href='tg://user?id={message.from_id}'>{message.from_user.first_name}</a>""",
                                                       parse_mode='html')


                        else:
                            await message.reply("""<b>Ushbu promo-kod endi mavjud emas</b>""", parse_mode='html')

        elif (msg == '!бонус' or msg == '!bonus') and (
                str(message.from_id) == ADMIN_ISMOIL or str(message.from_id) == ADMIN_ABDULLOH or str(
                message.from_id) == ADMIN_KABULOV or str(message.from_id) == ADMIN_JONY or str(
                message.from_id) == ADMIN_KARMP or str(
                message.from_id) == ADELYA) and not message.chat.id == message.from_id:
            if bonus == '0':
                random_bonus = random.randint(100000, 300000)
                new_balance = random_bonus + balance
                db.update_balance(message.from_id, new_balance)
                db.update_bonus_time(message.from_id, 1)
                if db.get_lang(message.from_id) == 'uz':
                    await message.reply(f"""<i>Adminlar uchun kichik sovg'a 🤍 </i>

<b>Qabul qildi: {random_bonus}💰</b>""", parse_mode='HTML')
                else:
                    await message.reply(f"""<i>Небольшой подарок для администрации 🤍 </i>

<b>Получено: {random_bonus}💰</b>""", parse_mode='html')
            else:
                if db.get_lang(message.from_id) == 'ru':
                    await message.reply("<b>Еще не время для получения бонуса.</b>", parse_mode='HTML')
                else:
                    await message.reply("<b>Hali bonusni olish vaqti emas.</b>", parse_mode='html')


        elif (msg == '!бонус' or msg == '!bonus') and not message.chat.id == message.from_id:
            if bonus == '0':
                random_bonus = random.randint(10000, 13000)
                new_balance = random_bonus + balance
                db.update_balance(message.from_id, new_balance)
                db.update_bonus_time(message.from_id, 1)
                if db.get_lang(message.from_id) == 'uz':
                    await message.reply(f"""<i>Adminlar tomonidan kichik sovg'a</i>🤍

<b>Qabul qildi: {random_bonus}💰</b>""", parse_mode='HTML')
                else:
                    await message.reply(f"""<i>Небольшой подарок от администрации 🤍 </i>

<b>Получено: {random_bonus}💰</b>""", parse_mode='html')
            else:
                if db.get_lang(message.from_id) == 'ru':
                    await message.reply("<b>Еще не время для получения бонуса.</b>", parse_mode='HTML')
                else:
                    await message.reply("<b>Hali bonusni olish vaqti emas.</b>", parse_mode='html')



        elif msg == 'admin.panel.admin' and message.chat.id == message.from_id:
            if str(message.from_id) == ADMIN_ABDULLOH or str(message.from_id) == ADMIN_KABULOV or str(
                    message.from_id) == ADMIN_ISMOIL or str(message.from_id) == ADMIN_JONY or str(
                    message.from_id) == ADMIN_KARMP and not message.chat.id == str(message.from_id):
                await message.reply("""<b>✅Siz botdan admin sifatida foydalanyapsiz</b>""", parse_mode='html')
                await message.answer("""<b>✅Admin-commands✅</b>

<code>!d [summa]</code> - <i>foydalanuvchilarga pul berish uchun (reply qilish yordamida)</i>

<code>!d [summa] [username]</code> - <i>foydalanuvchilarga pul berish uchun (username yozish orqali)</i>


<code>!d- [summa]</code> - <i>foydalanuvchilarga pul ayirish uchun (reply qilish yordamida)</i>

<code>!d- [summa] [username]</code> - <i>foydalanuvchilarga pul ayirish uchun (username yozish orqali)</i>


<code>/about</code> - <i>foydalanuvchi xaqida to'liq malumot olish (reply qilish yordamida)</i>

<code>/top_about</code> - <i>top-reytingdagi foydalanuvchilar haqida to'liq malumot olish</i>

<code>/active_limit_set_null</code> - <b><i>Warning</i></b> <i>Bu funksiyadan 1 kunda 1 marta va soat 0.00 da ishlating!</i>

<code>/set_balance [summa]</code> - <i>balansni kiritgan summangizni sozlash uchun</i>

<code>!aktivpromo [promo] [value] [max_users]</code> - <i>promo-kod yaratish uchun</i>

<code>!bonus</code> - <i>adminlar uchun ko'proq bonus</i>""", parse_mode='html')
            else:
                pass


        elif (msg.startswith('!д ') or msg.startswith('!d ')) and len(splitted_msg) == 2 and (
                str(message.from_id) == ADMIN_ABDULLOH or str(message.from_id) == ADMIN_KABULOV or str(
                message.from_id) == ADMIN_ISMOIL or str(message.from_id) == ADMIN_JONY or str(
                message.from_id) == ADMIN_KARMP) and not message.chat.id == message.from_id:
            if lang == 'ru':
                if splitted_msg[1].isdigit() and not int(splitted_msg[1]) == 0:
                    split_transfer = int(splitted_msg[1])
                    try:
                        response = message['reply_to_message']['from']['id']
                        response_name = message.reply_to_message.from_user.first_name
                        replied_user_balance = db.get_balance(response)
                        new_balance = replied_user_balance + split_transfer
                        db.update_balance(response, int(new_balance))
                        await message.reply(SUCCESFUL_TRANSFER_ADMIN(split_transfer))
                        await bot.send_message(chat_id=-1001830374842,
                                               text=f"""<b>#SUCCESFULLY_TRANSFER\n\nPul o'tkazildi:</b> {split_transfer}
Admin: <a href='tg://user?id={message.from_id}'>{message.from_user.first_name}</a>
Qabul qiluvchi: <a href='tg://user?id={response}'>{response_name}</a>""", parse_mode='html')

                    except Exception as exc:
                        print(exc)
                        await message.reply(NEED_REPLY())
            else:
                if splitted_msg[1].isdigit() and not int(splitted_msg[1]) == 0:
                    split_transfer = int(splitted_msg[1])
                    try:
                        response = message['reply_to_message']['from']['id']
                        response_name = message.reply_to_message.from_user.first_name
                        replied_user_balance = db.get_balance(response)
                        new_balance = replied_user_balance + split_transfer
                        db.update_balance(response, int(new_balance))
                        await message.reply(SUCCESFUL_TRANSFER_ADMIN_UZ(split_transfer))
                        await bot.send_message(chat_id=-1001830374842,
                                               text=f"""<b>#SUCCESFULLY_TRANSFER\n\nPul o'tkazildi:</b> {split_transfer}
Admin: <a href='tg://user?id={message.from_id}'>{message.from_user.first_name}</a>
Qabul qiluvchi: <a href='tg://user?id={response}'>{response_name}</a>""", parse_mode='html')

                    except Exception as exc:
                        print(exc)
                        await message.reply(NEED_REPLY_UZ())

        elif (msg.startswith('!д ') or msg.startswith('!d ')) and len(splitted_msg) == 3 and (
                str(message.from_id) == ADMIN_ABDULLOH or str(message.from_id) == ADMIN_KABULOV or str(
                message.from_id) == ADMIN_ISMOIL or str(message.from_id) == ADMIN_JONY or str(
                message.from_id) == ADMIN_KARMP) and not message.chat.id == message.from_id:
            if lang == 'ru':
                if splitted_msg[1].isdigit() and not int(splitted_msg[1]) == 0 and not splitted_msg[2] == '@none':
                    split_transfer = int(splitted_msg[1])
                    split_username = promo_split[2]
                    emplty_list = []
                    try:
                        user_name = db.get_username()
                        for user_names in user_name:
                            emplty_list.append(user_names[0].lower())
                            if user_names[0].lower() == split_username.lower():
                                user_id_index = db.get_user_id_all()
                                user_index = emplty_list.index(f'{split_username.lower()}')
                                user_balance = db.get_balance(user_id_index[user_index][0])
                                new_balance = user_balance + split_transfer
                                db.update_balance(user_id_index[user_index][0], int(new_balance))
                                await message.reply(SUCCESFUL_TRANSFER_ADMIN(split_transfer))
                                await bot.send_message(chat_id=-1001830374842,
                                                       text=f"""<b>#SUCCESFULLY_TRANSFER\n\nPul o'tkazildi:</b> {split_transfer}
Admin: <a href='tg://user?id={message.from_id}'>{message.from_user.first_name}</a>
Qabul qiluvchi: <a href='tg://user?id={user_id_index[user_index][0]}'>{split_username}</a>""", parse_mode='html')

                    except Exception as exc:
                        print(exc)
                        await message.reply(f"Bunday foydalanuvchi mavjud emas!")
            else:
                if splitted_msg[1].isdigit() and not int(splitted_msg[1]) == 0:
                    split_transfer = int(splitted_msg[1])
                    split_username = promo_split[2]
                    emplty_list = []
                    try:
                        user_name = db.get_username()
                        for user_names in user_name:
                            emplty_list.append(user_names[0].lower())
                            if user_names[0].lower() == split_username.lower():
                                user_id_index = db.get_user_id_all()
                                user_index = emplty_list.index(f'{split_username.lower()}')
                                user_balance = db.get_balance(user_id_index[user_index][0])
                                new_balance = user_balance + split_transfer
                                db.update_balance(user_id_index[user_index][0], int(new_balance))
                                await message.reply(SUCCESFUL_TRANSFER_ADMIN_UZ(split_transfer))
                                await bot.send_message(chat_id=-1001830374842,
                                                       text=f"""<b>#SUCCESFULLY_TRANSFER\n\nPul o'tkazildi:</b> {split_transfer}
Admin: <a href='tg://user?id={message.from_id}'>{message.from_user.first_name}</a>
Qabul qiluvchi: <a href='tg://user?id={user_id_index[user_index][0]}'>{split_username}</a>""", parse_mode='html')




                    except Exception as exc:
                        await message.reply(f"Bunday foydalanuvchi mavjud emas!")
                        pass


        elif (msg.startswith('!д ') or msg.startswith('!d ')) and len(splitted_msg) == 2 and (
                str(message.from_id) == ADMIN_ABDULLOH or str(message.from_id) == ADMIN_KARMP or str(
                message.from_id) == ADMIN_KABULOV or str(message.from_id) == ADMIN_ISMOIL or str(
                message.from_id) == ADMIN_JONY) and not message.chat.id == message.from_id:
            if lang == 'ru':
                if splitted_msg[1].isdigit() and not int(splitted_msg[1]) == 0:
                    split_transfer = int(splitted_msg[1])
                    try:
                        response = message['reply_to_message']['from']['id']
                        response_name = message.reply_to_message.from_user.first_name
                        replied_user_balance = int(db.get_balance(response))
                        new_balance = replied_user_balance + split_transfer
                        db.update_balance(response, int(new_balance))
                        await message.reply(SUCCESFUL_TRANSFER_ADMIN(split_transfer))
                        await bot.send_message(chat_id=-1001830374842,
                                               text=f"""<b>#SUCCESFULLY_TRANSFER\n\nPul o'tkazildi:</b> {split_transfer}
Admin: <a href='tg://user?id={message.from_id}'>{message.from_user.first_name}</a>
Qabul qiluvchi: <a href='tg://user?id={response}'>{response_name}</a>""", parse_mode='html')

                    except Exception as exc:
                        await message.reply(NEED_REPLY())
            else:
                if splitted_msg[1].isdigit():
                    split_transfer = int(splitted_msg[1])
                    try:
                        response = message['reply_to_message']['from']['id']
                        response_name = message.reply_to_message.from_user.first_name
                        replied_user_balance = int(db.get_balance(response))
                        new_balance = replied_user_balance + split_transfer
                        db.update_balance(response, int(new_balance))
                        await message.reply(SUCCESFUL_TRANSFER_ADMIN_UZ(split_transfer))
                        await bot.send_message(chat_id=-1001830374842,
                                               text=f"""<b>#SUCCESFULLY_TRANSFER\n\nPul o'tkazildi:</b> {split_transfer}
Admin: <a href='tg://user?id={message.from_id}'>{message.from_user.first_name}</a>
Qabul qiluvchi: <a href='tg://user?id={response}'>{response_name}</a>""", parse_mode='html')

                    except Exception as exc:
                        await message.reply(f"Bunday foydalanuvchi mavjud emas!")

        elif (msg.startswith('!д- ') or msg.startswith('!d- ')) and len(splitted_msg) == 3 and (
                str(message.from_id) == ADMIN_ABDULLOH or str(message.from_id) == ADMIN_KARMP or str(
                message.from_id) == ADMIN_KABULOV or str(message.from_id) == ADMIN_ISMOIL or str(
                message.from_id) == ADMIN_JONY) and not message.chat.id == message.from_id:
            if lang == 'ru':
                if splitted_msg[1].isdigit() and not int(splitted_msg[1]) == 0 and not splitted_msg[2] == '@none':
                    emplty_list = []
                    split_transfer = int(splitted_msg[1])
                    split_username = promo_split[2]
                    try:
                        user_name = db.get_username()
                        for user_names in user_name:
                            emplty_list.append(user_names[0].lower())
                            if user_names[0].lower() == split_username.lower():
                                user_id_index = db.get_user_id_all()
                                user_index = emplty_list.index(f'{split_username.lower()}')
                                user_balance = int(db.get_balance(user_id_index[user_index][0]))
                                new_balance = user_balance - split_transfer
                                db.update_balance(user_id_index[user_index][0], int(new_balance))
                                await message.reply(SUCCESFUL_TRANSFERMINUS_ADMIN(split_transfer))
                                await bot.send_message(chat_id=-1001830374842,
                                                       text=f"""<b>#SUCCESFULLY_TRANSFER_MINUS\n\nPul o'tkazildi:</b> {split_transfer}
Admin: <a href='tg://user?id={message.from_id}'>{message.from_user.first_name}</a>
Qabul qiluvchi: <a href='tg://user?id={user_id_index[user_index][0]}'>{split_username}</a>""", parse_mode='html')

                    except Exception as exc:
                        await message.reply(f"Bunday foydalanuvchi mavjud emas!")
            else:
                if splitted_msg[1].isdigit():
                    split_transfer = int(splitted_msg[1])
                    split_username = promo_split[2]
                    emplty_list = []
                    try:
                        user_name = db.get_username()
                        for user_names in user_name:
                            emplty_list.append(user_names[0].lower())
                            if user_names[0].lower() == split_username.lower():
                                user_id_index = db.get_user_id_all()
                                user_index = emplty_list.index(f'{split_username.lower()}')
                                user_balance = int(db.get_balance(user_id_index[user_index][0]))
                                new_balance = user_balance - split_transfer
                                db.update_balance(user_id_index[user_index][0], int(new_balance))
                                await message.reply(SUCCESFUL_TRANSFERMINUS_ADMIN(split_transfer))
                                await bot.send_message(chat_id=-1001830374842,
                                                       text=f"""<b>#SUCCESFULLY_TRANSFER_MINUS\n\nPul o'tkazildi:</b> {split_transfer}
Admin: <a href='tg://user?id={message.from_id}'>{message.from_user.first_name}</a>
Qabul qiluvchi: <a href='tg://user?id={user_id_index[user_index][0]}'>{split_username}</a>""", parse_mode='html')

                    except Exception as exc:
                        await message.reply(f"Bunday foydalanuvchi mavjud emas!")


        elif (msg.startswith('!д- ') or msg.startswith('!d-')) and len(splitted_msg) == 2 and (
                str(message.from_id) == ADMIN_ABDULLOH or str(message.from_id) == ADMIN_KABULOV or str(
                message.from_id) == ADMIN_KARMP or str(message.from_id) == ADMIN_ISMOIL or str(
                message.from_id) == ADMIN_JONY) and not message.chat.id == message.from_id:
            if lang == 'ru':
                if splitted_msg[1].isdigit() and not int(splitted_msg[1]) == 0:
                    split_transfer = int(splitted_msg[1])
                    try:
                        response = message['reply_to_message']['from']['id']
                        replied_user_balance = int(db.get_balance(response))
                        response_name = message.reply_to_message.from_user.first_name
                        new_balance = replied_user_balance - split_transfer
                        db.update_balance(response, int(new_balance))
                        await message.reply(SUCCESFUL_TRANSFERMINUS_ADMIN(split_transfer))
                        await bot.send_message(chat_id=-1001830374842,
                                               text=f"""<b>#SUCCESFULLY_TRANSFER_MINUS\n\nPul o'tkazildi:</b> -{split_transfer}
Admin: <a href='tg://user?id={message.from_id}'>{message.from_user.first_name}</a>
Qabul qiluvchi: <a href='tg://user?id={response}'>{response_name}</a>""", parse_mode='html')


                    except Exception as exc:
                        print(exc)
                        await message.reply(NEED_REPLY())
            else:
                if splitted_msg[1].isdigit() and not int(splitted_msg[1]) == 0:
                    split_transfer = int(splitted_msg[1])
                    try:
                        response = message['reply_to_message']['from']['id']
                        replied_user_balance = int(db.get_balance(response))
                        response_name = message.reply_to_message.from_user.first_name
                        new_balance = replied_user_balance - split_transfer
                        db.update_balance(response, int(new_balance))
                        await message.reply(SUCCESFUL_TRANSFERMINUS_ADMIN_UZ(split_transfer))
                        await bot.send_message(chat_id=-1001830374842,
                                               text=f"""<b>#SUCCESFULLY_TRANSFER_MINUS\n\nPul o'tkazildi:</b> -{split_transfer}
Admin: <a href='tg://user?id={message.from_id}'>{message.from_user.first_name}</a>
Qabul qiluvchi: <a href='tg://user?id={response}'>{response_name}</a>""", parse_mode='html')


                    except NameError:
                        print(exc)
                        await message.reply(NEED_REPLY())
                    except:
                        await message.reply(NEED_REPLY())

        elif (msg.startswith('prig ') or msg.startswith('приг')) and (
                str(message.from_id) == ADMIN_ISMOIL or str(message.from_id) == ADMIN_KABULOV or str(
                message.from_id) == ADMIN_KARMP or str(message.from_id) == ADMIN_ABDULLOH or str(
                message.from_id) == ADMIN_JONY) and not message.chat.id == message.from_id and len(splitted_msg) == 2:
            if lang == 'uz':
                if splitted_msg[1].isdigit() and not int(splitted_msg[1]) == 0:
                    split_prig = int(splitted_msg[1])
                    try:
                        response = message.reply_to_message.from_id
                        prig_x = 10000 * split_prig
                        replied_user_balance = int(db.get_balance(response))
                        new_balance = replied_user_balance + prig_x
                        db.update_balance(response, new_balance)
                        await message.reply(SUCCESFUL_TRANSFER_ADMIN_UZ(prig_x))
                        await bot.send_message(chat_id=-1001830374842, text=f"""<b>#PRIG\n\nPul o'tkazildi:</b> {prig_x}
Admin: <a href='tg://user?id={message.from_id}'>{message.from_user.first_name}</a>
Qabul qiluvchi: <a href='tg://user?id={response}'>{message.reply_to_message.from_user.first_name}</a>
PRIG: {split_prig}""", parse_mode='html')
                    except:
                        await message.reply(NEED_REPLY_UZ())
            else:
                if splitted_msg[1].isdigit() and not int(splitted_msg[1]) == 0:
                    split_prig = int(splitted_msg[1])
                    try:
                        response = message.reply_to_message.from_id
                        prig_x = 10000 * split_prig
                        replied_user_balance = int(db.get_balance(response))
                        new_balance = replied_user_balance + prig_x
                        db.update_balance(response, new_balance)
                        await message.reply(SUCCESFUL_TRANSFER_ADMIN(prig_x))
                        await bot.send_message(chat_id=-1001830374842,
                                               text=f"""<b>Pul o'tkazildi:</b> - {prig_x}
Admin: <a href='tg://user?id={message.from_id}'>{message.from_user.first_name}</a>
Qabul qiluvchi: <a href='tg://user?id={response}'>{message.reply_to_message.from_user.first_name}</a>
PRIG: {split_prig}""", parse_mode='html')
                    except:
                        await message.reply(NEED_REPLY())

        elif (msg.startswith('!т ') or msg.startswith('!t ')) and len(
                splitted_msg) == 2 and not message.chat.id == message.from_id:
            if lang == 'uz':
                if splitted_msg[1].isdigit() and not int(splitted_msg[1]) == 0:
                    split_transfer = int(splitted_msg[1])
                    limit_int = db.get_limit(message.from_id) + split_transfer
                    if split_transfer <= get_max_limit(limit_lvl):
                        if balance >= split_transfer:
                            if db.get_limit(message.from_id) <= get_max_limit(limit_lvl):
                                if limit_int <= get_max_limit(limit_lvl):
                                    try:
                                        response = message['reply_to_message']['from']['id']
                                        replied_user_balance = db.get_balance(response)
                                        new_balance = replied_user_balance + split_transfer
                                        if response == message.from_id:
                                            limit = db.get_limit(message.from_id)
                                            db.update_limit(message.from_id, int(limit) + split_transfer)
                                            limit_new = db.get_limit(message.from_id)
                                            await message.reply(
                                                f"""<b>{SUCCESFUL_TRANSFER_UZ(limit_new, get_max_limit(limit_lvl))}</b>""",
                                                parse_mode='HTML')
                                        else:
                                            db.update_balance(response, new_balance)
                                            db.update_balance(message.from_id, balance - split_transfer)
                                            limit = db.get_limit(message.from_id)
                                            db.update_limit(message.from_id, int(limit) + split_transfer)
                                            limit_new = db.get_limit(message.from_id)
                                            await message.reply(
                                                f"""<b>{SUCCESFUL_TRANSFER_UZ(limit_new, get_max_limit(limit_lvl))}</b>""",
                                                parse_mode='HTML')
                                    except:
                                        await message.reply(NEED_REPLY_UZ())
                                else:
                                    await message.reply(LIMIT_TEXT_UZ)
                            else:
                                await message.reply(LIMIT_TEXT_UZ)
                        else:
                            await message.reply(NOT_ENOUGH_MONEY_UZ(balance))
                    else:
                        await message.reply(LIMIT_TEXT_UZ)
            else:
                if splitted_msg[1].isdigit() and not int(splitted_msg[1]) == 0:
                    split_transfer = int(splitted_msg[1])
                    limit_int = db.get_limit(message.from_id) + split_transfer
                    if split_transfer <= get_max_limit(limit_lvl):
                        if balance >= split_transfer:
                            if db.get_limit(message.from_id) <= get_max_limit(limit_lvl):
                                if limit_int <= get_max_limit(limit_lvl):
                                    try:
                                        response = message['reply_to_message']['from']['id']
                                        replied_user_balance = db.get_balance(response)
                                        new_balance = replied_user_balance + split_transfer
                                        if response == message.from_id:
                                            limit = db.get_limit(message.from_id)
                                            db.update_limit(message.from_id, int(limit) + split_transfer)
                                            limit_new = db.get_limit(message.from_id)
                                            await message.reply(
                                                f"""<b>{SUCCESFUL_TRANSFER(limit_new, get_max_limit(limit_lvl))}</b>""",
                                                parse_mode='HTML')
                                        else:
                                            db.update_balance(response, new_balance)
                                            db.update_balance(message.from_id, balance - split_transfer)
                                            limit = db.get_limit(message.from_id)
                                            db.update_limit(message.from_id, int(limit) + split_transfer)
                                            limit_new = db.get_limit(message.from_id)
                                            await message.reply(
                                                f"""<b>{SUCCESFUL_TRANSFER(limit_new, get_max_limit(limit_lvl))}</b>""",
                                                parse_mode='HTML')


                                    except:
                                        await message.reply(NEED_REPLY())
                                else:
                                    await message.reply(LIMIT_TEXT)
                            else:
                                await message.reply(LIMIT_TEXT)
                        else:
                            await message.reply(NOT_ENOUGH_MONEY(balance))
                    else:
                        await message.reply(LIMIT_TEXT)

        elif (msg == '!банк' or msg == '!bank') and message.chat.id == message.from_id:
            await db.add_user_bank(message.from_id, 0, 1)
            await message.reply(f"""<b>💵Баланс в банке: {get_bank}</b>

<i>Пополнить счет - !банкввод сумма
Вывести - !банквывод сумма</i>""", parse_mode='HTML')



        elif (msg.startswith('!банкввод ') or msg.startswith('!bankvvod ')) and len(
                splitted_msg) == 2 and message.chat.id == message.from_id:
            try:
                if lang == 'ru':
                    if splitted_msg[1].isdigit() and not int(splitted_msg[1]) == 0:
                        bank_plus = int(splitted_msg[1])
                        if balance >= bank_plus:
                            new_bank = int(get_bank) + bank_plus
                            new_balance = balance - bank_plus
                            db.update_bank_balance(message.from_id, new_bank)
                            db.update_balance(message.from_id, new_balance)
                            await message.reply(f"""<b>✔️Баланс банка был пополнен</b>""", parse_mode='HTML')
                        else:
                            await message.reply(f"""<b>❌Не хватает денег для пополнения счета</b>""", parse_mode='html')
                else:
                    if splitted_msg[1].isdigit():
                        bank_plus = int(splitted_msg[1])
                        if balance >= bank_plus:
                            new_bank = int(get_bank) + bank_plus
                            new_balance = int(balance) - bank_plus
                            db.update_bank_balance(message.from_id, new_bank)
                            db.update_balance(message.from_id, new_balance)
                            await message.reply(f"""<b>✔️Bankning balansi muvvafaqiyatli to'ldirildi</b>""",
                                                parse_mode='HTML')
                        else:
                            await message.reply(f"""<b>❌Hisobni to'ldirish uchun maglag' yetarli emas</b>""",
                                                parse_mode='html')
            except:
                pass

        elif (msg == '!лимит' or msg == '!limit') and message.chat.id == message.from_id:
            try:
                limit_int = db.get_limit(message.from_id)
                if limit_lvl == 1:
                    await message.reply(f"""<b>⏱Дневной лимит: {limit_int}/{get_max_limit(limit_lvl)}
📈Уровень лимита: {limit_lvl}</b>""", reply_markup=limit_lvl1, parse_mode='html')
                elif limit_lvl == 2:
                    await message.reply(f"""<b>⏱Дневной лимит: {limit_int}/{get_max_limit(limit_lvl)}
📈Уровень лимита: {limit_lvl}</b>""", reply_markup=limit_lvl2, parse_mode='html')
                elif limit_lvl == 3:
                    await message.reply(f"""<b>⏱Дневной лимит: {limit_int}/{get_max_limit(limit_lvl)}
📈Уровень лимита: {limit_lvl}</b>""", reply_markup=limit_lvl3, parse_mode='html')
                elif limit_lvl == 4:
                    await message.reply(f"""<b>⏱Дневной лимит: {limit_int}/{get_max_limit(limit_lvl)}
📈Уровень лимита: {limit_lvl}</b>""", reply_markup=limit_lvl4, parse_mode='html')
                elif limit_lvl == 5:
                    await message.reply(f"""<b>⏱Дневной лимит: {limit_int}/{get_max_limit(limit_lvl)}
📈Уровень лимита: {limit_lvl}</b>""", reply_markup=limit_lvl5, parse_mode='html')
                elif limit_lvl == 6:
                    await message.reply(f"""<b>⏱Дневной лимит: {limit_int}/{get_max_limit(limit_lvl)}
📈Уровень лимита: {limit_lvl}</b>""", reply_markup=limit_lvl6, parse_mode='html')
                elif limit_lvl == 7:
                    await message.reply(f"""<b>⏱Дневной лимит: {limit_int}/{get_max_limit(limit_lvl)}
📈Уровень лимита: {limit_lvl}</b>""", reply_markup=limit_lvl7, parse_mode='html')
                elif limit_lvl == 8:
                    await message.reply(f"""<b>⏱Дневной лимит: {limit_int}/{get_max_limit(limit_lvl)}
📈Уровень лимита: {limit_lvl}</b>""", reply_markup=limit_lvl8, parse_mode='html')
                elif limit_lvl == 9:
                    await message.reply(f"""<b>⏱Дневной лимит: {limit_int}/{get_max_limit(limit_lvl)}
📈Уровень лимита: {limit_lvl}</b>""", reply_markup=limit_lvl9, parse_mode='html')
                elif limit_lvl == 10:
                    await message.reply(f"""<b>⏱Дневной лимит: {limit_int}/{get_max_limit(limit_lvl)}
📈Уровень лимита: {limit_lvl}</b>""", reply_markup=limit_lvl10, parse_mode='html')
                elif limit_lvl == 11:
                    await message.reply(f"""<b>⏱Дневной лимит: {limit_int}/{get_max_limit(limit_lvl)}
📈Уровень лимита: {limit_lvl} (MAX)</b>""", parse_mode='html')
            except:
                pass

        elif (msg.startswith('!банквывод ') or msg.startswith('!bankvivod ')) and len(
                splitted_msg) == 2 and message.chat.id == message.from_id:
            try:
                if splitted_msg[1].isdigit() and not int(splitted_msg[1]) == 0:
                    bank_plus = int(splitted_msg[1])
                    if get_bank >= bank_plus:
                        new_bank = int(get_bank) - bank_plus
                        new_balance = int(balance) + bank_plus
                        db.update_bank_balance(message.from_id, new_bank)
                        db.update_balance(message.from_id, new_balance)
                        await message.reply(f"""<b>✔️Деньги были перечислены на счет</b>""", parse_mode='HTML')
                    else:
                        await message.reply(f"""<b>❌Не хватает денег для списания счета</b>""", parse_mode='html')
            except:
                pass

        elif (msg == '!кланвход' or msg == '!klanvxod') and not message.chat.id == message.from_id:
            try:
                if lang == 'ru':
                    if clan_id_user == 'NoneClan.clanNone.clan.clan.None':
                        db.update_clan_user(str(group_id), str(message.from_id))
                        new_clan_name = db.get_clan_name(group_id)
                        await message.answer(f"✅ Вы успешно вступили в клан <b>{new_clan_name}</b>", parse_mode='html')
                    elif clan_id_user == str(message.chat.id):
                        await message.answer("<b>⛔️ Вы уже состоите в этом клане</b>", parse_mode='html')
                    else:
                        await message.answer(f"""<b>⛔️ Чтобы зайти в этот клан нужно выйти из предыдущего</b>
!кланвыход - для выхода из клана""", parse_mode='html')

                else:
                    if clan_id_user == 'NoneClan.clanNone.clan.clan.None':
                        db.update_clan_user(str(group_id), str(message.from_id))
                        new_clan_name = db.get_clan_name(group_id)
                        print(new_clan_name)
                        await message.answer(f"✅ Siz klanga muvaffaqiyatli qo'shildingiz <b>{new_clan_name}</b>",
                                             parse_mode='html')
                    elif clan_id_user == str(message.chat.id):
                        await message.answer("<b>⛔️ Siz allaqachon ushbu klan a'zosisiz</b>", parse_mode='html')
                    else:
                        await message.answer(f"""<b>⛔️ Bu klanga kirish uchun oldingisidan chiqish kerak</b>
        !klanvixod - klanni tark etish""", parse_mode='html')
            except Exception as exc:
                pass


        elif (msg == '!кланвыход' or msg == '!klanvixod') and not message.chat.id == message.from_id:
            try:
                if lang == 'ru':
                    if not clan_id_user == 'NoneClan.clanNone.clan.clan.None':
                        old_clan_name = db.get_clan_name(clan_id_user)
                        db.update_clan_user('NoneClan.clanNone.clan.clan.None', str(message.from_id))
                        await message.answer(f"✅ Вы успешно покинули клан <b>{old_clan_name}</b>", parse_mode='html')

                else:
                    if not clan_id_user == 'NoneClan.clanNone.clan.clan.None':
                        old_clan_name = db.get_clan_name(clan_id_user)
                        db.update_clan_user('NoneClan.clanNone.clan.clan.None', str(message.from_id))
                        await message.answer(f"✅Siz klandan muvaffaqiyatli tark ketdingiz <b>{old_clan_name}</b>",
                                             parse_mode='html')

            except Exception as exc:
                pass

        elif (msg.startswith('!klanname ') or msg.startswith('!кланимя ')) and len(
                promo_split) == 2 and not message.chat.id == message.from_id:
            try:
                if lang == 'ru':
                    if str(message.from_id) == str(creator_id):
                        new_clan_name = promo_split[1]
                        db.update_clan_name(new_clan_name, group_id)
                        await message.answer(f"<i>🛖 Название клана было изменено:</i> <b>{new_clan_name}</b>",
                                             parse_mode='html')
                else:
                    if str(message.from_id) == str(creator_id):
                        new_clan_name = promo_split[1]
                        db.update_clan_name(new_clan_name, group_id)
                        await message.answer(f"<i>🛖 Klan ismi o'zgardi:</i> <b>{new_clan_name}</b>", parse_mode='html')
            except Exception as exc:
                pass


        elif msg == '!klantop' or msg == '!клантоп':
            try:
                user_clan = db.get_clan_user(message.from_id)
                top = db.get_clan_top_name()
                top_id = db.get_clan_top_id()
                top_plays = db.get_clan_top_plays()
                if lang == 'ru':
                    if not user_clan == 'NoneClan.clanNone.clan.clan.None':

                        clan_id = db.get_clan_user(message.from_id)

                        index_user = top_id.index((str(clan_id),))
                        index_user_id = index_user + 1
                        await message.answer(f"""<b>1. {top[0][0]}  —  {top_str_to_int(int(top_plays[0][0]))}🎰
2.  {top[1][0]}  —  {top_str_to_int(int(top_plays[1][0]))}🎰
3.  {top[2][0]}  —  {top_str_to_int(int(top_plays[2][0]))}🎰
4.  {top[3][0]}  —  {top_str_to_int(int(top_plays[3][0]))}🎰
5.  {top[4][0]}  —  {top_str_to_int(int(top_plays[4][0]))}🎰
6.  {top[5][0]}  —  {top_str_to_int(int(top_plays[5][0]))}🎰
7.  {top[6][0]}  —  {top_str_to_int(int(top_plays[6][0]))}🎰
8.  {top[7][0]}  —  {top_str_to_int(int(top_plays[7][0]))}🎰 
9.  {top[8][0]}  —  {top_str_to_int(int(top_plays[8][0]))}🎰
10.  {top[9][0]}  —  {top_str_to_int(int(top_plays[9][0]))}🎰

Место клана в топе — {index_user_id}</b>""", parse_mode='html')
                    else:
                        await message.answer(f"""<b>1. {top[0][0]}  —  {top_str_to_int(int(top_plays[0][0]))}🎰
2.  {top[1][0]}  —  {top_str_to_int(int(top_plays[1][0]))}🎰
3.  {top[2][0]}  —  {top_str_to_int(int(top_plays[2][0]))}🎰
4.  {top[3][0]}  —  {top_str_to_int(int(top_plays[3][0]))}🎰
5.  {top[4][0]}  —  {top_str_to_int(int(top_plays[4][0]))}🎰
6.  {top[5][0]}  —  {top_str_to_int(int(top_plays[5][0]))}🎰
7.  {top[6][0]}  —  {top_str_to_int(int(top_plays[6][0]))}🎰
8.  {top[7][0]}  —  {top_str_to_int(int(top_plays[7][0]))}🎰 
9.  {top[8][0]}  —  {top_str_to_int(int(top_plays[8][0]))}🎰
10.  {top[9][0]}  —  {top_str_to_int(int(top_plays[9][0]))}🎰

Вы не состоите в клане</b>""", parse_mode='html')

                else:
                    if not user_clan == 'NoneClan.clanNone.clan.clan.None':
                        top = db.get_clan_top_name()
                        top_id = db.get_clan_top_id()
                        top_plays = db.get_clan_top_plays()
                        clan_id = db.get_clan_user(message.from_id)

                        user_clan = db.get_clan_user(message.from_id)

                        index_user = top_id.index((str(clan_id),))
                        index_user_id = index_user + 1
                        await message.answer(f"""<b>1. {top[0][0]}  —  {top_str_to_int(int(top_plays[0][0]))}🎰
2.  {top[1][0]}  —  {top_str_to_int(int(top_plays[1][0]))}🎰
3.  {top[2][0]}  —  {top_str_to_int(int(top_plays[2][0]))}🎰
4.  {top[3][0]}  —  {top_str_to_int(int(top_plays[3][0]))}🎰
5.  {top[4][0]}  —  {top_str_to_int(int(top_plays[4][0]))}🎰
6.  {top[5][0]}  —  {top_str_to_int(int(top_plays[5][0]))}🎰
7.  {top[6][0]}  —  {top_str_to_int(int(top_plays[6][0]))}🎰
8.  {top[7][0]}  —  {top_str_to_int(int(top_plays[7][0]))}🎰 
9.  {top[8][0]}  —  {top_str_to_int(int(top_plays[8][0]))}🎰
10.  {top[9][0]}  —  {top_str_to_int(int(top_plays[9][0]))}🎰

Klanning top-reyitinggi — {index_user_id}</b>""", parse_mode='html')
                    else:
                        await message.answer(f"""<b>1. {top[0][0]}  —  {top_str_to_int(int(top_plays[0][0]))}🎰
2.  {top[1][0]}  —  {top_str_to_int(int(top_plays[1][0]))}🎰
3.  {top[2][0]}  —  {top_str_to_int(int(top_plays[2][0]))}🎰
4.  {top[3][0]}  —  {top_str_to_int(int(top_plays[3][0]))}🎰
5.  {top[4][0]}  —  {top_str_to_int(int(top_plays[4][0]))}🎰
6.  {top[5][0]}  —  {top_str_to_int(int(top_plays[5][0]))}🎰
7.  {top[6][0]}  —  {top_str_to_int(int(top_plays[6][0]))}🎰
8.  {top[7][0]}  —  {top_str_to_int(int(top_plays[7][0]))}🎰 
9.  {top[8][0]}  —  {top_str_to_int(int(top_plays[8][0]))}🎰
10.  {top[9][0]}  —  {top_str_to_int(int(top_plays[9][0]))}🎰

Siz klan a'zosi emassiz</b>""", parse_mode='html')


            except Exception as exc:
                # print(exc)
                pass


        elif msg == 'mute' or msg == 'ban' or msg.startswith('mute ') or msg.startswith('мут ') or msg == 'мут':
            if message.reply_to_message.from_id == int(ADELYA):
                try:
                    msg_id = message.message_id
                    chat_id = message.chat.id
                    await bot.delete_message(chat_id=chat_id, message_id=msg_id)
                    await bot.unban_chat_member(chat_id=chat_id, user_id=int(ADELYA))
                except:
                    pass


        elif msg == 'трахнуть' or msg == 'поцеловать' or msg == '.трахнуть' or msg == '.поцеловать' or msg_all.startswith(
                '👉👌 | Ade_lya принудил к интиму ') or msg_all.endswith('принудил к интиму Ade_lya') or msg.startswith(
                '.трахнуть ') or msg.startswith('.поцеловать ') or msg.startswith('!поцеловать') or msg.startswith(
                '!трахнуть'):
            if message.reply_to_message.from_id == int(ADELYA) and not message.from_id == int(
                    ADMIN_ABDULLOH) and not msg_all == '👉👌 | Ade_lya принудил к интиму sk1ll' and not msg_all == '👉👌 | sk1ll принудил к интиму Ade_lya':
                try:
                    msg_id = message.message_id
                    chat_id = message.chat.id
                    await bot.delete_message(chat_id=chat_id, message_id=msg_id)
                except Exception as exc:
                    print(exc)
                    pass


        elif message.chat.id == -4091704676 and message.from_id == int(ADMIN_ABDULLOH):
            try:
                await message.forward(chat_id=-1001774771519)
            except:
                pass


        elif (msg == '!prig' or msg == '!приг') and message.chat.id == message.from_id:
            try:
                balance_prig = db.get_prig(message.from_id)
                if lang == 'ru':
                    await message.reply(f"""<b>🖇Баланс в приг: {balance_prig}</b>

<i>Снять деньги - <code>!гетприг [сумма]</code></i>""", parse_mode='html')
                else:
                    await message.reply(f"""<b>Balans Prig: {balance_prig}</b>

<i>Pul chiqarib olish - <code>!getprig [summa]</code></i>""", parse_mode='html')
            except:
                pass


        elif (msg.startswith('!гетприг ') or msg.startswith(
                '!getprig ')) and message.chat.id == message.from_id and len(splitted_msg) == 2:
            try:
                balance_prig = int(db.get_prig(message.from_id))
                if splitted_msg[1].isdigit():
                    if int(balance_prig) >= int(splitted_msg[1]):
                        if int(splitted_msg[1]) >= 70000:
                            get_balance = int(splitted_msg[1])
                            if lang == 'ru':
                                await message.reply(f"""<b>✔️Ваш баланс успешно пополнен: {get_balance}</b>""",
                                                    parse_mode='html')
                                db.update_prig(message.from_id, balance_prig - get_balance)
                                db.update_balance(message.from_id, balance + get_balance)
                            else:
                                await message.reply(
                                    f"""<b>✔️Balansingiz muvvafaqiyatli to'ldirildi: {get_balance}</b>""",
                                    parse_mode='html')
                                db.update_prig(message.from_id, balance_prig - get_balance)
                                db.update_balance(message.from_id, balance + get_balance)
                        else:
                            if lang == 'ru':
                                await message.answer("""<b>Сумма должна быть не менее 70 000</b>""", parse_mode='html')
                            else:
                                await message.answer("""<b>Summa 70.000 dan baland bo'lishi kerak</b>""",
                                                     parse_mode='html')
                    else:
                        if lang == 'ru':
                            await message.answer(f"""<b>❌Ваш баланс недостаточен! В балансе: {balance_prig}</b>""",
                                                 parse_mode='html')
                        else:
                            await message.answer(
                                f"""<b>❌Balansingizda mablag' yetarli emas! Balansda: {balance_prig}</b>""",
                                parse_mode='html')
            except Exception as exc:
                print(exc)
                pass

    except Exception as exc:
        print(exc)
        pass


@dp.callback_query_handler(lambda a: a.data)
async def inline(call: types.CallbackQuery):
    callback = call.data
    balance = db.get_balance(call.from_user.id)
    response = call['message']['chat']['id']

    try:
        if callback == 'promo':
            await bot.send_message(chat_id=call.from_user.id,
                                   text=f"<b>Введите новый промокод!\n\n!активпромо [ПРОМОКОД] Пример: !активпромо SPINCHIK</b>",
                                   parse_mode='html')
        elif callback == 'games':
            await bot.send_message(chat_id=response, text=f"<b>Выберите👇</b>", reply_markup=games_btn,
                                   parse_mode='html')
        elif callback == 'basket':
            await bot.send_message(chat_id=response, text=f"""<b>Игра баскетбол, где выигрыш зависит от забитого мяча. 
Коэффициенты: 2х или 3х
Ставка: 
<code>!б </code>[сумма ставки]
Пример: <code>!б 1000</code></b>""", parse_mode='html')
        elif callback == 'dart':
            await bot.send_message(chat_id=response, text=f"""<b>Игра, где выигрыш зависит от попадания в центр круга. Если игрок попадает в «яблочко», то получает 4х от суммы ставки. 
Коэффициенты:4х
Ставка: 
<code>!дартс </code>[сумма ставки]
Пример: <code>!дарст 1000</code></b>""", parse_mode='html')
        elif callback == 'slot':
            await bot.send_message(chat_id=response, text=f"""<b>Игра, где нужно выбить комбинацию из 2 или 3 похожих предметов в игровом автомате.
Коэффициенты: 
77 - 2х, 2Bar - 1,5х, 2🍇  и 2🍋 - 1,25

 777 - 6х, 3Bar - 4,5х, 3🍇 - и 3🍋 - 3х

Важно, чтобы предметы шли подряд. В остальных случаях ставка обнуляется, то есть вы получаете 0.
Ставка: !слот [сумма ставки]
Пример: !слот 1000</b>""", parse_mode='html')
        elif callback == 'boul':
            await bot.send_message(chat_id=response, text=f"""<b>Игра боулинг, где выигрыш зависит от кол-ва сбитых кеглей.
Коэффициенты: при выбивании 4/6 и 5/6 игрок получает 1,5х от суммы ставки, при выбивании 6/6 игрок получает 2х от суммы ставки.
Ставка: 
!боул [сумма ставки] 
Пример: !боул 1000</b>""", parse_mode='html')

        # Upgrade Limit Level
        elif callback == 'limitlvl1':
            if balance >= 750000:
                db.update_balance(call.from_user.id, balance - 750000)
                db.update_limit_lvl(call.from_user.id, 2)
                await call.answer("Уровень лимита успешно увеличен!")

            else:
                await call.answer("У вас недостаточно денег❌")
        elif callback == 'limitlvl2':
            if balance >= 1500000:
                db.update_balance(call.from_user.id, balance - 1500000)
                db.update_limit_lvl(call.from_user.id, 3)
                await call.answer("Уровень лимита успешно увеличен!")

            else:
                await call.answer("У вас недостаточно денег❌")
        elif callback == 'limitlvl3':
            if balance >= 2250000:
                db.update_balance(call.from_user.id, balance - 2250000)
                db.update_limit_lvl(call.from_user.id, 4)
                await call.answer("Уровень лимита успешно увеличен!")

            else:
                await call.answer("У вас недостаточно денег❌")
        elif callback == 'limitlvl4':
            if balance >= 3000000:
                db.update_balance(call.from_user.id, balance - 3000000)
                db.update_limit_lvl(call.from_user.id, 5)
                await call.answer("Уровень лимита успешно увеличен!")

            else:
                await call.answer("У вас недостаточно денег❌")
        elif callback == 'limitlvl5':
            if balance >= 3750000:
                db.update_balance(call.from_user.id, balance - 3750000)
                db.update_limit_lvl(call.from_user.id, 6)
                await call.answer("Уровень лимита успешно увеличен!")

            else:
                await call.answer("У вас недостаточно денег❌")

        elif callback == 'limitlvl6':
            if balance >= 4500000:
                db.update_balance(call.from_user.id, balance - 4500000)
                db.update_limit_lvl(call.from_user.id, 7)
                await call.answer("Уровень лимита успешно увеличен!")

            else:
                await call.answer("У вас недостаточно денег❌")
        elif callback == 'limitlvl7':
            if balance >= 5250000:
                db.update_balance(call.from_user.id, balance - 5250000)
                db.update_limit_lvl(call.from_user.id, 8)
                await call.answer("Уровень лимита успешно увеличен!")

            else:
                await call.answer("У вас недостаточно денег❌")
        elif callback == 'limitlvl8':
            if balance >= 6000000:
                db.update_balance(call.from_user.id, balance - 6000000)
                db.update_limit_lvl(call.from_user.id, 9)
                await call.answer("Уровень лимита успешно увеличен!")

            else:
                await call.answer("У вас недостаточно денег❌")
        elif callback == 'limitlvl9':
            if balance >= 6750000:
                db.update_balance(call.from_user.id, balance - 6750000)
                db.update_limit_lvl(call.from_user.id, 10)
                await call.answer("Уровень лимита успешно увеличен!")

            else:
                await call.answer("У вас недостаточно денег❌")
        elif callback == 'limitlvl10':
            if balance >= 7500000:
                db.update_balance(call.from_user.id, balance - 7500000)
                db.update_limit_lvl(call.from_user.id, 11)
                await call.answer("Уровень лимита успешно увеличен!")
            else:
                await call.answer("У вас недостаточно денег❌")
        elif callback == 'set_lang_button_uz':
            db.update_lang(call.from_user.id, 'ru')
            await call.answer("Язык успешно изменен!")
        elif callback == 'set_lang_button_ru':
            db.update_lang(call.from_user.id, 'uz')
            await call.answer("Til muvvafaqiyatli o'zgartirildi!")

        # Top About
        elif callback == 'top1_about':
            top = db.get_top()
            user_id = db.get_top_id()
            top_balance = db.get_top_balance()
            await bot.send_message(chat_id=response, text=f"""<b>About TOP - 1

First Name: <a href="tg://user?id={user_id[0][0]}">{top[0][0]}</a>
User Name: {db.get_username_where_id(user_id[0][0])}                  
Balance: {int(top_balance[0][0])}</b>""", parse_mode='html')

        elif callback == 'top2_about':
            top = db.get_top()
            user_id = db.get_top_id()
            top_balance = db.get_top_balance()
            await bot.send_message(chat_id=response, text=f"""<b>About TOP - 2

First Name: <a href="tg://user?id={user_id[1][0]}">{top[1][0]}</a>
User Name: {db.get_username_where_id(user_id[1][0])}                  
Balance: {int(top_balance[1][0])}</b>""", parse_mode='html')

        elif callback == 'top3_about':
            top = db.get_top()
            user_id = db.get_top_id()
            top_balance = db.get_top_balance()
            await bot.send_message(chat_id=response, text=f"""<b>About TOP - 3

First Name: <a href="tg://user?id={user_id[2][0]}">{top[2][0]}</a>
User Name: {db.get_username_where_id(user_id[2][0])}                  
Balance: {int(top_balance[2][0])}</b>""", parse_mode='html')

        elif callback == 'top4_about':
            top = db.get_top()
            user_id = db.get_top_id()
            top_balance = db.get_top_balance()
            await bot.send_message(chat_id=response, text=f"""<b>About TOP - 4

First Name: <a href="tg://user?id={user_id[3][0]}">{top[3][0]}</a>
User Name: {db.get_username_where_id(user_id[3][0])}                  
Balance: {int(top_balance[3][0])}</b>""", parse_mode='html')

        elif callback == 'top5_about':
            top = db.get_top()
            user_id = db.get_top_id()
            top_balance = db.get_top_balance()
            await bot.send_message(chat_id=response, text=f"""<b>About TOP - 5

First Name: <a href="tg://user?id={user_id[4][0]}">{top[4][0]}</a>
User Name: {db.get_username_where_id(user_id[4][0])}                  
Balance: {int(top_balance[4][0])}</b>""", parse_mode='html')

        elif callback == 'top6_about':
            top = db.get_top()
            user_id = db.get_top_id()
            top_balance = db.get_top_balance()
            await bot.send_message(chat_id=response, text=f"""<b>About TOP - 6

First Name: <a href="tg://user?id={user_id[5][0]}">{top[5][0]}</a>
User Name: {db.get_username_where_id(user_id[5][0])}                  
Balance: {int(top_balance[5][0])}</b>""", parse_mode='html')


        elif callback == 'top7_about':
            top = db.get_top()
            user_id = db.get_top_id()
            top_balance = db.get_top_balance()
            await bot.send_message(chat_id=response, text=f"""<b>About TOP - 7

First Name: <a href="tg://user?id={user_id[6][0]}">{top[6][0]}</a>
User Name: {db.get_username_where_id(user_id[6][0])}                  
Balance: {int(top_balance[6][0])}</b>""", parse_mode='html')


        elif callback == 'top8_about':
            top = db.get_top()
            user_id = db.get_top_id()
            top_balance = db.get_top_balance()
            await bot.send_message(chat_id=response, text=f"""<b>About TOP - 8

First Name: <a href="tg://user?id={user_id[7][0]}">{top[7][0]}</a>
User Name: {db.get_username_where_id(user_id[7][0])}                  
Balance: {int(top_balance[7][0])}</b>""", parse_mode='html')


        elif callback == 'top9_about':
            top = db.get_top()
            user_id = db.get_top_id()
            top_balance = db.get_top_balance()
            await bot.send_message(chat_id=response, text=f"""<b>About TOP - 9

First Name: <a href="tg://user?id={user_id[8][0]}">{top[8][0]}</a>
User Name: {db.get_username_where_id(user_id[8][0])}                  
Balance: {int(top_balance[8][0])}</b>""", parse_mode='html')


        elif callback == 'top10_about':
            top = db.get_top()
            user_id = db.get_top_id()
            top_balance = db.get_top_balance()
            await bot.send_message(chat_id=response, text=f"""<b>About TOP - 10

First Name: <a href="tg://user?id={user_id[9][0]}">{top[9][0]}</a>
User Name: {db.get_username_where_id(user_id[9][0])}                  
Balance: {int(top_balance[9][0])}</b>""", parse_mode='html')



    except Exception as exc:
        print(exc)
        pass


# Auto Delete (Sticker and GIFS)
@dp.message_handler(content_types=[types.ContentType.ANIMATION, types.ContentType.STICKER])
async def delete_gif(message: types.Message):
    if message.chat.id == -1001518782629:
        gif = message.message_id
        await bot.delete_message(chat_id=-1001518782629, message_id=gif)


# ADS
@dp.message_handler(content_types=types.ContentType.PHOTO)
async def ads_photo(message: types.Message):
    if message.chat.id == -1002096494546 and message.from_id == int(ADMIN_ABDULLOH):
        ids = db.get_users_for_ads()
        for user_ids in ids:
            try:
                # await bot.send_photo(chat_id=int(user_ids[0]), photo=photo, caption=caption, parse_mode='html')
                await message.forward(chat_id=int(user_ids[0]))
            except:
                pass


@dp.message_handler(content_types=types.ContentType.VIDEO)
async def ads_video(message: types.Message):
    if message.chat.id == -1002096494546 and message.from_id == int(ADMIN_ABDULLOH):
        ids = db.get_users_for_ads()
        for user_ids in ids:
            try:
                # await bot.send_video(chat_id=int(user_ids[0]), video=video, caption=caption, parse_mode='html')
                await message.forward(chat_id=int(user_ids[0]))
            except:
                pass


@dp.message_handler(content_types=types.ContentType.NEW_CHAT_MEMBERS)
async def new_chat_members(message: types.Message):
    try:
        await db.add_prig_user(message.from_id)
        if message.chat.id == -1001518782629 and not message.from_id == message.new_chat_members[0]['id']:
            msg_id = message.from_id
            balance = db.get_prig(message.from_id)
            new_balance = int(balance) + 10000
            db.update_prig(message.from_id, new_balance)
    except:
        pass


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp, skip_updates=True)
