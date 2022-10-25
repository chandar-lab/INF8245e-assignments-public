OK_FORMAT = True

test = {   'name': 'q2.1',
    'points': 3,
    'suites': [   {   'cases': [   {   'code': '>>> np.testing.assert_allclose(isinstance(frequency_bow_train_data, (np.ndarray, np.generic)), 1)\n'
                                               '>>> np.testing.assert_allclose(frequency_bow_train_data.dtype == float, 1)\n'
                                               '>>> np.testing.assert_allclose(isinstance(frequency_bow_val_data, (np.ndarray, np.generic)), 1)\n'
                                               '>>> np.testing.assert_allclose(frequency_bow_val_data.dtype == float, 1)\n'
                                               '>>> np.testing.assert_allclose(isinstance(frequency_bow_test_data, (np.ndarray, np.generic)), 1)\n'
                                               '>>> np.testing.assert_allclose(frequency_bow_test_data.dtype == float, 1)\n',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0.0},
                                   {   'code': '>>> to_test = frequency_bow(np.array(["this is is a randomword"]), vocab)\n'
                                               '>>> np.testing.assert_allclose(to_test.shape == (1, 1000), 1)\n'
                                               '>>> np.testing.assert_allclose(np.sum(to_test), 1.0)\n'
                                               '>>> to_test_array = np.zeros(len(vocab))\n'
                                               '>>> to_test_array[3] = 0.25\n'
                                               '>>> to_test_array[6] = 0.5\n'
                                               '>>> to_test_array[10] = 0.25\n'
                                               '>>> np.testing.assert_allclose(to_test[0], to_test_array)\n',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0.5},
                                   {   'code': '>>> to_test = frequency_bow(np.array(["randomword anotherrandomword"]), vocab)\n'
                                               '>>> np.testing.assert_allclose(to_test.shape == (1, 1000), 1)\n'
                                               '>>> np.testing.assert_allclose(np.sum(to_test), 0.0)\n',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0.5}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
