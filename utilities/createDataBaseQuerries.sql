create table users
(
    user_id      int auto_increment
        primary key,
    private_name varchar(20) null,
    last_name    varchar(20) null,
    email        varchar(40) not null,
    phone_number varchar(15) null,
    password     varchar(20) not null
);


INSERT INTO group14.users (user_id, private_name, last_name, email, phone_number, password) VALUES (1, 'cristiano', 'ronaldo', 'CR7@gmail.com', '054-4444444', '12345');
INSERT INTO group14.users (user_id, private_name, last_name, email, phone_number, password) VALUES (2, 'bruno', 'fernandes', 'Bronu@gmail.com', '054-4444445', '12346');
INSERT INTO group14.users (user_id, private_name, last_name, email, phone_number, password) VALUES (3, 'fred', 'fred', 'Fred@gmail.com', '054-4444446', '12347');
INSERT INTO group14.users (user_id, private_name, last_name, email, phone_number, password) VALUES (4, 'david', 'de gea', 'Saver@gmail.com', '054-4444447', '12348');
INSERT INTO group14.users (user_id, private_name, last_name, email, phone_number, password) VALUES (5, 'alex', 'ferguson', 'Sir@gmail.com', '054-4444448', '12349');

create table toys
(
    toy_id        int auto_increment
        primary key,
    toy_name      varchar(30)                      null,
    toy_category  enum ('4-', '8-', '9+')          null,
    is_taken      tinyint(1)                       not null,
    toy_condition enum ('bad', 'good', 'like new') not null,
    toy_image_url varchar(200)                     null
);

INSERT INTO group14.toys (toy_id, toy_name, toy_category, is_taken, toy_condition, toy_image_url) VALUES (1, 'robot', '9+', 1, 'good', 'https://cdn.azrieli.com/Images/a8b94a2a-d2ff-4ae2-a231-a8408c3e60b7/Normal/fd41b236.jpg');
INSERT INTO group14.toys (toy_id, toy_name, toy_category, is_taken, toy_condition, toy_image_url) VALUES (2, 'puzzle', '8-', 1, 'bad', null);
INSERT INTO group14.toys (toy_id, toy_name, toy_category, is_taken, toy_condition, toy_image_url) VALUES (3, 'teddyBear', '4-', 0, 'bad', 'https://i.pinimg.com/474x/15/ae/da/15aedaf16c4f801f05491ed9e7899c28.jpg');
INSERT INTO group14.toys (toy_id, toy_name, toy_category, is_taken, toy_condition, toy_image_url) VALUES (4, 'car', '9+', 0, 'like new', null);
INSERT INTO group14.toys (toy_id, toy_name, toy_category, is_taken, toy_condition, toy_image_url) VALUES (5, 'lego', '8-', 1, 'bad', null);

create table cities
(
    city_name varchar(20) not null
        primary key
);

INSERT INTO group14.cities (city_name) VALUES ('Ashdod');
INSERT INTO group14.cities (city_name) VALUES ('Ashqelon');
INSERT INTO group14.cities (city_name) VALUES ('Bat Yam');
INSERT INTO group14.cities (city_name) VALUES ('Beersheba');
INSERT INTO group14.cities (city_name) VALUES ('Bené Beraq');
INSERT INTO group14.cities (city_name) VALUES ('Bet Shemesh');
INSERT INTO group14.cities (city_name) VALUES ('Givatayim');
INSERT INTO group14.cities (city_name) VALUES ('Hadera');
INSERT INTO group14.cities (city_name) VALUES ('Haifa');
INSERT INTO group14.cities (city_name) VALUES ('Herẕliyya');
INSERT INTO group14.cities (city_name) VALUES ('Holon');
INSERT INTO group14.cities (city_name) VALUES ('Jerusalem');
INSERT INTO group14.cities (city_name) VALUES ('Kefar Sava');
INSERT INTO group14.cities (city_name) VALUES ('Lod');
INSERT INTO group14.cities (city_name) VALUES ('Modi‘in Makkabbim Re');
INSERT INTO group14.cities (city_name) VALUES ('Nahariyya');
INSERT INTO group14.cities (city_name) VALUES ('Nazareth');
INSERT INTO group14.cities (city_name) VALUES ('Netanya');
INSERT INTO group14.cities (city_name) VALUES ('Petah Tiqwa');
INSERT INTO group14.cities (city_name) VALUES ('Ra‘ananna');
INSERT INTO group14.cities (city_name) VALUES ('Rahat');
INSERT INTO group14.cities (city_name) VALUES ('Ramat Gan');
INSERT INTO group14.cities (city_name) VALUES ('Ramla');
INSERT INTO group14.cities (city_name) VALUES ('Reẖovot');
INSERT INTO group14.cities (city_name) VALUES ('Rishon LeẔiyyon');
INSERT INTO group14.cities (city_name) VALUES ('Tel Aviv-Yafo');

create table location
(
    user_id int                                               not null
        primary key,
    region  enum ('east', 'west', 'south', 'north', 'center') not null,
    adress  varchar(30)                                       not null,
    city    varchar(30)                                       not null,
    constraint location_cities_city_name_fk
        foreign key (city) references cities (city_name),
    constraint location_users_user_id_fk
        foreign key (user_id) references users (user_id)
);

INSERT INTO group14.location (user_id, region, adress, city) VALUES (1, 'east', 'yafo 12', 'Lod');
INSERT INTO group14.location (user_id, region, adress, city) VALUES (2, 'north', 'levinski 5', 'Nahariyya');
INSERT INTO group14.location (user_id, region, adress, city) VALUES (3, 'center', 'saloniki 10', 'Tel Aviv-Yafo');
INSERT INTO group14.location (user_id, region, adress, city) VALUES (4, 'center', 'saloniki 8', 'Tel Aviv-Yafo');
INSERT INTO group14.location (user_id, region, adress, city) VALUES (5, 'south', 'shimoni 4', 'Beersheba');

create table `user_toys table`
(
    user_id    int      not null,
    toy_id     int      not null,
    date_added datetime not null
        primary key,
    constraint `user_toys table_toys_toy_id_fk`
        foreign key (toy_id) references toys (toy_id),
    constraint `user_toys table_users_user_id_fk`
        foreign key (user_id) references users (user_id)
);

INSERT INTO group14.`user_toys table` (user_id, toy_id, date_added) VALUES (5, 5, '2022-02-16 17:09:54');
INSERT INTO group14.`user_toys table` (user_id, toy_id, date_added) VALUES (4, 1, '2022-02-16 17:09:57');
INSERT INTO group14.`user_toys table` (user_id, toy_id, date_added) VALUES (2, 4, '2022-05-16 17:09:47');
INSERT INTO group14.`user_toys table` (user_id, toy_id, date_added) VALUES (1, 2, '2022-07-16 17:09:42');
INSERT INTO group14.`user_toys table` (user_id, toy_id, date_added) VALUES (1, 3, '2022-07-16 17:09:45');

