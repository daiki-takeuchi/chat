create database if not exists chat_db character set utf8;
create user 'chat_user' identified by 'chat_user';
grant all on chat_db.* to 'chat_user';