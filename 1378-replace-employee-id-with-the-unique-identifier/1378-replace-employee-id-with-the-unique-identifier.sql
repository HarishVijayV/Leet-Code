# Write your MySQL query statement below
select s.id as unique_id , e.name from Employee e left join Employees s where e.id=s.unique_id