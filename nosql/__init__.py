# -*- coding: UTF8 -*-

from .config import Config
from .database import Database
from .utils import encode_json, decode_json, hash_iterable


class NoSQL:

    main_table = 'main'

    def __init__(self):
        self.db = DB(db_path="db/nosql.db")

    def _get_id(self, string: str) -> str:
        """
        Takes a string (JSON) and returns the ID.
        """
        if not isinstance(string, str):
            raise ValueError
        h = hash_iterable(string)  # Is hexadecimal.
        h_decimal = int(h, 16)
        return str(h_decimal)[:Config.id_len]

    def put(self, new_value: dict, table: str = main_table) -> str:
        if not isinstance(new_value, dict):
            raise ValueError
        value = encode_json(new_value)
        key = self._get_id(value)
        self.db.database_put(table, key, value)
        return key

    def get(self, key: str or int, table: str = main_table) -> dict or None:
        return decode_json(self.db.database_get(table, key))

    def get_all(self, table: str = main_table) -> dict or None:
        all_v = self.db.database_get_all(table)
        for k, v in all_v.items():
            all_v.update({k: decode_json(v)})
        return all_v

    def get_all_keys(self, table: str = main_table) -> set or None:
        return self.db.database_get_all_keys(table)


class DB(Database):
    def __init__(self, db_path):
        super().__init__(db_path, {})

    def database_get_all(self, table: str) -> dict or None:
        if self.column_exists(table):
            return self.query_column(table)

    def database_get_all_keys(self, table) -> set or None:
        if self.column_exists(table):
            return set(self.query_column(table).keys())

    def database_put(self, table: str, key: str, value: str) -> None:
        if self.column_exists(table):
            if not self.key_exists(table, key):
                self.insert_dict(table, {key: value})
        else:
            self.insert_new_column(table, dict)
            # Call the function recursively.
            # Could cause problems if the insert_new_column doesn't work.
            self.database_put(table, key, value)

    def database_get(self, table: str, key: str) -> str or None:
        if self.column_exists(table):
            if self.key_exists(table, key):
                return self.query(table, key)

