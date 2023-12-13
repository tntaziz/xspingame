from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup


help_button = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton("🎮Игры", callback_data='games')
    ],
    [
        InlineKeyboardButton("📑Другое", callback_data='other')
    ],
    [
        InlineKeyboardButton("🇺🇿Изменить язык", callback_data='set_lang_button_ru')
    ]
])

help_button_uz = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton("🎮O'yinlar", callback_data='games_uz')
    ],
    [
        InlineKeyboardButton("📑Boshqa", callback_data='other_uz')
    ],
    [
        InlineKeyboardButton("🇷🇺Tilni o'zgartirish", callback_data='set_lang_button_uz')
    ]
])

add_to_group_btn = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton("➕Добавить в группу", url='http://t.me/xspingamebot?startgroup=true')
    ]
])

add_to_group_btn_uz = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton("➕Guruhga qo'shish", url='http://t.me/xspingamebot?startgroup=true')
    ]
])

admin_button = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton("Promo💸", callback_data='promo')
    ]
])



# Games

games_btn = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton("🏀Баскетбол", callback_data='basket'),
        InlineKeyboardButton("🎯Дартс", callback_data='dart')
    ],
    [
        InlineKeyboardButton("🎰Слот", callback_data='slot'),
        InlineKeyboardButton("🎳Боулинг", callback_data='boul'),
        InlineKeyboardButton("🎲Кубик", callback_data='dice')
    ],
    [
        InlineKeyboardButton("🚀Ракета", callback_data='rocket'),
        InlineKeyboardButton("⚽️Футбол", callback_data='football')
    ],
    [
        InlineKeyboardButton("⬅️", callback_data='back_games')
    ]
])



# Buy

buy = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton("✅Sotib olish", url='https://t.me/xspinadmin')
    ]
])


# Limit Upgrade Buttons

limit_lvl1 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton("Повысить уровен - 750000", callback_data='limitlvl1')
    ]
])


limit_lvl2 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton("Повысить уровен - 1500000", callback_data='limitlvl2')
    ]
])


limit_lvl3 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton("Повысить уровен - 2250000", callback_data='limitlvl3')
    ]
])


limit_lvl4 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton("Повысить уровен - 3000000", callback_data='limitlvl4')
    ]
])


limit_lvl5 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton("Повысить уровен - 3750000", callback_data='limitlvl5')
    ]
])


limit_lvl6 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton("Повысить уровен - 4500000", callback_data='limitlvl6')
    ]
])


limit_lvl7 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton("Повысить уровен - 5250000", callback_data='limitlvl7')
    ]
])


limit_lvl8 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton("Повысить уровен - 6000000", callback_data='limitlvl8')
    ]
])


limit_lvl9 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton("Повысить уровен - 6750000", callback_data='limitlvl9')
    ]
])


limit_lvl10 = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton("Повысить уровен - 7500000", callback_data='limitlvl10')
    ]
])



# Top About

top_about_btn = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton("1️⃣", callback_data='top1_about'),
        InlineKeyboardButton("2️⃣", callback_data='top2_about'),
        InlineKeyboardButton("3️⃣", callback_data='top3_about'),
        InlineKeyboardButton("4️⃣", callback_data='top4_about'),
        InlineKeyboardButton("5️⃣", callback_data='top5_about')
    ],
    [
        InlineKeyboardButton("6️⃣", callback_data='top6_about'),
        InlineKeyboardButton("7️⃣", callback_data='top7_about'),
        InlineKeyboardButton("8️⃣", callback_data='top8_about'),
        InlineKeyboardButton("9️⃣", callback_data='top9_about'),
        InlineKeyboardButton("🔟", callback_data='top10_about')
    ]
])
