import tkinter as tk  #python的GUI工具包
from tkinter import messagebox  #警示視窗

default_bg_color = "white"

# Declare the winner and ask to restart the game
def declare_winner(winner):
    if winner == "Tie":  #平手則全部格子變紅色
        for r in range (3):
            for t in range (3):
                button1 = window.grid_slaves(row=r, column = t)[0]
                button1.config(bg='red')

    #依照贏的方式不同，決定要讓哪幾格變色（有成功連線的格子們）
    elif winner == "1":
        button1 = window.grid_slaves(row=0, column = 0)[0]
        button1.config(bg='blue')
        button1 = window.grid_slaves(row=0, column = 1)[0]
        button1.config(bg='blue')
        button1 = window.grid_slaves(row=0, column = 2)[0]
        button1.config(bg='blue')
    #以下太過繁瑣，附於appendix
    elif winner == "2":
        button1 = window.grid_slaves(row=1, column = 0)[0]
        button1.config(bg='blue')
        button1 = window.grid_slaves(row=1, column = 1)[0]
        button1.config(bg='blue')
        button1 = window.grid_slaves(row=1, column = 2)[0]
        button1.config(bg='blue')

    elif winner == "3":
        button1 = window.grid_slaves(row=2, column = 0)[0]
        button1.config(bg='blue')
        button1 = window.grid_slaves(row=2, column = 1)[0]
        button1.config(bg='blue')
        button1 = window.grid_slaves(row=2, column = 2)[0]
        button1.config(bg='blue')

    elif winner == "4":
        button1 = window.grid_slaves(row=0, column = 0)[0]
        button1.config(bg='blue')
        button1 = window.grid_slaves(row=1, column = 0)[0]
        button1.config(bg='blue')
        button1 = window.grid_slaves(row=2, column = 0)[0]
        button1.config(bg='blue')
        
    elif winner == "5":
        button1 = window.grid_slaves(row=0, column = 1)[0]
        button1.config(bg='blue')
        button1 = window.grid_slaves(row=1, column = 1)[0]
        button1.config(bg='blue')
        button1 = window.grid_slaves(row=2, column = 1)[0]
        button1.config(bg='blue')
        
    elif winner == "6":
        button1 = window.grid_slaves(row=0, column = 2)[0]
        button1.config(bg='blue')
        button1 = window.grid_slaves(row=1, column = 2)[0]
        button1.config(bg='blue')
        button1 = window.grid_slaves(row=2, column = 2)[0]
        button1.config(bg='blue')

    elif winner == "7":
        button1 = window.grid_slaves(row=0, column = 0)[0]
        button1.config(bg='blue')
        button1 = window.grid_slaves(row=1, column = 1)[0]
        button1.config(bg='blue')
        button1 = window.grid_slaves(row=2, column = 2)[0]
        button1.config(bg='blue')
    
    elif winner == "8":
        button1 = window.grid_slaves(row=0, column = 2)[0]
        button1.config(bg='blue')
        button1 = window.grid_slaves(row=1, column = 1)[0]
        button1.config(bg='blue')
        button1 = window.grid_slaves(row=2, column = 0)[0]
        button1.config(bg='blue')
    
    #ask if to continue
    answer = tk.messagebox.askyesno(title='End', message='Again?')
    
    if answer:  #使用者想繼續玩下一輪
        #play another round
        global board
        board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  #格子參數初始化

        for i in range (3):
            for j in range(3):
                button = window.grid_slaves(row=i, column=j)[0]
                #讓格子的顏色變回白色
                button.config(text="", bg=default_bg_color)
                # button.config(text="", bg='white')
        global current_player
        current_player = 1  #player初始化
    else:
        window.destroy()  

#check for a winner or a tie
def check_winner():
    winner = None  #用以存取贏的方式
    global whoWin  #紀錄是誰贏
    whoWin = 0
    count = 0
    #winner_path = []
    #check rows
    if (board[0][0] == board[0][1] == board[0][2] != 0):
        whoWin = board[0][0]  #看是哪一位玩家在這格留下紀錄
        winner = "1"  #贏的方式是type1
    elif (board[1][0] == board[1][1] == board[1][2] != 0):
        whoWin = board[1][0]
        winner = "2"
    elif (board[2][0] == board[2][1] == board[2][2] != 0):
        whoWin = board[2][0]
        winner = "3"

    #check columns
    if (board[0][0] == board[1][0] == board[2][0] != 0):
        whoWin = board[0][0]
        winner = "4"
    elif (board[0][1] == board[1][1] == board[2][1] != 0):
        whoWin = board[0][1]
        winner = "5"
    elif (board[0][2] == board[1][2] == board[2][2] != 0):
        whoWin = board[0][2]
        winner = "6"

    #check diagonals
    if (board[0][0] == board[1][1] == board[2][2] != 0):
        whoWin = board[0][0]
        winner = "7"
    elif (board[0][2] == board[1][1] == board[2][0] != 0):
        whoWin = board[1][1]
        winner = "8"

    #check if tie
    if whoWin==0:
        for k in range (3):
            for p in range (3):
                count = count + board[k][p]
        #當player1按過五次、player2按過四次則所有格子填滿，遊戲結束
        #1*5+2*4=13，所以若count=13就表示遊戲結束且平手
        if count==13:
            whoWin = 0
            winner = "Tie"
    
    if winner:  #若贏的方式有值（知道贏的type，有8種）
        declare_winner(winner)

#Handle button clicks
def handle_click(row, col):
    global current_player  #判斷是幾號玩家動作
    global board  #需要對board中被點選到的格子做改變
    
    #check with button has been clicked and change player
    #change text on botton to show 'O' or 'X'
    #把被選到的格子稱作button
    button = window.grid_slaves(row=row, column = col)[0]
    if board[row][col] == 0:  #表示那格尚未被選過
        if current_player == 1:
            board[row][col] = 1  #表示玩家1選到
            button.config(text='O')  #顯示"O"
            current_player = 2  #換成玩家2選格子
        else:
            board[row][col] = 2
            button.config(text='X')
            current_player = 1
        check_winner()  #檢查是否出現贏家或平手

#create board
def create_board():
    for i in range(3):  #長邊寬邊各有三格(3*3)
        for j in range(3):
            #相關表格設定
            button = tk.Button(window, text='', font=("Arial", 50),
                               height=2, width=6,
                               command=lambda row=i, col=j: handle_click(row, col))
            #grid適在畫九宮格使用，nsew指貼齊上下左右
            button.grid(row=i, column=j, sticky="nsew")

if __name__ == '__main__':  #避免其他檔案執行時執行到不必要指令，參考Reference 1

    #create main window
    window = tk.Tk()  #一個叫window的新視窗
    window.title("Lab3 Tic-Tac-Toe")  #視窗title

    #create game board
    create_board()

    #Initialize variables
    board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    current_player = 1

    #將Tkinter物件放入等待迴圈，讓window不斷重新整理
    window.mainloop()