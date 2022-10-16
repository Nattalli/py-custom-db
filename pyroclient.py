import Pyro5.api

uri = "PYRO:obj_8b9bd391c7bf4097a634d5873c26857f@localhost:58952"

name = input("Enter db name:\n").strip()
db_manager = Pyro5.api.Proxy(uri)
Pyro5.api.Proxy(db_manager.create_database("test_2"))
