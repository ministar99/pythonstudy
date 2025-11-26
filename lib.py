def makeMenu(filename):
    with open(filename, 'a') as f:
        while True:
            menu = input('메뉴입력 :').strip()
            price = input('가격입력 :').strip()

            if not menu or not price:
                break

            f.write(f'{menu},{price}\n')
            print(f'>> 저장됨: {menu}, {price}')


def readMenu(filename):
    lst = []
    with open(filename, 'r') as f:
        for line in f:
            stripped_line = line.strip()
            if stripped_line:
                lst.append(stripped_line)

        return lst


def updateMenu(filename):
    menu_list = readMenu(filename)

    if not menu_list:
        print('수정할 메뉴가 없습니다')
        return


    idx = 1
    for item in menu_list:
        print(f'{idx}. {item}')
        idx += 1


    idx_input = int(input('수정할 번호 입력: '))
    idx = idx_input - 1

    if 0 <= idx < len(menu_list):
        old_data = menu_list[idx]
        print(f'선택된 메뉴: {old_data}')

        new_menu = input('새 메뉴명: ').strip()
        new_price = input('새 가격: ').strip()

        if not new_menu or not new_price:
            print("수정 취소")
            return

        menu_list[idx] = f'{new_menu},{new_price}'
        print(f"'{old_data}' -> '{menu_list[idx]}'로 수정 완료.")

        with open(filename, 'w') as f:
            for item in menu_list:
                f.write(f'{item}\n')
    else:
        print('잘못된 번호입니다. 목록 범위를 확인하세요.')


def deleteMenu(filename):
    menu_list = readMenu(filename)
    if not menu_list:
        print('삭제할 메뉴가 없습니다')
        return


    idx = 1
    for item in menu_list:
        print(f'{idx}. {item}')
        idx += 1


    idx_input = int(input('삭제할 번호 입력: '))
    idx = idx_input - 1

    if 0 <= idx < len(menu_list):
        deleted_data = menu_list.pop(idx)
        print(f"'{deleted_data}' 삭제 완료.")

        with open(filename, 'w') as f:
            for item in menu_list:
                f.write(f'{item}\n')

