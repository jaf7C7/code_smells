from payroll import payslip


def employee(**overrides):
    defaults = {"name": "Ada", "hourly_rate": 20, "pension_opt_in": False, "student_loan": False}
    return {**defaults, **overrides}


def value(slip, label):
    for line in slip.splitlines():
        if line.startswith(label + ":"):
            return line.split(":", 1)[1].strip()
    return None


def test_names_the_employee():
    assert payslip(employee(), 40).splitlines()[0] == "Payslip for Ada"


def test_standard_week_is_paid_at_hourly_rate():
    assert value(payslip(employee(), 40), "Gross pay") == "800.00"


def test_overtime_is_paid_at_time_and_a_half():
    slip = payslip(employee(), 45)
    assert value(slip, "Hours") == "40 standard, 5 overtime"
    assert value(slip, "Gross pay") == "950.00"


def test_basic_rate_tax_on_income_above_allowance():
    assert value(payslip(employee(), 40), "Income tax") == "112.00"


def test_higher_rate_tax_on_income_above_basic_band():
    assert value(payslip(employee(hourly_rate=30), 40), "Income tax") == "244.00"


def test_national_insurance_above_threshold():
    assert value(payslip(employee(), 40), "National insurance") == "66.96"


def test_pension_is_deducted_only_when_opted_in():
    assert value(payslip(employee(), 40), "Pension") is None
    assert value(payslip(employee(pension_opt_in=True), 40), "Pension") == "40.00"


def test_student_loan_is_repaid_above_threshold():
    assert value(payslip(employee(), 40), "Student loan") is None
    assert value(payslip(employee(student_loan=True), 40), "Student loan") == "28.80"


def test_net_pay_is_gross_less_all_deductions():
    slip = payslip(employee(pension_opt_in=True, student_loan=True), 40)
    assert value(slip, "Net pay") == "552.24"
