from otter.test_files import test_case

OK_FORMAT = False

name = "q1.3"
points = 2

@test_case(points=0.5, hidden=False)
def test_q1_3_public_1(numpy, binary_bow_train_data, binary_bow_val_data, binary_bow_test_data):
    numpy.testing.assert_allclose(isinstance(binary_bow_train_data, (numpy.ndarray, numpy.generic)), 1)
    numpy.testing.assert_allclose(binary_bow_train_data.dtype == int, 1)
    numpy.testing.assert_allclose(isinstance(binary_bow_val_data, (numpy.ndarray, numpy.generic)), 1)
    numpy.testing.assert_allclose(binary_bow_val_data.dtype == int, 1)
    numpy.testing.assert_allclose(isinstance(binary_bow_test_data, (numpy.ndarray, numpy.generic)), 1)
    numpy.testing.assert_allclose(binary_bow_test_data.dtype == int, 1)

@test_case(points=0.5, hidden=False)
def test_q1_3_public_2(numpy, to_test):
    numpy.testing.assert_allclose(to_test.shape == (1, 1000), 1)
    numpy.testing.assert_allclose(numpy.unique(to_test), numpy.unique([0, 1]))
    numpy.testing.assert_allclose(numpy.where(to_test[0] == 1), numpy.array([[3, 6, 10]]))

