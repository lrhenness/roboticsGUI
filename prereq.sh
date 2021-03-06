#!/bin/bash

# Check if sudo
if [ `whoami` != root ]; then
    echo "Please run this script as root or using sudo."
    exit 1
fi

# MySQL section
read -r -p "Would you like to set up a local MySQL instance with a \"deploy\" table? [Y/n] " input
case $input in
    [yY][eE][sS]|[yY])
        echo "Answered yes. Script will install and configure a local instance of MySQL..."
        sleep 2
        apt update
        apt install -y mysql-server
        mysql -u root -e "CREATE DATABASE roboticsGUI;"
        mysql -u root -D roboticsGUI -e "CREATE TABLE deploy (id int, robot_id text, day_set int, time_start time, time_end time, linear_velocity float, angular_velocity float);"
        mysql -u root -e "CREATE USER 'robotics'@'localhost' IDENTIFIED BY 'GUI';"
        mysql -u root -e "GRANT ALL PRIVILEGES ON * . * TO 'robotics'@'localhost';"
        ;;
    [nN][oO]|[nN])
        echo "Answered no. Continuing..."
        sleep 2
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
    [yY][eE][sS]|[yY])
        echo "             For MySQL:            "
        echo "    Use localhost   for hostname   "
        echo "    Use robotics    for username   "
        echo "    Use GUI         for password   "
        echo "    Use roboticsGUI for database   "
        echo "==================================="
        echo "==============WARNING!============="
        echo "==================================="
        echo "      MySQL is unsecure in the     "
        echo "       current configuration.      "
        echo "  Please run the following to set  "
        echo "        up MySQL securely:         "
        echo "                                   "
        echo "     mysql_secure_installation     "
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