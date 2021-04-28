#!/bin/bash

# Check if sudo
if [[ "$EUID" = 0 ]]; then
    echo "(1) already root"
else
    sudo -k # make sure to ask for password on next sudo
    if sudo true; then
        echo "(2) correct password"
    else
        echo "(3) wrong password"
        exit 1
    fi
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
        mysql_secure_installation
        read -r -p "Enter the username chosen for MySQL " user
        read -r -p "Enter the password chosen for MySQL " pass
        read -r -p "Enter a database name to use for MySQL " db
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

# Run program now?
read -r -p "Would you like to run the program now? [Y/n] " input
case $input in
    [yY][eE][sS]|[yY])
        echo "Answered yes. Starting on localhost port 8080..."
        python3 roboticsGUI.py
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