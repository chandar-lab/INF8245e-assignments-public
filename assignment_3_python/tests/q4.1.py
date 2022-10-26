from otter.test_files import test_case

OK_FORMAT = False

name = "q4.1"
points = 2

@test_case(points=0.5, hidden=False)
def test_q4_1_public_1(numpy, f1_train_bnb_bow, f1_val_bnb_bow, f1_test_bnb_bow):
    numpy.testing.assert_allclose(f1_train_bnb_bow >= 0., 1)
    numpy.testing.assert_allclose(f1_train_bnb_bow <= 1., 1)
    numpy.testing.assert_allclose(f1_val_bnb_bow >= 0., 1)
    numpy.testing.assert_allclose(f1_val_bnb_bow <= 1., 1)
    numpy.testing.assert_allclose(f1_test_bnb_bow >= 0., 1)
    numpy.testing.assert_allclose(f1_test_bnb_bow <= 1., 1)

