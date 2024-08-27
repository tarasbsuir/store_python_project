# Module describes internet store


import sqlite3 as s
import getpass


class Internet_Store:
    '''Class description'''
    # Список товаров, добавить товар, убрать товары, продать  и т.д.
    
    def __init__(self) -> None:
        self.conn = s.connect('internet_store.db')
        self.c = self.conn.cursor()
        
    def add_product(self):
        '''Method addes product in list. (принять на склад)''' 
        self.name = input('Enter product name: ')
        self.description = input('Enter product description: ')
        self.price = input('Enter product price: ')
        self.status = input('Enter product status (0-1-2): ')
        self.c.execute('INSERT INTO goods (name, description, price, status) VALUES (?, ?, ?, ?)',
                       (self.name, self.description, self.price, self.status))
        self.conn.commit()
        print(f'Product was added: {self.name}')
        
    def delete_product(self):
        '''Method deletes product from list. (удалить товар)'''
        # Under development
        pass
    
    def show_product_list(self):
        '''Method shows list of products. (показать все товары)'''
        # Under development
        pass
    
    def sell_product(self):
        '''Method for seling goods. (продавать товары)'''
        # Under development
        pass
                
    def close_conn(self):
        self.conn.close()


class Product:
    '''Class description'''
    # Товар, что с ним делать? Редактировать поля товаров в БД?
    pass


class Store_Users:
    '''Class description'''
    # Этот класс вобще нужен? Что с ним сделать?
    pass


class App:
    '''Class description'''
    def __init__(self) -> None:
        self.cond = True

    def Run(self):
        print('''
        Internet Store. Use this program to make your purchases.
            ''')
        while self.cond:
            print(
                '''MENU:
1 - Sign in
0 - Exit'''
            )
            user_operation = input("Input operation: ") # Надо добавить вход по логину и паролю в БД
            
            if user_operation == "1":
                user_name = input("Enter user name: ")
                user_pass = getpass.getpass("Enter user password: ")
                conn = s.connect('internet_store.db') # Может создать отдельный класс DB_Connect?
                c = conn.cursor()
                c.execute('SELECT user_role from users where user_name = ? and user_pass = ?',
                          (user_name, user_pass))
                result_of_select = c.fetchall()
                
                if result_of_select == []:
                    print('USER NOT FOUND or password is incorrect.')
                
                elif result_of_select[0] == (0,):
                    print(
                '''ADMIN MENU: 
1 - add user
2 - del user
3 - block user
4 - upd user pass
0 - Exit'''
                    )
                    user_operation = input("Input operation: ")
                    
                elif result_of_select[0] == (1,):
                    print(
                '''MANAGER MENU: 
1 - add product
2 - del product
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
                    
                elif result_of_select[0] == (2,):
                    print(
                '''USER MENU: 
1 - show all products
2 - find product by name
3 - find product by article
4 - buy product
0 - Exit'''
                    )
                    user_operation = input("Input operation: ")
                
                
                # # Пригодится else?    
                # else:
                #      print('USER NOT FOUND')
                #      print(result_of_select)
                # try:
                #     pass
                #     # Тут подключение к БД и проверка логина и пароля
                # except Exception as e:  # Обработать ошибки с подключением к БД?
                #     print(e)
                # else:
                #     pass  # Что-то сделать надо!
                

            elif user_operation == "0":
                self.cond = False
                conn.close()
                print('''
             |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
             |||                        SEE YA!                      |||
             |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
             ''')
            else:
                print("Wrong command!!!")
