import random
import time

repeat = 0
player = int(input("몇번 반복? : "))

change_win = 0
not_change_win = 0

change_fail = 0
not_change_fail = 0

total_win = 0

door_list = ['door1', 'door2', 'door3']

selected_door_value = random.randint(1,3)
if selected_door_value == 1:
    selected_door = 'door1'
    not_selected_door = ['door2', 'door3']
elif selected_door_value == 2:
    selected_door = 'door2'
    not_selected_door = ['door1', 'door3']
elif selected_door_value == 3:
    selected_door = 'door3'
    not_selected_door = ['door1', 'door2']

selector_selected_door = ''
select_possible_door = ['door1', 'door2', 'door3']


def selector():
    global select
    select = random.choice(door_list)

def check():
    global show_not_selected_door

    print(f"select = {select}")

    if select:
        if select in not_selected_door:
            not_selected_door.remove(select)
            show_not_selected_door = not_selected_door[0]
        elif select not in not_selected_door:
            show_not_selected_door = not_selected_door[random.randint(0, 1)]
        print(f"{show_not_selected_door} 에는 상품이 없습니다.")
        select_possible_door.remove(show_not_selected_door)
    elif not select:
        not_selected_door.remove(select)
        print(f"{not_selected_door} 에는 상품이 없습니다.")
        select_possible_door.remove(not_selected_door)

def selector_select():
    global final_select
    global change_fail, change_win, not_change_fail, not_change_win
    global total_win
    final_select = random.randint(0, 1)

    if final_select == 1:
        if select == selected_door:
            print("성공")
            not_change_win += 1
            total_win += 1
        else:
            print("실패")
            not_change_fail += 1

    elif final_select == 0:
        if select in select_possible_door:
            select_possible_door.remove(select)
        if select_possible_door[0] == selected_door:
            print("성공")
            change_win += 1
            total_win += 1
        else:
            print("실패")
            change_fail += 1


def result():
    if final_select == 1:
        print("선택: 바꾸지 않음")
    else:
        print("선택: 바꿈")
    print(f"상품 위치: {selected_door}")

def reset():
    global select_possible_door
    global selected_door
    global not_selected_door

    select_possible_door = ['door1', 'door2', 'door3']

    selected_door_value = random.randint(1,3)
    if selected_door_value == 1:
        selected_door = 'door1'
        not_selected_door = ['door2', 'door3']
    elif selected_door_value == 2:
        selected_door = 'door2'
        not_selected_door = ['door1', 'door3']
    elif selected_door_value == 3:
        selected_door = 'door3'
        not_selected_door = ['door1', 'door2']


while repeat <= player:
    selector()
    check()
    selector_select()
    result()
    reset()
    repeat += 1


print(f"바꿔서 이긴 횟수: {change_win}")
print(f"바꿔서 진 횟수: {change_fail}")
print(f"안바꿔서 이긴 횟수: {not_change_win}")
print(f"안바꿔서 진 횟수: {not_change_fail}")

if total_win > 0:
    change_win_rate = change_win / total_win * 100
    not_change_win_rate = not_change_win / total_win * 100
elif total_win == 0:
    change_win_rate = change_win * 100
    not_change_win_rate = not_change_win * 100

print(f"바꿔서 이길 확률 : {change_win_rate}, 안바꿔서 이길 확률 : {not_change_win_rate}")

time.sleep(1000)


