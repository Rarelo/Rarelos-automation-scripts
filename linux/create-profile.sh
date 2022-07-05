#! /bin/bash

### Go to the firefox application directory and copy the settings from the default profile to the new one

#echo "profile_name: $1";
#echo "$1";

#go to home directory
cd
home="$(pwd)"
#echo $home

#save home directory as var $home
cd $home/.mozilla/firefox #go to
#firefox="$(pwd)" #save firefox directory

#save vars for default folder and destination new_profile folder
default="$(find . -maxdepth 1 -name "*default*" -print)"
new_profile="$(find . -maxdepth 1 -name "*$1*" -print)"

echo $default
echo $new_profile

cp -r $default/* $new_profile
