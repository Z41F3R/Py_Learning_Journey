#!/usr/bin/env python3

tiene_acceso = lambda admin, supervisor: admin or supervisor

acceso = tiene_acceso(True, False)
print(acceso)   

# Con que uno se cumpla la condición, se le dará acceso.
# False or False -> False
# False or True -> True
# True or False -> True
# True or True -> True