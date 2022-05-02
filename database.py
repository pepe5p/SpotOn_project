import sqlite3


class Database:
    """
    Class implemented to make interacting with SQLite DB easier.
    """

    # TODO: db and creating table
    # create table meals
    # (
    #     id integer constraint meals_pk primary key autoincrement,
    #     incl_ingr text,
    #     excl_ingr text,
    #     output    json
    # );

    def __init__(self) -> None:
        self.connection = sqlite3.connect("food_db")
        self.table = "meals"    # using only one table, so save as attribute
        self.cursor = self.connection.cursor()

    def __del__(self) -> None:
        self.connection.close()

    def insert(self, *values: any) -> None:
        query = f"INSERT INTO {self.table} VALUES ({','.join(['?' for _ in values])})"
        self.cursor.execute(query, values)
        self.connection.commit()

    def fetch_output(self, **conditions: list) -> list:
        """
        Method that gets stored output in JSON.
        :return: list of results
        """

        query = (f"SELECT output FROM {self.table} WHERE"
                 f" {' and '.join([f'{condition}=?' for condition in conditions])}")
        self.cursor.execute(query, [str(value) for value in conditions.values()])
        self.connection.commit()
        data = self.cursor.fetchall()

        return data[0][0] if data else data
