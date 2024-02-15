select * from flight;

select * from flyer;

select * from trip;

-- 1.List all flights (Flight_no) for those that leaves HOU or SFO

select 
      Flight_no 
from flight
where Flight_Origin in('HOU','SFO');

-- 2.Generate a list of all information about the frequently flyer whose first name starts with “D”.

select *
from flyer
where Flyer_Name like '%, D.';

-- 3.Generate a list of all flight operators, along with the number of flights of each operator, 
-- and its average miles per flight. Order the output by the average miles per flight in descending order.

select Flight_operator,
	   count(Flight_operator) as Number_of_flights,
       sum(Miles_per_flight) / count(Flight_operator) as Average_miles_per_flight
from  flight
group by Flight_operator
order by Average_miles_per_flight desc;
	   
-- 4.For each Flight_operator, calculate the number of trips commissioned by it with a fare greater than $300.	
    
select Flight_operator,
	   count(Flight_fare) as Trips_greater_than_300
from flight
join trip
on flight.Flight_no = trip.Flight_no
where Flight_fare > 300
group by Flight_operator;

-- 5.List the names of the flyers who ever went to Atlanta

select Flyer_Name
from flyer
join trip
on flyer.Frequent_Flyer_ID = trip.Frequent_Flyer_ID
join flight
on trip.Flight_no = flight.Flight_no
where Flight_Destination = 'ATL';
    
-- 6.Identify all the possible round trips from the flight table (e.g., there is an A to B trip and a B to A trip available). 
-- List the Flight_no, the origin, and the destination.

select f1.Flight_no,
	   f1.Flight_Origin,
       f1.Flight_Destination
from flight f1
join flight f2
on f1.Flight_Origin = f2.Flight_Destination
and f1.Flight_Destination = f2.Flight_Origin
and f1.Flight_no < f2.Flight_no;

-- 7.What is the most visited flight destination?
-- In case of a tie, list all of them.

select Flight_Destination
from flight
group by Flight_Destination
having count(*) = (select count(*)
			       from flight
				   group by Flight_Destination
                   order by count(*) DESC
                   limit 1);
            
-- 8.Extract the most popular author in the university (borrowed the most often by students)
-- In case of a tie, list all of them

select Book_First_Author
from book
join copy
on book.Book_ISBN = copy.Book_ISBN
join loan
on copy.Book_Call_No = loan.Book_Call_No
group by Book_First_Author
having count(*) = (select count(*)
			       from loan
				   group by Book_Call_No
                   order by count(*) DESC
                   limit 1);

-- 9.Use the loan table, for each student, calculate the total payment due for all books he/she borrowed. 
-- Assume that the university charges $0.1 per book per day for book loans.

select student.Stu_ID, 
       student.Stu_Name, 
       sum(datediff(loan.Due_Date,loan.Return_Date) * 0.1) as Payment_Due
from student
join loan
on student.Stu_ID = loan.Stu_ID
where loan.Due_Date > loan.Return_Date
group by student.Stu_ID,student.Stu_Name;

								



    