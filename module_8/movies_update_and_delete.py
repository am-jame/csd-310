import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "root",
    "password": "Asdvb678kl####",
    "host": "localhost",
    "database": "movies",
    "raise_on_warnings": True
}


def show_films(cursor, title):
    cursor.execute("SELECT film_name, film_director, genre_name, studio_name FROM film INNER JOIN genre ON "
                   "film.genre_id=genre.genre_id INNER JOIN studio ON film.studio_id=studio.studio_id")
    films = cursor.fetchall()

    print(f"\n  -- {title} --")

    for film in films:
        print(f"Film Name: {film[0]}\nDirector: {film[1]}\nGenre: {film[2]}\nStudio Name: {film[3]}\n")


try:
    db = mysql.connector.connect(**config)

    print("Database user {} connected to MySQL on host {} with database {}".format(
        config['user'], config['host'], config['database']
    ))

    cursor = db.cursor()

    show_films(cursor, "DISPLAYING FILMS AFTER DELETE")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username and password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist")

    else:
        print(err)

finally:
    db.close()
