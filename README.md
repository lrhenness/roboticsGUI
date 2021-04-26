# lrhenness/roboticsGUI

This project aims to create a web GUI front end for operating multiple robots using a stack consiting of the following:

* Web App: Python (PySimpleGUIWeb)
* Database: MySQL
* Robot Control: Arduino

Currently the scope of this project is restrained to bare essentials for functionality to complete tasks for an academic project. Feel free to repurpose or base other PySimpleGUI code on this.

## To Run:

*Only tested on Ubuntu 20.04*
1. Change to whichever directory you want
2. run the following to git clone this repository:

``` sudo git clone https://github.com/lrhenness/roboticsGUI.git ```

3. Run the following to install or update all prerequisites:

``` sudo sh roboticsGUI/prereq.sh ```

4. Make sure your MySQL database is running and you know the username and password for a user with read/write to the "deploy" table in any database.
5. Run the program!

``` echo "Starting..." && python3 roboticsGUI.py ```
