create database IoTS;

use IoTS;

create table Chair
(
	`chair_id` int not null auto_increment,
    `chair_name` nchar(50) not null,
    `chair_org` nvarchar(255) not null,
    `chair_info` text not null,
    `chair_add_time` date not null,
    `chair_update_time` date not null,
    primary key(`chair_id`)
);

create table ChairPic
(
	`chair_pic_id` int not null auto_increment,
    `chair_id` int not null,
    `session` int not null,
	`chair_pic_url` nvarchar(255) not null,
    primary key(`chair_pic_id`)
);

create table Conference
(
	`conference_id` int not null auto_increment,
    `session` int not null,
    `conference_topic` nchar(255) not null,
    `conference_start_time` datetime not null,
    `conference_end_time` datetime not null,
    `conference_locations` nvarchar(512) not null,
    `chair_id` int not null,
    primary key(`conference_id`)
);

create table User
(
	`user_id` int not null auto_increment,
    `user_name` nchar(255) not null,
    `user_email` nvarchar(255) not null,
    `user_password` nchar(20) not null,
    primary key(`user_id`)
);

create table Mange_Chair_Conference
(
	`manage_id` int not null auto_increment,
    `conference_id` int not null,
    `chair_id` int not null,
    primary key(`manage_id`)
);

