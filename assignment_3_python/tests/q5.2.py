OK_FORMAT = True

test = {   'name': 'q5.2',
    'points': 2,
    'suites': [   {   'cases': [   {   'code': '>>> def test_q5_2_public_1(numpy, f1_train_dt_best_config_fbow, f1_val_dt_best_config_fbow, f1_test_dt_best_config_fbow, best_max_depth):\n'
                                               '...     numpy.testing.assert_allclose(f1_train_dt_best_config_fbow >= 0., 1)\n'
                                               '...     numpy.testing.assert_allclose(f1_train_dt_best_config_fbow <= 1., 1)\n'
                                               '...     numpy.testing.assert_allclose(f1_val_dt_best_config_fbow >= 0., 1)\n'
                                               '...     numpy.testing.assert_allclose(f1_val_dt_best_config_fbow <= 1., 1)\n'
                                               '...     numpy.testing.assert_allclose(f1_test_dt_best_config_fbow >= 0., 1)\n'
                                               '...     numpy.testing.assert_allclose(f1_test_dt_best_config_fbow <= 1., 1)\n'
                                               '...     numpy.testing.assert_allclose(best_max_depth > 0, 1)\n'
                                               '>>> \n',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 2.0}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
