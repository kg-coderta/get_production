import os, sys, time
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title(u"Get Production")
root.geometry("800x1000")
root.configure(bg='#CCFFCC')

def GetValueSearchConditions(event):
  search_url = EditBox2.get()
  search_number = EditBox3.get()
  try:
    int_search_number = int(search_number)
    print(search_url)
    print(search_number)
  except ValueError:
    messagebox.showinfo('エラー', '数字を入力してください')
    EditBox2.delete(0,tk.END)
    EditBox3.delete(0,tk.END)

Static1 = tk.Label(root, text=u'自動取得アプリ', font=(u'ＭＳ ゴシック', 25))
Static1.place(x=320, y=10)
Static1.config(bg='#CCFFCC')

Static2 = tk.Label(root, text=u'商品検索URL', font=(u'ＭＳ ゴシック', 18))
Static2.place(x=100, y=70)
Static2.config(bg='#CCFFCC')

EditBox2 = tk.Entry(root, width=45)
EditBox2.place(x=230, y=70)


Static3 = tk.Label(root, text=u'取得件数', font=(u'ＭＳ ゴシック', 18))
Static3.place(x=100, y=110)
Static3.config(bg='#CCFFCC')

EditBox3 = tk.Entry(root, width=10)
EditBox3.place(x=230, y=110)


Button = tk.Button(root, text=u'実行', fg='#333333', height=2, width=10)
Button.config(bg='red')
Button.bind("<Button-1>",GetValueSearchConditions)
Button.place(x=550, y=190)


root.mainloop()