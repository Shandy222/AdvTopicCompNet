def cryptocurrency():
    options = ["Y", "N"]
    a = input("Are cryptocurrency transactions required? (Y / N)\n")
    while a not in options:
        a = input("Invalid answer. Are cryptocurrency transactions required? (Y / N)\n")
    
    return a

def privacy():
    options = ["Y", "N"]
    a = input("Is privacy needed? (Y / N)\n")
    while a not in options:
        a = input("Invalid answer. Is privacy needed?\n")
    
    return a

def contractconditions():
    options = ["Y", "N"]
    a = input("Is guaranteed execution of contact condtions required? (Y / N)\n")
    while a not in options:
        a = input("Invalid answer. Is guaranteed execution of contact condtions required?\n")
    
    return a

def governance():
    options = ["Decentralized", "Consortium", "Centralized"]
    a = input("Governanace type? (Decentralized / Consortium / Centralized)\n")
    while a not in options:
        a = input("Invalid answer. Governanace type? (Decentralized / Consortium / Centralized)\n")
    
    return a

def paymentsize():
    options = ["Y", "N"]
    a = input("Are there large payments? (Y / N)\n")
    while a not in options:
        a = input("Invalid answer. Are there large payments? (Y / N)\n")
    
    return a

def ELCmaturity():
    options = ["Efficiency & low cost", "Maturity"]
    a = input("Efficiency & low cost versus maturity? (Efficiency & low cost / Maturity)\n")
    while a not in options:
        a = input("Invalid answer. Efficiency & low cost versus maturity? (Efficiency & low cost / Maturity)\n")
    
    return a

def Ematurity():
    options = ["Efficiency", "Maturity"]
    a = input("Efficiency VS maturity? (Efficiency / Maturity)\n")
    while a not in options:
        a = input("Invalid answer. Efficiency VS maturity? (Efficiency / Maturity)\n")
    
    return a

def Framework():
    print(cryptocurrency())

Framework()
