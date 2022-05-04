import sqlite3


class Database:
    """
    Class implemented to make interacting with SQLite DB easier (Singleton).
    """

    instance = None

    def __new__(cls) -> None:
        if not cls.instance:
            cls.instance = super(Database, cls).__new__(cls)
        return cls.instance

    def __init__(self) -> None:
        self.connection = sqlite3.connect("food_db")
        self.cursor = self.connection.cursor()
        self.table = "meals"    # using only one table, so save as attribute

        tables = self.check_tables()
        if not tables:
            self.create_table()

    def __del__(self) -> None:
        self.connection.close()

    def check_tables(self) -> list:
        self.cursor.execute(f"SELECT tbl_name FROM sqlite_master WHERE type='table' AND tbl_name='{self.table}'")
        self.connection.commit()
        return self.cursor.fetchall()

    def create_table(self) -> None:
        self.cursor.execute(f"CREATE TABLE {self.table}"
                            f"(id INTEGER constraint {self.table}_pk PRIMARY KEY autoincrement,"
                            f"incl_ingr TEXT, excl_ingr TEXT, output JSON);")
        self.connection.commit()

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
