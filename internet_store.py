# Module describes internet store


import sqlite3 as s
import getpass

EXIT_MSG = ('''
             |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
             |||                        SEE YA!                      |||
             |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
            ''')
ABOUT_MSG = 'Internet Store. Use this program to make your purchases.'


class Internet_Store:
    '''Class description'''
    # TODO: Список товаров, добавить товар, убрать товары, продать  и т.д.
    
    def __init__(self) -> None:
        self.conn = s.connect('internet_store.db')
        self.c = self.conn.cursor()
        
    def add_product(self):
        '''Method addes product in list.''' 
        self.name = input('Enter product name: ')
        self.description = input('Enter product description: ')
        self.price = input('Enter product price: ')
        self.status = input('Enter product status (0-1-2): ')
        self.c.execute('INSERT INTO goods (name, description, price, status) VALUES (?, ?, ?, ?)',
                       (self.name, self.description, self.price, self.status))
        self.conn.commit()
        self.conn.close()
        print(f'Product was added: {self.name}')
        
    def delete_product(self):
        '''Method deletes product from list by article.'''
        article = int(input('Enter product article: '))
        self.c.execute('DELETE FROM goods WHERE article = ?', (article,))
        self.conn.commit()
        self.conn.close()
        print(f'Product #{article} was deleted successfully.')

    def show_product_list(self):
        '''Method shows list of products. (показать все товары)'''
        self.c.execute('SELECT * from goods')
        self.rows = self.c.fetchall()
        for row in self.rows:
            print(row)
        self.conn.close()











    def sell_product(self):
        '''Method for seling goods. (продавать товары)'''
        # Under development (ИЗМЕНИТЬ СТАТУТ товара В БД)
        pass


class Product:
    '''Class description'''
    # Товар, что с ним делать? Редактировать поля товаров в БД?
    pass


class Store_Users:
    '''Class description'''
    # Этот класс вобще нужен? Что с ним сделать? Класс для админки, вносить изменения в таблицу юзеров


    pass


class App:
    '''Class description'''
    def __init__(self) -> None:
        self.cond = True

    def Run(self):
        print(ABOUT_MSG)
        while self.cond:
            print(
                '''MENU:
1 - Sign in
2 - Register (пока не работает) - только с ролью юзер
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
                        Internet_Store().show_product_list()
                    elif user_operation == '4':
                        print('find product by name')
                    elif user_operation == '5':
                        print('find product by article (id)')
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
3 - find product by article
4 - buy product
0 - Exit'''
                    )
                    user_operation = input("Input operation: ")
                    if user_operation == '1':
                        print("show all products")  # только селект по доступным товарам со статусом 1 в наличии
                    elif user_operation == '2':
                        print('find product by name')
                    elif user_operation == '3':
                        print("find product by article")
                    elif user_operation == '4':
                        print('buy product')
                    elif user_operation == "0":
                        self.cond = False
                        conn.close()
                        print(EXIT_MSG)
                        
                # USER BLOCKED.
                elif result_of_select[0] == (3,):
                    print("User blocked")
                    
            # REG NEW USER.        
            elif user_operation == "2":
                print("REG NEW USER")

            elif user_operation == "3":
                print(ABOUT_MSG)

            elif user_operation == "0":
                self.cond = False
                conn.close()
                print(EXIT_MSG)
            else:
                print("Wrong command!!!")
