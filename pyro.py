import os
import Pyro5.api
from dataclasses import dataclass
from classes.manager import Manager
from classes.database import Database

os.environ["PYRO_SERIALIZER"] = "pickle"


@Pyro5.api.expose
@dataclass
class RemoteManager(Manager):
    databases: dict

    def create_database(self, name: str) -> Database:
        print("started creating")
        db = Database({})
        self.databases[name] = db
        print(f"created db with name: {name}")
        return daemon.register(db)

    def get_all_databases(self):
        print("returned all databases")
        return self.databases

    def get_database_by_name(self, name: str) -> Database:
        if [db for db_name, db in self.databases.items() if db_name == name]:
            print(f"get db with name {name}")
            return self.databases[name]
        else:
            print(f"db with name {name} doesn't exist")
            raise KeyError("Database with such name doesn't exist")

    def delete_database(self, name: str) -> None:
        print(f"deleted db {name}")
        self.databases.pop(name)


daemon = Pyro5.api.Daemon()
db_manager = RemoteManager({})
uri = daemon.register(db_manager)
db_manager.create_database("test")

print(uri)
daemon.requestLoop()
