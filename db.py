import aiosqlite

DB_NAME = "database.sqlite"

async def init_db():
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("""
        CREATE TABLE IF NOT EXISTS applications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            phone TEXT,
            email TEXT,
            comment TEXT
        )
        """)
        await db.commit()

async def add_application(name, phone, email, comment):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("""
        INSERT INTO applications (name, phone, email, comment)
        VALUES (?, ?, ?, ?)
        """, (name, phone, email, comment))
        await db.commit()

async def get_all_applications():
    async with aiosqlite.connect(DB_NAME) as db:
        cursor = await db.execute("SELECT * FROM applications")
        return await cursor.fetchall()
