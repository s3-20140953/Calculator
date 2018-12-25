import Tkinter as tk

window = tk.Tk()
window.title('Calculator')

display = tk.Entry(window).grid(columnspan = 5 , row = 0)
tk.Button(window, text = '7').grid(column = 0 , row = 1)
tk.Button(window, text = '8').grid(column = 1 , row = 1)
tk.Button(window, text = '9').grid(column = 2 , row = 1)
tk.Button(window, text = 'C').grid(column = 3 , columnspan = 2, row = 1)
tk.Button(window, text = '4').grid(column = 0 , row = 2)
tk.Button(window, text = '5').grid(column = 1 , row = 2)
tk.Button(window, text = '6').grid(column = 2 , row = 2)
tk.Button(window, text = 'X').grid(column = 3 , row = 2)
tk.Button(window, text = '/').grid(column = 4 , row = 2)
tk.Button(window, text = '1').grid(column = 0 , row = 3)
tk.Button(window, text = '2').grid(column = 1 , row = 3)
tk.Button(window, text = '3').grid(column = 2 , row = 3)
tk.Button(window, text = '+').grid(column = 3 , row = 3, rowspan = 2)
tk.Button(window, text = '-').grid(column = 4 , row = 3)
tk.Button(window, text = '0').grid(column = 0 , columnspan = 2, row = 4)
tk.Button(window, text = '.').grid(column = 2 , row = 4)
tk.Button(window, text = '=').grid(column = 4 , row = 4)

window.mainloop()