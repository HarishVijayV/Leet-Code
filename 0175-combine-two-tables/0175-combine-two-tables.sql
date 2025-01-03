-- Write your PostgreSQL query statement below
select firstName, lastName, city, state FROM person left join Address on person.personId=Address.personId