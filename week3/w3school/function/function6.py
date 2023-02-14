"""
If you do not know how many keyword arguments that will be passed into your function
add two asterisk: ** before the parameter name in the function definition.
"""

def my_function(**kid):
  print("His last name is " + kid["fname"])

my_function(fname = "Tobias", lname = "Refsnes")