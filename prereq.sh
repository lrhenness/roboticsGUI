#!/bin/bash

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
