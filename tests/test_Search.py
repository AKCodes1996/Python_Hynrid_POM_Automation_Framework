import pytest

from pages import  SearchPage
from utilities import excel_Utility


@pytest.mark.parametrize("p",excel_Utility.read_data_as_list())
def test_search_with_valid_prod(browser,p):
   # SearchPage.Search_product(browser, p)

