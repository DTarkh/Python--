# 1. შექმენით ცხრილი დეპოზიტების უწყისისთვის, დაარქვით Deposits და განსაზღვრეთ მასში შემდეგი სვეტები:
#
# •	DepositID
# •	DepOwnerName
# •	DateOfBirth
# •	City
# •	StreetName
# •	DepositAmount
# •	Interest
# •	Comission
# •	Total

# 2. სვეტების მონაცემთა ტიპები განსაზღვრეთ ლოგიკურად

# 3. შეავსეთ ცხრილი ინფორმაციით 2-3 დეპოზიტორის შესახებ (სვეტები DevOpOwner, DateOfBirth, City, StreetName)

# 4. შეავსეთ ცხრილი ინფორმაციით 5-6 დეპოზიტორის შესახებ (სვეტები DepOwnerName, DateOfBirth, DepositAmount, Comission, Total)

# 5. გამოიტანეთ აბსოლუტურად ყველა დეპოზიტორი

# 6. გამოიტანეთ ყველა ის დეპოზიტორი, რომლის დეპოზიტიც არის 1500-ზე მეტი

# 7. გამოიტანეთ ყველა ის დეპოზიტორი, რომელიც ცხოვრობს თბილისში რუსთაველის ქუჩაზე

# 8. გამოიტანეთ ყველა ის დეპოზიტორი, რომელიც ცხოვრობს ბათუმში, გორგასალიზ ქუჩაზე, დეპოზიტი აქვთ 1000-ზე მეტი და 2000-ზე ნაკლები

# 9. გამოიტანეთ ყველა ის დეპოზიტორი რომლის სახელიც იწყება ასო “დ”-ზე


#


create table Deposits(
    DepositID integer primary key not null,
    DepOwnerName varchar(20),
    DateOfBirth date,
    City varchar(20),
    StreetName varchar(50),
    DepositAmount float,
    Interest float,
    Commision float,
    Total float,
)


insert into Deposits(DepositID, DepOWnerName, DateOfBirth, City, StreetName) values('1', 'John Doe', '1992-10-23', 'Tbilisi', 'Khizanishvili')
insert into Deposits(DepositID, DepOWnerName, DateOfBirth, City, StreetName) values('2', 'Jahne Doe', '1993-10-23', 'Tbilisi', 'Khizanishvili')
insert into Deposits(DepositID, DepOWnerName, DateOfBirth, City, StreetName) values('3', 'David Tarkh', '1991-10-23', 'Tbilisi', 'Khizanishvili')

insert into Deposits(DepositId, DepOwnerName, DateOfBirth, DepositAmount, Commision, Total) values(4,'Tamar Tarkh', '1986-01-11', '4000', '33', '3570')
insert into Deposits(DepositId, DepOwnerName, DateOfBirth, DepositAmount, Commision, Total) values(5,'Brad Pitt', '1976-01-11', '14000', '330', '35700')
insert into Deposits(DepositId, DepOwnerName, DateOfBirth, DepositAmount, Commision, Total) values(6,'Johny Depp', '1966-01-11', '400000', '1133', '13570')
insert into Deposits(DepositId, DepOwnerName, DateOfBirth, DepositAmount, Commision, Total) values(7,'Adam Jhones', '1925-01-11', '234000', '233', '33570')
insert into Deposits(DepositId, DepOwnerName, DateOfBirth, DepositAmount, Commision, Total) values(8,'Tom Marks', '1965-01-23', '104000', '333', '43570')
insert into Deposits(DepositId, DepOwnerName, DateOfBirth, DepositAmount, Commision, Total) values(9,'Adam Jhones', '1980-01-11', '404000', '633', '53570')



#
# select * from deposits
# select * from deposits where depositamount > 1500
# select * from deposits where city = 'Tbilisi' and streetname = 'Rustaveli'
# select * from deposits where city = 'Batumi' and streetname = 'Gorgasali street' and depositamount > 1000 and depositamount < 2000
# select * from deposits where depownername like 'C%'



