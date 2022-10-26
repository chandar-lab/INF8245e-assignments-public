OK_FORMAT = True

test = {   'name': 'q4.1',
    'points': 2,
    'suites': [   {   'cases': [   {   'code': '>>> def test_q4_1_public_1(f1_train_bnb_bow, f1_val_bnb_bow, f1_test_bnb_bow):\n'
                                               '...     numpy.testing.assert_allclose(f1_train_bnb_bow >= 0., 1)\n'
                                               '...     numpy.testing.assert_allclose(f1_train_bnb_bow <= 1., 1)\n'
                                               '...     numpy.testing.assert_allclose(f1_val_bnb_bow >= 0., 1)\n'
                                               '...     numpy.testing.assert_allclose(f1_val_bnb_bow <= 1., 1)\n'
                                               '...     numpy.testing.assert_allclose(f1_test_bnb_bow >= 0., 1)\n'
                                               '...     numpy.testing.assert_allclose(f1_test_bnb_bow <= 1., 1)\n'
                                               '>>> \n',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0.5}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
