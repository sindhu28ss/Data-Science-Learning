
drop database if exists `employeetraining`; -- drop the database if already exists
create database `employeetraining`; -- create database, note to enclose the database name with a pair of backticks
use `employeetraining`; -- the following sql code applies to this database

create table `employee` (
	`emp_id` int(5) not null default '10000', -- manually type a tab
    `last_name` varchar(20) default null, -- varchar holds up to 8000 characters
    `first_name` varchar(20) default null, -- there are many sequence possible to define table columns, but for peace of mind, let us use "datatype","null/no null", "default value"
    `dept` varchar(10) not null,
    `salary` int(10) not null default '0',
    `hire_date` date not null,
    primary key (`emp_id`), -- create primary key 
    constraint employee_unique UNIQUE (`emp_id`) -- we created a unque constraint, the emp_id has to be unique. We can also create unique constraint with more than one fields, such as 'constraint employee_unique UNIQUE (`last_name`,`first_name`)'
											   -- which means that the combination of first name and last name has to be unique
) engine=InnoDB default charset=utf8; -- InnoDB is the newest storage engine

-- after the tabel is created, we enter the values

INSERT INTO `employee` (`Emp_ID`, `Last_Name`, `First_Name`, `Dept`, `Salary`, `Hire_Date`) VALUES
(10020, 'Marvin', 'John', 'Mktg', 65000, '2004-03-01'), -- remember this date format
(10300, 'Carter', 'Michael', 'Sales', 60000, '2005-02-01'),
(20040, 'Sanches', 'Jose', 'Sales', 58000, '2007-08-01'),
(20139, 'Gates', 'Susan', 'Acctg', 62000, '2006-03-01'),
(21113, 'Li', 'Ping', 'Ops', 55000, '2008-09-01');

-- commonly used data types in sql
-- bit 0 and 1
-- int -2,147,483,648 to 2,147,483,647
-- bigint -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807
-- float -1.79E + 308 to 1.79E + 308
-- date YYYY-MM-DD
-- time HH:MI:SS
-- datetime YYYY-MM-DD HH:MI:SS
-- timestamp number of seconds after ‘1970-01-01 00:00:00’ UTC
-- varchar up to 8000 characters
-- text max 2GB text data

CREATE TABLE `course` (
  `training_course` int(3) NOT NULL,
  `course_name` varchar(1) NOT NULL,
  primary key (training_course)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `course` (`Training_Course`, `Course_Name`) VALUES
(101, 'A'),
(103, 'C'),
(202, 'E'),
(205, 'B'),
(207, 'F'),
(210, 'D');

CREATE TABLE `registration` (
  `Course_Date` date NOT NULL,
  `Emp_ID` int(5) NOT NULL,
  `Training_Course` int(3) NOT NULL,
  primary key (`Emp_ID`,`Training_Course`), -- create a composite primary key
  foreign key (Emp_ID) references employee (emp_id),
  foreign key (Training_Course) references course (training_course)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


INSERT INTO `registration` (`Course_Date`, `Emp_ID`, `Training_Course`) VALUES
('2004-04-01', 10020, 101),
('2004-09-01', 10020, 205),
('2005-08-01', 10300, 103),
('2006-08-01', 10300, 210),
('2008-08-01', 20040, 210),
('2007-09-01', 20139, 202),
('2009-09-01', 21113, 207);