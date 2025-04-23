import re
import tkinter as tk
from tkinter import filedialog

def remove_onbehalf_extension():
    # Set up tkinter root window (it won't appear)
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Open file dialog for the user to select an extension.js file
    file_path = filedialog.askopenfilename(
        title="Select your extension.js file", 
        filetypes=[("JavaScript Files", "*.js")]
    )

    # Check if the user selected a file
    if file_path:
        print(f"Selected file: {file_path}")
        
        # Define the pattern to remove
        pattern = r'"x-onbehalf-extension-id":\s*`\${.*?}/.*?`'

        # Read the content of the file with UTF-8 encoding (handle potential encoding issues)
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                file_content = file.read()

            # Replace the matched pattern with an empty string (i.e., remove it)
            updated_content = re.sub(pattern, '', file_content)

            # Write the updated content back to the file
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(updated_content)

            print(f"File {file_path} has been updated.")

        except UnicodeDecodeError:
            print(f"Error: Could not read the file {file_path}. It may not be in UTF-8 encoding.")
        except Exception as e:
            print(f"An error occurred: {e}")
    else:
        print("No file selected.")

# Call the function
remove_onbehalf_extension()
