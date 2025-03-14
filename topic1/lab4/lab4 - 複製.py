import tkinter as tk

def SetValue():
    # label的字串會在不同func中改變，所以用var
    global var
    # 也是因為字串內容會改變，所以選擇textvariable = var
    tk.Label(f1, textvariable=var, height = 3).grid(column=0, row=0)

out = []

def click(num):
    global var
    global out
    # 當使用者按C，會清除所有東西
    if(num=='C'):
        var.set('0')
        clear()
    elif(num.isdigit()):
        num = int(num)
        # 還沒有輸入或是已輸入一組數字加上運算符號
        if(len(out)==0 or len(out)==2):
            out.append(num)
        # 要在第一組數字或第二組數字後面加上其他數字
        # e.g. 讓21變成215
        elif(len(out)==1 or len(out)==3):
            # 特例，可能是負數
            if((len(out)==1)and(out[0]=='-')):
                out[0] = num*(-1)
            elif((len(out)==3)and(out[2]=='-')):
                out[2] = num*(-1)
                print(num)
            # 可能會是多個位數的數字
            else:
                temp4 = int(out[(len(out)-1)])
                # 在負數最後面加一位
                if(temp4<0):
                    temp = temp4*10 - num
                # 在正數最後面加一位
                else:
                    temp = temp4*10 + num
                # 轉為str存入out
                out[len(out)-1] = str(temp)

        var.set(out)

    # 輸入的是運算符號（不含=，包含負數的負號）
    elif(num!='='):
        out.append(num)
        var.set(out)
    # 輸入=，開始計算 
    else:
        calculate()
        var.set(out)

def clear():
    global var
    global out
    out.clear()  # 清空out[]
    var.set('0')  # 清空，顯示0

#加減乘除
def calculate():
    global var
    global out
    result1 = int(out[0])
    result2 = int(out[2])
    if(out[1] == '+'):
        ans = result1 + result2
    elif(out[1] == '-'):
        ans = result1 - result2
    elif(out[1] == 'x'):
        ans = result1 * result2
    elif(out[1] == '/'):
        # 分母不可為零
        if(out[2]==0):
            ans = 'ERROR'
        else:
            ans = int(result1/result2)
    # 為了能直接用答案做下一次運算
    # 先清空out，再把ans作為out的第0項
    out.clear()
    out.append(str(ans))
    var.set(out)
  
if __name__ == "__main__":
    # 創造tkinter的物件主視窗
    window = tk.Tk()
    window.title('Lab4')

    f1 = tk.Frame(window)
    f2 = tk.Frame(window)

    # frame.pack() --> 用來指定widget在視窗上的位置
    f1.pack()
    f2.pack()

    var = tk.StringVar()
    # 用來設定var字串變數的值，一開始顯示0
    var.set('0')
    SetValue()  # 使stringVar能成功顯示

    #設定個按鍵位置，包含0~9, +, -, *, /, =, c

    btn7 = tk.Button(f2, text='7', borderwidth=5, width=6, height=2, command=lambda: click('7')).grid(column=0, row=0)
    btn8 = tk.Button(f2, text='8', borderwidth=5, width=6, height=2, command=lambda: click('8')).grid(column=1, row=0)
    btn9 = tk.Button(f2, text='9', borderwidth=5, width=6, height=2, command=lambda: click('9')).grid(column=2, row=0)
    btn_mul = tk.Button(f2, text='x',borderwidth=5, width=6, height=2, command=lambda: click('x')).grid(column=3, row=0)
    
    btn4 = tk.Button(f2, text='4',borderwidth=5, width=6, height=2, command=lambda: click('4')).grid(column=0, row=1)
    btn5 = tk.Button(f2, text='5',borderwidth=5, width=6, height=2, command=lambda: click('5')).grid(column=1, row=1)
    btn6 = tk.Button(f2, text='6',borderwidth=5, width=6, height=2, command=lambda: click('6')).grid(column=2, row=1)
    btn_sub = tk.Button(f2, text='-',borderwidth=5, width=6, height=2, command=lambda: click('-')).grid(column=3, row=1)
    
    btn1 = tk.Button(f2, text='1',borderwidth=5, width=6, height=2, command=lambda: click('1')).grid(column=0, row=2)
    btn2 = tk.Button(f2, text='2',borderwidth=5, width=6, height=2, command=lambda: click('2')).grid(column=1, row=2)
    btn3 = tk.Button(f2, text='3',borderwidth=5, width=6, height=2, command=lambda: click('3')).grid(column=2, row=2)
    btn_add = tk.Button(f2, text='+',borderwidth=5, width=6, height=2, command=lambda: click('+')).grid(column=3, row=2)

    btn0 = tk.Button(f2, text='0',borderwidth=5, width=6, height=2, command=lambda: click('0')).grid(column=0, row=3)
    btn_clear = tk.Button(f2, text='C', borderwidth=5, width=6, height=2, command=lambda: click('C')).grid(column=1, row=3)
    btn_equ = tk.Button(f2, text='=', borderwidth=5, width=6, height=2, command=lambda: click('=')).grid(column=2, row=3)
    btn_div = tk.Button(f2, text='/',borderwidth=5, width=6, height=2, command=lambda: click('/')).grid(column=3, row=3)
    
    window.mainloop()