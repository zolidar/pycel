from pycel.lib.function_helpers import excel_helper
from pycel.excelutil import DIV0

@excel_helper(number_params=(0, 1, 2, 3, 4))
def pmt(rate, nper, pv, fv=0, type=0):
    # Excel reference: https://support.microsoft.com/en-us/office/
    #   pmt-function-0214da64-9a63-4996-bc20-214433fa6441
    if rate == 0:
        if nper == 0:
            return DIV0
        result = -(pv + fv) / nper
    else:
        term = (1 + rate)**nper
        if type == 1:
            result = (fv * rate / (term - 1) + pv * rate / (1 - 1 / term)) / (1 + rate)
        else:
            result = fv * rate / (term - 1) + pv * rate / (1 - 1 / term)
    return result
