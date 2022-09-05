OK_FORMAT = True

test = {   'name': 'question 2',
    'points': None,
    'suites': [   {   'cases': [   {   'code': '>>> _rng = np.random.default_rng(41)\n'
                                               '>>> _X = _rng.integers(0, 100, 1)\n'
                                               '>>> np.testing.assert_equal(\n'
                                               '...     problem_2(_X),\n'
                                               '...     (np.amax(_X), np.argmax(_X)))\n'
                                               '>>> _X = _rng.integers(0, 100, 20)\n'
                                               '>>> np.testing.assert_equal(\n'
                                               '...     problem_2(_X),\n'
                                               '...     (np.amax(_X), np.argmax(_X)))\n'
                                               '>>> _X = _rng.integers(0, 100, 100)\n'
                                               '>>> np.testing.assert_equal(\n'
                                               '...     problem_2(_X),\n'
                                               '...     (np.amax(_X), np.argmax(_X)))\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
