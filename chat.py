import tkinter as tk

# Khởi tạo cửa sổ chính
root = tk.Tk()
root.title("Center Button Example with pack()")
root.geometry("400x300")

# Tạo một Frame
frame = tk.Frame(root)
frame.pack(expand=True, fill='both')  # Giãn rộng Frame để lấp đầy không gian trống

# Tạo Button và đặt vào giữa Frame
button = tk.Button(frame, text="This is a button")
button.pack(expand=True)  # Giãn rộng Button để căn giữa theo chiều ngang và chiều dọc

root.mainloop()
