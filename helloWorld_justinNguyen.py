import keyboard # This line imports a keyboard package, a crucial component of this code. ~~~~~~~~~~~~~~~~~

import time # This line imports the time package, which would help prevent spamming any key to be detected.

design = -1 #~~~~~~~~~~~~~~~~~ This sets a value to a variable that would be used later on. ~~~~~~~~~~~~~~~
designStatus = "Disabled" #~~~ This variable would be used for a specific text later. ~~~~~~~~~~~~~~~~~~~~~

while True: # Line 8 keeps the code running until broken. ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    if keyboard.is_pressed("M"): # This line detects whether "M" is pressed on the keyboard. ~~~~~~~~~~~~~~
        design = design * -1 # This is the way that the design variable can alternate convieniently ~~~~~~~
        if design == 1: # This checks for a value of 1. It is like setting design to true but with numbers.
            designStatus = "Enabled" # The text is set to enable, to be displayed to the user later. ~~~~~~
        if design == -1: # Design is checked for a value of -1. This is like using an else statement but ~~
            designStatus = "Disabled" # that didn't work. As for this line, the opposite of Line 13 ~~~~~~~
        print("Aesthetic Mode: " + designStatus) # This shows the user whether aesthetic mode is on or off.
        time.sleep(0.25) # This line should curtail, at least to some degree, spamming of the key. ~~~~~~~~

    if keyboard.is_pressed("J"): # In this block, the actual "Hello World!" printing begins. ~~~~~~~~~~~~~~
        if design == 1: # This nested if statement would be if Aesthetic Mode is on. ~~~~~~~~~~~~~~~~~~~~~~
            print("") # This is to skip a line, in case the inputed "J" is visible in the output GUI. ~~~~~
            print("") # Here, an additional space is made. ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            print("|+<++><++><++><++><++><++><++><++><++><++><++><++>+|") # This prints the top of the box.
            print("| Hello World!                                     |") # This is the goal of the HW. ~~~
            print("|                                                  |") # Adds a space between lines. ~~~
            print("| This prints \"Hello World!\" in 2 different ways,  |") # Description. ~~~~~~~~~~~~~~~~
            print("| according to specific conditions.                |") # Continued sentence. ~~~~~~~~~~~
            print("|                                                  |") # Another filler for looks. ~~~~~
            print("| Developer: Justin Nguyen                         |") # Developer Name. ~~~~~~~~~~~~~~~
            print("| File Created: 05/06/2025                         |") # File creation date. ~~~~~~~~~~~
            print("| Last Edited On: 05/06/2025                       |") # Latest edit date. ~~~~~~~~~~~~~
            print("|+<++><++><++><++><++><++><++><++><++><++><++><++>+|") # Bottom of the box. ~~~~~~~~~~~~
            break # This line ends the program. ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        if design == -1: # The alternate print is produced by this block of code for Aesthetic Mode off. ~~
            print("") # This again is space filler like those in Lines 21-22. ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            print("") # This adds a space between the potential typed letter and the message to be printed.
            print("Hello World!") # Finally, the two words you've been waiting for! ~~~~~~~~~~~~~~~~~~~~~~~
            print("The words, \"Hello World\" are printed in 2 ways, based on certain conditions.") # Desc.
            print("Justin Nguyen made this on May 6th, 2025 and edited it also on May 6th, 2025.") # Dev. ~
            break # The code comes to its conclusion with these five letters. Did you enjoy the ride? ~~~~~
