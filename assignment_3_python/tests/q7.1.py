OK_FORMAT = True

test = {   'name': 'q7.1',
    'points': 2,
    'suites': [   {   'cases': [   {   'code': '>>> def test_q7_1_public_1(f1_train_svm_best_config_bow, f1_val_svm_best_config_bow, f1_test_svm_best_config_bow, best_C, best_max_iter):\n'
                                               '...     numpy.testing.assert_allclose(f1_train_svm_best_config_bow >= 0., 1)\n'
                                               '...     numpy.testing.assert_allclose(f1_train_svm_best_config_bow <= 1., 1)\n'
                                               '...     numpy.testing.assert_allclose(f1_val_svm_best_config_bow >= 0., 1)\n'
                                               '...     numpy.testing.assert_allclose(f1_val_svm_best_config_bow <= 1., 1)\n'
                                               '...     numpy.testing.assert_allclose(f1_test_svm_best_config_bow >= 0., 1)\n'
                                               '...     numpy.testing.assert_allclose(f1_test_svm_best_config_bow <= 1., 1)\n'
                                               '...     numpy.testing.assert_allclose(best_C > 0, 1)\n'
                                               '...     numpy.testing.assert_allclose(best_max_iter > 0, 1)\n'
                                               '>>> \n',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 2.0}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
