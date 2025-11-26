import lib


def job_menu():
    while True:
        sel = input('작업을 선택하세요(m : 메뉴선택, o : 주문관리, s : 매출조회, x : 프로그램 종료) ')
        if sel == 'm':
            while True:
                menu_sel = input('메뉴 작업을 선택하세요(c : 메뉴추가, r : 메뉴표시, u : 메뉴추가, d : 메뉴삭제, x : 메뉴관리 종료')
                if menu_sel == 'c':
                    lib.makeMenu('menu.txt')
                elif menu_sel == 'r':
                    lib.readMenu('menu.txt')
                elif menu_sel == 'u':
                    lib.updateMenu('menu.txt')
                elif menu_sel == 'd':
                    lib.deleteMenu('menu.txt')
                else :
                    break
        if sel == 'x':
            print('종료되었습니다.')
            break

print(job_menu())







'''
file_name = 'menu.txt'
lib.makeMenu(file_name)
menu_list = lib.readMenu(file_name)
print(f'메뉴명 : {menu_list}')
'''