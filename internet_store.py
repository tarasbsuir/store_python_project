# Module describes internet store


import sqlite3 as s


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
        self.price = float(input('Enter product price: '))
        self.status = int(input('Enter product status (0-1-2): '))
        self.c.execute('INSERT INTO goods (name, description, price, status) VALUES (?, ?, ?, ?)',
                       (self.name, self.description, self.price, self.status))
        self.conn.commit()
        print(f'Product was added: {self.name}')
        
    def delete_product(self):
        '''Method deletes product from list. (удалить товар)'''
        pass
    
    def show_product_list(self):
        '''Method shows list of products. (показать все товары)'''
        pass
    
    def show_product_list(self):
        '''Method for seling goods. (продавать товары)'''
        pass
                
    def close_conn(self):
        self.conn.close()





class Product(Internet_Store):
    '''Class description'''
    # Товар что с ним делать? Редактировать поля товаров?
    
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
0 - exit'''
            )
            user_operation = input("Input operation: ") # Надо добавить вход по логину и паролю в БД
            
            if user_operation == "1":
                user_name = input("Enter user name: ")
                user_pass = int(input("Enter user password: "))
                
                
                
                
                
                
                '''
                try:
                    pass
                    # Тут подключение к БД и проверка логина и пароля
                except Exception as e:  # Обработать ошибки с подключением к БД?
                    print(e)
                else:
                    pass  # Что-то сделать надо!
                '''    

            elif user_operation == "0":
                self.cond = False
                print('''
             |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
             |||                        SEE YA!                      |||
             |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
             ''')
            else:
                print("Wrong command!!!")
