def payslip(employee, hours_worked):
    hourly_rate = employee["hourly_rate"]
    standard_hours = min(hours_worked, 40)
    overtime_hours = max(hours_worked - 40, 0)
    gross = standard_hours * hourly_rate + overtime_hours * hourly_rate * 1.5

    weekly_allowance = 240
    taxable = max(gross - weekly_allowance, 0)
    basic_band = 700
    if taxable <= basic_band:
        income_tax = taxable * 0.2
    else:
        income_tax = basic_band * 0.2 + (taxable - basic_band) * 0.4

    insurance_threshold = 242
    national_insurance = max(gross - insurance_threshold, 0) * 0.12

    pension = 0
    if employee["pension_opt_in"]:
        pension = gross * 0.05

    student_loan = 0
    if employee["student_loan"]:
        repayment_threshold = 480
        if gross > repayment_threshold:
            student_loan = (gross - repayment_threshold) * 0.09

    deductions = income_tax + national_insurance + pension + student_loan
    net = gross - deductions

    lines = [
        f"Payslip for {employee['name']}",
        f"Hours: {standard_hours} standard, {overtime_hours} overtime",
        f"Gross pay: {gross:.2f}",
        f"Income tax: {income_tax:.2f}",
        f"National insurance: {national_insurance:.2f}",
    ]
    if pension:
        lines.append(f"Pension: {pension:.2f}")
    if student_loan:
        lines.append(f"Student loan: {student_loan:.2f}")
    lines.append(f"Net pay: {net:.2f}")
    return "\n".join(lines)
