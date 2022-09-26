# FoondaMate-Coding-Challenge

App Command Line Inteface Python Solution For Solving Linear Equations of type ax+b = dx+e 

Open a Command Line(Terminal on UNIX, CMD on Windows- can use the Subsys for Linux Terminal) clone this repo 
```
$git clone https://github.com/Manuel-Sphe/FooddaMate-Coding-Challenge.git
```
Go To the Project's Directory
```
$ cd FooddaMate-Coding-Challenge
```



## Creating a virtual environment (Windows) so that you can run the correct python version

Initialiaze the environment folder:
```
$ virtualenv.exe venv
```

If virtualenv is not found run
```
$ pip install virtualenv.exe
```

Activate the virtual environment:
```
$ source venv/Scripts/activate
```

## Creating a virtual environment (MACOS or Linux)

Activate the environment folder:
```
$ python3 -m venv venv
```

Activate the virtual environment:
```
$ . venv/bin/activate
```


## Running the backend

Run the following command to try solve an equation of your choice:

```
$ python3 Solution.py
```

To run Intergration Tests
```
$python3 Intergration_test.py
```

To run the Unit Tests
```
$python3 Unit_test.py
```



## CLI Classes Structure 
```
.
|──── Solution.py
|──── Equation.py
|──── Expression.py
|──── Intergration_test.py
|──── Intergration_test.json
|──── Unit_test.py
|──── README.md
