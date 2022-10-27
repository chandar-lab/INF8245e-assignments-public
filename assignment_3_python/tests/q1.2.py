from otter.test_files import test_case

OK_FORMAT = False

name = "q1.2"
points = 2

@test_case(points=1.0, hidden=False)
def test_q1_2_public_1(numpy, pandas, pick_most_frequent_words):
    _tmp = pick_most_frequent_words(pandas.Series(data=["apple orange apple"]), vocab_size=1)
    numpy.testing.assert_allclose(isinstance(_tmp, list), 1)
    numpy.testing.assert_allclose(_tmp == ["apple"], 1)

