OK_FORMAT = True

test = {   'name': 'question 3a',
    'points': None,
    'suites': [   {   'cases': [   {   'code': '>>> pd.testing.assert_frame_equal(\n'
                                               '...     problem_3a(df_city_pop),\n'
                                               "...     df_city_pop.melt(id_vars=['city', 'country'], var_name='year', value_name='population'))\n",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
