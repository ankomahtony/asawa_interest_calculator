import numpy as np

def AFV(amount, type, int, year):
    if type == "Compound":
        return amount * ((1 + (int) / 100) ** year)
    else:
        return amount * (1 + (int / 100) * year)

def APV(amount, type, int, year):
    if type == "Compound":
        return amount / ((1 + (int) / 100) ** year)
    else:
        return amount / (1 + (int / 100) * year) 

def interestRate(pv, fv, type, year):
    if type == "Compound":
        return ((fv / pv)**(1/year)) - 1
    else:
        return (fv - pv) / (year * pv)


def yearsExpected(pv, fv, type, int):
    if type == "Compound":
        return (np.log(fv / pv) / np.log(1 + int))
    else:
        return (fv - pv) / (int * pv)
