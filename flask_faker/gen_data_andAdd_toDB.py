#!/usr/bin/python3.8
from gettext import install
from faker import Faker
from tinydb import TinyDB, Query
from flask import Flask, jsonify, request


class Write_to_db():
    def __init__(self) -> None:
        pass

    def query_db_size(self):
        return (len(db.all()))

    def generate_data(self):
        fake = Faker()
        names = [(fake.unique.name(), fake.address(), fake.city(),
                  fake.credit_card_number(), fake.phone_number(), fake.job()) for i in range(1000)]
        #assert len(set(names)) == len(names)
        for var in enumerate(names):
            db.insert({"id": var[0], "name": var[1][0],
                      "address": var[1][1], "city": var[1][2]})


def main():
    global db
    db = TinyDB('db.json')
    inst = Write_to_db()
    x = inst.query_db_size()
    if int(x) > 500:
        print("DB loaded")
    else:
        print("Loading to DB")
        with open("db.json", "w") as fhand:
            pass
        inst.generate_data()

    ## FLASK Section###
    # flask_inst = flask_call()
    # global app
    # app = Flask(__name__)
    # app.run(debug=True)


if __name__ == "__main__":
    main()

