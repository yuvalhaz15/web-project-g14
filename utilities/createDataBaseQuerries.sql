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


INSERT INTO group14.users (user_id, private_name, last_name, email, phone_number, password) VALUES (1, 'כריסטיאנו', 'רונלדו', 'CR7@gmail.com', '054-4444444', '12345');
INSERT INTO group14.users (user_id, private_name, last_name, email, phone_number, password) VALUES (2, 'ברונו', 'פרננדס', 'Bronu@gmail.com', '054-4444445', '12346');
INSERT INTO group14.users (user_id, private_name, last_name, email, phone_number, password) VALUES (3, 'פרד', 'פרד', 'Fred@gmail.com', '054-4444446', '12347');
INSERT INTO group14.users (user_id, private_name, last_name, email, phone_number, password) VALUES (4, 'דויד', 'דה חאה', 'Saver@gmail.com', '054-4444447', '12348');
INSERT INTO group14.users (user_id, private_name, last_name, email, phone_number, password) VALUES (5, 'אלקס', 'פרגוסון', 'Sir@gmail.com', '054-4444448', '12349');

create table toys
(
    toy_id        int auto_increment
        primary key,
    toy_name      varchar(30)                    null,
    toy_category  enum ('4-', '8-', '9+')        null,
    is_taken      tinyint(1)                     not null,
    toy_image_url varchar(200)                   null,
    toy_condition enum ('טוב', 'ישן', 'כמו חדש') null
);


INSERT INTO group14.toys (id, toy_name, toy_category, is_taken, toy_image_url, toy_condition) VALUES (1, 'רובוט', '9+', 1, 'https://cdn.azrieli.com/Images/a8b94a2a-d2ff-4ae2-a231-a8408c3e60b7/Normal/fd41b236.jpg', 'כמו חדש');
INSERT INTO group14.toys (id, toy_name, toy_category, is_taken, toy_image_url, toy_condition) VALUES (2, 'פאזל', '8-', 1, null, 'ישן');
INSERT INTO group14.toys (id, toy_name, toy_category, is_taken, toy_image_url, toy_condition) VALUES (3, 'דובון', '4-', 0, 'https://i.pinimg.com/474x/15/ae/da/15aedaf16c4f801f05491ed9e7899c28.jpg', 'טוב');
INSERT INTO group14.toys (id, toy_name, toy_category, is_taken, toy_image_url, toy_condition) VALUES (4, 'מכונית', '9+', 0, null, 'ישן');
INSERT INTO group14.toys (id, toy_name, toy_category, is_taken, toy_image_url, toy_condition) VALUES (5, 'לגו', '8-', 1, null, 'טוב');

create table cities
(
    city_name varchar(20) not null
        primary key
);

INSERT INTO group14.cities (city_name) VALUES ('אשדוד');
INSERT INTO group14.cities (city_name) VALUES ('אשקלון');
INSERT INTO group14.cities (city_name) VALUES ('באר שבע');
INSERT INTO group14.cities (city_name) VALUES ('בית שמש');
INSERT INTO group14.cities (city_name) VALUES ('בני ברק');
INSERT INTO group14.cities (city_name) VALUES ('בת ים');
INSERT INTO group14.cities (city_name) VALUES ('גבעתיים');
INSERT INTO group14.cities (city_name) VALUES ('הרצליה');
INSERT INTO group14.cities (city_name) VALUES ('חדרה');
INSERT INTO group14.cities (city_name) VALUES ('חולון');
INSERT INTO group14.cities (city_name) VALUES ('חיפה');
INSERT INTO group14.cities (city_name) VALUES ('ירושלים');
INSERT INTO group14.cities (city_name) VALUES ('כפר סבא');
INSERT INTO group14.cities (city_name) VALUES ('לוד');
INSERT INTO group14.cities (city_name) VALUES ('מודיעין');
INSERT INTO group14.cities (city_name) VALUES ('נהריה');
INSERT INTO group14.cities (city_name) VALUES ('נצרת');
INSERT INTO group14.cities (city_name) VALUES ('נתניה');
INSERT INTO group14.cities (city_name) VALUES ('פתח תקווה');
INSERT INTO group14.cities (city_name) VALUES ('ראשון לציון');
INSERT INTO group14.cities (city_name) VALUES ('רהט');
INSERT INTO group14.cities (city_name) VALUES ('רחבות');
INSERT INTO group14.cities (city_name) VALUES ('רמלה');
INSERT INTO group14.cities (city_name) VALUES ('רמת גן');
INSERT INTO group14.cities (city_name) VALUES ('רעננה');
INSERT INTO group14.cities (city_name) VALUES ('תל אביב-יפו');


create table location
(
    user_id int                                           not null
        primary key,
    adress  varchar(30)                                   not null,
    city    varchar(30)                                   not null,
    region  enum ('מזרח', 'מערב', 'דרום', 'צפון', 'מרכז') not null,
    constraint location_cities_city_name_fk_cities
        foreign key (city) references cities (city_name),
    constraint location_users_user_id_fk
        foreign key (user_id) references users (user_id)
);

INSERT INTO group14.location (user_id, adress, city, region) VALUES (1, 'יפו 12', 'לוד', 'מזרח');
INSERT INTO group14.location (user_id, adress, city, region) VALUES (2, 'בליקנד 14', 'נהריה', 'צפון');
INSERT INTO group14.location (user_id, adress, city, region) VALUES (3, 'מצדה 11', 'תל אביב-יפו', 'מרכז');
INSERT INTO group14.location (user_id, adress, city, region) VALUES (4, 'חי טייב 13', 'תל אביב-יפו', 'מרכז');
INSERT INTO group14.location (user_id, adress, city, region) VALUES (5, 'שמעוני 4', 'באר שבע', 'דרום');

create table user_toys
(
    user_id    int      not null,
    toy_id     int      not null,
    date_added datetime not null
        primary key,
    constraint `user_toys table_toys_toy_id_fk`
        foreign key (toy_id) references toys (id),
    constraint `user_toys table_users_user_id_fk`
        foreign key (user_id) references users (user_id)
);

INSERT INTO group14.user_toys  (user_id, toy_id, date_added) VALUES (5, 5, '2022-02-16 17:09:54');
INSERT INTO group14.user_toys  (user_id, toy_id, date_added) VALUES (4, 1, '2022-02-16 17:09:57');
INSERT INTO group14.user_toys (user_id, toy_id, date_added) VALUES (2, 4, '2022-05-16 17:09:47');
INSERT INTO group14.user_toys  (user_id, toy_id, date_added) VALUES (1, 2, '2022-07-16 17:09:42');
INSERT INTO group14.user_toys  (user_id, toy_id, date_added) VALUES (1, 3, '2022-07-16 17:09:45');

