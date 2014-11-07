#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# SQLite3 db operations module
# author: Bart Grzybicki <bgrzybicki@gmail.com>

import sqlite3

def create_db(db_name):
    #global db
    try:
        db = sqlite3.connect(db_name)
        c = db.cursor()

        c.execute('''CREATE TABLE DL_RAZEM
                    (ID   TEXT    PRIMARY KEY,
                    DATA    TEXT,
                    LICZBY  TEXT);''')

        c.execute('''CREATE TABLE EL
                    (ID   TEXT    PRIMARY KEY,
                    DATA    TEXT,
                    LICZBY  TEXT);''')

        c.execute('''CREATE TABLE ML
                    (ID   TEXT    PRIMARY KEY,
                    DATA    TEXT,
                    LICZBY  TEXT);''')
    except sqlite3.Error as e:
        print('Błąd SQLite3: ' + e.args[0])
        print('Błąd utworzenia bazy danych!')
    finally:
        if db:
            db.close()

def insert(db_name, table, data_dict):
    #global db
    try:
        db = sqlite3.connect(db_name)
        c = db.cursor()

        if table == 'DL_RAZEM':
            c.execute('''INSERT INTO DL_RAZEM(ID, DATA, LICZBY)
                        VALUES(?, ?, ?)''', (data_dict['id'], data_dict['data'], data_dict['liczby'],))
        elif table == 'EL':
            c.execute('''INSERT INTO EL(ID, DATA, LICZBY)
                        VALUES(?, ?, ?)''', (data_dict['id'], data_dict['data'], data_dict['liczby'],))
        elif table == 'ML':
            c.execute('''INSERT INTO ML(ID, DATA, LICZBY)
                        VALUES(?, ?, ?)''', (data_dict['id'], data_dict['data'], data_dict['liczby'],))
        db.commit()
    except sqlite3.Error as e:
        print('Błąd SQLite3: ' + e.args[0])
        print('Błąd importu losowań do bazy danych!')
    finally:
        if db:
            db.close()

def main():
    db_name = 'test.db'
    tbl = 'ML'
    #liczby = [1, 2, 3, 4, 5, 6]
    liczby = '1,2,3,4,5,6'
    data = {'id': '999', 'data': '2014.11.07', 'liczby': liczby}
    print('dboperations module')
    create_db(db_name)
    insert(db_name, tbl, data)

if __name__ == '__main__':
    main()
