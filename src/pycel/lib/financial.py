from pycel.lib.function_helpers import excel_helper
from pycel.excelutil import DIV0, NUM_ERROR
import numpy as np
import numpy_financial as npf

@excel_helper(number_params=(0, 1, 2, 3, 4))
def pmt(rate, nper, pv, fv=0, type=0):
    # Excel reference: https://support.microsoft.com/en-us/office/
    #   pmt-function-0214da64-9a63-4996-bc20-214433fa6441
    # return -pv * rate / (1 - power(1 + rate, -nper))
    try:
        if type == 0:
            result = npf.pmt(
                float(rate), float(nper), float(pv), fv=float(fv), when='end')
        else:
            result = npf.pmt(
                float(rate), float(nper), float(pv), fv=float(fv), when='begin')
        if np.isnan(result):
            return NUM_ERROR
        return result
    except (ZeroDivisionError, ValueError):
        return NUM_ERROR
