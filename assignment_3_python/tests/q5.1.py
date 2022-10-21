OK_FORMAT = True

test = {   'name': 'q5.1',
    'points': 2,
    'suites': [   {   'cases': [   {   'code': '>>> np.testing.assert_allclose(f1_train_dt_best_config_bow >= 0., 1)\n'
                                               '>>> np.testing.assert_allclose(f1_train_dt_best_config_bow <= 1., 1)\n'
                                               '>>> np.testing.assert_allclose(f1_val_dt_best_config_bow >= 0., 1)\n'
                                               '>>> np.testing.assert_allclose(f1_val_dt_best_config_bow <= 1., 1)\n'
                                               '>>> np.testing.assert_allclose(f1_test_dt_best_config_bow >= 0., 1)\n'
                                               '>>> np.testing.assert_allclose(f1_test_dt_best_config_bow <= 1., 1)\n'
                                               '>>> np.testing.assert_allclose(best_max_depth > 0, 1)\n',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0.0}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
