import tkinter as tk

def select_items(listbox, indices):
    # Bỏ chọn tất cả các mục trước khi chọn mục mới
    listbox.selection_clear(0, tk.END)
    
    # Chọn các mục dựa trên các chỉ số cho trước
    for index in indices:
        listbox.select_set(index)

# Hàm để in ra các mục đã được chọn
def show_selected_items():
    selected_indices = listbox.curselection()  # Lấy các chỉ số của các mục đã chọn
    selected_items = [listbox.get(i) for i in selected_indices]  # Lấy nội dung của các mục đã chọn
    print("Selected items:", selected_items)

# Khởi tạo cửa sổ chính
root = tk.Tk()
root.title("Select Specific Items in Listbox")
root.geometry("300x200")

# Tạo Listbox với chế độ chọn nhiều mục
listbox = tk.Listbox(root, selectmode=tk.MULTIPLE, width=30, height=10)
listbox.pack(pady=10)

# Thêm các mục vào Listbox
items = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5",
         "Item 6", "Item 7", "Item 8", "Item 9", "Item 10"]

for item in items:
    listbox.insert(tk.END, item)

# Chọn các mục theo chỉ số cho trước
indices_to_select = [1, 3, 5]  # Chọn các mục thứ 2, 4 và 6 (chỉ số bắt đầu từ 0)
select_items(listbox, indices_to_select)

# Tạo nút để hiển thị các mục đã chọn
button = tk.Button(root, text="Show Selected Items", command=show_selected_items)
button.pack(pady=10)

root.mainloop()
