from PIL import Image


"""
codes:
0 = OK
"""

class Connection:
    def __init__(self):
        self.ip = ''

    def connect(self):
        "todo"
        return 0

    def create_account(self,name,pw):
        "todo"
        return 0

    def login(self,name,pw):
        "todo"
        return 0

    def logout(self):
        "todo"
        return 0


    def get_menu(self):
        "todo"
        return {0:{"preis":13.5,"name":"beispiel"}}

    def get_image(self,id):
        "todo"
        return Image.new('RGBA', (1, 1))

    def get_cart(self):
        "todo"
        return {0:2}#id:ammount

    def set_ammount(self,id,ammount):#setzt fügt hinzu oder entfernt
        "todo"
        return 0

    def cleare_cart(self):
        "todo"
        return 0

    def order_cart(self,location):
        "todo"
        return 0#order id

    def get_order_status(slef,order_id):
        "todo"
        return 0#0: in berabeitung,1: versendet,2: angekommen,-1 fehler

    
