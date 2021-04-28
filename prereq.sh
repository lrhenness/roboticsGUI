#!/bin/bash

# Check if sudo
if [ `whoami` != root ]; then
    echo "Please run this script as root or using sudo."
    exit 1
fi

# MySQL section
read -r -p "Is MySQL up and running with a \"deploy\" table? [Y/n] " input
case $input in
    [yY][eE][sS]|[yY])
        echo "Answered yes. Continuing..."
        sleep 2
        ;;
    [nN][oO]|[nN])
        echo "Answered no. Script will install and configure a local instance of MySQL..."
        sleep 2
        apt update
        apt install -y mysql-server
        #mysql_secure_installation
        read -r -p "Enter the USERNAME you chose for MySQL " user
        read -r -p "Enter the PASSWORD you chose for MySQL " pass
        read -r -p "Enter a new DATABASE name to use for MySQL " db
        mysql -u $user -p$pass -e "CREATE DATABASE $db;"
        mysql -u $user -p$pass -D $db -e "CREATE TABLE deploy (id int, robot_id text, day_set int, time_start time, time_end time, linear_velocity float, angular_velocity float);"
        ;;
    *)
        echo "Invalid input..."
        exit 1
        ;;
esac

# Dependancy updating/installing
apt update
apt install -y python3 python3-pip
pip3 install pySimpleGUIWeb
pip3 install mysql-connector-python
pip3 install datetime
echo "==================================="
echo "==============SUCCESS!============="
echo "==================================="
echo "    You can now run the program    "
echo "      python3 roboticsGUI.py       "
echo "==================================="
case $input in
    [nN][oO]|[nN])
        echo "             For MySQL:            "
        echo "     Use localhost for hostname    "
        echo "     Use the username, password,   "
        echo "   and database chosen previously. "
        echo "==================================="
        ;;
esac

# Run program now?
read -r -p "Would you like to run the program now? [Y/n] " prog
case $prog in
    [yY][eE][sS]|[yY])
        echo "Answered yes. Starting on localhost port 8080..."
        SCRIPTPATH="$( cd -- "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"
        python3 $SCRIPTPATH/roboticsGUI.py
        ;;
    [nN][oO]|[nN])
        echo "Answered no. Exiting!..."
        exit 1
        ;;
    *)
        echo "Invalid input. Exiting..."
        exit 1
        ;;
esac