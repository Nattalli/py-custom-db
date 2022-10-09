from dataclasses import dataclass
from classes.rows import Row
from classes.columns import (Column, COLUMN_TYPES)


@dataclass
class Table:
    name: str
    columns: list
    rows: list

    def get_all_values_as_dict(self) -> list:
        return [
            {
                self.columns[index].name: row.values[index]
                for index in range(len(self.columns))
            }
            for row in self.rows
        ]

    def add_column(self, name: str, type: int) -> None:
        if name in [column.name for column in self.columns]:
            raise KeyError(f"Column with {name} name is already exists")
        try:
            self.columns.append(Column(name, type))
        except Exception as error:
            raise ValueError(error)

    def get_column(self, name: str) -> str:
        columns = [column for column in self.columns if column.name == name]
        if columns:
            column = columns[0]
            return f"Column name: {column.name}\nColumn type: " \
                   f"{[column_[2] for column_ in COLUMN_TYPES if column_[0] == column.type][0]}"
        else:
            raise KeyError("Not existed column")

    def validate_row(self, row_values) -> bool | None:
        if len(row_values) != len(self.columns):
            return False

        for index in range(len(row_values)):
            column_type = self.columns[index].type
            column = [column_[2] for column_ in COLUMN_TYPES if column_[0] ==
                      column_type][0]
            try:
                column(row_values[index])
            except Exception:
                return False

        return True

    def add_row(self, row_values) -> None:
        if self.validate_row(row_values):
            self.rows.append(Row(row_values))

    def get_row(self, index: int) -> list:
        return self.rows[index].values

    def change_row(self, index: int, new_values: list) -> None:
        if self.validate_row(new_values):
            self.rows[index] = Row(new_values)

    def delete_row(self, index: int) -> None:
        self.rows.pop(index)

    def change_name(self, old_name: str, name: str) -> None:
        if name == old_name:
            raise KeyError("You should change table name!")
        if name in [column.name for column in self.columns]:
            raise KeyError("Column with such name already exists!")
        else:
            columns = [column for column in self.columns if column.name == old_name][0]
            columns.name = name

    def replace_columns(self, name_first: str, name_second: str) -> None:
        column_names = [column.name for column in self.columns]
        if name_first in column_names and name_second in column_names:
            counter_first = 0
            counter_second = 0
            for column in self.columns:
                if column.name != name_first:
                    counter_first += 1
                else:
                    break

            for column in self.columns:
                if column.name != name_second:
                    counter_second += 1
                else:
                    break

            self.columns[counter_first], self.columns[counter_second] = \
                self.columns[counter_second], self.columns[counter_first]

            for row in self.rows:
                row.values[counter_first], row.values[counter_second] = \
                    row.values[counter_second], row.values[counter_first]
        else:
            assert KeyError("Enter existed column names!")
