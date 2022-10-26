OK_FORMAT = True

test = {   'name': 'q1.2',
    'points': 2,
    'suites': [   {   'cases': [   {   'code': '>>> def test_q1_2_public_1(numpy, vocab):\n'
                                               '...     numpy.testing.assert_allclose(type(vocab) == list, 1)\n'
                                               '...     numpy.testing.assert_allclose(len(vocab) == 1000, 1)\n'
                                               '>>> \n',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0.5}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
