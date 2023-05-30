import sqlite3 as sq
from settings.answerText import compliteAnswer, errorAnswer
import datetime

def start_sqlite_db():
    global conn, cur
    conn = sq.connect('mainDb.db')
    cur = conn.cursor()
    conn.execute("""CREATE TABLE IF NOT EXISTS users(
        user_db_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        user_tg_id INTEGER NOT NULL,
        reputation INTEGER DEFAULT 0,
        total_sex_times INTEGER DEFAULT 0,
        mounth_sex_times INTEGER DEFAULT 0,
        day_sex_times INTEGER DEFAULT 0,
        max_of_day_sex INTEGER DEFAULT 0,
        max_of_mounth_sex INTEGER DEFAULT 0,
        max_of_oldmounth_sex INTEGER DEFAULT 0
    )""")
    conn.commit()

async def checkUsersInDb(id):
    var = cur.execute(f"SELECT user_tg_id FROM users WHERE user_tg_id = {id}").fetchone()
    if not var:
        return False
    else:
        return True
    
async def addNewUsersInDb(id, name):
    var = cur.execute(f"SELECT user_tg_id FROM users WHERE user_tg_id = {id}").fetchone()
    if not var:
        cur.execute("SELECT user_tg_id FROM users")
        cur.execute("INSERT INTO users(user_tg_id, name) VALUES(?, ?)", (id, name))
        conn.commit()
        return "Регистрация прошла успешно!"
    else:
        return "Ты уже зарегистирован!"

async def addOneTimeSexDb(id):
    try:
        var_total = cur.execute(f"SELECT total_sex_times FROM users WHERE user_tg_id = {id}").fetchone()
        day_of_mouth = datetime.datetime.today()
        day_naw = str(day_of_mouth).split("-")[2]
        day_naw = day_naw.split()[0]
        h_now = datetime.datetime.now()
        now = h_now.strftime("%H%M")

        if int(now) <= 2400 and int(now) >= 2350:
            del now
            cur.execute(f"UPDATE users SET day_sex_times = 0 WHERE user_tg_id = {id}")
        else:
            var_day = cur.execute(f"SELECT day_sex_times FROM users WHERE user_tg_id = {id}").fetchone()
            if var_day == None:
                var_day = (0,)
            cur.execute(f"UPDATE users SET day_sex_times = {var_day[0] + 1} WHERE user_tg_id = {id}")

        if day_naw <= "1":
            cur.execute(f"UPDATE users SET mounth_sex_times = 0 WHERE user_tg_id = {id}")
            conn.commit()
        else:
            del day_naw
            var_mounth = cur.execute(F"SELECT mounth_sex_times FROM users WHERE user_tg_id = {id}").fetchone()
            if var_mounth == None:
                var_mounth = (0,)
            cur.execute(f"UPDATE users SET mounth_sex_times = {var_mounth[0] + 1} WHERE user_tg_id = {id}")
            conn.commit()

        if var_total == None:
            var_total = (0,)
        else:
            cur.execute(f"UPDATE users SET total_sex_times = {var_total[0] + 1} WHERE user_tg_id = {id}")
            conn.commit()
            return "Обновление статистики прошло успешно"
    except Exception as _e:
        print(_e)
        return "Ошибка обноления статитсики"

async def showTotalTimesSexDb(id):
    try:
        return cur.execute(f"SELECT total_sex_times FROM users WHERE user_tg_id = {id}").fetchone()
    except Exception as _e:
        print(_e)
        return "Ошибка"

async def showMounthTimesSexDb(id):
    try:
        return cur.execute(f"SELECT mounth_sex_times FROM users WHERE user_tg_id = {id}").fetchone()
    except Exception as _e:
        print(_e)
        return "Ошибка"

async def showDayTimesSexDb(id):
    try:
        return cur.execute(f"SELECT day_sex_times FROM users WHERE user_tg_id = {id}").fetchone()
    except Exception as _e:
        print(_e)
        return "Ошибка"
    
async def showMaxStatisticOfMounthDb(id):
    var = cur.execute(f"SELECT mounth_sex_times FROM users WHERE user_tg_id = {id}").fetchone()
    if var == None:
        var = (0,)
    var_max = cur.execute(f"SELECT max_of_mounth_sex FROM users WHERE user_tg_id = {id}").fetchone()
    if var_max == None:
        var_max = (0,)
    if var[0] >= var_max[0]:
        cur.execute(f"UPDATE users SET max_of_mounth_sex = {var[0]} WHERE user_tg_id = {id}")
        conn.commit()
        del var, var_max
    return cur.execute(f"SELECT max_of_mounth_sex FROM users WHERE user_tg_id = {id}").fetchone()

async def showMaxStatisticOfDayDb(id):
    var = cur.execute(f"SELECT day_sex_times FROM users WHERE user_tg_id = {id}").fetchone()
    if var == None:
        var = (0,)
    var_max = cur.execute(f"SELECT max_of_day_sex FROM users WHERE user_tg_id = {id}").fetchone()
    if var_max == None:
        var_max = (0,)
    if var[0] > var_max[0]:
        cur.execute(f"UPDATE users SET max_of_day_sex = {var[0]} WHERE user_tg_id = {id}")
        conn.commit()
        del var, var_max
    return cur.execute(f"SELECT max_of_day_sex FROM users WHERE user_tg_id = {id}").fetchone()
