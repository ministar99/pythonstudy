import Calculator

cafeMenu = Calculator.Menu()
cafeOrder = Calculator.Order()
cafeSale = Calculator.Sale()
'''cafeMenu.display()'''
while True:
    answer = input('작업을 선택하세요(m : 메뉴선택, o : 주문관리, s : 매출조회, x : 프로그램 종료) ')
    if answer == 'm':
        while True:
            reply = input('메뉴 작업을 선택하세요(c : 메뉴추가, r : 메뉴표시, u : 메뉴추가, d : 메뉴삭제, x : 메뉴관리 종료)')
            if reply == 'x': break
            elif reply == 'c':
                cafeMenu.append()
            elif reply == 'r':
                cafeMenu.display()
            elif reply == 'u':
                cafeMenu.update()
            elif reply == 'd':
                cafeMenu.delete()
            cafeMenu.save()

    elif answer == 'o':
        while True:
            reply1 = input("주문관리 작업을 선택하세요(a : 주문추가, r : 주문내역, d:주문취소, x: 종료) : ")
            if reply1 == 'x':
                total_sum, mobile_num = cafeOrder.check()
                cafeSale.add(list(cafeOrder.orderlist), total_sum, mobile_num)
                cafeOrder.orderlist = []
                cafeOrder.save()
                cafeSale.display()
                break
            elif reply1 == 'a':
                cafeOrder.add(menu_instance=cafeMenu)
            elif reply1 == 'r':
                cafeOrder.display()
            elif reply1 == 'd':
                cafeOrder.delete()


    elif answer == 's':
        while True:
            reply2 = input('매출관리 작업을 선택하세요(a: 매출추가, r: 매출보기, x : 작업 종료) : ')
            if reply2 == 'x':
                break
            if reply2 == 'a':
                cafeSale.add( )
            if reply2 == 'r':
                cafeSale.display()


    else:
        break