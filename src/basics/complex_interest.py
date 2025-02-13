def complex_interest(A, b,t):
    principal_amount = A
    rate_interest_amount = b
    time = t
    compound_interest = int(principal_amount * (1 + rate_interest_amount / 100)**time)
    print("compound interest = ", compound_interest)


    ci = principal_amount * (pow((1+rate_interest_amount/100), time))
    print("ci",ci)

res = complex_interest(250000,36,1)