import datetime

class Menu:
    def __init__(self):
        self.item = []
        f=open("menu.txt","r")
        menulist = f.readlines()
        f.close()
        for line in menulist:
            ar = line.split(',')
            self.item.append((ar[0],int(ar[1])))

    def display(self):
        n=1
        for x in self.item:
            print(f'{n}.{x[0]},{x[1]}')
            n+=1

    def append(self):
        while True:
            menu = input('메뉴를 입력하세요 : ')
            price = input('가격을 입력하세요 : ')

            if menu and price:
                self.item.append((menu, int(price)))
                print(f'>> 저장됨: {menu}, {price}')
            else:
                break

    def update(self):
        if not self.item:
            print('수정할 부분이 없움')
            return

        idx = int(input('수정할 메뉴 번호 : ')) -1
        if 0 <= idx < len(self.item):
            menu, price = self.item[idx]
            print(f'선택된 메뉴 : {menu}, {price}')

            new_name = input('새 메뉴명 : ')
            new_price = input('새 가격 : ')

            if not new_name or not new_price:
                print('수정 취소')
                return

            self.item[idx] = (new_name, new_price)
            print(f'{self.item[idx]}로 수정완료')



    def delete(self):
        if not self.item:
            print('삭제할 메뉴가 없습니다')
            return

        idx = int(input('삭제할 메뉴 번호 : '))-1
        if 0 <= idx < len(self.item):
            delete = self.item.pop(idx)
            print('삭제완료')
        else:
            print('잘못된 번호')



    def save(self):
        try:
            with open('menu.txt','w') as f:
                for x in self.item:
                    f.write(f'{x[0]},{x[1]}\n')
        except FileNotFoundError:
            print('파일저장 실패')


class Order:
    def __init__(self):
        self.orderlist = []
        self.order_num = 1

        f = open('order.txt','r')
        order_data = f.readlines()
        f.close()

        for line in order_data:
            line = line.strip()
            if not line: continue

    def add(self, menu_instance):

        menu_instance.display()
        name, price = menu_instance.item[0]

        while True:
           num = int(input('메뉴번호를 입력하세요 : '))
           count = int(input('수량을 입력하세요 : '))

           if num and count:
                total_price = price * count
                self.orderlist.append((name, count, total_price))
                print(f'주문이 완료되었습니다. {name},{count},{total_price}')
                self.save()
                break



    def display(self):
        if not self.orderlist:
            print('현재 주문 내역이 없습니다')
            return
        for name, count, total_price in self.orderlist:
            print(f" 메뉴 : {name} , 수량 : {count}개 , 총 가격 : {total_price:,d}원")

    def delete(self):
        if not self.orderlist:
            print('삭제할 주문 내역이 없습니다')
            return

        idx = int(input('삭제할 주문 번호 : '))- 1
        if 0 <= idx < len(self.orderlist):
            delete1 = self.orderlist.pop(idx)
            print('삭제 완료')
        else:
            print('잘못된 번호')

    def check(self):
        total_sum = 0
        for name, count, total_price in self.orderlist:
         total_sum += total_price

        mile = input('마일리지를 입력할 번호를 입력하세요 : ')
        mobile_num = mile if mile else '미입력'

        return mobile_num, total_sum



    def save(self):
        try :
            with open('order.txt','w') as f:
                for name, count, total_price in self.orderlist:
                    f.write(f'{name},{count},{total_price}\n')
        except FileNotFoundError:
            print("주문 파일 저장 실패")


class Sale:
    def __init__(self):
        self.history = []
        try:
            with open('history.txt','r') as f:
                f.close()
        except FileNotFoundError:
            pass


    def add(self,order_list, mobile_num, total_sum):

        count, total_price, name = order_list[0]
        now = datetime.datetime.now()

        try:
            with open('history.txt','a') as f:
                f.write(f'메뉴 : {name},수량 : {count}, 총 가격 :{total_price}, 모바일 : {mobile_num},'
                        f'시간 : {now}\n')
                f.write(f'총 매출 : {total_sum}\n')
        except FileNotFoundError:
            print('저장 실패')

    def display(self):
        try:
            with open('history.txt','r') as f:
                bill = f.read()
                if bill.strip():
                    print(bill)
                else:
                    print('등록된 정보가 없다')
        except FileNotFoundError:
            print('매출기록이 없습니다.')