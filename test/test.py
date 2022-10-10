import pytest
from classes.manager import Manager


def test_manager_create_db():
    db_manager = Manager({})
    db_manager.create_database("test_db")
    db_manager.create_database("test2_db")
    assert len(db_manager.get_all_databases()) == 2, "Had to be created 2 db"


def test_create_manager_without_db():
    db_manager = Manager({})
    assert len(db_manager.get_all_databases()) == 0, ("Manager shouldn't "
                                                      "contain dbs")


def test_manager_get_database_by_name():
    db_manager = Manager({})
    db = db_manager.create_database("test_db")
    assert db_manager.get_database_by_name("test_db") == db, (f"Calling "
                                                              f"database_by_name() method had to return {db} db, but actual it "
                                                              f"{db_manager.get_database_by_name('test_db')}")


def test_manager_delete_db():
    db_manager = Manager({})
    db_manager.create_database("test_db")
    db_manager.delete_database("test_db")
    assert len(db_manager.get_all_databases()) == 0, ("Manager shouldn't "
                                                      "contain dbs")


@pytest.mark.parametrize(
    "field_name,field_type",
    (
            ("number", 0),
            ("real", 1),
            ("char", 2),
            ("str", 3),
            ("html", 4),
            ("str_invl", 5),
    )
)
def test_table_add_column(field_name, field_type):
    db_manager = Manager({})
    db_manager.create_database("test_db")
    db_manager.databases["test_db"].add_new_table("first")
    db_manager.databases["test_db"].get_table("first").add_column(field_name,
                                                                  field_type)
    assert (db_manager.databases["test_db"].get_table("first").
            get_column(field_name) is not None), (f"Should be created column "
                                                  f"with type {field_type} and name {field_name}")


@pytest.mark.parametrize(
    "columns,quantity",
    (
            ([("number", 0), ("real", 1)], 2),
            ([("number", 0), ("real", 1), ("char", 2), ("str", 3)], 4),
            ([
                 ("number", 0),
                 ("real", 1),
                 ("char", 2),
                 ("str", 3),
                 ("html", 4),
                 ("str_invl", 5)
             ], 6),
    )
)
def test_table_add_columns(columns, quantity):
    db_manager = Manager({})
    db_manager.create_database("test_db")
    db_manager.databases["test_db"].add_new_table("first")
    for column in columns:
        db_manager.databases["test_db"].get_table("first").add_column(
            column[0],
            column[1])
    assert db_manager.databases["test_db"].get_table("first"). \
               get_columns_quantity() == quantity, \
               f"Should be created {quantity} columns"


@pytest.mark.parametrize(
    "row_values,is_created",
    (
            ([1, 2.7, "c", "sss", "<span>Hey!</span>", ["a", "b"]], True),
            ([10, 18.0, "a", "Hello", "<span>M?</span>", ["b", "c"]], True),
            ([1, 2.7, "c", "<span>Hey!</span>", ["a", "b"]], False),
            ([1, 2.7, "c", "sss", "<span>Hey!</span>", ["a", "b"]], True),
            ([1, 2, "c", "s", "<span>Hey!</span>", ["a", "b"]], True),
    )
)
def test_table_add_row(row_values, is_created):
    columns = [
        ("number", 0),
        ("real", 1),
        ("char", 2),
        ("str", 3),
        ("html", 4),
        ("str_invl", 5)
    ]
    db_manager = Manager({})
    db_manager.create_database("test_db")
    db_manager.databases["test_db"].add_new_table("first")
    for column in columns:
        db_manager.databases["test_db"].get_table("first").add_column(
            column[0], column[1])
    db_manager.databases["test_db"].get_table("first").add_row(row_values)
    assert len(db_manager.databases["test_db"].get_table("first").
               get_all_values_as_dict()) == is_created, "Not value rows number"


def test_change_table_name():
    columns = [
        ("number", 0),
        ("real", 1),
        ("char", 2),
        ("str", 3),
        ("html", 4),
        ("str_invl", 5)
    ]
    db_manager = Manager({})
    db_manager.create_database("test_db")
    db_manager.databases["test_db"].add_new_table("first")
    for column in columns:
        db_manager.databases["test_db"].get_table("first").add_column(
            column[0], column[1])
    db_manager.databases["test_db"].get_table("first").change_name("real", "new")
    assert db_manager.databases["test_db"].get_table("first").\
               get_all_column_names() == ["number", "new", "char", "str",
                                          "html", "str_invl"], \
        "The Real column name should be changed for 'new' name"


def test_change_swap_tables():
    columns = [
        ("number", 0),
        ("real", 1),
        ("char", 2),
        ("str", 3),
        ("html", 4),
        ("str_invl", 5)
    ]
    db_manager = Manager({})
    db_manager.create_database("test_db")
    db_manager.databases["test_db"].add_new_table("first")
    for column in columns:
        db_manager.databases["test_db"].get_table("first").add_column(
            column[0], column[1])
    db_manager.databases["test_db"].get_table("first").replace_columns(
        "number", "char")
    assert db_manager.databases["test_db"].get_table("first"). \
               get_all_column_names() == ["char", "real", "number", "str",
                                          "html", "str_invl"], \
        "The 'number' column name should be swapped with 'char' column"
