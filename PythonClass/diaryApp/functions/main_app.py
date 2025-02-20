from functions.diary import Diary

def main_application():
    user_name = input("Enter your name: ").strip()
    if not user_name:
        print("Name cannot be empty, Exiting application.")
        return

    password = input("Enter your password: ").strip()
    if not password:
        print("Password cannot be empty, Exiting application.")
        return

    diary = Diary(user_name, password)

    diary.unlock_diary(password)
    if diary.is_locked():
        print("Unable to unlock your diary, Exiting application.")
        return
    else:
        print("Diary unlocked successfully!")

    while True:
        print("\n===== Main Menu ===== ")
        print("1. Create a new entry")
        print("2. Update an existing entry")
        print("3. Delete an existing entry")
        print("4. View all entries")
        print("5. Lock diary")
        print("6. Unlock diary")
        print("7. Exit")
        choice = input("Enter your choice (1-7): ").strip()

        if choice == '1':
            title = input("Enter entry title: ").strip()
            body = input("Enter entry body: ").strip()
            try:
                diary.create_entry(title, body)
                print("Entry created successfully.")
            except Exception as e:
                print("Error:", e)

        elif choice == '2':
            try:
                update_id = int(input("Enter the ID of the entry to update: ").strip())
                new_title = input("Enter new title: ").strip()
                new_body = input("Enter new body: ").strip()
                diary.update_entry(update_id, new_title, new_body)
                print("Entry updated successfully.")
            except Exception as e:
                print("Error:", e)

        elif choice == '3':
            try:
                delete_id = int(input("Enter the ID of the entry to delete: ").strip())
                diary.delete_entry(delete_id)
                print("Entry deleted successfully.")
            except Exception as e:
                print("Error:", e)

        elif choice == '4':
            try:
                view_id = int(input("Enter the ID of the entry to view: ").strip())
                entry = diary.find_entry_by_id(view_id)
                if entry:
                    details = (
                        f"ID: {entry.id}\n"
                        f"Title: {entry.title}\n"
                        f"Body: {entry.body}\n"
                        f"Created On: {entry.time}\n"
                    )
                    print(details)
                else:
                    print("No entry found with that ID.")
            except Exception as e:
                print("Error:", e)

        elif choice == '5':
            diary.lock_diary()
            print("Diary has been locked.")

        elif choice == '6':
            unlock_pass = input("Enter the password to unlock your diary: ").strip()
            try:
                diary.unlock_diary(unlock_pass)
                if diary.is_locked():
                    print("Incorrect password, Diary remains locked.")
                else:
                    print("Diary unlocked successfully!")
            except ValueError as e:
                print("Error unlocking diary: ", e)
        elif choice == '7':
            print("Exiting the Diary App, Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == '__main__':
    main_application()