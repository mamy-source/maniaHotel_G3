create database if not exists maniahotel;
use maniahotel;

drop table if exists 'Customers';
create table if not exists 'Customers'(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
    email VARCHAR(255) UNIQUE NOT NULL
    adress VARCHAR(255) NOT NULL
    phone VARCHAR(15),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP    
);

drop table if exists 'Rooms';
create table if not exists 'Rooms'(
    id INT AUTO_INCREMENT PRIMARY KEY,
    room_types VARCHAR(200) NOT NULL,
    room_number int(50) DEFAULT NULL UNIQUE
    price int(100) NOT NULL,
    is_active boolean DEFAULT False
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP    


);

drop table if exists 'Reservations';
create table if not exists 'Reservations'(
    id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT(10),
    FOREIGN KEY(customer_id) REFERENCES Customers(id) ON DELETE CASCADE,

    reservation_date datetime DEFAULT NULL,
    check_in datetime DEFAULT NULL,
    check_out datetime DEFAULT NULL,
    room_id int(10),
    FOREIGN KEY(room_id) REFERENCES Rooms(id) ON DELETE CASCADE,
    paiments boolean DEFAULT False,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP    


);

drop table if exists 'login';
create table if not exists 'login'(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(200) NOT NULL UNIQUE,
    password VARCHAR(100) NOT NULL,
    confirm_mdp VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP 
);


