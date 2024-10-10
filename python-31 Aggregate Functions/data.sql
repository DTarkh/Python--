

select * from newemployee where cityid is null

select cityname, employeeid, firstname, lastname, departmentid, bankabr from newemployee right join cities on newemployee.cityid = cities.cityid

select firstname, lastname, cityname, idnumber,  departmentname, bankname from newemployee
        left join cities on newemployee.cityid = cities.cityid
        left join employeeids on newemployee.employeeid = employeeids.employeeid
        left join departments on newemployee.departmentid = departments. departmentid
        left join banks on newemployee.bankabr = banks.bankabr
group by firstname, lastname, cityname, idnumber,  departmentname, bankname

create table Customers(
    CustomerID serial primary Key,
    FullName Varchar(30),
    Email Varchar,
	Phone Varchar
    )

insert into Customers(CustomerID, FullName, Email, Phone) values ('1234', 'John Doe', 'dawdw@gmail.com', '995 5343432' )
insert into Customers(CustomerID, FullName, Email, Phone) values ('1233', 'Greg Martin', 'dfefwdw@gmail.com', '995343432' )
insert into Customers(CustomerID, FullName, Email, Phone) values ('12353', 'James Smith', 'ffffawdw@gmail.com', '995 111432' )
insert into Customers(CustomerID, FullName, Email, Phone) values ('13334', 'Brad Pitt', 'da334wdw@gmail.com', '995 544432' )
insert into Customers(CustomerID, FullName, Email, Phone) values ('111234', 'Johny Depp', 'dawvee4dw@gmail.com', '995 566732' )
insert into Customers(CustomerID, FullName, Email, Phone) values ('14647734', 'Christian Bale', 'eeee4@gmail.com', '995 5333332' )

create table Sales
(
    SaleID      serial primary Key,
    CustomerID  Int,
--     Foreign Key References Customers.CustomerID)
    ProductName Varchar,
    Quantity    Float,
    UnitPrice   Float,
    SaleDate    Timestamp
)



insert into Sales(SaleID, CustomerID, ProductName, Quantity, UnitPrice, SaleDate) values ('22', '1234', 'Shoes', '1', '40.2', '12.04.2024')
insert into Sales(SaleID, CustomerID, ProductName, Quantity, UnitPrice, SaleDate) values ('23', '1233', 'umbrella', '2', '44', '11.04.2024')
insert into Sales(SaleID, CustomerID, ProductName, Quantity, UnitPrice, SaleDate) values ('24', '12353', 'shelf', '3', '47', '10.04.2024')
insert into Sales(SaleID, CustomerID, ProductName, Quantity, UnitPrice, SaleDate) values ('25', '13334', 'table', '5', '50.5', '09.04.2024')
insert into Sales(SaleID, CustomerID, ProductName, Quantity, UnitPrice, SaleDate) values ('26', '111234', 'chair', '20', '60.2', '08.04.2024')
insert into Sales(SaleID, CustomerID, ProductName, Quantity, UnitPrice, SaleDate) values ('27', '14647734', 'stocks', '100', '80', '04.04.2024')

alter table Sales add constraint customeridfk foreign key (customerid) references Customers(customerid)


-- 5. გამოთვალეთ გაყიდვების სრული თანხა, გამოიტანეთ სახელით TotalRevenue
select sum(UnitPrice) as TotalRevenue from sales

-- 6. გამოთვალეთ გაყიდული რაოდენობის საშუალო, სახელით AvarageSales

select avg(UnitPrice) as AverageSales from sales

-- 7. გამოიტანეთ მომხმარებელი და მისი გაყიდვები ერთად, მომხმარებლები რომელთაც გაყიდვები აქვთ

select Customers.customerid, fullname, productname, quantity from customers left join sales on customers.customerid = sales.customerid

-- 8. გამოიტანეთ მომხმარებელი და მისი გაყიდვები ერთად, მომხმარებლები რომელთაც გაყიდვები არ აქვთ



-- 9. გამოიტანეთ გაყიდული პროდუქტი თავისი რაოდენობით, დააჯგუფეთ პროდუქტის სახელით\

select ProductName, quantity from sales group by ProductName, quantity

-- 10. გამოიტანეთ მომხმარებელი და მისი სრული გაყიდვები, დააჯგუფეთ მომხმარებლის სახელის მიხედვით

select fullName, productname from Customers left join sales on customers.CustomerID = sales.CustomerID group by  fullName, productname
