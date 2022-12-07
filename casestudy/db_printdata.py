# Group 3
# Bryce Kellas, Andrew McCloud, Charlene Centeno, James Beck
# Module 9 - Milestone 2
#
# Script to initialize the Outland Adventures database and populate tables with 6 records.

import mysql.connector
from mysql.connector import errorcode


config = {
    "user": "root",
    "password": "Asdvb678kl####",
    "host": "127.0.0.1",
    "database": "outland",
    "raise_on_warnings": False
}


try:
    db = mysql.connector.connect(**config)

    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"],config["host"],config["database"]))

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

cursor = db.cursor()

# Display tables
# Inventory
cursor.execute("""SELECT * FROM inventory""")
inventory = cursor.fetchall()

print(" -- INVENTORY --")
for item in inventory:
    print(f"{item[0]}\tQuantity: {item[1]}\tLocation: {item[2]}")

# Products
cursor.execute("""SELECT * FROM products""")
products = cursor.fetchall()
print("\n -- PRODUCTS --")
for item in products:
    print(f'{item[0]}\tName: {item[1]}\tCost: ${item[2]}\tManufacturer: {item[3]}\tRental Cost: ${item[5]}')

# Locations
cursor.execute("""SELECT * FROM locations""")
locations = cursor.fetchall()
print("\n -- LOCATIONS --")
for item in locations:
    print(f"{item[0]}\t{item[1]}")

# Employees
cursor.execute("""SELECT * FROM employees""")
employees = cursor.fetchall()
print("\n -- EMPLOYEES --")
for item in employees:
    print(f"{item[0]}\tName: {item[1]}\tDepartment: {item[2]}")

# Trips
cursor.execute("""SELECT * FROM trips""")
trips = cursor.fetchall()
print("\n -- TRIPS --")
for item in trips:
    print(f"{item[0]}\tEmployee ID: {item[1]}\tLocation ID: {item[2]}\tAirport: {item[3]}\tAirfare: ${item[4]}"
          f"\tDepert Date: {item[5]}\tReturn Date: {item[6]}\tInnoculations: {item[7]}")

# Customers
cursor.execute("""SELECT * FROM customers""")
customers = cursor.fetchall()
print("\n -- CUSTOMERS --")
for item in customers:
    print(f"{item[0]}\tName: {item[1]}\tAddress: {item[2]} {item[3]}, {item[4]} {item[5]}\tEmail: {item[6]}\t"
          f"Phone Number: {item[7]}\tTrip ID: {item[8]}")

# Orders
cursor.execute("""SELECT * FROM orders""")
orders = cursor.fetchall()
print("\n -- ORDERS --")
for item in orders:
    print(f"{item[0]}\tCustomer ID: {item[0]}\tCustomer ID: {item[1]}\tOrder Date: {item[2]}\tTotal: ${item[3]}"
          f"\tProduct ID: {item[4]}\tRental Start Date: {item[6]}\tRental End Date: {item[7]}\tTotal: ${item[8]}")

db.close()
