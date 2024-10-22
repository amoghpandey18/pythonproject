import tkinter as tk
from tkinter import messagebox, simpledialog

class Library:
    def __init__(self):
        self.books = ["Dune by Frank Herbert",
                      "A Brief History of Time",
                      "Geronimo Stilton: The Mummy with No Name",
                      "Harry Potter and the Chamber of Secrets",
                      "Robin Sharma: Who Will Cry When You Die"]
        self.issued_books = {}

    def add_book(self, book_name):
        self.books.append(book_name)

    def display_books(self):
        return self.books

    def issue_book(self, book_name, user):
        if book_name in self.books:
            self.books.remove(book_name)
            self.issued_books[book_name] = user
            return True
        return False

    def return_book(self, book_name):
        if book_name in self.issued_books:
            user = self.issued_books.pop(book_name)
            self.books.append(book_name)
            return user
        return None

    def issued_books_list(self):
        return self.issued_books


class LibraryGUI:
    def __init__(self, root, library):
        self.library = library
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("400x400")

        # Buttons and Labels for the GUI
        self.label = tk.Label(self.root, text="Library Management System", font=('Arial', 16))
        self.label.pack(pady=10)

        self.add_button = tk.Button(self.root, text="Add Book", command=self.add_book)
        self.add_button.pack(pady=5)

        self.display_button = tk.Button(self.root, text="Display All Books", command=self.display_books)
        self.display_button.pack(pady=5)

        self.issue_button = tk.Button(self.root, text="Issue Book", command=self.issue_book)
        self.issue_button.pack(pady=5)

        self.return_button = tk.Button(self.root, text="Return Book", command=self.return_book)
        self.return_button.pack(pady=5)

        self.issued_button = tk.Button(self.root, text="View Issued Books", command=self.view_issued_books)
        self.issued_button.pack(pady=5)

        self.exit_button = tk.Button(self.root, text="Exit", command=self.root.quit)
        self.exit_button.pack(pady=5)

    def add_book(self):
        book_name = simpledialog.askstring("Add Book", "Enter the name of the book:")
        if book_name:
            self.library.add_book(book_name)
            messagebox.showinfo("Success", f"'{book_name}' has been added to the library.")

    def display_books(self):
        books = self.library.display_books()
        if books:
            book_list = "\n".join(books)
            messagebox.showinfo("Available Books", f"Books in the Library:\n{book_list}")
        else:
            messagebox.showinfo("No Books", "No books are currently available in the library.")

    def issue_book(self):
        book_name = simpledialog.askstring("Issue Book", "Enter the name of the book to issue:")
        user = simpledialog.askstring("User", "Enter the name of the user:")
        if book_name and user:
            if self.library.issue_book(book_name, user):
                messagebox.showinfo("Success", f"'{book_name}' has been issued to {user}.")
            else:
                messagebox.showwarning("Error", f"'{book_name}' is not available or has already been issued.")

    def return_book(self):
        book_name = simpledialog.askstring("Return Book", "Enter the name of the book to return:")
        if book_name:
            user = self.library.return_book(book_name)
            if user:
                messagebox.showinfo("Success", f"'{book_name}' has been returned by {user}.")
            else:
                messagebox.showwarning("Error", f"'{book_name}' was not issued.")

    def view_issued_books(self):
        issued_books = self.library.issued_books_list()
        if issued_books:
            issued_list = "\n".join([f"'{book}' issued to {user}" for book, user in issued_books.items()])
            messagebox.showinfo("Issued Books", f"Issued Books:\n{issued_list}")
        else:
            messagebox.showinfo("No Issued Books", "No books have been issued.")


def main():
    root = tk.Tk()
    library = Library()
    app = LibraryGUI(root, library)
    root.mainloop()


if __name__ == "__main__":
    main()
