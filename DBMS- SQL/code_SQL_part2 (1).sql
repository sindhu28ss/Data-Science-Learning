-- 1. table join

-- 1.1 inner join
select *
from registration
inner join employee on employee.emp_id=registration.Emp_ID;
-- inner join only join tables when they share keys in common, 

-- when we swap registration and employee in the following code, we get similar results, only different column arrangement
select *
from employee
inner join registration on employee.emp_id=registration.Emp_ID;

-- now let's insert some rows into employee table
insert into employee VALUES
(10025, 'Peng', 'Xie', 'Mktg', 65000, '2004-03-01');
-- if you run the inner join again, nothing changes, because the newly inserted employee doesn't have a key 10025 in the registration table.
-- please keep this new record in the table for the rest of the class.

-- inner join with the same table, sometimes used for a unary relationship
-- first,create a new column managerID, make 10300 to be tbe manager of 10020 and 21113
-- in this way, we created a unary relationship 
alter table employee
add managerID int(10) default null;

update employee
set managerID = 10300 
where emp_id = 10020;

update employee
set managerID = 10300
where emp_id = 21113;

-- write a SQL query that finds employees who earn more than their managers. 
select * from employee;

select a.emp_id, a.last_name, a.first_name
from employee as a 
inner join employee as b on a.managerID = b.emp_id -- note here it is not a.emp_id = b.managerID
where a.salary > b.salary; -- note here it is not a.salary < b.salary

select a.emp_id, a.last_name, a.first_name, a.salary,a.managerID,b.salary
from employee as a 
inner join employee as b on a.managerID = b.emp_id -- note here it is not a.emp_id = b.managerID
where a.salary > b.salary;

-- now remove the new columns
alter table employee
drop managerID;

-- 1.2 left join
-- find all matching values from the right table and attach corresponding records to the left table
select *
from registration -- this is the left table
left join employee on employee.emp_id=registration.Emp_ID;

-- but when you swap the left table with the right table, you can see the difference
select *
from employee -- this is the left table
left join registration on employee.emp_id=registration.Emp_ID;
-- the newly inserted employee is matched with null values
-- the right join is the same

-- 1.3 cross join
-- this is the same as the first example in this code snippet
select *
from employee -- this is the left table
cross join registration;

-- 1.4 table join exercises
-- total number of courses taken by employees from each department
select *
from employee as E inner join registration as R on E.emp_id=R.Emp_ID;
-- during inner join, if there two records in one table (e.g., John Marvin) matching the same record in the other table
-- there will be two records in the inner join table.

select E.dept, count(E.emp_id) as total_course_taken
from employee as E inner join registration as R on E.emp_id=R.Emp_ID
group by E.dept;

-- output the employee's first name and the number of upper division courses they have taken
-- suppose those courses starting with 2 are upper division courses.
select E.first_name, count(E.emp_id) 
from employee as E left join registration as R on E.emp_id=R.Emp_ID
where R.Training_Course like '%2__%'
group by E.emp_id;

-- show all employee infor for those who studied at least 2 courses.
select E.* -- if just *, you will get all employee column and the registration column
from employee as E left join registration as R on E.emp_id=R.Emp_ID
group by E.emp_id
having count(E.emp_id)>=2;

-- count the number of courses taken by each employee
-- show 0 if the employee did not take any courses

-- proposal 1 (incorrect)
select E.first_name, E.last_name, count(E.emp_id)
from registration as R left join employee as E
on R.Emp_ID = E.emp_id
group by E.emp_id;

-- proposal 2 (incorrect)
select E.first_name, E.last_name, count(E.emp_id)
from employee as E left join registration as R
on R.Emp_ID = E.emp_id
group by E.emp_id;

-- solution 1
select E.first_name, E.last_name, 
sum(case 
	when R.Emp_ID is not null then 1 else 0
end) as course_count
from employee as E left join registration as R
on R.Emp_ID = E.emp_id
group by E.emp_id;

-- solution 2 (better than solution 1 for less memory consumption)
select E.first_name, E.last_name, count(R.Emp_ID)
from employee as E left join registration as R
on R.Emp_ID = E.emp_id
group by E.emp_id;
-- -----------------------------------------------------------------------------------------------------------------
-- 2 set operation

-- before the next example, add the following table
create table staff (
	staff_id int(5) not null default '10000',
    last_name varchar(20) default null, 
    first_name varchar(20) default null, 
    dept varchar(10) not null,
    salary int(10) not null default '0',
    hire_date date not null,
    primary key (staff_id)
); 

INSERT INTO staff VALUES
(329, 'w', 'z', 'Acctg', 65000, '2008-02-01'),
(21113, 'Li', 'Ping', 'Ops', 55000, '2008-09-01'); -- note that Li Ping is both a staff and an employee

-- 2.1 union
-- connect queries from two tables together
-- the retrieved items from both tables should be of the same data type, the columns in same order, and the same number of columns
-- in the following example, we want to union the employee table and the staff table
select last_name, first_name, dept from employee;
union
select last_name, first_name, dept from staff; -- please check that Li Ping is not repeated in the output

-- 2.2 intersect
-- What if we want the intersection between the two sets? such as Li Ping only
-- Note that the emp_id is not equal to the staff_id
-- but unfortunately, intersect command is not available as native command in MySQL community server.
select E.first_name, E.last_name
from employee as E inner join staff as S on E.first_name=S.first_name and E.last_name=S.last_name; -- here we cannot join by the id, because staff id and emp_id are different
-- -----------------------------------------------------------------------------------------------------------------
-- 3 subqueries

-- 3.1 subqueries in the where clause
-- the dictinct name of employees who has higher salary than the average salary
select distinct E.emp_id
from employee as E
where E.salary>
(select avg(salary) from employee);

select * from employee;

-- show the name of the course that is taken only once
-- method 1: not using subquery
select distinct C.course_name
from registration as R left join course as C on R.Training_Course=C.training_course
group by R.training_course
having count(R.training_course)=1;

select * from registration;
select * from course;

-- method 2: using subquery
select C.course_name
from course as C -- for each record in the course table, we check the following where clause
where (select count(R.training_course) from registration as R -- we don't have to load the course table from the where clause because it is loaded from the main query, passed down to the subquery 
where R.Training_Course=C.training_course
)=1; -- actually, for each course from the course table, we run such a subquery and check if the result is 1.

-- 3.2 subqueries in the select clause
-- check if all employee other than those in the sales department has salary greater than all employee in the sales department
select E.emp_id, E.last_name, E.first_name, E.dept, 
(case 
when E.salary>all(select salary from employee where employee.dept='sales') then "true" -- E.salary> all(subquery) will compare E.salary with all record in the subquery, and return True only when E.salary is greater than all records, The all operator only works for query outputs
else "false"
end) as torf -- the alias for this return field is named torf
from employee as E
where E.dept <>'sales'; -- the employ cannot be in the sales department

-- 3.3 subqueries in the from clause
-- show employee infor for those who studied 2 courses.
select *
from
(select E.*, count(*) as course_count
from employee as E inner join registration as R on E.emp_id=R.Emp_ID
group by E.emp_id) as derived  -- when the subquery itself is used as a table to query, we need to give it an alias
where derived.course_count=2;

-- Alternative
select E.*, count(*) as course_count
from employee as E inner join registration as R on E.emp_id=R.Emp_ID
group by E.emp_id  -- when the subquery itself is used as a table to query, we need to give it an alias
having course_count=2;


-- find the average salary of department with average salary greater than 60000
select department,avg_salary -- these two names are from the derived table
from (select E.dept as department, avg(E.salary) as avg_salary -- so in the derived table, you mush give them the same name
from employee as E
group by E.dept) as derived -- every derived table must have an alias
where derived.avg_salary>60000;

-- note that in the previous example we can rename the relation and the field name later 
select department,avg_salary
from (select E.dept, avg(E.salary) 
from employee as E
group by E.dept) as derived(department, avg_salary) -- we name the derived table and rename its field here
where derived.avg_salary>60000;

-- what is the maximum total salary expenditure among all departments?
select max(total_salary)
from (select E.dept, sum(E.salary)
from employee as E
group by E.dept) as derived(department, total_salary);

select max(total_salary)
from (select E.dept, sum(E.salary) as total_salary
from employee as E
group by E.dept) as derived;

-- 3.4 subqueries in other places

-- find department with the highest average salary
select E.dept
from employee as E
group by E.dept
having avg(E.salary) >= all(select avg(salary) from employee group by dept); -- after the group by, in the having statement, the avg(salary) is for each group, and if something is >=all(subquery), it is the highest. We cannot use the max here, because this is not a return field, but a subquery

-- -----------------------------------------------------------------------------------------------------------------
-- 4. over clause

-- using the employee training database
-- show a report that displays each employee's name and salary, 
-- also show in the same row the department average/max/min salary, and number of employees in the department

-- method 1, inner join the summary statics with the original table
select employee.first_name, employee.last_name, employee.salary,
summary.totalEmployees_in_dept, summary.avgSalary_in_dept, 
summary.maxSalary_in_dept, summary.minsalary_in_dept
from employee
inner join 
	(select dept, count(*) as totalEmployees_in_dept,
	avg(salary) as avgSalary_in_dept,
	max(salary) as maxSalary_in_dept,
	min(salary) as minSalary_in_dept
	from employee
	group by dept) as summary
on summary.dept = employee.dept;
    
-- method 2, using over clause
select employee.first_name, employee.last_name, employee.salary,
count(*) over (partition by dept) as totalEmployees_in_dept,
avg(salary) over (partition by dept) as avgSalary_in_dept,
max(salary) over (partition by dept) as maxSalary_in_dept,
min(salary) over (partition by dept) as minSalary_in_dept
from employee;
-- -----------------------------------------------------------------------------------------------------------------
-- 5 date related operations

-- the date
select emp_id
from employee
where hire_date between '2004-01-01' and '2006-01-01';

-- library function now
-- run line by line
select now();
select date(now());
select curdate();
select datediff('2018-01-01', (select now())); -- the number of days to a date
select datediff('2018-01-01', '2023-01-01'); 

-- check the following functions
select day(now());
select month(now());
select quarter(now());
select year(now());
select weekday(now());
select week(now());

-- the date_sub function used to calculate the date that an interval ago.
select date_sub(now(),interval 10 day);
select date_sub(now(),interval -10 day);
select unix_timestamp(date_sub(now(),interval -10 day)); -- this is the unix time

-- retrieve employee hired within 5000 days ago
select emp_id 
from employee
where hire_date<=(select date_sub(now(),interval 5000 day));

-- how many days have passed since the company last hire employees
select datediff(now(),(select min(hire_date) from employee));
-- -----------------------------------------------------------------------------------------------------------------
-- 6 views

-- 6.1 create view
-- MySQL Views are virtual tables generated by the query.
-- These Views are considered objects, so they can be easily queried by the SELECT statement. 
-- MySQL Views do not store the physical data on the database.
-- when you need a subquery repeated, you can save it as a view
-- it will show in the view section of a database (after refresh)

create view employeehireyear as
select employee.emp_id, employee.first_name, employee.last_name,year(employee.hire_date) as recently_hired_year
from employee;

-- then you can write queries using the view
select * from employeehireyear;
select max(recently_hired_year)
from employeehireyear;

select max(recently_hired_year) as new
from employeehireyear;

-- delete view
drop view employeehireyear;

-- once a view is created, you cannot create the same view
-- but you can change it using the wrench icon 
-- you can also use the create the replace key word
create or replace view employeehireyear as
select employee.emp_id,employee.first_name, employee.last_name, substring(year(employee.hire_date), 3,4) -- only the last two digit of the year
from employee;

select * from employeehireyear;

-- 6.2 example: using views for one of our previous questions
-- show employee infor for those who studied 2 courses.
-- step 1: create a view showing the number of courses taken by each employee
create view n_courses as 
select employee.emp_id, count(*) as n_course
from employee, registration
where employee.emp_id = registration.Emp_ID
group by employee.emp_id;

select * from n_courses;

-- step 2: select those who taking at least two courses
select emp_id from n_courses
where n_course = 2;
-- -----------------------------------------------------------------------------------------------------------------
-- 7 procedures

-- a procedure is a program (a query) that can be called to quickly get a result
-- you can make frequently used queries procedures

-- 7.1 procedure with no parameters
-- note: you need to create the procedure in a separate query script
delimiter //-- define procedure delimiter
-- semicolon is used to separate each sql statement, 
-- but a procedure may contain multiple statements, 
-- so we define a different delimiter to recognize a complete procedure

-- create a procedure, when called, outputs a list of of senior employees who have been working for over 15 years 
delimiter //
create procedure displaysenioremployee()
	begin 
		set @senioryear = 15; -- statement 1
		select * from employee 
        where datediff((select now()), employee.hire_date)/365 >= @senioryear; -- statement 2 
	end//
-- you can directly run the procedure by clicking the lightning button next to the procedure 
-- or you can call the procedure in SQL, such as
call employeetraining.displaysenioremployee();
-- this procedure doesnot require any parameters

-- 7.2 procedure with parameters
delimiter //
-- the number of year threshold becomes an input
create procedure displaysenioremployee(in threshold int) -- input is threshold, which is an integer
	begin 
		select * from employee 
        where datediff((select now()), employee.hire_date)/365 >= threshold;
	end//
-- when you run this using the lightning button, a input request will pop up to prompt the input
-- if you run using call, need to do this
call employeetraining.displaysenioremployee(15);

-- 7.3 drop procedure
drop procedure displaysenioremployee;

-- 7.4 example: using procedure for one of our previous questions
-- show employee infor for those who studied 2 courses.
-- step 1 create a procedure to get the number of courses taken by each employee
delimiter //
create procedure n_courses()
	begin 
		select employee.emp_id, 
        sum(case when registration.Training_Course is not null then 1 else 0 end) as n_course 
        from employee left join registration on employee.emp_id = registration.Emp_ID
        group by employee.emp_id;
	end//
-- can we do this?
select emp_id from call employeetraining.n_courses()
where n_course = 2

call employeetraining.n_courses()
-- no, we cannot call procedure in query. Procedure can be seen as fixed and shortened sql programs
-- -----------------------------------------------------------------------------------------------------------------
-- 8 function

-- 8.1 create a function that tell if an employee is senior or junior
-- input is the year hired
-- output is senor or not
-- if worked more than 15 years, then senior, otherwise, junior

delimiter //
create function employeelevel (
	yearhired date, -- the input is yearhired, which is a date type input
    threshold int
)
returns varchar(20)
deterministic
begin
	declare emplevel varchar(20);
    if (datediff((select now()), yearhired)/365)>=threshold then
		set emplevel = "senior";
	else
		set emplevel = "junior";
	end if;
    return (emplevel);
end//

-- call the function
select employeetraining.employeelevel('2001-01-01',15); -- will return "senior"

-- 8.2 use function in a query
-- get a list of senior employees (i.e., those who worked more than 15 years)
select * from employee
where employeetraining.employeelevel(employee.hire_date, 15) = "senior";

-- 8.3 use function in a procedure
-- define a procedure to count the number of seniors
delimiter //
create procedure count_senior(in threshold int)
	begin 
		select count(*) from employee 
        where employeetraining.employeelevel(employee.hire_date, threshold) = "senior";
	end//
call employeetraining.count_senior(15);

-- 8.4 example: using function for one of our previous questions
-- show employee infor for those who studied 2 courses.
-- step 1 create a function to return the number of courses taken by employee given emp_id
delimiter //
create function n_course (
	id int
)
returns boolean -- return type is true or false, a boolean
deterministic
begin
	declare res boolean; -- declare return variable
    if (select n_course from n_courses where emp_id = id) = 2 then -- the subquery uses a view "n_courses" created in section 6.2 
		set res = true;
	else
		set res = false;
	end if;
    return (res);
end//
-- step 2: use the function in the query
select * from employee
where employeetraining.n_course(employee.emp_id) = true;

-- 8.4 important notes
-- 1. functions can be called by a procedure or within a query
-- 2. a procedure cannot be called within a query because itself is a set of predefined querie
-- -----------------------------------------------------------------------------------------------------------------
-- 9 some practices

-- count the number of students in each department
select Stu_Dep, count(*) from student as n_student
group by Stu_Dep;

-- which book title has the most copies in the library?
select copy.Book_ISBN, count(*) as n_copies 
from copy
group by copy.Book_ISBN
order by n_copies desc
limit 1;

-- generate a list of student for those who ever return book within 30 days of due date.
select distinct Stu_ID 
from loan
where loan.Due_Date-loan.Return_Date<30;

select * from loan;

-- what is the number of books borrowed by each student?
select Stu_ID, count(*) as n_books_borrowed
from loan
group by Stu_ID;

-- show the number of chemistry books borrowed by each student
select student.Stu_ID,student.Stu_Name,count(*)
from student,loan,copy,book
where student.Stu_ID=loan.Stu_ID
and loan.Book_Call_No=copy.Book_Call_No
and copy.Book_ISBN=book.Book_ISBN
and book.Book_Title in ("Basic Chemistry","Advanced Chemistry")
group by student.Stu_ID;

-- generate a list of student who have borrowed the book game theory
select distinct S.Stu_ID
from loan as L, copy as C, book as B, student as S
where S.Stu_ID=L.Stu_ID and L.Book_Call_No=C.Book_Call_No and C.Book_ISBN=B.Book_ISBN
and B.Book_Title='Game Theory';

-- extract the duration of the book borrow for each Borrow_ID
select L.Borrow_ID, datediff(L.Due_Date, L.Borrow_date) as duration
from loan as L;

-- calcuate the percentage of students who have ever return the book exactly on the due date
select(
	(select count(distinct L.Stu_ID)
	from loan as L
	where L.Due_Date=L.Return_Date)
    /
    (select count(*) from student)) as pct_of_return_on_time;
    
   
	select count(distinct case when L.Due_Date=L.Return_Date then L.Stu_ID else null end)/count(distinct S.Stu_ID)
	from student S
    left join loan L
    on S.Stu_ID=L.Stu_ID
	
-- calcuate the percentage of the book titles that has some copies borrowed before 2012 but still on the loan
-- still not returned means that the return date is 1900/01/01
select count(distinct C.Book_ISBN)/(select count(*) from book) as proportion
from loan as L, copy as C
where L.Book_Call_No=C.Book_Call_No
and L.Return_Date='1900/01/01' and L.Borrow_Date<='2012/01/01';

-- extract the books call no of the books which are returned on a Saturday.
-- the weekday function: 0 is Monday, 6 is Sunday.
select L.Borrow_ID
from loan as L
where weekday(L.Return_Date)=5;

-- count the number of students who have ever borrowed any books for each department
select S.Stu_Dep, count(distinct S.Stu_ID) 
from loan as L left join student as S on L.Stu_ID=S.Stu_ID
group by S.Stu_Dep;

-- generate a list of unique student in the Econ department who borrowed earlier than all students in the MGT department
select distinct S.Stu_ID,S.Stu_Dep
from student as S, loan as L
where S.Stu_Dep='ECON'
and S.Stu_ID=L.Stu_ID
and L.Borrow_Date<all(select Borrow_Date from loan, student where loan.Stu_ID=student.Stu_ID and student.Stu_Dep='MGT');


select distinct S.Stu_ID,S.Stu_Dep
from student as S, loan as L
where S.Stu_Dep='ECON'
and S.Stu_ID=L.Stu_ID
and L.Borrow_Date<(select min(Borrow_Date) from loan, student where loan.Stu_ID=student.Stu_ID and student.Stu_Dep='MGT');


-- calculate the number of chemistry book borrowed by each students.
select S.Stu_ID, sum(case when B.Book_Title='Basic Chemistry' then 1 else 0 end) as num_chem
from student as S, loan as L, copy as C, book as B
where S.Stu_ID=L.Stu_ID and L.Book_Call_No=C.Book_Call_No and C.Book_ISBN=B.Book_ISBN
group by S.Stu_ID

-- define a procedure, given an integer n, it returns the top n unique salarys
delimiter //
create procedure top_n_salary(in n int)
	begin 
		select distinct salary from employee 
        order by salary desc
        limit n;
	end//

call top_n_salary(2)