from otter.test_files import test_case

OK_FORMAT = False

name = "q6.1"
points = 2

@test_case(points=2.0, hidden=False)
def test_q6_1_public_1(f1_train_lr_best_config_bow, f1_val_lr_best_config_bow, f1_test_lr_best_config_bow, best_C, best_max_iter):
    np.testing.assert_allclose(f1_train_lr_best_config_bow >= 0., 1)
    np.testing.assert_allclose(f1_train_lr_best_config_bow <= 1., 1)
    np.testing.assert_allclose(f1_val_lr_best_config_bow >= 0., 1)
    np.testing.assert_allclose(f1_val_lr_best_config_bow <= 1., 1)
    np.testing.assert_allclose(f1_test_lr_best_config_bow >= 0., 1)
    np.testing.assert_allclose(f1_test_lr_best_config_bow <= 1., 1)
    np.testing.assert_allclose(best_C > 0, 1)
    np.testing.assert_allclose(best_max_iter > 0, 1)

