import sqlite3  # TODO: write to requirements


class Database:
    def __init__(self):
        self.connection = sqlite3.connect("food_db")
        self.table = "meals"
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.connection.close()

    def insert(self, *values):
        query = f"INSERT INTO {self.table} VALUES ({','.join(['?' for _ in values])})"
        self.cursor.execute(query, values)
        self.connection.commit()

    def fetch_output(self, **conditions):
        query = (f"SELECT output FROM {self.table} WHERE"
                 f" {' and '.join([f'{condition}=?' for condition in conditions])}")
        self.cursor.execute(query, [str(value) for value in conditions.values()])
        self.connection.commit()
        data = self.cursor.fetchall()
        return data
