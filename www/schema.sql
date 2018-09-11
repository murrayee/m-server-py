--  schema.sql

drop database if exists murray;

create database murray;

use murray;


create table users (
  `id`           varchar(50)  not null,
  `avatar`       varchar(500) not null,
  `username`     varchar(20)  not null,
  `password`     varchar(20)  not null,
  `firstLetter`  varchar(20)  not null,
  `phone`        varchar(20)  not null,
  `socketId`     varchar(100) not null,
  `onlineStatus` varchar(100) not null,
  `vibration`    bool         not null,
  `created_at`   real         not null,
  key `idx_created_at` (`created_at`),
  primary key (`id`)
)
  engine = innodb
  default charset = utf8;