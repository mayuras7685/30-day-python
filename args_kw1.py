"""
we use the “*” notation like this – *args OR **kwargs – as our function’s argument when we have doubts about the number of  arguments we should pass in a function.” 
"""
def funargs(normal, *args, **kw):
  print(normal)
  for item in args:
    print(item)
  print("Every individual role:\n")
  for key, value in roles.items():
    print(f"{key} is {value}")
normal = "This is our company pillars"
names = ["Mayur", "Deep", "Viraj", "Vir"]
roles = {"Mayue" : "MD", "Deep" : "Marketing Head", "Viraj" : "Manufacturing", "Vir": "SDE"}
funargs(*names, **roles)
"""
output:
Mayur
Deep
Viraj
Vir
"""
#output after normal and **kw argument
"""
output:
This is our company pillars

Deep
Viraj
Vir
Every individual role:        

Mayue is MD
Deep is Marketing Head        
Viraj is Manufacturing        
Vir is SDE
"""