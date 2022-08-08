import os
import sys
import directories

#note to self
#tried making a shortcut based off of a working profile shortcut and seemed to completly break from the exe line 
#can't even unbreak it now
#related website https://www.addictivetips.com/ubuntu-linux-tips/create-application-menu-shortcuts-linux/
#also the problem that the create shortcut used by both profile and shortcut code so fixing the method 
#for one script breaks the other 

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

