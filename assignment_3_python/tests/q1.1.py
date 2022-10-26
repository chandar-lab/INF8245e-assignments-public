OK_FORMAT = True

test = {   'name': 'q1.1',
    'points': 2,
    'suites': [   {   'cases': [   {   'code': '>>> def test_q1_1_public_1(numpy, train_data, val_data, test_data):\n'
                                               '...     numpy.testing.assert_allclose(isinstance(train_data["reviewText"], pandas.Series), 1)\n'
                                               '...     numpy.testing.assert_allclose(isinstance(val_data["reviewText"], pandas.Series), 1)\n'
                                               '...     numpy.testing.assert_allclose(isinstance(test_data["reviewText"], pandas.Series), 1)\n'
                                               '>>> \n',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0.5}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
