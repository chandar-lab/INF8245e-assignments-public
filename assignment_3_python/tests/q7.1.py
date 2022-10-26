from otter.test_files import test_case

OK_FORMAT = False

name = "q7.1"
points = 2

@test_case(points=2.0, hidden=False)
def test_q7_1_public_1(numpy, f1_train_svm_best_config_bow, f1_val_svm_best_config_bow, f1_test_svm_best_config_bow, best_C, best_max_iter):
    numpy.testing.assert_allclose(f1_train_svm_best_config_bow >= 0., 1)
    numpy.testing.assert_allclose(f1_train_svm_best_config_bow <= 1., 1)
    numpy.testing.assert_allclose(f1_val_svm_best_config_bow >= 0., 1)
    numpy.testing.assert_allclose(f1_val_svm_best_config_bow <= 1., 1)
    numpy.testing.assert_allclose(f1_test_svm_best_config_bow >= 0., 1)
    numpy.testing.assert_allclose(f1_test_svm_best_config_bow <= 1., 1)
    numpy.testing.assert_allclose(best_C > 0, 1)
    numpy.testing.assert_allclose(best_max_iter > 0, 1)

