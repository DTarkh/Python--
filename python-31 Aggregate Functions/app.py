# წინა დავალებაში შექმნილ ცხრილებზე გამოიტანეთ ინფორმაციები ჯოინების გამოყენებით:
#
#
# 1. ინფორმაცია თანამშრომლების შესახებ, რომელსაც არ აქვს მითითებული ქალაქი
#
# 2. ყველა ქალაქი და მათი შესაბამისი ველები თანამშრომლების ცხრილიდან(null ჩათვლით)
#
# 3 სრულყოფილი ინფორმაცია თანამშრომლების შესახებ
#
#
#
#
#
# აგრეგატული ფუნქციები
#
#
# 1. შექმენით ცხრილი Customers შემდეგი სვეტებით:
#
# 	CustomerID (Primary Key)
# 	FullName (Varchar)
# 	Email (Varchar)
# 	Phone (Varchar)
#
#
# 2. შექმენით ცხრილი Sales შემდეგი სვეტებით:
#
# 	SaleID (Primary Key)
# 	CustomerID (Int, Foreign Key References Customers.CustomerID)
# 	ProductName (Varchar)
# 	Quantity (Float)
# 	UnitPrice (Float)
# 	SaleDate (Timestamp)
#
# 3. შეავსეთ Customer ცხრილი 6-7 ჩანაწერით (ყველა სვეტი)
#
# 4. შეავსეთ Sales ცხრილი 6-7 ჩანაწერით (ყველა სვეტი)
#




# 5. გამოთვალეთ გაყიდვების სრული თანხა, გამოიტანეთ სახელით TotalRevenue
#
# 6. გამოთვალეთ გაყიდული რაოდენობის საშუალო, სახელით AvarageSales
#
# 7. გამოიტანეთ მომხმარებელი და მისი გაყიდვები ერთად, მომხმარებლები რომელთაც გაყიდვები აქვთ
#
# 8. გამოიტანეთ მომხმარებელი და მისი გაყიდვები ერთად, მომხმარებლები რომელთაც გაყიდვები არ აქვთ
#
# 9. გამოიტანეთ გაყიდული პროდუქტი თავისი რაოდენობით, დააჯგუფეთ პროდუქტის სახელით
#
# 10. გამოიტანეთ მომხმარებელი და მისი სრული გაყიდვები, დააჯგუფეთ მომხმარებლის სახელის მიხედვით
#
