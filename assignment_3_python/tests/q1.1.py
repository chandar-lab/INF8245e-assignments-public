from otter.test_files import test_case

OK_FORMAT = False

name = "q1.1"
points = 2

@test_case(points=0.5, hidden=False)
def test_q1_1_public_1(np, train_data, val_data, test_data):
    np.testing.assert_allclose(isinstance(train_data["reviewText"], pd.Series), 1)
    np.testing.assert_allclose(isinstance(val_data["reviewText"], pd.Series), 1)
    np.testing.assert_allclose(isinstance(test_data["reviewText"], pd.Series), 1)

