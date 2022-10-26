from otter.test_files import test_case

OK_FORMAT = False

name = "q1.3"
points = 2

@test_case(points=0.5, hidden=False)
def test_q1_3_public_1(binary_bow_train_data, binary_bow_val_data, binary_bow_test_data):
    np.testing.assert_allclose(isinstance(binary_bow_train_data, (np.ndarray, np.generic)), 1)
    np.testing.assert_allclose(binary_bow_train_data.dtype == int, 1)
    np.testing.assert_allclose(isinstance(binary_bow_val_data, (np.ndarray, np.generic)), 1)
    np.testing.assert_allclose(binary_bow_val_data.dtype == int, 1)
    np.testing.assert_allclose(isinstance(binary_bow_test_data, (np.ndarray, np.generic)), 1)
    np.testing.assert_allclose(binary_bow_test_data.dtype == int, 1)

@test_case(points=0.5, hidden=False)
def test_q1_3_public_2(to_test):
    np.testing.assert_allclose(to_test.shape == (1, 1000), 1)
    np.testing.assert_allclose(np.unique(to_test), np.unique([0, 1]))
    np.testing.assert_allclose(np.where(to_test[0] == 1), np.array([[3, 6, 10]]))

