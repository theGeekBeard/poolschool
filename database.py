class Database:

    def __init__(self, con):
        self.db = con
        self.sql = self.db.cursor()

    # Setters

    async def change_stock(self, text, status):
        with self.db:
            self.sql.execute(f"UPDATE stock SET stock_text='{text}', status={status}")

    # Getters

    async def get_stock(self):
        self.sql.execute(f"SELECT stock_text, status FROM stock")
        stock = self.sql.fetchone()
        return stock
