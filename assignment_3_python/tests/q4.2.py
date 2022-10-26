OK_FORMAT = True

test = {   'name': 'q4.2',
    'points': 2,
    'suites': [   {   'cases': [   {   'code': '>>> def test_q4_2_public_1(numpy, f1_train_gnb_fbow, f1_val_gnb_fbow, f1_test_gnb_fbow):\n'
                                               '...     numpy.testing.assert_allclose(f1_train_gnb_fbow >= 0., 1)\n'
                                               '...     numpy.testing.assert_allclose(f1_train_gnb_fbow <= 1., 1)\n'
                                               '...     numpy.testing.assert_allclose(f1_val_gnb_fbow >= 0., 1)\n'
                                               '...     numpy.testing.assert_allclose(f1_val_gnb_fbow <= 1., 1)\n'
                                               '...     numpy.testing.assert_allclose(f1_test_gnb_fbow >= 0., 1)\n'
                                               '...     numpy.testing.assert_allclose(f1_test_gnb_fbow <= 1., 1)\n'
                                               '>>> \n',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0.5}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
