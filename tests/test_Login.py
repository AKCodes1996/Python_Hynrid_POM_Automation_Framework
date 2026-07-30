
import pytest

from pages import  LoginPage
from utilities import excel_Utility

@pytest.mark.parametrize("p",excel_Utility.read_data_as_list())
def test_Login_with_valid_prod(browser,p):
    LoginPage.Login_product(browser,p)







