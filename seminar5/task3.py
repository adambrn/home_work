from tkinter import *
import random
from tkinter import messagebox
from turtle import delay

buttons_list = [''] * 9
move_list = list(range(9))
move_number = 0
game_mode = 1
stop_game_flag = False
player = 1

def new_game():
    global move_number ,buttons_list, stop_game_flag, move_list, game_mode
    
    for i in range(9):
        buttons[i].config(text = '',state='active')
    buttons_list = [''] * 9
    move_list = list(range(9))
    move_number = 0
    stop_game_flag = False
    game_mode = 1
    label['text'] = 'Игра с компьютером'

def new_game_2():
    global move_number ,buttons_list, stop_game_flag, move_list, game_mode, player
    
    for i in range(9):
        buttons[i].config(text = '',state='active')
    buttons_list = [''] * 9
    move_list = list(range(9))
    move_number = 0
    stop_game_flag = False
    game_mode = 2
    player = 1
    label['text'] = 'Ход игрока 1'

def stop_game(text = 'Игрок'):
    global move_number ,buttons_list, stop_game_flag, move_list
    if len(move_list) == 0:
        messagebox.showinfo('Игра окончена', 'Ничья!')
    else:
        for i in move_list:
            buttons[i].config(state='disabled')
        messagebox.showinfo('Игра окончена', f'Победил {text}!')
    stop_game_flag = True

def check_next_move(value):
        global buttons_list
        if (buttons_list[0] == value and buttons_list[1] == value and buttons_list[2] == '') : return 2
        if (buttons_list[0] == value and buttons_list[1] == '' and buttons_list[2] == value) : return 1
        if (buttons_list[0] == '' and buttons_list[1] == value and buttons_list[2] == value) : return 0
        if (buttons_list[3] == value and buttons_list[4] == value and buttons_list[5] == '') : return 5
        if (buttons_list[3] == value and buttons_list[4] == '' and buttons_list[5] == value) : return 4
        if (buttons_list[3] == '' and buttons_list[4] == value and buttons_list[5] == value) : return 3
        if (buttons_list[6] == value and buttons_list[7] == value and buttons_list[8] == '') : return 8
        if (buttons_list[6] == value and buttons_list[7] == '' and buttons_list[8] == value) : return 7
        if (buttons_list[6] == '' and buttons_list[7] == value and buttons_list[8] == value) : return 6
        if (buttons_list[0] == value and buttons_list[3] == value and buttons_list[6] == '') : return 6
        if (buttons_list[0] == value and buttons_list[3] == '' and buttons_list[6] == value) : return 3
        if (buttons_list[0] == '' and buttons_list[3] == value and buttons_list[6] == value) : return 0
        if (buttons_list[1] == value and buttons_list[4] == value and buttons_list[7] == '') : return 7
        if (buttons_list[1] == value and buttons_list[4] == '' and buttons_list[7] == value) : return 4
        if (buttons_list[1] == '' and buttons_list[4] == value and buttons_list[7] == value) : return 1
        if (buttons_list[2] == value and buttons_list[5] == value and buttons_list[8] == '') : return 8
        if (buttons_list[2] == value and buttons_list[5] == '' and buttons_list[8] == value) : return 5
        if (buttons_list[2] == '' and buttons_list[5] == value and buttons_list[8] == value) : return 2
        if (buttons_list[0] == value and buttons_list[4] == value and buttons_list[8] == '') : return 8
        if (buttons_list[0] == value and buttons_list[4] == '' and buttons_list[8] == value) : return 4
        if (buttons_list[0] == '' and buttons_list[4] == value and buttons_list[8] == value) : return 0
        if (buttons_list[2] == value and buttons_list[4] == value and buttons_list[6] == '') : return 6
        if (buttons_list[2] == value and buttons_list[4] == '' and buttons_list[6] == value) : return 4
        if (buttons_list[2] == '' and buttons_list[4] == value and buttons_list[6] == value) : return 2
        value = 'X'
        if (buttons_list[0] == value and buttons_list[1] == value and buttons_list[2] == '') : return 2
        if (buttons_list[0] == value and buttons_list[1] == '' and buttons_list[2] == value) : return 1
        if (buttons_list[0] == '' and buttons_list[1] == value and buttons_list[2] == value) : return 0
        if (buttons_list[3] == value and buttons_list[4] == value and buttons_list[5] == '') : return 5
        if (buttons_list[3] == value and buttons_list[4] == '' and buttons_list[5] == value) : return 4
        if (buttons_list[3] == '' and buttons_list[4] == value and buttons_list[5] == value) : return 3
        if (buttons_list[6] == value and buttons_list[7] == value and buttons_list[8] == '') : return 8
        if (buttons_list[6] == value and buttons_list[7] == '' and buttons_list[8] == value) : return 7
        if (buttons_list[6] == '' and buttons_list[7] == value and buttons_list[8] == value) : return 6
        if (buttons_list[0] == value and buttons_list[3] == value and buttons_list[6] == '') : return 6
        if (buttons_list[0] == value and buttons_list[3] == '' and buttons_list[6] == value) : return 3
        if (buttons_list[0] == '' and buttons_list[3] == value and buttons_list[6] == value) : return 0
        if (buttons_list[1] == value and buttons_list[4] == value and buttons_list[7] == '') : return 7
        if (buttons_list[1] == value and buttons_list[4] == '' and buttons_list[7] == value) : return 4
        if (buttons_list[1] == '' and buttons_list[4] == value and buttons_list[7] == value) : return 1
        if (buttons_list[2] == value and buttons_list[5] == value and buttons_list[8] == '') : return 8
        if (buttons_list[2] == value and buttons_list[5] == '' and buttons_list[8] == value) : return 5
        if (buttons_list[2] == '' and buttons_list[5] == value and buttons_list[8] == value) : return 2
        if (buttons_list[0] == value and buttons_list[4] == value and buttons_list[8] == '') : return 8
        if (buttons_list[0] == value and buttons_list[4] == '' and buttons_list[8] == value) : return 4
        if (buttons_list[0] == '' and buttons_list[4] == value and buttons_list[8] == value) : return 0
        if (buttons_list[2] == value and buttons_list[4] == value and buttons_list[6] == '') : return 6
        if (buttons_list[2] == value and buttons_list[4] == '' and buttons_list[6] == value) : return 4
        if (buttons_list[2] == '' and buttons_list[4] == value and buttons_list[6] == value) : return 2
        return random.choice(move_list)

def computer_move(button_push_number):
    global move_number ,buttons_list, stop_game_flag, move_list

    if button_push_number == 4 and move_number == 1:
        current_move = random.choice(move_list)
    elif button_push_number != 4 and move_number == 1:
        current_move = 4
    if move_number > 1:
        current_move = check_next_move('O')
           
    
    buttons_list[current_move] = 'O'
    buttons[current_move].config(text='O', state='disabled')
    move_list.remove(current_move)
    move_number +=1

def player_move(button_push_number,value):
    global move_number ,buttons_list, stop_game, move_list

    buttons_list[button_push_number] = value
    buttons[button_push_number].config(text=value,  state='disabled')
    move_list.remove(button_push_number)
    move_number +=1

def check_win(value):
    global buttons_list
    if (buttons_list[0] == value and buttons_list[1] == value and buttons_list[2] == value) \
        or (buttons_list[3] == value and buttons_list[4] == value and buttons_list[5] == value) \
        or (buttons_list[6] == value and buttons_list[7] == value and buttons_list[8] == value) \
        or (buttons_list[0] == value and buttons_list[3] == value and buttons_list[6] == value) \
        or (buttons_list[1] == value and buttons_list[4] == value and buttons_list[7] == value) \
        or (buttons_list[2] == value and buttons_list[5] == value and buttons_list[8] == value) \
        or (buttons_list[0] == value and buttons_list[4] == value and buttons_list[8] == value) \
        or (buttons_list[2] == value and buttons_list[4] == value and buttons_list[6] == value):
        return True

def push(button_push_number,game_mode):
    global move_number ,buttons_list, stop_game_flag, move_list, player

    if game_mode == 1:
        
        if len(move_list) > 0 and not stop_game_flag:
            
            player_move(button_push_number,'X')
            if check_win('X'):
                stop_game()
        if len(move_list) > 0 and not stop_game_flag:
            
            computer_move(button_push_number)
            if check_win('O'):
                stop_game('Компьютер')
        
        if len(move_list) == 0 and not stop_game_flag:
            stop_game()
        
    elif game_mode == 2:
        label['text'] = f'Ход игрока {player}'
        if player == 1 : x = 'X'
        else: x ='O'
        if len(move_list) > 0 and not stop_game_flag:
            player_move(button_push_number,x)
            if check_win(x):
                stop_game(f'Игрок {player}')
        if len(move_list) == 0:
            stop_game()
        else : 
            if player == 1 : player = 2
            else: player = 1
        label['text'] = f'Ход игрока {player}'

criss_cross = Tk()
label = Label(criss_cross,width=27, text='Игра с компьютером',font=('Arial',12,'bold'))
buttons = [Button(criss_cross,width=5,height=2,font=('Arial',20,'bold'),command = lambda x=i: push(x,game_mode)) for i in range(9)]
menubar = Menu()
new_game_menu = Menu(tearoff=0)
new_game_menu.add_command(label='С компьютером',command=new_game)
new_game_menu.add_command(label='2 игрока', command=new_game_2)
menubar.add_cascade(label='Новая игра', menu=new_game_menu)
menubar.add_command(label='Выход',command=criss_cross.quit)
criss_cross.resizable(False, False)
criss_cross.config(menu=menubar)
label.grid(row=0, column=0, columnspan=3)
row = 1
col = 0
for i in range(9):
    buttons[i].grid(row=row, column=col)
    col += 1
    if col == 3:
        row +=1
        col = 0

criss_cross.mainloop()