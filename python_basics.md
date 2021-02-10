# Get Ready for Python 

Program python on VSCode 
1. Install Python extension in 
2. python3 --version
3. Right click on editor and you can run whole file in terminal, or select few line and run etc

## set default python to python3  if it is python27
Add below line to ~/.bashrc
```sh
alias python=python3
```
to see commands specific to python27, e.g. to get version of python 2 prefix python with command
```sh
$ command python --version
```

## Update Python (say from 3.6 to 3.8)
Install it 
```sh
$ sudo apt update -y
$ sudo apt install python3.8
```
and set 3.6 and 3.8 as alternative
```sh
$ sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.6 1
$ sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.8 2
```
Select the option(index for python 3.8) from list of alternatives what one can get by running 
```sh
sudo update-alternatives --config python3
```

## Debugging
1. Set breakpoint using F9 or click same as visual studio
2. Initialize debugger usign F5, select Python file for now.
3. F10, F11 , Shift + F11, F5, Shift + F5 works same as visusal studio
4. Ctrl + Shift + F5 restarts the app
### Use Debug Console 
Explore and work with variable using Debug Console. Open Debug Console tab and write variable/expression on `>` prompt

### Configure debug information 
launch.json is the standard name for a file containing debugging configurations.

1. Run (Ctrl + Shift + D) also gives a link to create launch.json
2. Create launch.json, which will go to folder .vscode/ in cur directory



## Install python packages
1. pip3 install numpy
2. sudo apt-get install python3-matplotlib

# TODO:
Python : Add example to take argument from command line 
https://www.tutorialspoint.com/python/python_command_line_arguments.htm

## Reference 
https://code.visualstudio.com/docs/editor/variables-reference
https://www.tutorialspoint.com/python/python_command_line_arguments.htm