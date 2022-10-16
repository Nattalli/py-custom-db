import pickle
from dataclasses import dataclass
from classes.table import Table


@dataclass
class Database:
    tables: dict

    def get_table(self, name: str) -> Table:
        return self.tables[name]

    def get_all_tables_as_str(self) -> str:
        return str(self.tables)

    def get_all_tables_as_dict(self) -> dict:
        return {f"Table name {name}": f"Table content {str(table)}\n" for name,
                table in self.tables.items()}

    def add_new_table(self, name: str) -> None:
        if self.tables.get(name, None) is None:
            self.tables[name] = Table(name, [], [])
        else:
            assert KeyError("Table with such name exists")

    def remove_table(self, name: str) -> None:
        if name in self.tables.keys():
            self.tables.pop(name)

    def export_db(self, path: str) -> None:
        with open(f"{path}.pickle", "wb") as file:
            pickle.dump(self, file)

    def import_db(self, path: str):
        with open(f"{path}.pickle", "rb") as file:
            self = pickle.load(file)
            return self
