import os
from rb_tree import insert, search, get_height, get_size, get_black_height

def main():
    root = None
    print("=== English Dictionary using Red-Black Tree ===\n")

    # Get the exact folder where this Python file is saved
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Create the full path to the dictionary file
    dict_path = os.path.join(script_dir, "dictionary.txt")

    while True:
        print("\n1. Load Dictionary")
        print("2. Insert Word")
        print("3. Look-up a Word")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ").strip()

        # Option 1: Load Dictionary
        if choice == "1":
            try:
                # Open the file using the full path we created above
                with open(dict_path, "r", encoding="utf-8") as file:
                    for line in file:
                        word = line.strip()
                        if word:
                            root = insert(root, word)
                print("Dictionary loaded successfully!")

                if root:
                    print("Size:", get_size(root))
                    print("Height:", get_height(root))
                    print("Black Height:", get_black_height(root))
                    
            except FileNotFoundError:
                print("dictionary.txt not found. Starting with empty dictionary.")
            except Exception:
                print("Error loading dictionary file.")

        # Option 2: Insert Word
        elif choice == "2":
            word = input("Enter the word to insert: ").strip()
            
            # Check if the user entered nothing
            if not word:
                print("Word cannot be empty!")
                continue

            # Check if the word already exists in the tree
            if search(root, word) is not None:
                print("ERROR: Word already in the dictionary!")
            else:
                # Insert the new word into the tree
                root = insert(root, word)
                
                # Add the new word to the text file using the full path
                with open(dict_path, "a", encoding="utf-8") as file:
                    file.write(word + "\n")
                
                print("Word inserted successfully!")
                
                # Print tree details after insertion
                print("Size:", get_size(root))
                print("Height:", get_height(root))
                print("Black Height:", get_black_height(root))

        # Option 3: Look-up a Word
        elif choice == "3":
            word = input("Enter the word to look up: ").strip()
            
            # Search for the word in the tree
            if search(root, word) is not None:
                print("YES")
            else:
                print("NO")

        # Option 4: Exit
        elif choice == "4":
            print("Goodbye!")
            break

        # If the user enters a wrong number
        else:
            print("Invalid choice! Please enter 1, 2, 3 or 4.")

# Run the program
main()
