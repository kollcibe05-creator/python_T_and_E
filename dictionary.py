#!/usr/bin/env python3

student_details = {
    "first_name" : "Titus",
    "last_name": "Juma",
    "address":{ "city" : "Nairobi",
    "zip-code" : "21000",
    },
    "friends" : ["one", "two", "three"]

}
# print(student_details["address"]["city"])
# print(student_details["friends"])
# print(student_details)
# print(student_details.get("address", "Nop"))

# print(int.__base__)


list_ = ["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"]
index_ = list_.index("needle")
print(index_)

if "needle" in list_:
    print(f"Found needle at position {index_}")



SQlite Viewer,SQLLIte Viewer

bash :
sqlite3 <file.db>
CREATE TABLE users( id primary key, name TEXT, email TEXT, password Text) !!!!#autoincrement#


CREATE TABLE customers( id primary key,user_id INTEGER CONSTRAINT FK_user_id FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE);

CREATE TABLE roles (id primary key, name TEXT)

ALTER TABLE users ADD COLUMN role_id INTEGER,# FOREIGN KEY;

INSERT INTO roles (name) VALUES ("Admin");
INSERT INTO roles (name) VALUES ("Customer");
INSERT INTO roles (name) VALUES ("Organization");


UPDATE roles SET id = Null WHERE id = NULL #and 

INSERT INTO users (name, email) VALUES("John", john@gmail.com)


SELECT FROM users;
SELECT * FROM users
SELECT * FROM users WHERE name =  "John" 

DELETE FROM users where name = "John"

.schema    ~ layouts 

diagram db, fastAPI


db.sql 
CREATE DATABASE falcon
CREATE TABLE customers{
    id primary key,AUTOINCREMENT
    user_id INTEGER,
    name TEXT
    CONSTRAINT fk_users FOREIGN KEY (users);
    
}

