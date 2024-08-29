import sqlite3 as s
import getpass


# Module describes internet store


EXIT_MSG = ('''
             |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
             |||                        SEE YA!                      |||
             |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
            ''')
ABOUT_MSG = 'Internet Store. Use this program to make your purchases.'


class Internet_Store:
    '''Class describes Internet Store.'''
    
    def __init__(self) -> None:
        self.conn = s.connect('internet_store.db')
        self.c = self.conn.cursor()
        
    def add_product(self):
        '''Method addes product in list.''' 
        self.name = input('Enter product name: ')
        self.description = input('Enter product description: ')
        self.price = input('Enter product price: ')
        self.c.execute('INSERT INTO goods (name, description, price, status) VALUES (?, ?, ?, ?)',
                       (self.name, self.description, self.price, 1))
        self.conn.commit()
        self.conn.close()
        print(f'Product was added: {self.name}')
        
    def delete_product(self):
        '''Method deletes product from list by article.'''
        article = input('Enter product article: ')
        self.c.execute('DELETE FROM goods WHERE article = ?', (article,))
        self.conn.commit()
        self.conn.close()
        print(f'Product #{article} was deleted successfully.')

    def show_product_list_for_manager(self):
        '''Method shows list of products (all products).'''
        self.c.execute('SELECT * from goods')
        self.rows = self.c.fetchall()
        for row in self.rows:
            print(row)
        self.conn.close()
        
    def show_product_list_for_user(self):
        '''Method shows list of products (all available products for users).'''
        self.c.execute('SELECT * from goods WHERE status = 1')
        self.rows = self.c.fetchall()
        for row in self.rows:
            print(row[:4])  # Cut status for users.
        self.conn.close()

    def sell_product(self):
        '''Method for selling goods (sell product). 
        To sell product change status to 2.'''
        article = input('Enter product article: ')
        self.c.execute('UPDATE goods SET status = 2 WHERE article = ?', (article))
        self.conn.commit()
        self.conn.close()
        print(f'Product #{article} was sold.')
        
    def find_product_by_name(self) -> tuple:
        '''Method helps find product in list by name.'''
        name = input('Please input product name: ')
        self.c.execute('SELECT * FROM goods WHERE name = ?', name)
        self.row = self.c.fetchall()
        return self.row
        
    def find_product_by_article(self) -> tuple:
        '''Method helps find product in list by article(id).'''
        article = input('Please input product article: ')
        self.c.execute('SELECT * FROM goods WHERE article = ?', article)
        self.row = self.c.fetchall()
        return self.row


class Product(Internet_Store):
    '''Class describes product.'''
    pass
    '''TODO: 6 - change product price
             7 - change product status
             8 - change product name
             9 - change product description
             '''


class Store_Users_Admin:
    '''Class for manage users.'''

    def __init__(self) -> None:
        self.conn = s.connect('internet_store.db')
        self.c = self.conn.cursor()
        
    def add_user(self, user_name, user_role, user_pass):
        '''Method addes user in DB. Accept 3 args name, role, pass'''
        self.c.execute('INSERT INTO users (user_name, user_role, user_pass) VALUES (?, ?, ?)',
                       (user_name, user_role, user_pass))
        self.conn.commit()
        self.conn.close()
        print(f'User was added: {user_name}')
    
    '''TODO:
    2 - del user
    3 - block user
    4 - upd user pass
    5 - show all users
    '''


class App:
    '''Class for starting application.'''
    def __init__(self) -> None:
        self.cond = True

    def Run(self):
        print(ABOUT_MSG)
        while self.cond:
            print(
                '''MENU:
1 - Sign in
2 - Register user
3 - About Store
0 - Exit'''
            )
            user_operation = input("Input operation: ")
            
            if user_operation == "1":
                user_name = input("Enter user name: ")
                user_pass = getpass.getpass("Enter user password: ")
                
                
                conn = s.connect('internet_store.db')
                c = conn.cursor()
                c.execute('SELECT user_role from users where user_name = ? and user_pass = ?',
                          (user_name, user_pass))
                result_of_select = c.fetchall()
                
                
                if result_of_select == []:
                    print('USER NOT FOUND or password is incorrect.')
                
                # ADMIN MENU.
                elif result_of_select[0] == (0,):  # обернуть в цикл while
                    print(
                '''ADMIN MENU: 
1 - add user
2 - del user
3 - block user
4 - upd user pass
5 - show all users
0 - Exit'''
                    )
                    user_operation = input("Input operation: ")
                    if user_operation == '1':
                        print("ADD USER")
                        user_name = input('Enter user name: ')
                        print('''User roles description:
0 - admin
1 - manager
2 - user
3 - blocked user'''
)
                        user_role = input('Enter user role (0-1-2-3): ')
                        user_pass = getpass.getpass("Enter user password: ")
                        Store_Users_Admin().add_user(user_name, user_role, user_pass)
                    elif user_operation == '2':
                        print('del user')
                    elif user_operation == '3':
                        print("block user")
                    elif user_operation == '4':
                        print('upd user pass')
                    elif user_operation == '5':
                        print('all users')
                    elif user_operation == "0":
                        self.cond = False
                        conn.close()
                        print(EXIT_MSG)
                    else:
                        print("Wrong command!!!")
                
                # MANAGER MENU.  
                elif result_of_select[0] == (1,):  # обернуть в цикл while
                    print(
                '''MANAGER MENU: 
1 - add product
2 - delete product
3 - show all products
4 - find product by name
5 - find product by article (id)

6 - change product price
7 - change product status
8 - change product name
9 - change product description
0 - Exit'''
                    )
                    user_operation = input("Input operation: ")
                    if user_operation == '1':
                        print("ADD product")
                        Internet_Store().add_product()
                    elif user_operation == '2':
                        print('delete product')
                        Internet_Store().delete_product()
                    elif user_operation == '3':
                        print("show all products")
                        Internet_Store().show_product_list_for_manager()
                    elif user_operation == '4':
                        print('find product by name')
                        res = Internet_Store().find_product_by_name()
                        print(res)
                    elif user_operation == '5':
                        print('find product by article (id)')
                        res = Internet_Store().find_product_by_article()
                        print(res)
                    elif user_operation == '6':
                        print('change product price')
                    elif user_operation == '7':
                        print('change product status')
                    elif user_operation == '8':
                        print('change product name')
                    elif user_operation == '9':
                        print('change product description')
                    elif user_operation == "0":
                        self.cond = False
                        conn.close()
                        print(EXIT_MSG)
                    else:
                        print("Wrong command!!!")
                
                # WORK USER MENU. 
                elif result_of_select[0] == (2,):  # обернуть в цикл while
                    print(
                '''USER MENU: 
1 - show all products
2 - find product by name
3 - find product by article (id)
4 - buy product (sell product)
0 - Exit'''
                    )
                    user_operation = input("Input operation: ")
                    if user_operation == '1':
                        print("show all products")
                        Internet_Store().show_product_list_for_user()
                    elif user_operation == '2':
                        print('find product by name')
                        res = Internet_Store().find_product_by_name()  # Добавть срез статуса товара или добавить условие если статус не 1 то нет товара если 1 то есть
                        print(res)
                    elif user_operation == '3':
                        print("find product by article")
                        res = Internet_Store().find_product_by_article()  # -----//-----
                        print(res)
                    elif user_operation == '4':
                        print('buy product')
                        Internet_Store().sell_product()
                    elif user_operation == "0":
                        self.cond = False
                        conn.close()
                        print(EXIT_MSG)
                        
                # USER BLOCKED.
                elif result_of_select[0] == (3,):
                    print("User blocked. Please call administrator.")
                    
            # REG NEW USER.        
            elif user_operation == "2":
                print("REG NEW USER")
                user_name = input('Enter user name: ')
                user_pass = getpass.getpass("Enter user password: ")
                Store_Users_Admin().add_user(user_name, 2, user_pass)
                
            elif user_operation == "3":
                print(ABOUT_MSG)
            elif user_operation == "0":
                self.cond = False
                Internet_Store().conn.close()
                print(EXIT_MSG) 
            else:
                print("Wrong command!!!")
