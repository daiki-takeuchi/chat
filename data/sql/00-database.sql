create database if not exists chat_db character set utf8;
create user 'chat_user' identified by 'chat_user';
grant all on chat_db.* to 'chat_user';
create database if not exists chat_db_test character set utf8;
create user 'chat_user_test' identified by 'chat_user_test';
grant all on chat_db_test.* to 'chat_user_test';