from otter.test_files import test_case

OK_FORMAT = False

name = "q1.2"
points = 2

@test_case(points=0.5, hidden=False)
def test_q1_2_public_1(np, vocab):
    np.testing.assert_allclose(type(vocab) == list, 1)
    np.testing.assert_allclose(len(vocab) == 1000, 1)

