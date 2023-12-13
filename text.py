YOU_LOSED = """❌Вы проиграли😔"""
YOU_LOSED_UZ = """❌Siz yutqazdingiz😔"""
LIMIT_TEXT = """Сумма превышает дневной лимит. Для увеличения лимита введите команду !лимит боту!"""
LIMIT_TEXT_UZ = """Miqdor kunlik limitdan oshib ketdi. Limitni oshirish uchun botga !limit buyrug'ini kiriting!"""


def ADD_PROMO(promo, value, max, admin):
    text = f"""#CREATED_PROMO\n\n✅Промокод успешно добавлен!

Чтобы использовать промокод:
<code>!промокод {promo}</code>

Сумма промокода: {value}
Максимальный пользователь: {max}

Админ: @{admin}"""

    return text


def USE_PROMO(value):
    text = f"""Вы успешно использовали промокод ✅.

Баланс пополнен на {value}💰"""

    return text


def NOT_ENOUGH_MONEY(value):
    text = f"""Не хватает денег. На балансе: {int(value)} 💰."""

    return text


def NOT_ENOUGH_MONEY_UZ(value):
    text = f"""Pul yetarli emas. Balansda: {int(value)} 💰."""

    return text


def YOU_WIN(value):
    text = f"""🏆 Вы победили

Сумма выигрыша — {value} 💰."""

    return text


def YOU_WIN_UZ(value):
    text = f"""🏆 Siz yutdingiz

Yutuq miqdori — {value} 💰."""

    return text


def YOU_WIN_ROCKET(value, summa):
    text = f"""🚀Ракета остановилась на <b>{value}</b>
✅Вы выйграли {int(summa)} 💰"""

    return text


def YOU_WIN_ROCKET_UZ(value, summa):
    text = f"""🚀Raketa toxtadi: <b>{value}</b>
✅Siz yutdingiz {int(summa)} 💰"""

    return text


def YOU_LOSED_ROCKET(value):
    text = f"""Ракета остановилась на <b>{value}</b>
❌Вы проиграли😔"""

    return text


def YOU_LOSED_ROCKET_UZ(value):
    text = f"""Raketa toxtadi: <b>{value}</b>
❌Siz yutqazdingiz"""

    return text


def NEED_REPLY_UZ():
    text = f"""Siz pul o'tkazishingiz kerak bo'lgan odamning xabariga javob berishingiz kerak."""

    return text


def NEED_REPLY():
    text = f"""Нужно ответить на сообщение человека, которому нужно передать деньги."""

    return text


def SUCCESFUL_TRANSFER(value, limit):
    text = f"""Трансфер прошел успешно.
Текущий лимит : {int(value)}/{limit}"""

    return text


def SUCCESFUL_TRANSFER_UZ(value, limit):
    text = f"""Transfer muvaffaqiyatli bo'ldi.
Hozirgi limit: {int(value)}/{limit}"""

    return text


def SUCCESFUL_TRANSFER_ADMIN(value):
    text = f"""Выдал: {int(value)}"""

    return text


def SUCCESFUL_TRANSFER_ADMIN_UZ(value):
    text = f"""Berdi: {int(value)}"""

    return text


def SUCCESFUL_TRANSFERMINUS_ADMIN(value):
    text = f"""Выдал: -{int(value)}"""

    return text


def SUCCESFUL_TRANSFERMINUS_ADMIN_UZ(value):
    text = f"""Berdi: -{int(value)}"""

    return text


def BONUS(value):
    text = f"""Небольшой подарок от администрации</i>🤍

        Получено: {value}💰"""

    return text


def ADMIN_BONUS(value):
    text = f"""Небольшой подарок для администрации 🤍 </i>

    Получено: {value}💰"""

    return text
