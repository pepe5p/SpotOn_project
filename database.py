import sqlite3


class Database:
    """object implemented to interact with SQLite DB easier"""

    def __init__(self):
        self.connection = sqlite3.connect("food_db")
        self.table = "meals"    # using only one table, so save as attribute
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.connection.close()

    def insert(self, *values):
        """method that stores input and output of 'find_food' function"""

        query = f"INSERT INTO {self.table} VALUES ({','.join(['?' for _ in values])})"
        self.cursor.execute(query, values)
        self.connection.commit()

    def fetch_output(self, **conditions) -> list:
        """method that gets stored output in JSON"""

        query = (f"SELECT output FROM {self.table} WHERE"
                 f" {' and '.join([f'{condition}=?' for condition in conditions])}")
        self.cursor.execute(query, [str(value) for value in conditions.values()])
        self.connection.commit()
        data = self.cursor.fetchall()

        '''data can be either [] or [(JSON,)]'''
        return data[0][0] if data else data
