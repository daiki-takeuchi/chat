CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT,
    user_name VARCHAR(128) ,
    mail VARCHAR(255) ,
    password VARCHAR(256) ,
    job VARCHAR(256) ,
    self_introduction VARCHAR(2048) ,
    created_at DATETIME NOT NULL ,
    created_user VARCHAR(128) NOT NULL ,
    updated_at DATETIME NOT NULL ,
    updated_user VARCHAR(128) NOT NULL ,
    PRIMARY KEY (id) ,
    UNIQUE KEY (mail)
    ) ENGINE = INNODB;


CREATE TABLE IF NOT EXISTS posts (
    id INT NOT NULL AUTO_INCREMENT,
    user_id INT NOT NULL ,
    content VARCHAR(128),
    created_at DATETIME NOT NULL ,
    created_user VARCHAR(128) NOT NULL ,
    updated_at DATETIME NOT NULL ,
    updated_user VARCHAR(128) NOT NULL ,
    PRIMARY KEY (id)
    ) ENGINE = INNODB;


CREATE TABLE IF NOT EXISTS following (
    id INT NOT NULL AUTO_INCREMENT,
    user_id INT NOT NULL ,
    following_id INT NOT NULL ,
    created_at DATETIME NOT NULL ,
    created_user VARCHAR(128) NOT NULL ,
    updated_at DATETIME NOT NULL ,
    updated_user VARCHAR(128) NOT NULL ,
    PRIMARY KEY (id),
    UNIQUE KEY (user_id, following_id)
    ) ENGINE = INNODB;
