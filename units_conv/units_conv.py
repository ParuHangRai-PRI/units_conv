import math

def si(val):
    if isinstance(val, str):
        val = float(val)
    exponent = 0
    Hunits = {
        0: "",
        3: "K",
        6: "M",
        9: "G",
        12: "T",
        15: "P"
    }
    Lunits = {
        3: "m",
        6: "u",
        9: "n",
        12: "p",
        15: "f"
    }
    keys = list(Hunits)
    keys1 = list(Lunits)
    if(val >= 1):
        val = val/10
        while val > 1:
            val = val/10
            exponent = exponent + 1
        for i in range(6):
            if(exponent<=keys[i]):
                if(exponent%3==0):
                    return f"{val*10}"+" "+Hunits[keys[i]]
                else:
                    return f"{val* math.pow(10,exponent%3+1):.3f}"+" "+Hunits[keys[i-1]]
    else:
        while val < 1:
            val = val*10
            exponent = exponent - 1
        for i in range(5):
            if(abs(exponent)<=keys1[i]):
                    return f"{val*pow(10,exponent%3):.3f}"+" "+Lunits[keys1[i]]

def res(val):
    res = si(val) + "Ohm"
    return(res)

def cap(val):
    cap = si(val) + "F"
    return(cap)

def ind(val):
    cap = si(val) + "H"
    return(cap)

def volts(val):
    cap = si(val) + "V"
    return(cap)

def amps(val):
    cap = si(val) + "A"
    return(cap)

def freq(val):
    cap = si(val) + "Hz"
    return(cap)

def valufy(arg): 
    unit = ""
    val = ""
    si_vals = {
        "K": 3,
        "k": 3,
        "M": 6,
        "G": 9,
        "g": 9,
        "T": 12,
        "t": 12,
        "m": -3,
        "u": -6,
        "n": -9,
        "p": -12,
        "f": -15,
    }
    keys = list(si_vals)
    for ltr in arg:
        if(ltr.isalpha()):
            unit = unit + ltr 
        else:
            val = val + ltr  
    for units in keys:
        if units == unit[0]:
            return float(val)*pow(10,si_vals[units])
        
    return float(val) 