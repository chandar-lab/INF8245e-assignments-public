OK_FORMAT = True

test = {   'name': 'q6.1',
    'points': 2,
    'suites': [   {   'cases': [   {   'code': '>>> np.testing.assert_allclose(f1_train_lr_best_config_bow >= 0., 1)\n'
                                               '>>> np.testing.assert_allclose(f1_train_lr_best_config_bow <= 1., 1)\n'
                                               '>>> np.testing.assert_allclose(f1_val_lr_best_config_bow >= 0., 1)\n'
                                               '>>> np.testing.assert_allclose(f1_val_lr_best_config_bow <= 1., 1)\n'
                                               '>>> np.testing.assert_allclose(f1_test_lr_best_config_bow >= 0., 1)\n'
                                               '>>> np.testing.assert_allclose(f1_test_lr_best_config_bow <= 1., 1)\n'
                                               '>>> np.testing.assert_allclose(best_C > 0, 1)\n'
                                               '>>> np.testing.assert_allclose(best_max_iter > 0, 1)\n',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0.5}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
