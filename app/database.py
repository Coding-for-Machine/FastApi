import asyncpg
from .config import DB_URL

class Database:
    def __init__(self, db_url: str):
        self.db_url = db_url
        self.conn = None

    async def connect(self):
        """Asinxron bazaga ulanish."""
        if self.conn is None or self.close():
            self.conn = await asyncpg.connect(
                user='asadbek',
                password='asadbek',
                database='tests',
                host='localhost'
            )
            
    async def close(self):
        """Bazaga ulanishni yopish."""
        if self.conn is not None:
            await self.conn.close()
            self.conn = None

    async def execute(self, query: str, *args):
        """So‘rovni bajarish (INSERT, UPDATE, DELETE)."""
        await self.connect()
        async with self.conn.acquire() as conn:
            async with conn.transaction():
                return await conn.execute(query, *args)

    async def fetch(self, query: str, *args):
        """Natija olish (SELECT)."""
        await self.connect()
        async with self.conn.acquire() as conn:
            return await conn.fetch(query, *args)

db = Database(DB_URL)
