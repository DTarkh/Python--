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
#
# select * from deposits
# select * from deposits where depositamount > 1500
# select * from deposits where city = 'Tbilisi' and streetname = 'Rustaveli'
# select * from deposits where city = 'Batumi' and streetname = 'Gorgasali street' and depositamount > 1000 and depositamount < 2000
# select * from deposits where depownername like 'C%'



