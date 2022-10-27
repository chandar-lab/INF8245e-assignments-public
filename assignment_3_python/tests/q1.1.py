from otter.test_files import test_case

OK_FORMAT = False

name = "q1.1"
points = 2

@test_case(points=0.5, hidden=False)
def test_q1_1_public_1(numpy, pandas, remove_punctuation):
    _tmp = remove_punctuation(pandas.Series(data=["This. is a test?!"]))
    numpy.testing.assert_allclose(isinstance(_tmp, pandas.Series), 1)
    numpy.testing.assert_allclose(_tmp.tolist() == ["This is a test"], 1)
    
@test_case(points=0.5, hidden=False)
def test_q1_1_public_2(numpy, pandas, set_to_lower_case):
    _tmp = set_to_lower_case(pandas.Series(data=["This IS a TeST"]))
    numpy.testing.assert_allclose(isinstance(_tmp, pandas.Series), 1)
    numpy.testing.assert_allclose(_tmp.tolist() == ["this is a test"], 1)
    
