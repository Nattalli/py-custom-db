from dataclasses import dataclass
from typing import Dict
from classes.database import Database


@dataclass
class Manager:
    databases: dict

    def create_database(self, name: str) -> Database:
        self.databases[name] = Database({})
        return self.databases[name]

    def get_all_databases(self):
        return self.databases

    def get_database_by_name(self, name: str) -> Database:
        if [db for db_name, db in self.databases.items() if db_name == name]:
            return self.databases[name]
        else:
            raise KeyError("Database with such name doesn't exist")

    def delete_database(self, name: str) -> None:
        self.databases.pop(name)
