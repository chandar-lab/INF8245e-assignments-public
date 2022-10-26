OK_FORMAT = True

test = {   'name': 'q6.2',
    'points': 2,
    'suites': [   {   'cases': [   {   'code': '>>> def test_q6_2_public_1(f1_train_lr_best_config_fbow, f1_val_lr_best_config_fbow, f1_test_lr_best_config_fbow, best_C, best_max_iter):\n'
                                               '...     numpy.testing.assert_allclose(f1_train_lr_best_config_fbow >= 0., 1)\n'
                                               '...     numpy.testing.assert_allclose(f1_train_lr_best_config_fbow <= 1., 1)\n'
                                               '...     numpy.testing.assert_allclose(f1_val_lr_best_config_fbow >= 0., 1)\n'
                                               '...     numpy.testing.assert_allclose(f1_val_lr_best_config_fbow <= 1., 1)\n'
                                               '...     numpy.testing.assert_allclose(f1_test_lr_best_config_fbow >= 0., 1)\n'
                                               '...     numpy.testing.assert_allclose(f1_test_lr_best_config_fbow <= 1., 1)\n'
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
