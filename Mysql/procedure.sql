select * from cs_dpt_list;
use ai_saravanan;

delimiter ##
drop procedure if exists insert_into;##
create procedure insert_into
( in s_noparam int,
in nameparam varchar(50),
in ageparam int,
in genderparam varchar(50),
in date_of_birthparam date,
in ph_noparam long,
in mark_pctparam varchar(5))
begin 
insert into cs_dpt_list(s_no,name,age,gender,date_of_birth,ph_no,mark_pct)
value(s_noparam,nameparam,ageparam,genderparam,date_of_birthparam,ph_noparam,mark_pctparam);
end ##
delimiter ;

call insert_into(8,'Elanilaa',20,'Female','2004-02-03',8525843264,'98%');

delimiter ##
drop procedure if exists value_updates;##
create procedure value_updates
(in tablename varchar(50),
in columnname varchar(50),
in valuechange varchar(50),
in idname varchar(50),
in id int)
begin 
set @updatestatement=concat(' update ' , tablename ,' set ', columnname ,' =  \' ', valuechange ,' \'',' where ' , idname ,'=',id);
prepare stmt from @updatestatement;
execute stmt;
end ##
delimiter ;

call value_updates('cs_dpt_list','gender','Female','s_no',7);

call sa();


delimiter ##
drop procedure if exists delete_value;##
create procedure delete_value
(in tablename varchar(50),
in idname varchar(50),
in id int)
begin 
set @statement=concat(' delete from ' , tablename , ' where ' , idname ,' = ',id);
prepare stmt from @statement;
execute stmt;
end ##
delimiter ;

call delete_value('cs_dpt_list','s_no',8);



delimiter ##
drop procedure if exists add_column;##
create procedure add_column(
in tablename varchar(75),
in columnname varchar(75)
)
begin
set @Statement =  concat( 'alter table ',tablename,' add column ',columnname,'varchar(50)');
prepare stmts from @Statement;
execute stmts;

end ##
delimiter ;

call drop_value1('cs_dpt_list','Attendance_parce');