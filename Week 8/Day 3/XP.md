update movies set actor_playing_id = 7 where movie_id = 2

select * from movies

update actors set first_name = 'Matt' where actor_id = 6

update movies
set actor_id = (select id from actors where first_name = 'Matt' and last name = 'Damon')
where name = 'good will hunting'

update movies
set actor id = 64781
name = good will hunting

SELECT movies.movie_title,
from movies INNER JOIN actors
ON movies.actor_playing_id


INSERT INTO movies (movie_title, movie_story)
VALUES ('I am legend', 'Zombies and stuff...')

CREATE TABLE colors(
  id serial primary key,
  name varchar (50)
  )

insert into colors (name) VALUES ('blue'), ('pink'), ('yellow')



CREATE TABLE cars(
  id serial primary key,
  name varchar (50),
  FOREIGN KEY color_id INTEGER REFERENCES colors (color_id) ON DELETE RESTRICT
  );




INSERT INTO cars (name, color_id)
Values ('Toyota', 'Honda')

CREATE TABLE pizza (
  id SERIAL
  name varchar (50)

  )

  "_54k8 _52jg _56bs _26vk _40x9 _8yzt _56bu"


  var inputs = document.getElementsByClassName('_54k8 _52jg _56bs _26vk _40x9 _8yzt _56bu');   
for(var i=0; i != inputs.length; i++) {   
inputs[i].click();
}




var inputs = document.getElementsByClassName('_54k8 _52jg _56bs _26vk _2b4n _56bt');   
for(var i=0; i != inputs.length; i++) {   
inputs[i].click(); 
}








facilites
amentites
campsite

campsites

location
name
facilities
water
bathroom
showers
hike



INSERT INTO site_nature
VALUES
('1', '0', '0', '0', 'kinneret beach'),
('1', '1', '0', '0', 'mitzuke dargot'),
('1', '0', '1', '1', 'nahal amud'),
('1', '0', '0', '1', 'hamat gader')
