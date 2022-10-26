from otter.test_files import test_case

OK_FORMAT = False

name = "q1.1"
points = 2

@test_case(points=0.25, hidden=False)
def test_q1_1_public_1(numpy, pandas, train_data, val_data, test_data):
    numpy.testing.assert_allclose(isinstance(train_data["reviewText"], pandas.Series), 1)
    numpy.testing.assert_allclose(isinstance(val_data["reviewText"], pandas.Series), 1)
    numpy.testing.assert_allclose(isinstance(test_data["reviewText"], pandas.Series), 1)

@test_case(points=0.25, hidden=False)
def test_q1_1_public_2(numpy, train_data):
    numpy.testing.assert_allclose("." in train_data["reviewText"][0], 0)
    
