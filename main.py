from classes.manager import Manager
import PySimpleGUI as sg

if __name__ == "__main__":

    db_manager = Manager({})

    sg.theme('Light Blue')

    layout_start = [[sg.Text("Choose what would you like to do:")],
                    [sg.Button("Create Database")],
                    [sg.Button("Get All Databases")],
                    [sg.Button("Get Database By Name")],
                    [sg.Button("Go Into Database by Name")],
                    [sg.Button("Delete Database")],
                    [sg.Button("Exit the program")]]

    window_start = sg.Window(title="Custom db", layout=layout_start,
                             margins=(200, 100))
    while True:
        event, values = window_start.read()

        if event == "Exit the program" or event == sg.WIN_CLOSED:
            break

        elif event == "Create Database":

            window_input_text = sg.Window(title="Custom db",
                                          layout=[
                                              [sg.Text("Input database name")],
                                              [sg.InputText()],
                                              [sg.Submit(), sg.Cancel()]],
                                          margins=(200, 100))
            event_first, values_first_3 = window_input_text.read()

            text_input = values_first_3[0]
            try:
                db_manager.create_database(text_input)
                sg.popup(f"Database {text_input} created successfully!")
            except:
                sg.popup(f"Database {text_input} is already exists!")

            window_input_text.close()

        elif event == "Get All Databases":
            sg.popup(f"Existed databases: \n{db_manager.get_all_databases()}")

        elif event == "Get Database By Name":
            window_input_text = sg.Window(title="Custom db",
                                          layout=[
                                              [sg.Text("Input database name")],
                                              [sg.InputText()],
                                              [sg.Submit(), sg.Cancel()]],
                                          margins=(200, 100))
            event_first, values_first = window_input_text.read()

            text_input = values_first[0]
            window_input_text.close()

            try:
                db = db_manager.get_database_by_name(text_input)
                sg.popup(f"Database {text_input}: \n {db}")
            except Exception:
                sg.popup(f"Database with name {text_input} doesn't exist")

        elif event == "Delete Database":
            window_input_text = sg.Window(title="Custom db",
                                          layout=[
                                              [sg.Text("Input database name")],
                                              [sg.InputText()],
                                              [sg.Submit(), sg.Cancel()]],
                                          margins=(200, 100))
            event_first, values_first_2 = window_input_text.read()

            text_input = values_first_2[0]

            window_delete_db = sg.Window(title="Custom db",
                                         layout=[[sg.Text("Are you sure?")],
                                                 [sg.Button("Yes")],
                                                 [sg.Button("No")]],
                                         margins=(200, 100))

            event_second, values_second = window_delete_db.read()
            if event_second == "Yes":
                try:
                    db_manager.delete_database(text_input)
                    sg.popup(f"Database {text_input} deleted")
                except Exception as error:
                    sg.popup(f"Error occured: {error}")
            window_delete_db.close()
            window_input_text.close()

        elif event == "Go Into Database by Name":
            window_input_text = sg.Window(title="Custom db",
                                          layout=[
                                              [sg.Text("Input database name")],
                                              [sg.InputText()],
                                              [sg.Submit(), sg.Cancel()]],
                                          margins=(200, 100))
            event_first, values_first = window_input_text.read()

            text_input = values_first[0]
            window_input_text.close()

            try:
                db_manager.get_database_by_name(text_input)

                while True:

                    window_new = sg.Window(title=f"Work with {text_input} db",
                                           layout=[
                                               [sg.Text(
                                                   "Select needed option")],
                                               [sg.Button(
                                                   "Get all existed tables")],
                                               [sg.Button(
                                                   "Get table by name")],
                                               [sg.Button(
                                                   "Add new table")],
                                               [sg.Button(
                                                   "Go into Table by Name")],
                                               [sg.Button(
                                                   "Remove table")],
                                               [sg.Button("Export db")],
                                               [sg.Button("Import db")],
                                               [sg.Button(
                                                   "Back to the main page")]
                                           ],
                                           margins=(200, 100))
                    event_second, values_second = window_new.read()

                    try:

                        if event_second == "Back to the main page" or \
                                event_second == sg.WIN_CLOSED:
                            window_new.close()
                            break
                        elif event_second == "Export db":

                            window_input_text_export = sg.Window(
                                f"Export {text_input} db",
                                layout=[
                                    [sg.Text(
                                        'Input database path')],
                                    [sg.InputText()],
                                    [sg.Submit(),
                                     sg.Cancel()]],
                                margins=(200, 100))
                            event_third, values_third = window_input_text_export.read()

                            text_input_export = values_third[0]
                            window_input_text_export.close()
                            try:
                                db_manager.databases[text_input].export_db(
                                    text_input_export)
                                sg.popup(f"Exported!")
                            except:
                                sg.popup("Export failed")
                        elif event_second == "Import db":

                            window_input_text_import = sg.Window(f"Import db",
                                                                 layout=[
                                                                     [sg.Text(
                                                                         'Input database path')],
                                                                     [
                                                                         sg.InputText()],
                                                                     [
                                                                         sg.Submit(),
                                                                         sg.Cancel()]],
                                                                 margins=(
                                                                 200, 100))
                            event_third, values_third = window_input_text_import.read()

                            text_input_import = values_third[0]
                            window_input_text_import.close()
                            try:
                                db_manager.databases[text_input].import_db(
                                    text_input_import)
                                sg.popup(f"Imported!")
                            except:
                                sg.popup("db does not exist!")
                        elif event_second == "Add new table":

                            window_input_text_add_table = sg.Window(
                                f"Add table",
                                layout=[
                                    [sg.Text(
                                        'Input table name')],
                                    [sg.InputText()],
                                    [sg.Submit(),
                                     sg.Cancel()]],
                                margins=(200, 100))
                            event_third, values_third = window_input_text_add_table.read()

                            text_input_table_name = values_third[0]
                            window_input_text_add_table.close()
                            try:
                                db_manager.databases[text_input] \
                                    .add_new_table(text_input_table_name)
                                sg.popup(f"Table created!")
                            except:
                                sg.popup("This table name is already exists")
                        elif event_second == "Remove table":

                            window_input_text_remove_table = sg.Window(
                                f"Remove table",
                                layout=[
                                    [sg.Text(
                                        'Input table name')],
                                    [sg.InputText()],
                                    [sg.Submit(),
                                     sg.Cancel()]],
                                margins=(200, 100))
                            event_third, values_third = window_input_text_remove_table.read()

                            text_input_table_name = values_third[0]
                            window_input_text_remove_table.close()
                            try:
                                db_manager.databases[text_input].remove_table(
                                    text_input_table_name)
                                sg.popup(f"Table removed!")
                            except:
                                sg.popup("Table with this name doesn't exist")
                        elif event_second == "Get table by name":

                            window_input_text_get_table = sg.Window(
                                f"Get table",
                                layout=[
                                    [sg.Text(
                                        'Input table name')],
                                    [sg.InputText()],
                                    [sg.Submit(),
                                     sg.Cancel()]],
                                margins=(200, 100))
                            event_third, values_third = window_input_text_get_table.read()

                            text_input_table_name = values_third[0]
                            window_input_text_get_table.close()
                            try:
                                table = db_manager.databases[
                                    text_input].get_table(
                                    text_input_table_name)
                                sg.popup(
                                    f"Table {text_input_table_name}:\n{table}")
                            except:
                                sg.popup("Table with this name doesn't exist")
                        elif event_second == "Get all existed tables":
                            try:
                                table = db_manager.databases[
                                    text_input].get_all_tables_as_dict()
                                sg.popup(f"Table info:\n{table}")
                            except:
                                sg.popup("Something went wrong")

                        elif event_second == "Go into Table by Name":

                            window_input_table_name_into = sg.Window(title="Go Into Table",
                                                          layout=[
                                                              [sg.Text(
                                                                  "Input table name")],
                                                              [sg.InputText()],
                                                              [sg.Submit(),
                                                               sg.Cancel()]],
                                                          margins=(200, 100))
                            event_into, values_into = window_input_table_name_into.read()

                            text_input_table_name_into = values_into[0]
                            window_input_table_name_into.close()

                            try:
                                db_manager.databases[text_input].get_table(
                                    text_input_table_name_into)

                                while True:

                                    window_new_col = sg.Window(
                                        title=f"Work with {text_input_table_name_into} table",
                                        layout=[
                                            [sg.Button(
                                                "Add column")],
                                            [sg.Button(
                                                "Get column by name")],
                                            [sg.Button(
                                                "Get all values")],
                                            [sg.Button(
                                                "Add row")],
                                            [sg.Button(
                                                "Get row by index")],
                                            [sg.Button(
                                                "Change row")],
                                            [sg.Button("Delete row")],
                                            [sg.Button("*Change column name")],
                                            [sg.Button("*Swap to columns")],
                                            [sg.Button(
                                                "Back to the main page")]
                                        ],
                                        margins=(200, 100))
                                    event_second, values_second = window_new_col.read()

                                    try:

                                        if event_second == "Back to the main page" or \
                                                event_second == sg.WIN_CLOSED:
                                            window_new.close()
                                            break
                                        elif event_second == "Add column":
                                            window_input_text_add_column = sg.Window(
                                                f"Add column",
                                                layout=[
                                                    [sg.Text(
                                                        'Input column name and type')],
                                                    [sg.InputText()],
                                                    [sg.InputText()],
                                                    [sg.Submit(),
                                                     sg.Cancel()]],
                                                margins=(200, 100))
                                            event_third, values_third = window_input_text_add_column.read()

                                            text_input_column_name, text_input_column_type = values_third[0], values_third[1]
                                            window_input_text_add_column.close()
                                            try:
                                                db_manager.databases[text_input].get_table(text_input_table_name_into).add_column(str(text_input_column_name), int(text_input_column_type))
                                            except:
                                                sg.popup(
                                                    "This column name is already exists")
                                        elif event_second == "Get column by name":
                                            window_input_text_get_column = sg.Window(
                                                f"Get column",
                                                layout=[
                                                    [sg.Text(
                                                        'Input column name:')],
                                                    [sg.InputText()],
                                                    [sg.Submit(),
                                                     sg.Cancel()]],
                                                margins=(200, 100))
                                            event_third, values_third = window_input_text_get_column.read()

                                            text_input_column_name = values_third[0]
                                            window_input_text_get_column.close()
                                            try:
                                                col = db_manager.databases[text_input].get_table(text_input_table_name_into).get_column(text_input_column_name)
                                                sg.popup(
                                                    f"Column:\n{col}")
                                            except:
                                                sg.popup(
                                                    "This column name does not exist")
                                        elif event_second == "Get all values":
                                            try:
                                                val = db_manager.databases[text_input].get_table(text_input_table_name_into).get_all_values_as_dict()
                                                sg.popup(
                                                    f"Values:\n{val}")
                                            except:
                                                sg.popup(
                                                    "Something went wrong")
                                        elif event_second == "Add row":
                                            window_input_text_add_row = sg.Window(
                                                f"Add column",
                                                layout=[
                                                    [sg.Text(
                                                        'Input row values with comma separator')],
                                                    [sg.InputText()],
                                                    [sg.Submit(),
                                                     sg.Cancel()]],
                                                margins=(200, 100))
                                            event_third, values_third = window_input_text_add_row.read()

                                            text_input_row_values = values_third[0]
                                            window_input_text_add_row.close()
                                            try:
                                                db_manager.databases[
                                                    text_input].get_table(
                                                    text_input_table_name_into).add_row(str(text_input_row_values).split(", "))
                                            except:
                                                sg.popup(
                                                    "Not valid!")
                                        elif event_second == "Change row":
                                            window_input_text_change_row = sg.Window(
                                                f"Add column",
                                                layout=[
                                                    [sg.Text(
                                                        'Input row values with comma separator')],
                                                    [sg.InputText()],
                                                    [sg.Submit(),
                                                     sg.Cancel()]],
                                                margins=(200, 100))
                                            event_third, values_third = window_input_text_change_row.read()

                                            text_input_row_values = values_third[0]
                                            window_input_text_change_row.close()
                                            try:
                                                db_manager.databases[
                                                    text_input].get_table(
                                                    text_input_table_name_into).change_row(str(text_input_row_values).split(", "))
                                            except:
                                                sg.popup("Not valid!")
                                        elif event_second == "Get row by index":
                                            window_input_text_get_row = sg.Window(
                                                f"Get row",
                                                layout=[
                                                    [sg.Text(
                                                        'Input row index:')],
                                                    [sg.InputText()],
                                                    [sg.Submit(),
                                                     sg.Cancel()]],
                                                margins=(200, 100))
                                            event_third, values_third = window_input_text_get_row.read()

                                            text_input_row_index = values_third[0]
                                            window_input_text_get_row.close()
                                            try:
                                                row = db_manager.databases[text_input].get_table(text_input_table_name_into).get_row(int(text_input_row_index))
                                                sg.popup(
                                                    f"Row:\n{row}")
                                            except:
                                                sg.popup(
                                                    "This row does not exist")
                                        elif event_second == "Delete row":
                                            window_input_text_delete_row = sg.Window(
                                                f"Delete row",
                                                layout=[
                                                    [sg.Text(
                                                        'Input row index:')],
                                                    [sg.InputText()],
                                                    [sg.Submit(),
                                                     sg.Cancel()]],
                                                margins=(200, 100))
                                            event_third, values_third = window_input_text_delete_row.read()

                                            text_input_row_index = values_third[0]
                                            window_input_text_delete_row.close()
                                            try:
                                                db_manager.databases[text_input].get_table(text_input_table_name_into).delete_row(int(text_input_row_index))
                                            except:
                                                sg.popup(
                                                    "This row does not exist")
                                        elif event_second == "*Change column name":
                                            window_input_text_change_column = sg.Window(
                                                f"*Change column name",
                                                layout=[
                                                    [sg.Text(
                                                        'Input old and new column names')],
                                                    [sg.InputText()],
                                                    [sg.InputText()],
                                                    [sg.Submit(),
                                                     sg.Cancel()]],
                                                margins=(200, 100))
                                            event_third, values_third = window_input_text_change_column.read()

                                            text_input_column_old_name, text_input_column_new_name = values_third[0], values_third[1]
                                            window_input_text_change_column.close()
                                            try:
                                                db_manager.databases[text_input].get_table(text_input_table_name_into).change_name((text_input_column_old_name), (text_input_column_new_name))
                                            except:
                                                sg.popup(
                                                    "This column name is already exists or you enter not valid old name")
                                        elif event_second == "*Swap to columns":
                                            window_input_text_change_column = sg.Window(
                                                f"*Swap to columns",
                                                layout=[
                                                    [sg.Text(
                                                        'Input column names you would like to swap')],
                                                    [sg.InputText()],
                                                    [sg.InputText()],
                                                    [sg.Submit(),
                                                     sg.Cancel()]],
                                                margins=(200, 100))
                                            event_third, values_third = window_input_text_change_column.read()

                                            text_input_column_first_name, text_input_column_second_name = values_third[0], values_third[1]
                                            window_input_text_change_column.close()
                                            try:
                                                db_manager.databases[text_input].get_table(text_input_table_name_into).replace_columns((text_input_column_first_name), (text_input_column_second_name))
                                            except:
                                                sg.popup(
                                                    "This column name is already exists or you enter not valid old name")
                                    except:
                                        sg.popup(
                                            "Something went wrong")
                                    window_new_col.close()
                                window_new_col.close()
                            except:
                                sg.popup(
                                    f"Table with name {text_input} doesn't exist")
                    except:
                        sg.popup(
                            f"Table with name {text_input} doesn't exist")

                    window_new.close()
            except:
                sg.popup(f"Database with name {text_input} doesn't exist")

    window_start.close()
