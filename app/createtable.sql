CREATE TABLE appointments(
id 	    SERIAL 	Primary Key,
name 	VARCHAR(200) 	Not Null,
start_datetime 	TIMESTAMP 	Not Null,
end_datetime 	TIMESTAMP 	Not Null,
description 	TEXT 	Not Null,
private 	BOOLEAN 	Not Null
);
Column name 	Column type 	Constraints
id 	    SERIAL 	Primary Key
name 	VARCHAR(200) 	Not Null
start_datetime 	TIMESTAMP 	Not Null
end_datetime 	TIMESTAMP 	Not Null
description 	TEXT 	Not Null
private 	BOOLEAN 	Not Null

INSERT INTO appointments (name, start_datetime, end_datetime, description, private)
VALUES
('My appointment', '2023-04-17 14:00:00', '2023-04-17 15:00:00',
 'An appointment for me', false);
