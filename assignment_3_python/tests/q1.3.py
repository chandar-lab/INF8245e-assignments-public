OK_FORMAT = True

test = {   'name': 'q1.3',
    'points': 2,
    'suites': [   {   'cases': [   {   'code': '>>> np.testing.assert_allclose(isinstance(binary_bow_train_data, (np.ndarray, np.generic)), 1)\n'
                                               '>>> np.testing.assert_allclose(binary_bow_train_data.dtype == int, 1)\n'
                                               '>>> np.testing.assert_allclose(isinstance(binary_bow_val_data, (np.ndarray, np.generic)), 1)\n'
                                               '>>> np.testing.assert_allclose(binary_bow_val_data.dtype == int, 1)\n'
                                               '>>> np.testing.assert_allclose(isinstance(binary_bow_test_data, (np.ndarray, np.generic)), 1)\n'
                                               '>>> np.testing.assert_allclose(binary_bow_test_data.dtype == int, 1)\n',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0.0},
                                   {   'code': '>>> to_test = binary_bow(np.array(["this is is a randomword"]), vocab)\n'
                                               '>>> np.testing.assert_allclose(to_test.shape == (1, 1000), 1)\n'
                                               '>>> np.testing.assert_allclose(np.unique(to_test), np.unique([0, 1]))\n'
                                               '>>> np.testing.assert_allclose(np.where(to_test[0] == 1), np.array([[3, 6, 10]]))\n',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 1.0}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
