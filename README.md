# FoondaMate-Coding-Challenge

The backend flask app is an api that allows get requests with equation as params and send bank a json data with steps of solving the equation.

Move to the backend directory and run the following commands:

## Creating a virtual environment (Windows)

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

Run the following command:

```
$ python3 Solution.py
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
