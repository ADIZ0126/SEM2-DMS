'''
DMS QUESTION 5
'''
def evaluate_polynomial(coefficients, n):
    result = 0#VARIABLE TO STORE RESULT
    power=1
    for coefficient in coefficients:# enumerate() KEEPS TRACK OF EACH ELEMEMT IN LIST S
        result += coefficient * power
        power*=n

    return result


# Example usage
coefficients = [4,2,9]#WRITING COFFICIENTS IN REVERSED ORDER
n = 5

result = evaluate_polynomial(coefficients, n)# CALLING THE evaluate_polynomial()
print(f"f({n}) = {result}")
