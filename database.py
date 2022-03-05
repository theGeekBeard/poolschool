class Database:

    def __init__(self, con):
        self.db = con
        self.sql = self.db.cursor()

    # Setters

    async def change_stock(self, text, status):
        with self.db:
            self.sql.execute(f"UPDATE stock SET stock_text='{text}', status={status}")

    async def add_user(self, user_id):
        with self.db:
            self.sql.execute(f"SELECT * FROM users WHERE user_id={user_id}")
            if not self.sql.fetchone():
                self.sql.execute(f"INSERT INTO users(user_id) VALUES({user_id})")

    # Getters

    async def get_stock(self):
        self.sql.execute(f"SELECT stock_text, status FROM stock")
        stock = self.sql.fetchone()
        return stock

    async def get_statistic(self):
        self.sql.execute("SELECT COUNT(user_id) FROM users")
        return self.sql.fetchone()[0]
