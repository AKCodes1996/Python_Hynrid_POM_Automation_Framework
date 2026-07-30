import pytest

from pages import RegisterPage
from utilities import excel_Utility


@pytest.mark.parametrize("p",excel_Utility.read_data_as_list())
def test_Register_with_valid_prod(browser,p):
    RegisterPage.Reg_product(browser,p)
