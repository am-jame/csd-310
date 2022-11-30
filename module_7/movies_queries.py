#  James Beck
#  27 November 2022
#  CSD 310 Module 7
#  Displays studios, genres, films, and directors from database

import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "root",
    "password": "Asdvb678kl####",
    "host": "localhost",
    "database": "movies",
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)

    print("Database user {} connected to MySQL on host {} with database {}".format(
        config['user'], config['host'], config['database']
    ))

    cursor = db.cursor()

    print("\n--DISPLAYING Studio RECORDS --")
    cursor.execute("SELECT * FROM studio")
    studios = cursor.fetchall()
    for s in studios:
        print(f"Studio ID: {s[0]}\nStudio Name: {s[1]}\n")

    print("\n--DISPLAYING Genre RECORDS --")
    cursor.execute("SELECT * FROM genre")
    genres = cursor.fetchall()
    for g in genres:
        print(f"Genre ID: {g[0]}\nGenre Name: {g[1]}\n")

    print("\n--DISPLAYING Short Films RECORDS --")
    cursor.execute("SELECT * FROM film WHERE film_runtime < 120")
    short_films = cursor.fetchall()
    for f in short_films:
        print(f"Film Name: {f[1]}\nRuntime: {f[3]}\n")

    print("\n--DISPLAYING Director RECORDS in order--")
    cursor.execute("SELECT * FROM film ORDER BY film_director")
    films = cursor.fetchall()
    for f in films:
        print(f"Film Name: {f[1]}\nDirector: {f[4]}\n")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username and password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist")

    else:
        print(err)

finally:
    db.close()
