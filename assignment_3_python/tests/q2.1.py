OK_FORMAT = True

test = {   'name': 'q2.1',
    'points': 3,
    'suites': [   {   'cases': [   {   'code': '>>> def test_q2_1_public_1(numpy, frequency_bow_train_data, frequency_bow_val_data, frequency_bow_test_data):\n'
                                               '...     numpy.testing.assert_allclose(isinstance(frequency_bow_train_data, (numpy.ndarray, numpy.generic)), 1)\n'
                                               '...     numpy.testing.assert_allclose(frequency_bow_train_data.dtype == float, 1)\n'
                                               '...     numpy.testing.assert_allclose(isinstance(frequency_bow_val_data, (numpy.ndarray, numpy.generic)), 1)\n'
                                               '...     numpy.testing.assert_allclose(frequency_bow_val_data.dtype == float, 1)\n'
                                               '...     numpy.testing.assert_allclose(isinstance(frequency_bow_test_data, (numpy.ndarray, numpy.generic)), 1)\n'
                                               '...     numpy.testing.assert_allclose(frequency_bow_test_data.dtype == float, 1)\n'
                                               '>>> \n',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0.5},
                                   {   'code': '>>> def test_q2_1_public_2(numpy, to_test, vocab):\n'
                                               '...     numpy.testing.assert_allclose(to_test.shape == (1, 1000), 1)\n'
                                               '...     numpy.testing.assert_allclose(numpy.sum(to_test), 1.0)\n'
                                               '...     to_test_array = numpy.zeros(len(vocab))\n'
                                               '...     to_test_array[3] = 0.25\n'
                                               '...     to_test_array[6] = 0.5\n'
                                               '...     to_test_array[10] = 0.25\n'
                                               '...     numpy.testing.assert_allclose(to_test[0], to_test_array)\n'
                                               '>>> \n',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0.5},
                                   {   'code': '>>> def test_q2_1_public_3(numpy, to_test):\n'
                                               '...     numpy.testing.assert_allclose(to_test.shape == (1, 1000), 1)\n'
                                               '...     numpy.testing.assert_allclose(numpy.sum(to_test), 0.0)\n'
                                               '>>> \n',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0.5}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
