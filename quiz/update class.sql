-- SQLite
UPDATE auth_user 
set last_name="Not Updated"
where last_name is not null; 