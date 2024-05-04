import math
from pycel.excelutil import NUM_ERROR
import pytest
from pycel.lib.financial import pmt

@pytest.mark.parametrize(
    'data, result', (
        ((0.14,7,112347,0,0), -26198.8),
        ((0.08 / 12, 10, 10000,0,0), -1037.03),
        ((0.08 / 12, 10, 10000,0,1), -1030.164),
    )
)
def test_pmt(data, result):
    assert math.isclose(pmt(*data), result, rel_tol=1e-3)


def test_pmt_error():
    assert pmt(0,0,0) == NUM_ERROR
    assert pmt(0,0,10000) == NUM_ERROR

