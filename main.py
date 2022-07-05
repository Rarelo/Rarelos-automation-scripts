import os
import sys
import directories

## add project subfolders as module locations
sys.path.insert(0,directories.LINUX)
sys.path.insert(0,directories.WINDOWS)

import commonmethods
import linuxmethods

def main():
    '''top level function code'''
    print("")
    ###operating system check + exit code
    operating_system = commonmethods.get_operating_system()
    if operating_system == None:
        print("Exiting...")
        return None
    if operating_system == 'linux':
        user_choice = commonmethods.choose_script(operating_system)
        #print(type(user_choice))
        if user_choice == '1':
            linuxmethods.create_firefox_profile()
        if user_choice == '2':
            linuxmethods.create_linux_shortcut()
## code body
main()

