
# Introduction to the Virtual Lab

A virtual lab interface gives students remote access to equipment in laboratories via the internet without having to be physically present near the equipment.
The idea is that lab experiments can be made accessible to a larger audience which may not have the resources to set up the experiment at their place.
Another use-case scenario is that the experiment setup must be placed at a specific location which may not be habitable.

The PSLab’s capabilities can be increased significantly by setting up a framework that allows remote data acquisition and control.
It can then be deployed in various test and measurement scenarios such as an interactive environment monitoring station.

In the beginning, we will follow a basic [tutorial](https://code.tutsplus.com/series/creating-a-web-app-from-scratch-using-python-flask-and-mysql--cms-827) to create a web-app using flask.

## Dependencies

### Backend

The virtual lab will be hosted using [Python-Flask](http://flask.pocoo.org/), which is a BSD Licensed microframework for Python based on Werkzeug and Jinja 2  .

It will also use MySql to handle a database containing user credentials and data

### Frontend

coming soon.

## Installing dependencies

+ Install THE MYSQL DATABASE
  + sudo apt-get install mysql-server
  + provide the password. Username is root by default

The following command will install flask as well as dependencies such as Jinja2, itsdangerous, click, and Werkzeug
sudo pip install flask

sudo pip install flask-mysql


## Configuring the database

In the following steps, we will create some tables and procedure in the MySql database. As the project matures, this procedure will be automated.

Open a command prompt, and execute the following. Username equals `root` by default.
`mysql -u <username> -p `

Copy paste the following mysql commands and procedures into the prompt

`CREATE DATABASE VirtualUsers;`

Create a table called `tbl_user` in the database we just created.
```
use VirtualUsers;

CREATE TABLE `VirtualUsers`.`tbl_user` (
  `user_id` BIGINT NULL AUTO_INCREMENT,
  `user_name` VARCHAR(50) NULL,
  `user_username` VARCHAR(100) NULL,
  `user_password` VARCHAR(100) NULL,
  PRIMARY KEY (`user_id`));
```

Create a procedure to add a user with the following keys : name, username (e-mail) ,password
```
use VirtualUsers;

DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_createUser`(
    IN p_name VARCHAR(50),
    IN p_username VARCHAR(100),
    IN p_password VARCHAR(100)
)
BEGIN
    if ( select exists (select 1 from tbl_user where user_username = p_username) ) THEN
     
        select 'Username Exists !!';
     
    ELSE
     
        insert into tbl_user
        (
            user_name,
            user_username,
            user_password
        )
        values
        (
            p_name,
            p_username,
            p_password
        );
     
    END IF;
END$$
DELIMITER ;
```

create a procedure to validate a login attempt
```
use VirtualUsers;
DELIMITER $$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_validateLogin`(
IN p_username VARCHAR(100)
)
BEGIN
    select * from tbl_user where user_username = p_username;
END$$
DELIMITER ;
```

Add a table for storing small code snippets
```
CREATE TABLE `tbl_code` (
  `code_id` int(11) NOT NULL AUTO_INCREMENT,
  `code_title` varchar(45) DEFAULT NULL,
  `code_description` varchar(50000) DEFAULT NULL,
  `code_user_id` int(11) DEFAULT NULL,
  `code_date` datetime DEFAULT NULL,
  PRIMARY KEY (`code_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
```

add a procedure to add a small script
```
USE VirtualUsers;
DROP procedure IF EXISTS `VirtualUsers`.`sp_addCode`;
 
DELIMITER $$
USE `VirtualUsers`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_addCode`(
    IN p_title varchar(45),
    IN p_description varchar(50000),
    IN p_user_id bigint
)
BEGIN
    insert into tbl_code(
        code_title,
        code_description,
        code_user_id,
        code_date
    )
    values
    (
        p_title,
        p_description,
        p_user_id,
        NOW()
    );
END$$
 
DELIMITER ;
```

A procedure to retrieve list of stored code by username
```
USE VirtualUsers;
DROP procedure IF EXISTS `sp_GetCodeByUser`;
 
DELIMITER $$
USE `VirtualUsers`$$
CREATE PROCEDURE `sp_GetCodeByUser` (
IN p_user_id bigint
)
BEGIN
    select * from tbl_code where code_user_id = p_user_id;
END$$
 
DELIMITER ;
```


## Running the app

`./run.py`
navigate to localhost:5000 in your web browser

