OK_FORMAT = True

test = {   'name': 'q1.3',
    'points': 2,
    'suites': [   {   'cases': [   {   'code': '>>> def test_q1_3_public_1(binary_bow_train_data, binary_bow_val_data, binary_bow_test_data):\n'
                                               '...     numpy.testing.assert_allclose(isinstance(binary_bow_train_data, (numpy.ndarray, numpy.generic)), 1)\n'
                                               '...     numpy.testing.assert_allclose(binary_bow_train_data.dtype == int, 1)\n'
                                               '...     numpy.testing.assert_allclose(isinstance(binary_bow_val_data, (numpy.ndarray, numpy.generic)), 1)\n'
                                               '...     numpy.testing.assert_allclose(binary_bow_val_data.dtype == int, 1)\n'
                                               '...     numpy.testing.assert_allclose(isinstance(binary_bow_test_data, (numpy.ndarray, numpy.generic)), 1)\n'
                                               '...     numpy.testing.assert_allclose(binary_bow_test_data.dtype == int, 1)\n'
                                               '>>> \n',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0.5},
                                   {   'code': '>>> def test_q1_3_public_2(to_test):\n'
                                               '...     numpy.testing.assert_allclose(to_test.shape == (1, 1000), 1)\n'
                                               '...     numpy.testing.assert_allclose(numpy.unique(to_test), numpy.unique([0, 1]))\n'
                                               '...     numpy.testing.assert_allclose(numpy.where(to_test[0] == 1), numpy.array([[3, 6, 10]]))\n'
                                               '>>> \n',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0.5}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
