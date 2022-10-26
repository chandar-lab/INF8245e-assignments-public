from otter.test_files import test_case

OK_FORMAT = False

name = "q7.2"
points = 2

@test_case(points=2.0, hidden=False)
def test_q7_2_public_1(numpy, f1_train_svm_best_config_fbow, f1_val_svm_best_config_fbow, f1_test_svm_best_config_fbow, best_C, best_max_iter):
    numpy.testing.assert_allclose(f1_train_svm_best_config_fbow >= 0., 1)
    numpy.testing.assert_allclose(f1_train_svm_best_config_fbow <= 1., 1)
    numpy.testing.assert_allclose(f1_val_svm_best_config_fbow >= 0., 1)
    numpy.testing.assert_allclose(f1_val_svm_best_config_fbow <= 1., 1)
    numpy.testing.assert_allclose(f1_test_svm_best_config_fbow >= 0., 1)
    numpy.testing.assert_allclose(f1_test_svm_best_config_fbow <= 1., 1)
    numpy.testing.assert_allclose(best_C > 0, 1)
    numpy.testing.assert_allclose(best_max_iter > 0, 1)

