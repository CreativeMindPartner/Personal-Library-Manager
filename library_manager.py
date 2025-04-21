import json
import os

# File to store library data
data_file = 'library.txt'

def load_library():
    """Load library data from library.txt or return an empty list if file doesn't exist."""
    print("Debug: Loading library")  # Debug print
    if os.path.exists(data_file):
        try:
            with open(data_file, 'r') as file:
                return json.load(file)
        except json.JSONDecodeError as e:
            print(f"Error: Invalid JSON in {data_file}. Starting with empty library. ({e})")
            return []
        except Exception as e:
            print(f"Error loading {data_file}: {e}")
            return []
    print(f"Debug: {data_file} not found, starting with empty library")
    return []

def save_library(library):
    """Save library data to library.txt."""
    print("Debug: Saving library")  # Debug print
    try:
        with open(data_file, 'w') as file:
            json.dump(library, file, indent=4)  # Indent for readable JSON
    except Exception as e:
        print(f"Error saving to {data_file}: {e}")

def add_book(library):
    """Add a new book to the library."""
    try:
        title = input("Enter book title: ").strip()
        if not title:
            print("Error: Title cannot be empty.")
            return
        
        author = input("Enter author: ").strip()
        if not author:
            print("Error: Author cannot be empty.")
            return
        
        year = input("Enter publication year: ").strip()
        if not year.isdigit():
            print("Error: Year must be a number.")
            return
        
        genre = input("Enter genre: ").strip()
        if not genre:
            print("Error: Genre cannot be empty.")
            return
        
        read_input = input("Have you read this book? (yes/no): ").strip().lower()
        read = read_input == 'yes'
        if read_input not in ['yes', 'no']:
            print("Error: Please enter 'yes' or 'no'.")
            return

        new_book = {
            "title": title,
            "author": author,
            "year": year,
            "genre": genre,
            "read": read
        }
        library.append(new_book)
        save_library(library)
        print(f'Book "{title}" added successfully!')
    except Exception as e:
        print(f"Error adding book: {e}")

def remove_book(library):
    """Remove a book by title."""
    try:
        title = input("Enter the title of the book to remove: ").strip()
        initial_length = len(library)
        library[:] = [book for book in library if book['title'].lower() != title.lower()]
        if len(library) < initial_length:
            save_library(library)
            print(f'Book "{title}" removed successfully!')
        else:
            print(f'Book "{title}" not found.')
    except Exception as e:
        print(f"Error removing book: {e}")

def search_books(library):
    """Search books by title or author."""
    try:
        search_by = input("Search by title or author: ").strip().lower()
        if search_by not in ['title', 'author']:
            print("Error: Please enter 'title' or 'author'.")
            return
        
        search_term = input(f"Enter the {search_by}: ").strip().lower()
        results = [book for book in library if search_term in book[search_by].lower()]
        
        if results:
            print("\nSearch Results:")
            for book in results:
                status = "Read" if book['read'] else "Unread"
                print(f'{book["title"]} by {book["author"]} ({book["year"]}) - {book["genre"]} - {status}')
        else:
            print("No matching books found.")
    except Exception as e:
        print(f"Error searching books: {e}")

def display_all_books(library):
    """Display all books in the library."""
    try:
        if library:
            print("\nAll Books:")
            for book in library:
                status = "Read" if book['read'] else "Unread"
                print(f'{book["title"]} by {book["author"]} ({book["year"]}) - {book["genre"]} - {status}')
        else:
            print("No books in the library.")
    except Exception as e:
        print(f"Error displaying books: {e}")

def display_statistics(library):
    """Display library statistics."""
    try:
        total_books = len(library)
        read_books = len([book for book in library if book['read']])
        percentage_read = (read_books / total_books * 100) if total_books > 0 else 0
        print(f"\nLibrary Statistics:")
        print(f"Total Books: {total_books}")
        print(f"Books Read: {read_books}")
        print(f"Percentage Read: {percentage_read:.2f}%")
    except Exception as e:
        print(f"Error displaying statistics: {e}")

def main():
    """Main function to run the library manager."""
    print("Debug: Program started")  # Debug print
    try:
        library = load_library()
        while True:
            print("\n=== Personal Library Manager ===", flush=True)
            print("1. Add Book", flush=True)
            print("2. Remove Book", flush=True)
            print("3. Search Books", flush=True)
            print("4. Display All Books", flush=True)
            print("5. Display Statistics", flush=True)
            print("6. Exit", flush=True)

            choice = input("Enter your choice (1-6): ").strip()
            print(f"Debug: User entered choice {choice}")  # Debug print

            if choice == '1':
                add_book(library)
            elif choice == '2':
                remove_book(library)
            elif choice == '3':
                search_books(library)
            elif choice == '4':
                display_all_books(library)
            elif choice == '5':
                display_statistics(library)
            elif choice == '6':
                print("Thank you for using the Library Manager. Goodbye!")
                save_library(library)
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")
    except KeyboardInterrupt:
        print("\nProgram interrupted. Saving library and exiting.")
        save_library(library)
    except Exception as e:
        print(f"Error in main: {e}")

if __name__ == "__main__":
    main()