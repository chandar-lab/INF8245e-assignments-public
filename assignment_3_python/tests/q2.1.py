from otter.test_files import test_case

OK_FORMAT = False

name = "q2.1"
points = 3

@test_case(points=0.5, hidden=False)
def test_q2_1_public_1(numpy, frequency_bow_train_data, frequency_bow_val_data, frequency_bow_test_data):
    numpy.testing.assert_allclose(isinstance(frequency_bow_train_data, (numpy.ndarray, numpy.generic)), 1)
    numpy.testing.assert_allclose(frequency_bow_train_data.dtype == float, 1)
    numpy.testing.assert_allclose(isinstance(frequency_bow_val_data, (numpy.ndarray, numpy.generic)), 1)
    numpy.testing.assert_allclose(frequency_bow_val_data.dtype == float, 1)
    numpy.testing.assert_allclose(isinstance(frequency_bow_test_data, (numpy.ndarray, numpy.generic)), 1)
    numpy.testing.assert_allclose(frequency_bow_test_data.dtype == float, 1)

@test_case(points=0.5, hidden=False)
def test_q2_1_public_2(numpy, to_test, vocab):
    numpy.testing.assert_allclose(to_test.shape == (1, 1000), 1)
    numpy.testing.assert_allclose(numpy.sum(to_test), 1.0)
    to_test_array = numpy.zeros(len(vocab))
    to_test_array[3] = 0.25
    to_test_array[6] = 0.5
    to_test_array[10] = 0.25
    numpy.testing.assert_allclose(to_test[0], to_test_array)

@test_case(points=0.5, hidden=False)
def test_q2_1_public_3(numpy, to_test):
    numpy.testing.assert_allclose(to_test.shape == (1, 1000), 1)
    numpy.testing.assert_allclose(numpy.sum(to_test), 0.0)

