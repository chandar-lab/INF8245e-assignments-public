from otter.test_files import test_case

OK_FORMAT = False

name = "q4.2"
points = 2

@test_case(points=0.5, hidden=False)
def test_q4_2_public_1(f1_train_gnb_fbow, f1_val_gnb_fbow, f1_test_gnb_fbow):
    np.testing.assert_allclose(f1_train_gnb_fbow >= 0., 1)
    np.testing.assert_allclose(f1_train_gnb_fbow <= 1., 1)
    np.testing.assert_allclose(f1_val_gnb_fbow >= 0., 1)
    np.testing.assert_allclose(f1_val_gnb_fbow <= 1., 1)
    np.testing.assert_allclose(f1_test_gnb_fbow >= 0., 1)
    np.testing.assert_allclose(f1_test_gnb_fbow <= 1., 1)

