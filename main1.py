"""
What does the if __name__ == “__main__”: do?
Before executing code, Python interpreter reads source file and define few special variables/global variables. 
If the python interpreter is running that module (the source file) as the main program, it sets the special __name__ variable to have a value “__main__”. If this file is being imported from another module, __name__ will be set to the module's name. Module's name is available as value to __name__ global variable. 
"""
def prinmay(string):
  return f'this is string {string}'

def add(num1, num2):
  return num1+ num2 +5

if __name__ == '__main__' :

  print(prinmay("Mayur"))
  o = add(6,4)
  print(o)
