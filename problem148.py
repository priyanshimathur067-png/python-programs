def check_loan_eligibility(salary, age, credit_score):

    if age < 21 or age > 60:
        return "Not eligible"

    if salary < 25000:
        return "Salary requirement not satisfied"

    if credit_score < 700:
        return "Credit score too low"

    return "Loan eligible"


salary = 40000
age = 28
credit_score = 750

print(check_loan_eligibility(salary, age, credit_score))