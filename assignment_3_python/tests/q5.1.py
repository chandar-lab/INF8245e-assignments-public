from otter.test_files import test_case

OK_FORMAT = False

name = "q5.1"
points = 2

@test_case(points=2.0, hidden=False)
def test_q5_1_public_1(f1_train_dt_best_config_bow, f1_val_dt_best_config_bow, f1_test_dt_best_config_bow, best_max_depth):
    np.testing.assert_allclose(f1_train_dt_best_config_bow >= 0., 1)
    np.testing.assert_allclose(f1_train_dt_best_config_bow <= 1., 1)
    np.testing.assert_allclose(f1_val_dt_best_config_bow >= 0., 1)
    np.testing.assert_allclose(f1_val_dt_best_config_bow <= 1., 1)
    np.testing.assert_allclose(f1_test_dt_best_config_bow >= 0., 1)
    np.testing.assert_allclose(f1_test_dt_best_config_bow <= 1., 1)
    np.testing.assert_allclose(best_max_depth > 0, 1)

