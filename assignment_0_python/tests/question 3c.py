OK_FORMAT = True

test = {   'name': 'question 3c',
    'points': None,
    'suites': [   {   'cases': [   {   'code': '>>> pd.testing.assert_frame_equal(\n'
                                               '...     problem_3c(df_city_pop),\n'
                                               "...     df_city_pop.melt(id_vars=['city', 'country'], var_name='year', value_name='population') \\\n"
                                               "...             .groupby(['country', 'year']) \\\n"
                                               "...             .apply(lambda group_df: pd.Series({ 'population': np.sum(group_df['population']) })) \\\n"
                                               '...             .reset_index() \\\n'
                                               "...             .pivot(index='country', columns='year', values='population'))\n",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
