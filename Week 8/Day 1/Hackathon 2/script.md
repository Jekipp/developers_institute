select * from actors
select count(first_name) from actors
select count(first_name) as nb_rows from actors


number of rows of who has more than 3 oscars
select first_name from actors where number_oscars < 3;
select max(number_oscars) from actors;

select first_name from actors where select min(age) from actors = age

select * from actors order by asc limit 1
select * from actors order by dsc limit 1

select first_name from actors
where age = max (number_oscars)

select count( * ) nb_actors, sum(number_oscars) sum_oscars,
avg(number_oscars) avg_oscars, max(number_oscars) max_oscars
from actors
where number_oscars > 3


select distinct first_name from actors

group by
