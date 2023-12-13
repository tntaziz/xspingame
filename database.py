import sqlite3


async def create_table():
    conn = sqlite3.connect('xspin.db')
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
    user_id VARCHAR(255),
    balance INT,
    bonus_time VARCHAR(255),
    limit_balance INT,
    ismi VARCHAR(255)
    )
    """)

    cur.execute("""CREATE TABLE IF NOT EXISTS promo (
        user_id VARCHAR(255),
        promo VARCHAR(255)
        )
    """)

    cur.execute("""CREATE TABLE IF NOT EXISTS bank (
        user_id VARCHAR(255),
        balance INT,
        bank_level VARCHAR(255)
        )
    """)

    cur.execute("""CREATE TABLE IF NOT EXISTS limit_lvl (
        user_id VARCHAR(255),
        limit_level INT
    )""")

    cur.execute("""CREATE TABLE IF NOT EXISTS add_promo (
    promo_name VARCHAR(255),
    price INT,
    max_user INT
    )""")

    cur.execute("""CREATE TABLE IF NOT EXISTS lang (
    user_id VARCHAR(255),
    user_name VARCHAR(255),
    lang VARCHAR(255)
    )""")

    cur.execute("""CREATE TABLE IF NOT EXISTS statistics_users (
    user_id VARCHAR(255),
    played INT
    )""")

    cur.execute("""CREATE TABLE IF NOT EXISTS clans (
    group_id VARCHAR(255),
    creator_id VARCHAR(255),
    all_plays INT,
    clan_name VARCHAR(255)
    )""")

    cur.execute("""CREATE TABLE IF NOT EXISTS clan_users (
    user_id VARCHAR(255),
    first_name VARCHAR(255),
    played INT,
    clan_id VARCHAR(255)
    )""")

    cur.execute("""CREATE TABLE IF NOT EXISTS debt (
    user_id VARCHAR(255),
    first_name VARCHAR(255),
    debt_bool INT,
    debt_balance INT    
    )""")

    cur.execute("""CREATE TABLE IF NOT EXISTS prig (
    user_id VARCHAR(255),
    balance INT  
    )""")

    conn.commit()
    conn.close()


# conn = sqlite3.connect('xspin.db')
# cur = conn.cursor()
# cur.execute("""ALTER TABLE clan_users
# ADD clan_id VARCHAR(255);""")
# conn.commit()
# conn.close()

async def add_clan_user(user_id, first_name, played, clan_id):
    try:
        conn = sqlite3.connect('xspin.db')
        cur = conn.cursor()
        user = cur.execute(f"""SELECT * FROM clan_users WHERE user_id = {str(user_id)}""").fetchone()
        if not user:
            cur.execute(f"""
                INSERT INTO clan_users (user_id, first_name, played, clan_id) VALUES (?, ?, ?, ?)
            """, (str(user_id), first_name, played, clan_id))

        conn.commit()
        conn.close()
    except Exception as exc:
        print(exc)
        pass


async def add_prig_user(user_id):
    try:
        conn = sqlite3.connect('xspin.db')
        cur = conn.cursor()
        user = cur.execute(f"""SELECT * FROM prig WHERE user_id = {str(user_id)}""").fetchone()
        if not user:
            cur.execute(f"""
                INSERT INTO prig (user_id, balance) VALUES (?, ?)
            """, (str(user_id), 0))

        conn.commit()
        conn.close()
    except Exception as exc:
        print(exc)
        pass


async def add_user_stat(user_id, played):
    try:
        conn = sqlite3.connect('xspin.db')
        cur = conn.cursor()
        user = cur.execute(f"""SELECT * FROM statistics_users WHERE user_id = {str(user_id)}""").fetchone()
        if not user:
            cur.execute(f"""
                INSERT INTO statistics_users (user_id, played) VALUES (?, ?)
            """, (user_id, played))

        conn.commit()
        conn.close()
    except Exception as exc:
        print(exc)
        pass


async def add_clan(group_id: str, creator_id, all_plays, clan_name):
    try:
        conn = sqlite3.connect('xspin.db')
        cur = conn.cursor()
        user = cur.execute(f"""SELECT * FROM clans WHERE group_id = {str(group_id)}""").fetchone()
        if not user:
            cur.execute(f"""
                INSERT INTO clans (group_id, creator_id, all_plays, clan_name) VALUES (?, ?, ?, ?)
            """, (group_id, creator_id, all_plays, clan_name))

        conn.commit()
        conn.close()
    except Exception as exc:
        print(exc)
        pass


async def add_lang_user(user_id: str, user_name, lang):
    try:
        conn = sqlite3.connect('xspin.db')
        cur = conn.cursor()
        user = cur.execute(f"""SELECT * FROM lang WHERE user_id = {str(user_id)}""").fetchone()
        if not user:
            cur.execute(f"""
                INSERT INTO lang (user_id, user_name, lang) VALUES (?, ?, ?)
            """, (user_id, user_name, lang))

        conn.commit()
        conn.close()
    except Exception as exc:
        print(exc)
        pass


async def add_user(user_id: str, balance, bonus_time, limit_balance, first_name):
    try:
        conn = sqlite3.connect('xspin.db')
        cur = conn.cursor()
        user = cur.execute(f"""SELECT * FROM users WHERE user_id = {str(user_id)}""").fetchone()
        if not user:
            cur.execute(f"""
                INSERT INTO users (user_id, balance, bonus_time, limit_balance, ismi) VALUES (?,?,?,?,?)
            """, (user_id, balance, str(bonus_time), limit_balance, first_name))

        conn.commit()
        conn.close()
    except:
        pass


async def add_promo(user_id: str, promo):
    conn = sqlite3.connect('xspin.db')
    cur = conn.cursor()
    cur.execute(f"""
            INSERT INTO promo (user_id, promo) VALUES (?, ?)
        """, (str(user_id), promo))

    conn.commit()
    conn.close()


def get_balance(user_id: str):
    try:
        conn = sqlite3.connect('xspin.db')
        cur = conn.cursor()

        balans = cur.execute(f"""SELECT balance FROM users WHERE user_id == {str(user_id)}""").fetchone()

        conn.commit()
        conn.close()

        try:
            return balans[0]
        except:
            pass

    except:
        pass


def get_prig(user_id: str):
    try:
        conn = sqlite3.connect('xspin.db')
        cur = conn.cursor()

        balans = cur.execute(f"""SELECT balance FROM prig WHERE user_id == {str(user_id)}""").fetchone()

        conn.commit()
        conn.close()

        try:
            return balans[0]
        except:
            pass

    except:
        pass


def get_lang(user_id: str):
    try:
        conn = sqlite3.connect('xspin.db')
        cur = conn.cursor()

        balans = cur.execute(f"""SELECT lang FROM lang WHERE user_id == {str(user_id)}""").fetchone()

        conn.commit()
        conn.close()

        try:
            return balans[0]
        except:
            pass

    except:
        pass


def get_user_id_all():
    try:
        conn = sqlite3.connect('xspin.db')
        cur = conn.cursor()

        balans = cur.execute(f"""SELECT user_id FROM lang ORDER BY user_id""").fetchall()

        conn.commit()
        conn.close()

        try:
            return balans
        except:
            pass

    except:
        pass


def update_balance(user_id: str, value):
    try:
        conn = sqlite3.connect('xspin.db')
        cur = conn.cursor()

        cur.execute(
            f"""UPDATE users SET balance = {value} WHERE user_id = {str(user_id)}""")

        conn.commit()
        conn.close()

    except:
        pass


def update_lang(user_id: str, value):
    try:
        conn = sqlite3.connect('xspin.db')
        cur = conn.cursor()

        cur.execute(
            f"""UPDATE lang SET lang = ? WHERE user_id = ?""", (value, str(user_id)))

        conn.commit()
        conn.close()

    except:
        pass


async def add_user_bank(user_id: str, balance, bank_level):
    conn = sqlite3.connect('xspin.db')
    cur = conn.cursor()
    user = cur.execute(f"""SELECT * FROM bank WHERE user_id == {str(user_id)}""").fetchone()
    if not user:
        cur.execute(f"""
        INSERT INTO bank (user_id, balance, bank_level) VALUES ({str(user_id)}, {balance}, {str(bank_level)})
        """)

    conn.commit()
    conn.close()


def set_bonus_null():
    conn = sqlite3.connect('xspin.db')
    cur = conn.cursor()

    update_bonus = cur.execute(f"""UPDATE users SET bonus_time = {str(0)}""").fetchone()

    conn.commit()
    conn.close()


def update_bonus_time(user_id: str, value):
    conn = sqlite3.connect('xspin.db')
    cur = conn.cursor()

    update_bonus = cur.execute(
        f"""UPDATE users SET bonus_time = {str(value)} WHERE user_id = {str(user_id)}""").fetchone()

    conn.commit()
    conn.close()


def get_limit(user_id: str):
    conn = sqlite3.connect('xspin.db')
    cur = conn.cursor()

    limit_balans = cur.execute(f"""SELECT limit_balance FROM users WHERE user_id = {str(user_id)}""").fetchone()

    conn.commit()
    conn.close()
    try:
        return limit_balans[0]
    except:
        pass


def get_bonus(user_id: str):
    try:
        conn = sqlite3.connect('xspin.db')
        cur = conn.cursor()

        bonus_time = cur.execute(f"""SELECT bonus_time FROM users WHERE user_id = {str(user_id)}""").fetchone()

        conn.commit()
        conn.close()
        try:
            return bonus_time[0]
        except:
            pass
    except:
        pass


def update_limit(user_id: str, value):
    try:
        conn = sqlite3.connect('xspin.db')
        cur = conn.cursor()

        cur.execute(f"""UPDATE users SET limit_balance = {value} WHERE user_id = {str(user_id)}""")
        conn.commit()
        conn.close()
    except:
        pass


def get_bank(user_id: str):
    try:
        conn = sqlite3.connect('xspin.db')
        cur = conn.cursor()

        bank_balans = cur.execute(f"""SELECT balance FROM bank WHERE user_id == {str(user_id)}""").fetchone()

        conn.commit()
        conn.close()

        try:
            return bank_balans[0]
        except:
            pass

    except:
        pass


def update_bank_balance(user_id, value):
    try:
        conn = sqlite3.connect('xspin.db')
        cur = conn.cursor()

        cur.execute(f"""UPDATE bank SET balance = {value} WHERE user_id == {str(user_id)}""")
        conn.commit()
        conn.close()
    except:
        pass


def update_bank_lvl(user_id, value):
    try:
        conn = sqlite3.connect('xspin.db')
        cur = conn.cursor()

        cur.execute(f"""UPDATE bank SET bank_level = {str(value)} WHERE user_id == {str(user_id)}""")
        conn.commit()
        conn.close()
    except:
        pass


def update_prig(user_id, value):
    try:
        conn = sqlite3.connect('xspin.db')
        cur = conn.cursor()

        cur.execute(f"""UPDATE prig SET balance = {value} WHERE user_id == {str(user_id)}""")
        conn.commit()
        conn.close()
    except:
        pass


def update_limit_null():
    try:
        conn = sqlite3.connect('xspin.db')
        cur = conn.cursor()

        cur.execute(f"""UPDATE users SET limit_balance = '0'""")
        conn.commit()
        conn.close()
    except:
        pass


def get_bank_lvl(user_id: str):
    try:
        conn = sqlite3.connect('xspin.db')
        cur = conn.cursor()

        bank_balans = cur.execute(f"""SELECT bank_level FROM bank WHERE user_id == {str(user_id)}""").fetchone()

        conn.commit()
        conn.close()

        try:
            return bank_balans[0]
        except:
            pass

    except:
        pass


def get_top():
    conn = sqlite3.connect('xspin.db')
    cur = conn.cursor()

    top = cur.execute("""SELECT ismi FROM users ORDER BY balance DESC""").fetchall()

    conn.commit()
    conn.close()

    try:
        return top
    except:
        pass


def get_top_balance():
    conn = sqlite3.connect('xspin.db')
    cur = conn.cursor()

    top = cur.execute("""SELECT balance FROM users ORDER BY balance DESC""").fetchall()

    conn.commit()
    conn.close()

    try:
        return top
    except:
        pass


def get_top_id():
    conn = sqlite3.connect('xspin.db')
    cur = conn.cursor()

    top = cur.execute("""SELECT user_id FROM users ORDER BY balance DESC""").fetchall()

    conn.commit()
    conn.close()

    try:
        return top
    except Exception as ec:
        print(ec)
        pass


def get_used_promo(user_id):
    conn = sqlite3.connect('xspin.db')
    cur = conn.cursor()

    top = cur.execute(f"""SELECT * FROM promo WHERE user_id == {str(user_id)}""").fetchall()

    conn.commit()
    conn.close()

    try:
        return top
    except:
        pass


def get_limit_lvl(user_id):
    conn = sqlite3.connect('xspin.db')
    cur = conn.cursor()

    top = cur.execute(f"""SELECT limit_level FROM limit_lvl WHERE user_id = {str(user_id)}""").fetchone()

    conn.commit()
    conn.close()

    try:
        return top[0]
    except:
        pass


def get_username():
    conn = sqlite3.connect('xspin.db')
    cur = conn.cursor()

    top = cur.execute(f"""SELECT user_name FROM lang ORDER BY user_id""").fetchall()

    conn.commit()
    conn.close()

    try:
        return top
    except:
        pass


def get_username_where_id(user_id):
    conn = sqlite3.connect('xspin.db')
    cur = conn.cursor()

    top = cur.execute(f"""SELECT user_name FROM lang WHERE user_id = {str(user_id)}""").fetchone()

    conn.commit()
    conn.close()

    try:
        return top[0]
    except:
        pass


def update_limit_lvl(user_id, value):
    try:
        conn = sqlite3.connect('xspin.db')
        cur = conn.cursor()

        cur.execute(f"""UPDATE limit_lvl SET limit_level = {value} WHERE user_id == {str(user_id)}""").fetchone()

        conn.commit()
        conn.close()
    except:
        pass


def update_name(user_id, value):
    try:
        conn = sqlite3.connect('xspin.db')
        cur = conn.cursor()

        cur.execute(f"""UPDATE users SET ismi = ? WHERE user_id == ?""", (value, str(user_id)))

        conn.commit()
        conn.close()
    except Exception as exc:
        print(exc)
        pass


async def add_user_limit_lvl(user_id: str, value):
    try:
        conn = sqlite3.connect('xspin.db')
        cur = conn.cursor()
        user = cur.execute(f"""SELECT * FROM limit_lvl WHERE user_id == {str(user_id)}""").fetchone()
        if not user:
            cur.execute(f"""
            INSERT INTO limit_lvl (user_id, limit_level) VALUES ({str(user_id)}, {value})
            """)
        conn.commit()
        conn.close()
    except:
        pass


def add_new_promo(name, value, max):
    try:
        conn = sqlite3.connect('xspin.db')
        cur = conn.cursor()
        cur.execute(f"""INSERT INTO add_promo (promo_name, price, max_user, used_users) VALUES (?, ?, ?, ?)""",
                    (name, int(value), int(max), 0))
        conn.commit()
        conn.close()
    except Exception as exc:
        print(exc)
        pass


def get_promo_name():
    conn = sqlite3.connect('xspin.db')
    cur = conn.cursor()

    top = cur.execute(f"""SELECT promo_name FROM add_promo""").fetchall()

    conn.commit()
    conn.close()

    try:
        return top
    except:
        pass


def get_promo_price():
    conn = sqlite3.connect('xspin.db')
    cur = conn.cursor()

    top = cur.execute(f"""SELECT price FROM add_promo""").fetchall()

    conn.commit()
    conn.close()

    try:
        return top
    except:
        pass


def get_promo_max_user():
    conn = sqlite3.connect('xspin.db')
    cur = conn.cursor()

    top = cur.execute(f"""SELECT max_user FROM add_promo""").fetchall()

    conn.commit()
    conn.close()

    try:
        return top
    except:
        pass


def get_promo_used_user():
    conn = sqlite3.connect('xspin.db')
    cur = conn.cursor()

    top = cur.execute(f"""SELECT used_users FROM add_promo""").fetchall()

    conn.commit()
    conn.close()

    try:
        return top
    except:
        pass


def update_max_user(promo, value):
    try:
        conn = sqlite3.connect('xspin.db')
        cur = conn.cursor()

        cur.execute(f"""UPDATE add_promo SET used_users == ? WHERE promo_name == ?""", (int(value), promo))

        conn.commit()
        conn.close()
    except Exception as exc:
        print(exc)
        pass


def get_clans(group_id: str):
    try:
        conn = sqlite3.connect('xspin.db')
        cur = conn.cursor()

        balans = cur.execute(f"""SELECT group_id FROM clans WHERE group_id = {str(group_id)}""").fetchone()

        conn.commit()
        conn.close()

        try:
            return balans[0]
        except:
            pass

    except:
        pass


def get_clan_name(group_id: str):
    try:
        conn = sqlite3.connect('xspin.db')
        cur = conn.cursor()

        balans = cur.execute(f"""SELECT clan_name FROM clans WHERE group_id = {str(group_id)}""").fetchone()

        conn.commit()
        conn.close()

        try:
            return balans[0]
        except:
            pass

    except:
        pass


def get_clan_user(user_id: str):
    try:
        conn = sqlite3.connect('xspin.db')
        cur = conn.cursor()

        balans = cur.execute(f"""SELECT clan_id FROM clan_users WHERE user_id == {str(user_id)}""").fetchone()

        conn.commit()
        conn.close()

        try:
            return balans[0]
        except:
            pass

    except Exception as exc:
        print(exc)
        pass


def update_clan_user(clan_id, user_id):
    try:
        conn = sqlite3.connect('xspin.db')
        cur = conn.cursor()

        cur.execute(f"""UPDATE clan_users SET clan_id == ? WHERE user_id == ?""", (str(clan_id), str(user_id)))

        conn.commit()
        conn.close()
    except Exception as exc:
        print(exc)
        pass


def update_clan_name(clan_name, group_id):
    try:
        conn = sqlite3.connect('xspin.db')
        cur = conn.cursor()

        cur.execute(f"""UPDATE clans SET clan_name == ? WHERE group_id == ?""", (str(clan_name), str(group_id)))

        conn.commit()
        conn.close()
    except Exception as exc:
        print(exc)
        pass


def update_stat(user_id: str, played: int):
    try:
        conn = sqlite3.connect('xspin.db')
        cur = conn.cursor()

        cur.execute(f"""UPDATE statistics_users SET played == ? WHERE user_id == ?""", (played, str(user_id)))

        conn.commit()
        conn.close()
    except Exception as exc:
        print(exc)
        pass


def get_stat_user(user_id: str):
    try:
        conn = sqlite3.connect('xspin.db')
        cur = conn.cursor()

        balans = cur.execute(f"""SELECT played FROM statistics_users WHERE user_id == {str(user_id)}""").fetchone()

        conn.commit()
        conn.close()

        try:
            return balans[0]
        except:
            pass

    except:
        pass


# conn = sqlite3.connect('xspin.db')
# cur = conn.cursor()

# top = cur.execute(f"""DELETE FROM add_promo WHERE promo_name = 'Solo_infinity_top'""").fetchall()
#
# conn.commit()
# conn.close()


# Clan

def get_clan_top_name():
    conn = sqlite3.connect('xspin.db')
    cur = conn.cursor()

    top = cur.execute("""SELECT clan_name FROM clans ORDER BY all_plays DESC""").fetchall()

    conn.commit()
    conn.close()

    try:
        return top
    except Exception as ec:
        # print(ec)
        pass


def get_clan_top_plays():
    conn = sqlite3.connect('xspin.db')
    cur = conn.cursor()

    top = cur.execute("""SELECT all_plays FROM clans ORDER BY all_plays DESC""").fetchall()

    conn.commit()
    conn.close()

    try:
        return top
    except Exception as ec:
        # print(ec)
        pass


def get_clan_top_id():
    conn = sqlite3.connect('xspin.db')
    cur = conn.cursor()

    top = cur.execute("""SELECT group_id FROM clans ORDER BY all_plays DESC""").fetchall()

    conn.commit()
    conn.close()

    try:
        return top
    except Exception as ec:
        # print(ec)
        pass


def update_clan_plays_count(user_id, group_id, value):
    if not group_id == 'NoneClan.clanNone.clan.clan.None':
        try:
            conn = sqlite3.connect('xspin.db')
            cur = conn.cursor()

            cur.execute(f"""UPDATE clan_users SET played == ? WHERE user_id == ?""", (value, str(user_id)))

            conn.commit()
            conn.close()
        except Exception as exc:
            # print(exc)
            pass
    else:
        pass


def get_plays_clan(user_id):
    conn = sqlite3.connect('xspin.db')
    cur = conn.cursor()

    top = cur.execute(f"""SELECT played FROM clan_users WHERE user_id = {str(user_id)}""").fetchone()

    conn.commit()
    conn.close()

    try:
        return top[0]
    except Exception as ec:
        # print(ec)
        pass


def update_clan_plays(group_id, value):
    try:
        if not group_id == 'NoneClan.clanNone.clan.clan.None':
            conn = sqlite3.connect('xspin.db')
            cur = conn.cursor()

            cur.execute(f"""UPDATE clans SET all_plays == ? WHERE group_id == ?""", (value, str(group_id)))

            conn.commit()
            conn.close()
        else:
            pass
    except Exception as exc:
        # print(exc)
        pass


def get_clan_plays(group_id):
    try:
        conn = sqlite3.connect('xspin.db')
        cur = conn.cursor()

        top = cur.execute(f"""SELECT all_plays FROM clans WHERE group_id = {str(group_id)}""").fetchone()

        conn.commit()
        conn.close()

        try:
            return top[0]
        except Exception as ec:
            print(ec)
            pass
    except Exception as exc:
        # print(exc)
        pass


def get_users_for_ads():
    try:
        conn = sqlite3.connect('xspin.db')
        cur = conn.cursor()

        balans = cur.execute(f"""SELECT user_id FROM users""").fetchall()

        conn.commit()
        conn.close()

        try:
            return balans
        except:
            pass

    except:
        pass
