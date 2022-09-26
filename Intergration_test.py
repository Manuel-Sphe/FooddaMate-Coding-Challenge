import json
from Expession import Expression
from Equation import Equation
from Solution import Solve

# Opening JSON file
test_cases = open('Intergration_test.json')
  
# returns JSON object as 
# a dictionary
data = json.load(test_cases)
  
# Iterating through the json
# list
print("{:<10} {:<20} {:<25} {:<25} {:<25} {:<10}".format('Test No.','Test Case','Test Input','Expected Output', 'Code Output', 'Result'))
for case in data['test_cases']:
    equation = case["test_input"]
   
    code_output = Solve(equation)
    test_result = "fail"
    if code_output == case["expected_output"]:
        print("pass")
        test_result = "pass"

    print("{:<10} {:<20} {:<25} {:<25} {:<25} {:<10}".format(case["test_number"], case["test_case"], case["test_input"],case["expected_output"], code_output, test_result)) 
  
# Closing file
test_cases.close()