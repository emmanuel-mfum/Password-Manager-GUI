# Password-Manager-GUI
Password manager program made with Python and the  Tkinter module.

This program allows the user to save his credetnials for different websites on his computer.
To run this program, simply make sure that all 3 files are in the same directory and run the main.py file.
A window should pop up asking the user to insert the website name and password. There is already an email address filling the email field.
However, the user can simply replace the email in the statement email_entry.insert(0, "abc@gmail.com") by his own.
The user must also enter a password, or generate a strong password that will automatically fill the password field, by clicking on the "Generate Password" button

Clicking on the "Generate Password" button also copies the password generated by the program onto the user's clipboard thanks to the Python module Pyperclip.
The user then can click on the button "Add" to save his credentials on a .txt file called "data.txt". There is already some data in it due to tests I made on this program.
Simply erase it if you fee like it.

