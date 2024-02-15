-- 1. create database

-- 1.1 basics
drop database if exists test; -- drop the database if already exists
create database test; -- create database, note to enclose the database name with a pair of backticks
use test; -- the following sql code applies to this database

create table employee (
	empid int(5) not null default 1,
    address varchar(50) default null,
	primary key (empid),
    unique (empid,address)
);

insert into employee (empid, address) values -- note that if we do "insert into employee (address, empid) values", we will get value type errors
(2, "place A"),
(3, "place B");

create table phone (
	phone int(10),
    EmpID int(5) not null,
    primary key (phone) using HASH, -- you can also using BTREE
	foreign key (EmpID) references employee (empid) -- adding foreign key constraints help keep data integrity. 
													-- e.g., in the following insert line, you cannot insert (510222222, 4)
);													-- the referenced field in foreign key constraints must be either unique or primary key.
													-- and it must be of the same data type.
													-- if you don't have the foreign key constraints, then you are OK to insert (510222222, 4)

insert into phone values 
(510222222, 2),
(520333333, 2),
(312323232, 3); 

-- 1.2 enforcing cardinality
-- how to enforce one-to-one, one-to-many, and many-to-many?
create table phone (
	phone int(10),
    EmpID int(5) not null,
    primary key (phone) using HASH, -- you can also using BTREE
	foreign key (EmpID) references employee (empid),
    unique (EmpID) -- one employee only has one entry in this table (one employee has up to one phone)
);
-- since phone is the primary key, it must be unique, then with the "unique (EmpID)", the EmpID becomes unique too, 
-- the cardinality is 1 for both employee and phone.
-- if you try to run 
insert into phone values 
(510222222, 2),
(520333333, 2),
(312323232, 3); 
-- you will get error, since the employee 2 is not unique (employee2 has two numbers)
-- with "unique (EmpID)", we have a one-to-one relationship
-- without "unique (EmpID)", we have a one-to-many relationship 

-- is it possible to make a many-to-many relationship?
-- allowing a many-to-many relationship is simply not to impose any contraints. But....
-- because when each phone number can be used by multiple employees in this setting, 
-- the same phone number may appear multiple times in the table
-- so you can not use it as the primary key anymore. 
-- we will need to create an ID column now.

create table phone (
	ID int AUTO_INCREMENT not null, -- when only insert other values, this column value will automatically increment
	phone int(10),
    EmpID int(5) not null,
    primary key (ID) using HASH, -- you can also using BTREE
	foreign key (EmpID) references employee (empid)
);

insert into phone (phone, EmpID) values -- when we have a column that is auto-increment, we must specify the columns we want to insert values 
(510222222, 2),
(520333333, 2),
(520333333, 3),
(312323232, 3); 
-- by creating a dedicated primary key in the association entity (note that the phone table is itself the association entity, since there is no other attributes for phone numbers, we don't need to create another table to document these attributes) 
-- we allow for a many-to-many relationship, one phone number can be used by many employees
-- one employee can have multiple phone numbers.
-- the reason that we only have two tables for a many-to-many relationship is that the phone numbers does not have any attributes. 
-- if phone numbers have attributes, we need three tables.
--------------------------------------------------------------------------------------------------------------------------------------------------
-- 2. update, delete, and other commands

-- 2.1 describe a table
desc course;

-- 2.2 update a table
update course
set course_name="H" -- the H is a value, so enclose it with double quote. If enclose with backticks, it means a field called H.
where training_course="101"; -- remember that update, set where is a single clause, do need to add comma, or semi colon in the middle
-- if you omit the where clause, it will update all the rows.
-- but if you are in safe mode, you cannot do the update without a where clause. If you really want to update all rows, disable the safe mode
-- to disable the safe mode, go to the edit->preference->SQL editor->scroll down to uncheck the safe mode->reconnect to database

-- 2.3 add column
alter table course
add course_difficulty varchar(10) default 1;

-- add a calculated column
-- add a column showing the monthly salary
alter table employee
add monthly_salary int as (employee.salary/12);

-- 2.4 drop column
alter table course
drop course_difficulty;

-- 2.5 drop rows
delete from  course
where course.training_course='101';

-- 2.6 drop table
drop table course;
--------------------------------------------------------------------------------------------------------------------------------------------------
-- 3. building blocks

-- 3.1 select from where

-- now let's reload the employeetraining database
-- the three basic components of select

-- select -> indicate what column you want from the database
-- from  -> indicate what are the tables involved to retrieve the data
-- where -> indicate the conditions

-- select all columns from a specific table
select * from course; 

-- generate a list of all last name and first name for all employees
select employee.first_name, employee.last_name
from employee;

-- generate a unique list of department.
select dept 
from employee;

-- however, the mktg and sales are repeated. Use the distinct method to remove the duplicates
select distinct dept 
from employee;

-- the where clause
-- select employees from sales department
select emp_id 
from employee
where dept="Sales";

-- 3.2 and or not
-- the and clause, used to link multiple conditions
-- select employees from sales department with salary greater than 60k
select emp_id, first_name, last_name 
from employeetraining.employee
where dept="Sales"
and salary>=60000;

-- the or clause, used to link multiple conditions
-- select employees with greater than 60k salary or from Operations department
select emp_id, first_name, last_name 
from employeetraining.employee
where salary>=60000
or dept="Ops";

-- the not operator
-- select employee not from the sales department
select emp_id, first_name, last_name 
from employeetraining.employee
where not dept="Sales";

-- 3.3 order by
-- order employees by first_name in decending order (for ascending order use asc (the default is asc))
select * 
from employeetraining.employee
order by first_name desc;

-- first order employees according to department in a descending order, then order by salary in ascending order
select * 
from employeetraining.employee
order by dept desc, salary asc;

-- sometimes when there are so many returned values, we only need to see the first few. 
-- what are the two highest salaries.
select emp_id, salary 
from employee
order by salary desc
limit 2;

-- 3.4 in operator
-- you can use or to achieve the same function, but this is easier if you have many options.
-- generate a list of employee from sales or operations department
select emp_id 
from employee 
where dept in ("Sales","Ops");

-- not in operator (duplicates are not removed)
select emp_id, dept
from employee 
where dept not in ("Mktg","Ops");

-- 3.5 between and 
-- generate a list of employees with salary between 58000 and 62000
select emp_id, salary 
from employee 
where salary between 58000 and 62000;
-- the 58000 and the 62000 are inclusive

-- you can also declare variables, but the variable declared can only be accessed by the current client, but not other clients
SET @low = 58000, @high = 62000; -- if you have different section of codes, the semicolon is a must.
select emp_id, salary from employee where salary between @low and @high;

-- 3.6 summary a table
select min(salary), max(salary), avg(salary), sum(salary)
from employee;

-- give the summary statistics alias
select min(salary) as minsalary, max(salary) as maxsalary, avg(salary) as avgsalary, sum(salary) as totalsalary
from employee;

-- count
select count(*)
from employee
where salary>=56000;

-- count unique number of deptments
select count(distinct dept) from employee;
select count(distinct dept) as n_dept from employee; -- with alias

-- 3.7 like operator
select emp_id
from employee
where first_name like "j%"; -- first name start with letter j

select emp_id
from employee
where last_name like "%s"; -- last name ends with letter s

select emp_id
from employee
where last_name like "%v%"; -- last name has the letter v in it

select emp_id
from employee
where first_name like "_o%"; -- the second letter in first name is o -- the pattern is the same as "%_o%"

select emp_id
from employee
where first_name like "%_____%"; -- at least 5 character in first name

-- 3.8 group by
-- count the number of employees in each department
select dept, count(*) as n_emp
from employee
group by dept; -- for each different deparment, we do the above operations.

-- check the number of times each course is registered
select Training_Course, count(*) as n_reg
from registration
group by Training_Course;

-- check the number of times each course is registered after 2004
select Training_Course, count(*) as n_reg
from registration
where Course_Date>='2004-12-31' -- before group by, this is applied to individual record 
group by Training_Course;

-- calculate the average salary for each dept, sort according to the number of employees in each department
select avg(salary) as avgsalary, dept
from employee
where hire_date>='2001-01-01' -- this is how to format date in SQL
group by dept 
order by count(*) desc; -- order by number of employees in each department

-- same thing, but order by the average salary.
-- everything after the group by is applied to the groups generated.
select avg(salary) as avgsalary, dept
from employee
where hire_date>='2001-01-01' 
group by dept 
order by avgsalary;

-- in the following example, we constraint that the department name has to contain at least 4 characters. So Ops is excluded
-- where is used to constraint individual records, while having is used to constraint groups. The dept in the having clause referes to the group dept. 
select avg(salary), dept
from employee
where hire_date>='2001-01-01'
group by dept
having dept like '%____%';

-- showing the number of pacipating students for courses with at least two students.
select Training_Course, count(*) as n_stu
from registration
group by Training_Course
having n_stu >= 2;

-- 3.9 substring and concat
-- the substring function
-- get the first three letter of employee's first name
select substring(last_name, 1, 3) as first_three
from employee;

-- the concat function
-- get the full name of employees in the format "last_name, first_name"
select concat(last_name,', ', first_name) as full_name from employee;

-- add a full name column showing the full name as (first_name,', ',last_name)
alter table employee
add column fullname varchar(255) as (concat(last_name,', ', first_name));

select * from employee;

alter table employee
drop column fullname;

-- 3.10 row_number, rank, and dense rank
-- the difference between rank and dense rank is when there are ties

-- suppose we add an employee with 60000 salary, now there is a tie
insert into employee values 
(20000, "A", "B", "MKTG", 60000, "2004-01-03");

-- check the difference between rank and dense_rank
select emp_id, salary,
	row_number() over (order by salary desc),
    rank() over (order by salary desc),
    dense_rank() over (order by salary desc)
FROM employee;
-- more on over clause after discussing table joins

-- now remove the row to restore the employee table
delete from employee
where employee.emp_id=20000;
--------------------------------------------------------------------------------------------------------------------------------------------------
-- 4 case statement

-- say we want to generate a report on the employee's salary, but we don't want to show the real number, but "high salary" or "low salary"
-- simply remove the usual salary field in the select clause and replaice it with the case statement.
-- this entire case statement is actuall a field
select emp_id, 
(case
	when employee.salary>=60000 then "high salary"
    when employee.salary>=58000 then "median salary"
    else "low salary"
 end) as salaryindicator
from employee;

-- check if the employee salary reaches the minimum wage
set @min_wage= 59000;
select employee.emp_id,
(case 
	when employee.salary>@min_wage then "OK"
	when employee.salary=@min_wage then "equal"
	else "Lower Than Min Wage"
end) as min_wage_satiafaction
from employee;

-- sort the employee table by dept when there are at least three departments, otherwise sort by the employee's id.
select emp_id, first_name, last_name 
from employee
order by 
(case 
	when (select count(distinct dept) from employee)>=3 then dept
	else emp_id 
end);

-- the following code generate binary indicators showing if a particular employee belongs to one department
select emp_id, 
(case 
	when dept="Sales" then 1 
	else 0
end) as sales,
(case 
	when dept='Mktg' then 1
	else 0
end) as marketing,
(case 
	when dept='acctg' then 1
	else 0
end) as accounting,
(case 
	when dept='Ops' then 1
	else 0
end) as operation
from employee;

-- since the case statement generate a field, we can use avg, sum, max, min as usual in the select clause.
-- the following code will generate the count of employees in each department
select
sum(case 
	when dept="Sales" then 1 
	else 0
end) as n_sales,
sum(case 
	when dept='Mktg' then 1
	else 0
end) as n_marketing,
sum(case 
	when dept='acctg' then 1
	else 0
end) as n_accounting,
sum(case 
	when dept='Ops' then 1
	else 0
end) as n_operation
from employee;
--------------------------------------------------------------------------------------------------------------------------------------------------
-- 5. query from multiple tables

-- 5.1 the basics
-- select from two tables, we got cross join of the two tables
-- the employee table has 5 rows, and the registration table has 7 rows, so the output has 35 rows
-- however, many of them do not make sense -> 10300	Carter	Michael	Sales	60000	2005-02-01	2004-04-01	10020	101
select *
from employee, registration;

-- we can easily remove these wrong records by linking the primary key and foreign key, i.e forcing the Emp_ID in the registration table the same as the emp_id in the employee tables
select *
from employee, registration  -- switching these two tables will only make the output to arrange the fields in registration table first
where employee.emp_id=registration.Emp_ID;
-- now we end up with only 7 rows.
-- this is actually called a inner join

-- we can also select from multiple tables. These tables will be cross joined as well.
select * 
from employee, registration, course; -- cross join three tables. 
-- also check select count(*) =210 = 6*5*7

select * 
from course; 

select *
from employee, registration, course -- switching these two tables will only make the output to arrange the fields in registration table first
where employee.emp_id=registration.Emp_ID
and registration.Training_Course=course.training_course;

select *
from employee, registration, course -- switching these two tables will only make the output to arrange the fields in registration table first
where employee.emp_id=registration.Emp_ID
and registration.Training_Course=course.training_course;

select *
from employee
join registration-- switching these two tables will only make the output to arrange the fields in registration table first
on employee.emp_id=registration.Emp_ID
join course
on registration.Training_Course=course.training_course;

-- get a list of employee who took course 210
select first_name, last_name
from employee, registration
where employee.emp_id=registration.Emp_ID
and registration.Training_Course=210;

-- get a list of course name of the course existing before 2006
select course_name
from course, registration
where course.training_course=registration.training_course
and registration.Course_Date<'2006-01-01';

-- number of employees who took 101, 103, or 210
-- is the following code correct? If not, how to correct (change count(*) to count(distinct employee.emp_id))
select count(*)
from registration, employee
where registration.Training_Course in (101,103,210)
and employee.emp_id=registration.Emp_ID;

select count(distinct employee.emp_id)
from registration, employee
where registration.Training_Course in (101,103,210)
and employee.emp_id=registration.Emp_ID;

-- the name of employee who took course A
select first_name, last_name
from course, registration, employee
where course.course_name='A'
and registration.training_course=course.training_course
and employee.emp_id=registration.Emp_ID;

-- count how many employees took course D in each department
select dept, count(*) as n_emp
from employee,registration,course
where employee.emp_id=registration.Emp_ID
and registration.Training_Course=course.training_course
and course.course_name="D"
group by dept;

-- 5.2 table alias
select E.emp_id, R.Training_Course 
from employee as E, registration as R
where E.emp_id=R.Emp_ID;

-- who took both the 101 course and the 205 course?
select E.first_name, E.last_name
from employee as E, registration as R1, registration as R2 -- cross join the same table to compare between differnet records
where E.emp_id=R1.Emp_ID
and E.emp_id=R2.Emp_ID
and R1.Training_Course=101
and R2.Training_Course=205;

-- next, we show some example with the book loan database
-- suppose we want to generate a list of student's name for those who have ever borrowed the book A00001
select distinct student.Stu_ID,student.Stu_Name
from student,loan
where student.Stu_ID=loan.Stu_ID
and loan.Book_Call_No="A00001";

-- generate a list of sutdent names for those who heve ever borrowed the book Basic Chemistry authored by Rudy,H
select distinct student.Stu_ID,student.Stu_Name
from student,loan,copy,book
where student.Stu_ID=loan.Stu_ID
and loan.Book_Call_No=copy.Book_Call_No
and copy.Book_ISBN=book.Book_ISBN
and book.Book_Title="Basic Chemistry"
and book.Book_First_Author="Rudy, H.";

-- show the number of chemistry books borrowed by each student
select student.Stu_ID,student.Stu_Name, count(*) n_borrow
from student,loan,copy,book
where student.Stu_ID=loan.Stu_ID
and loan.Book_Call_No=copy.Book_Call_No
and copy.Book_ISBN=book.Book_ISBN
and book.Book_Title like "%Chemistry%"
group by student.Stu_ID;
--------------------------------------------------------------------------------------------------------------------------------------------------
-- 6. some exercise

-- calculate the number of Pass and Fail for each branch
select interview.Bran_ID,
sum(case
	when interview.Interview_Result="Pass" then 1
    else 0
end) as pass,
sum(case
	when interview.Interview_Result="Fail" then 1
    else 0
end) as fail
from interview
group by interview.Bran_ID;

-- calculate the number of Pass and Fail for each branch for each interview round
select interview.Bran_ID, interview.Interview_Round,
sum(case
	when interview.Interview_Result="Pass" then 1
    else 0
end) as pass,
sum(case
	when interview.Interview_Result="Fail" then 1
    else 0
end) as fail
from interview
group by interview.Bran_ID, interview.Interview_Round;

-- who are the candidate that passed the first round
select interview.Cand_ID
from interview
where interview.Interview_Round="First" and interview.Interview_Result="Pass";

-- who are the candidate that passed the first round and the second round for the same branch?
select *
from interview as E1, interview as E2
where E1.Interview_Round = "First" and E1.Interview_Result = "Pass"
and E2.Interview_Round = "Second" and E2.Interview_Result = "Pass"
and E1.Bran_ID = E2.Bran_ID;

select *
from interview;

-- get a list of applicant who applied for at least two branches.
select interview.Cand_ID
from interview
group by interview.Cand_ID
having count(distinct interview.Bran_ID)>1;

-- which branch receives the most applications?
select interview.Bran_ID, count(distinct interview.Cand_ID) as candidate_count
from interview
group by interview.Bran_ID
order by candidate_count desc
limit 1;

-- for each application, calculate its the start date and end date
select interview.Cand_ID, interview.Bran_ID, min(interview.Interview_Date) as interview_start_date, max(interview.Interview_Date) as interview_end_date
from interview
group by interview.Cand_ID,interview.Bran_ID;

-- calculate the passing rate for each branch. Passing rate = number of pass / num of interviews.
select interview.Bran_ID,
sum(case 
	when interview.Interview_Result="Pass" then 1
    else 0
end)/count(*) as passing_rate
from interview
group by interview.Bran_ID
