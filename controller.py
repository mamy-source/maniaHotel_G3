import mysql.connector
import matplotlib.pyplot as pt



# SQL connection
connection = mysql.connector.connect(
    host = 'localhost',
    user = 'miekely',
    password = 'Admin123#',
    database = 'maniahotel'
)

cursor = connection.cursor(buffered=True)

# Get the user from database
def checkUser(username,password):
    query = f"SELECT count(name) FROM login WHERE name = '{username}' and BINARY password = '{password}';"
    cursor.execute(query)
    query = None
    a = cursor.fetchone()[0] >= 1
    return a

#update username ande password
def updateUsername(username,password,new_username):
    query = f"UPDATE login SET name='{new_username}'WHERE name='{username}' and password='{password}' limit 1;"
    cursor.execute(query)
    query1 = f"SELECT count(name) FROM login WHERE name='{new_username}' and password='{password}'"
    cursor.execute(query1)
    return cursor.fetchone()[0] >= 1

def updatePassword(password,username,new_password):
    query = f"UPDATE login SET password='{new_password}' WHERE name='{username}' and password = '{password}' limit 1;"
    cursor.execute(query)
    query1 = f"SELECT count(name) FROM login WHERE name='{username}' and password='{new_password}'"
    cursor.execute(query1)
    return cursor.fetchone()[0] >= 1

# Add customers
def add_customer(name, email, address, phone):
    query = f"INSERT INTO Customers(name,email,address,phone) values ('{name}', '{email}','{address}','{phone}');"
    cursor.execute(query)
    if cursor.rowcount == 0:
        return False
    return True

# Get all customers
def get_customer():
    query = "SELECT * FROM Customers"
    cursor.execute(query)
    if cursor.rowcount == 0:
        return False
    return cursor.fetchall()

# Add rooms
def add_room(room_type,room_number, price):
    query = f"INSERT INTO rooms(room_type,room_number,price)VALUES('{room_type}','{room_number}','{price}');"
    cursor.execute(query)
    if cursor.rowcount == 0:
        return False
    return True

# Get all rooms
def get_room():
    query = "SELECT * FROM rooms"
    cursor.execute(query)
    if cursor.rowcount == 0:
        return []
    columns = [column[0] for column in cursor.description]  # Récupère les noms des colonnes
    rows = cursor.fetchall()
    # Convertir chaque ligne en dictionnaire
    return [dict(zip(columns, row)) for row in rows]

# Add reservations
def add_reservation(customer_id, reservation_date,check_in,check_out,room_id):
    query = f"INSERT INTO reservations(customer_id,reservation_date,check_in,check_out,room_id) VALUES('{customer_id}','{reservation_date}','{check_in}','{check_out}','{room_id}');"
    cursor.execute(query)
    if cursor.rowcount == 0:
        return False
    return True

# Get all reservations
def get_reservation():
    query = "SELECT * FROM reservations"
    cursor.execute(query)
    if cursor.rowcount == 0:
        return False
    return cursor.fetchall()

# delete customers
def delete_customer(id):
    query = f"DELETE FROM Customers WHERE id = '{id}';"
    cursor.execute(query)
    if cursor.rowcount == 0:
        return False
    return True

# delete rooms
def delete_room(id):
    query = f"DELETE FROM rooms WHERE id = '{id}';"
    cursor.execute(query)
    if cursor.rowcount == 0:
        return False
    return True

# delete reservations
def delete_reservation(id):
    query = f"DELETE FROM reservations WHERE id='{id}';"
    cursor.execute(query)
    if cursor.rowcount == 0:
        return False
    return True

# update customers
def update_customer(new_name,new_email,new_phone, new_address, id):
    query = f"UPDATE Customers set name = '{new_name}',email='{new_email}',address= '{new_address}',phone='{new_phone}' WHERE id='{id}';"
    cursor.execute(query)
    if cursor.rowcount == 0:
        return False
    return True
# update rooms
def update_room(id,new_room_number,new_room_type,new_price):
    query = f"UPDATE rooms SET room_number='{new_room_number}',room_type='{new_room_type}',price='{new_price}' WHER id='{id}';"
    cursor.execute(query)
    if cursor.rowcount == 0:
        return False
    return True

#update reservations
def update_reservation(new_customer,new_check_in,new_check_out,new_reservation_date,id):
    query = f"UPDATE reservations SET customer_id ='{new_customer}',reservation_date='{new_reservation_date}',chek_in='{new_check_in}',check_out='{new_check_out}' WHERE id='{id}';"
    cursor.execute(query)
    if cursor.rowcount == 0:
        return False
    return True