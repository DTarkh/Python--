import psycopg2


host = 'localhost'
port = 5432
database = 'Book\'s Store'
user = 'postgres'
password = '9919'


connection = psycopg2.connect(host=host, port=port, database=database, user=user, password=password)
print('Connection established')


cursor = connection.cursor()


class Book:


    def __init__(self):
        self.connection = connection
        self.cursor = self.connection.cursor()

    def create_books_table(self):
        create_table_query = '''
           CREATE TABLE IF NOT EXISTS books (
               title VARCHAR(100),
               author VARCHAR(100),
               release_year INT,
               isbn INT PRIMARY KEY
           )
           '''
        self.cursor.execute(create_table_query)
        self.connection.commit()
        print("Table 'books' created successfully")



    def add_book(self, title, author, release_year, isbn):
        query = '''
        insert into books (title, author, release_year, isbn)
        values (%s, %s, %s, %s)
        '''

        values = (title, author, release_year, isbn)
        self.cursor.execute(query, values)
        self.connection.commit()
        print(f'Book "{title}" added successfully')


    def get_books(self):
        query = '''
            select * from books
        '''

        cursor.execute(query)
        print(cursor.fetchall())



    def find_book(self, isbn):
        query = '''
            select * from books where isbn=%s
        '''
        value = (isbn, )
        cursor.execute(query, value)
        # print(cursor.fetchone())

        found_book = cursor.fetchone()
        if found_book:
            print(f"found {found_book}")
            return found_book
        else:
            print("Book not found")
            return None



    def update_book(self, title, author, release_year, isbn):
        query = '''
            update books set title = %s, author = %s, release_year = %s, isbn = %s
        '''
        values = (title, author, release_year, isbn)
        cursor.execute(query, values)
        connection.commit()
        print(f'Updated successfully')

    def delete_book(self, isbn):

        query = '''
            delete from books where isbn = %s
        '''
        values = (isbn,)
        cursor.execute(query, values)
        connection.commit()

        if cursor.rowcount > 0:
            connection.commit()
            print(f'Book with ISBN {isbn} was deleted successfully')
        else:
            print(f'Book with ISBN {isbn} not found')




new_table = Book()
# new_table.create_books_table()
# new_table.add_book('Dune', 'Frank Herbert', 1962, 2234)
new_table.add_book('Star Wars', 'George Lucas', 1960, 1032)
# new_table.get_books()
# new_table.find_book('1032')
# new_table.update_book('Dune', 'Frank Herbert', 1957, 2234)
# new_table.delete_book('1032')