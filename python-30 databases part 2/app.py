#
# # გადაანაწილეთ ცხრილებში მონაცემები, გამოიყენეთ ექსელის ფაილი,
# # აღწერეთ ცხრილები ამავე ექსელის ფაილში და თითოეული ცხრილი
# # გადაიტანეთ მონაცემთა ბაზაში, დაამატეთ შესაბამისი შეზღუდვები
# # და შეიყვანეთ გარკვეული ინფორმაცია თითოეულ ცხრილში
#
#
#
# create table newemployee(
#     employeeid integer not null,
#     firstname varchar(20),
#     lastname varchar(20) not null,
#     departmentid integer not null,
#     cityid integer not null,
#     bankabr varchar(5) not null
# )
#
#
# alter table newemployee add constraint cityidfk foreign key (cityid) references cities(cityid);
# alter table newemployee add constraint bankabrfk foreign key (bankabr) references banks(bankabr);
# alter table newemployee add constraint departmentidfk foreign key (departmentid) references departments(departmentid);
# alter table newemployee add constraint employeeidfk foreign key (employeeid) references employeeids(employeeid);
#
#
# create table cities(
#     cityid serial primary key,
#     cityname varchar(20)
# )
#
# create table employeeids(
#     employeeid serial primary key,
#     idnumber integer
# )
#
# alter table employeeids add constraint uniqueemployeeid unique (employeeid)
#
# create table banks(
#     bankabr varchar(5),
#     bankname varchar(20)
# )
#
# alter table banks add constraint uniquebankabbreviation unique (bankabr)
#
# create table departments(
#     departmentid serial primary key,
#     departmentname varchar(20)
# )
#
# insert into cities(cityname) values ('Tbilisi'), ('Batumi'), ('Kutaisi'), ('Telave'), ('Zugdiid')
# insert into departments(departmentid) values ('1'), ('2'), ('3'), ('4'), ('5')
# insert into employeeids(employeeid) values ('1'), ('2'), ('3'), ('4'), ('5')
# insert into banks(bankabr, bankname) values ('TBC', 'TBC Bank'), ('Bog', 'Bank of Georgia'), ('rico', 'Rico Credit'), ('Halyk', 'Halyk Bank'), ('MBC', 'Business Capital')
# insert into employeeids(employeeid) values ('1'),('2'), ('3'), ('4'), ('5')
#
# insert into newemployee(employeeid, lastname, departmentid, cityid, bankabr) values ('1', 'Doe', 2, 2, 'TBC' )
