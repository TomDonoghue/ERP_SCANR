"""   """

from erpsc.count import *

#######################################################################################
################################ TESTS - ERPSC - COUNT ################################
#######################################################################################

def test_erpsc_count():
    """Test the ERPSCCount object."""

    # Check that ERPSCCount returns properly
    assert Count()

def test_scrape_test_save():
    """   """

    counts = Count()

    # Add ERPs and terms
    counts.set_erps(['N400', 'P600'])
    counts.set_terms(['language', 'memory'])

    counts.scrape_data()

    assert True

    check_funcs(counts)
    save_func(counts)

def check_funcs(counts):
    """   """

    # Check that all check functions run
    counts.check_cooc_erps()
    counts.check_cooc_terms()
    counts.check_top()
    counts.check_counts('erp')
    counts.check_counts('term')

    assert True

def save_func(counts):
    """   """
    pass
