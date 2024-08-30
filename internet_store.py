import sqlite3 as s
import pwinput


# Module describes internet store


EXIT_MSG = ('''
             |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
             |||                        SEE YA!                      |||
             |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
            ''')
ABOUT_MSG = 'Internet Store. Use this program to make your purchases.'


class DB_Connect:
    '''Class describes connection to database (SQLlite).'''
    def __init__(self) -> None:
        self.conn = s.connect('internet_store.db')
        self.c = self.conn.cursor()


class Internet_Store(DB_Connect):
    '''Class describes Internet Store.'''
    
    def add_product(self):
        '''Method addes product in list.''' 
        self.name = input('Enter product name: ')
        self.description = input('Enter product description: ')
        self.price = input('Enter product price: ')
        self.c.execute('INSERT INTO goods (name, description, price, status)\
                       VALUES (?, ?, ?, ?)',
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
        rows = self.c.fetchall()
        for row in rows:
            print(row)
        self.conn.close()
        
    def show_product_list_for_user(self):
        '''Method shows list of products (all available products for user).'''
        self.c.execute('SELECT * from goods WHERE status = 1')
        rows = self.c.fetchall()
        for row in rows:
            print(row[:4])  # Cut status for users.
        self.conn.close()

    def sell_product(self):
        '''Method for selling goods (sell product). 
        To sell product change status to 2.'''
        article = input('Enter product article: ')
        self.c.execute('UPDATE goods SET status = 2 WHERE article = ?',
                       (article))
        self.conn.commit()
        self.conn.close()
        print(f'Product #{article} was sold.')
        
    def find_product_by_name(self) -> list:
        '''Method helps find product in list by name.'''
        name = input('Please input product name: ')
        self.c.execute('SELECT * FROM goods WHERE name = ?', (name,))
        row = self.c.fetchall()
        return row
        
    def find_product_by_article(self) -> list:
        '''Method helps find product in list by article(id).'''
        article = input('Please input product article: ')
        self.c.execute('SELECT * FROM goods WHERE article = ?', (article,))
        row = self.c.fetchall()
        return row


class Product(DB_Connect):
    '''Class describes product and can change product fields in DB.'''
    def chnage_product_price(self):
        '''Method chnages product price.'''
        article = input('Enter product article: ')
        price = input('Enter new price: ')
        self.c.execute('UPDATE goods SET price = ? WHERE article = ?',
                       (price, article,))
        self.conn.commit()
        self.conn.close()
        print(f'Price for product with article #{article} was changed.')

    def chnage_product_status(self):
        '''Method chnages product status.'''
        article = input('Enter product article: ')
        status = input('Enter new status: ')
        self.c.execute('UPDATE goods SET status = ? WHERE article = ?',
                       (status, article,))
        self.conn.commit()
        self.conn.close()
        print(f'Status for product with article #{article} was changed.')

    def chnage_product_name(self):
        '''Method chnages product name.'''
        article = input('Enter product article: ')
        name = input('Enter new product name: ')
        self.c.execute('UPDATE goods SET name = ? WHERE article = ?',
                       (name, article,))
        self.conn.commit()
        self.conn.close()
        print(f'Name for product with article #{article} was changed.')

    def chnage_product_description(self):
        '''Method chnages product description.'''
        article = input('Enter product article: ')
        description = input('Enter new description: ')
        self.c.execute('UPDATE goods SET description = ? WHERE article = ?',
                       (description, article,))
        self.conn.commit()
        self.conn.close()
        print(f'Description for product with article #{article} was changed.')


class Store_Users_Admin(DB_Connect):
    '''Class for manage users.'''
        
    def add_user(self, user_name, user_role, user_pass):
        '''Method addes user in DB. Accept 3 args name, role, pass'''
        self.c.execute('INSERT INTO users (user_name, user_role, user_pass)\
                       VALUES (?, ?, ?)', (user_name, user_role, user_pass))
        self.conn.commit()
        self.conn.close()
        print(f'User was added: {user_name}')

    def delete_user(self):
        user_id = input('Enter user_id: ')
        self.c.execute('DELETE FROM users WHERE user_id = ?', (user_id,))
        self.conn.commit()
        self.conn.close()
        print(f'User with ID #{user_id} was deleted successfully.')

    def block_user(self):
        user_id = input('Enter user_id: ')
        self.c.execute('UPDATE users SET user_role = 3 WHERE user_id = ?',
                       (user_id,))
        self.conn.commit()
        self.conn.close()
        print(f'User with ID #{user_id} was blocked successfully.')

    def change_user_password(self):
        user_id = input('Enter user_id: ')
        user_pass = pwinput.pwinput("Enter user password: ", '*')
        self.c.execute('UPDATE users SET user_pass = ? WHERE user_id = ?',
                       (user_pass, user_id,))
        self.conn.commit()
        self.conn.close()
        print(f'User with ID #{user_id} was blocked successfully.')
    
    def show_all_users(self):
        self.c.execute('SELECT * FROM users')
        rows = self.c.fetchall()
        for row in rows:
            print(row)
        self.conn.close()


class App:
    '''Class for starting application.'''
    def __init__(self) -> None:
        self.cond = True
        self.admin_cond = True
        self.manager_cond = True
        self.user_cond = True

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
                user_pass = pwinput.pwinput("Enter user password: ", '*')
                conn = s.connect('internet_store.db')
                c = conn.cursor()
                c.execute('SELECT user_role from users where user_name = ?\
                          and user_pass = ?', (user_name, user_pass))
                result_of_select = c.fetchall()
                
                if result_of_select == []:
                    print('USER NOT FOUND or password is incorrect.')
                
                # ADMIN MENU.
                elif result_of_select[0] == (0,):
                    while self.admin_cond:
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
                            user_pass = pwinput.pwinput("Enter user password: ", '*')
                            Store_Users_Admin().add_user(user_name, user_role, user_pass)
                        elif user_operation == '2':
                            print('del user')
                            Store_Users_Admin().delete_user()
                        elif user_operation == '3':
                            print("block user")
                            Store_Users_Admin().block_user()
                        elif user_operation == '4':
                            print('upd user pass')
                            Store_Users_Admin().change_user_password()
                        elif user_operation == '5':
                            print('all users')
                            Store_Users_Admin().show_all_users()
                        elif user_operation == "0":
                            self.cond = False
                            self.admin_cond = False
                            conn.close()
                            print(EXIT_MSG)
                        else:
                            print("Wrong command!!!")
                
                # MANAGER MENU.  
                elif result_of_select[0] == (1,):
                    while self.manager_cond:
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
                            print(res[0])
                        elif user_operation == '5':
                            print('find product by article (id)')
                            res = Internet_Store().find_product_by_article()
                            print(res[0])
                        elif user_operation == '6':
                            print('change product price')
                            Product().chnage_product_price()
                        elif user_operation == '7':
                            print('change product status')
                            Product().chnage_product_status()
                        elif user_operation == '8':
                            print('change product name')
                            Product().chnage_product_name()
                        elif user_operation == '9':
                            print('change product description')
                            Product().chnage_product_description()
                        elif user_operation == "0":
                            self.cond = False
                            self.manager_cond = False
                            conn.close()
                            print(EXIT_MSG)
                        else:
                            print("Wrong command!!!")
                
                # WORK USER MENU. 
                elif result_of_select[0] == (2,):
                    while self.user_cond:
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
                            res = Internet_Store().find_product_by_name()
                            if len(res) != 0:
                                if res[0][4] == 1:
                                    print(res[0])
                                else:
                                    print('Product not found.')
                            else:
                                print('Product not found.')
                        elif user_operation == '3':
                            print("find product by article")
                            res = Internet_Store().find_product_by_article()
                            if len(res) != 0:
                                if res[0][4] == 1:
                                    print(res[0])
                                else:
                                    print('Product not found.')
                            else:
                                print('Product not found.')
                        elif user_operation == '4':
                            print('buy product')
                            Internet_Store().sell_product()
                        elif user_operation == "0":
                            self.cond = False
                            self.user_cond = False
                            conn.close()
                            print(EXIT_MSG)
                        else:
                            print("Wrong command!!!")
                        
                    # USER BLOCKED.
                elif result_of_select[0] == (3,):
                    print("User blocked. Please call administrator.")
                    
            # REG NEW USER.        
            elif user_operation == "2":
                print("REG NEW USER")
                user_name = input('Enter user name: ')
                user_pass = pwinput.pwinput("Enter user password: ", '*')
                Store_Users_Admin().add_user(user_name, 2, user_pass)
                
            elif user_operation == "3":
                print(ABOUT_MSG)
            elif user_operation == "0":
                self.cond = False
                Internet_Store().conn.close()
                print(EXIT_MSG) 
            else:
                print("Wrong command!!!")
