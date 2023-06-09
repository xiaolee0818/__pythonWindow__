'''
#專案在學習grid的編排
'''
import tkinter as tk
from tkinter import ttk


class Window(tk.Tk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        ttkStyle = ttk.Style()
        ttkStyle.theme_use('default')
        ttkStyle.configure('red.TFrame', background='#ff0000')
        ttkStyle.configure('white.TFrame', background='#ffffff')
        ttkStyle.configure('yellow.TFrame', background='yellow')
        ttkStyle.configure('white.TLabel', background='#ffffff')
        ttkStyle.configure('gridLabel.TLabel', font=(
            'Helvetica', 16), foreground='#666666')
        ttkStyle.configure('gridEntry.TEntry', font=('Helvetica', 16))

        mainFrame = ttk.Frame(self)
        mainFrame.pack(expand=True, fill=tk.BOTH, padx=30, pady=30)

        topFrame = ttk.Frame(mainFrame, height=100)
        topFrame.pack(fill=tk.X)

        ttk.Label(topFrame, text="BMI試算", font=(
            'Helvetica', '20')).pack(pady=20)

        bottomFrame = ttk.Frame(mainFrame)
        bottomFrame.pack(expand=True, fill=tk.BOTH)
        bottomFrame.columnconfigure(0, weight=3, pad=20)
        bottomFrame.columnconfigure(1, weight=5, pad=20)
        bottomFrame.rowconfigure(0, weight=1, pad=20)
        bottomFrame.rowconfigure(3, weight=1, pad=20)
        bottomFrame.rowconfigure(4, weight=1, pad=20)
        bottomFrame.rowconfigure(5, weight=1, pad=20)
        bottomFrame.rowconfigure(6, weight=1, pad=20)

        ttk.Label(bottomFrame, text="姓名:", style='gridLabel.TLabel').grid(
            column=0, row=0, sticky=tk.E)
        self.nameEntry = ttk.Entry(bottomFrame, style='gridEntry.TEntry')
        self.nameEntry.grid(column=1, row=0, sticky=tk.W, padx=10)

        ttk.Label(bottomFrame, text="出生年月日:", style='gridLabel.TLabel').grid(
            column=0, row=1, sticky=tk.E)
        ttk.Label(bottomFrame, text="(2000/03/01)",
                  style='gridLabel.TLabel').grid(column=0, row=2, sticky=tk.E)

        self.birthEntry = ttk.Entry(bottomFrame, style='gridEntry.TEntry')
        self.birthEntry.grid(column=1, row=1, sticky=tk.W, rowspan=2, padx=10)

        ttk.Label(bottomFrame, text="身高(cm):", style='gridLabel.TLabel').grid(
            column=0, row=3, sticky=tk.E)
        self.heightEntry = ttk.Entry(bottomFrame, style='gridEntry.TEntry')
        self.heightEntry.grid(column=1, row=3, sticky=tk.W, padx=10)
        self.heightEntry.insert(1, '180')  # default value

        ttk.Label(bottomFrame, text="體重(kg):", style='gridLabel.TLabel').grid(
            column=0, row=4, sticky=tk.E)
        self.weightEntry = ttk.Entry(bottomFrame, style='gridEntry.TEntry')
        self.weightEntry.grid(column=1, row=4, sticky=tk.W, padx=10)
        self.weightEntry.insert(1, '100')  # default value

        self.messageText = tk.Text(
            bottomFrame, height=5, width=35, state=tk.NORMAL, takefocus=0, bd=0)
        self.messageText.grid(column=0, row=5, sticky=tk.N+tk.S, columnspan=2)

        self.commitBtn = ttk.Button(bottomFrame, text="計算", command=self.bmi)
        self.commitBtn.grid(column=1, row=6, sticky=tk.W)

    def bmi(self):
        # 公式 BMI = kg / (m*m)
        bmi_set = round(float(self.weightEntry.get()) /
                        (float(self.heightEntry.get())*float(self.heightEntry.get()))*10000, 2)
        if bmi_set >= 30:
            result = bmi_set
            abc = '重度肥胖'
        elif bmi_set >= 28:
            result = bmi_set
            abc = '肥胖'
        elif bmi_set >= 24:
            result = bmi_set
            abc = '超重'
        elif bmi_set >= 18.5:
            result = bmi_set
            abc = '正常'
        else:
            result = bmi_set
            abc = '偏瘦'

        self.messageText.insert(tk.END, '您的BMI值為：%s\n' % result)
        self.messageText.insert(tk.END, abc + '\n')


def main():
    '''
    這是程式的執行點
    '''
    window = Window()
    window.title("BMI計算")
    # window.geometry("400x500")
    window.mainloop()


if __name__ == "__main__":
    main()
