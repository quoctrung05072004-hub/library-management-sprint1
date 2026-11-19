import tkinter as tk
from tkinter import messagebox
from library_system.repository import BookRepository
from library_system.service import BookService
from library_system.search import BookSearch

class LibraryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sprint 1 Mini - Quản lý thư viện")
        self.repo = BookRepository("library.db")
        self.service = BookService(self.repo)
        self.search = BookSearch(self.repo)
        self.entries = {}
        for row, (key, label) in enumerate((
            ("title", "Tên sách"), ("author", "Tác giả"), ("isbn", "ISBN")
        )):
            tk.Label(root, text=label).grid(row=row, column=0, padx=10, pady=5, sticky="w")
            self.entries[key] = tk.Entry(root, width=45)
            self.entries[key].grid(row=row, column=1, padx=10, pady=5)
        tk.Button(root, text="Thêm sách", command=self.add_book).grid(row=3, column=1, pady=8)
        tk.Label(root, text="Từ khóa tìm tên sách").grid(row=4, column=0, padx=10)
        self.search_entry = tk.Entry(root, width=45)
        self.search_entry.grid(row=4, column=1, pady=6)
        tk.Button(root, text="Tìm sách", command=self.find_books).grid(row=5, column=1, pady=4)
        tk.Button(root, text="Xem tất cả sách", command=self.show_all).grid(row=6, column=1, pady=4)
        self.results = tk.Listbox(root, width=72, height=10)
        self.results.grid(row=7, column=0, columnspan=2, padx=10, pady=10)
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        self.show_all()

    def add_book(self):
        try:
            self.service.add_book(**{key: entry.get() for key, entry in self.entries.items()})
        except ValueError as exc:
            messagebox.showerror("Không thêm được sách", str(exc))
            return
        messagebox.showinfo("Thành công", "Đã thêm sách mới")
        for entry in self.entries.values():
            entry.delete(0, tk.END)
        self.show_all()

    def fill_results(self, books):
        self.results.delete(0, tk.END)
        for book in books:
            self.results.insert(tk.END, f"{book.id}. {book.title} — {book.author} — ISBN: {book.isbn}")
        if not books:
            self.results.insert(tk.END, "Không tìm thấy sách nào")

    def find_books(self):
        self.fill_results(self.search.search_by_title(self.search_entry.get()))

    def show_all(self):
        self.fill_results(self.repo.get_all())

    def close(self):
        self.repo.close()
        self.root.destroy()

if __name__ == "__main__":
    window = tk.Tk()
    LibraryApp(window)
    window.mainloop()
