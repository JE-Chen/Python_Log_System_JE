import unittest

import JELogSystem


class TestLogSystem(unittest.TestCase):

    def test_set_broadcast_lv(self):
        for num in range(5):
            self.assertEqual(JELogSystem.LogSystem().set_board_cast_lv(num), num)

    def test_log(self):
        boardcast = 0
        JELogSystem.LogSystem().set_board_cast_lv(boardcast)
        self.assertNotEqual(JELogSystem.LogSystem().normal(), "Not Run")
        self.assertNotEqual(JELogSystem.LogSystem().info(), "Not Run")
        self.assertNotEqual(JELogSystem.LogSystem().debug(), "Not Run")
        self.assertNotEqual(JELogSystem.LogSystem().warning(), "Not Run")
        self.assertNotEqual(JELogSystem.LogSystem().error(), "Not Run")
        self.assertNotEqual(JELogSystem.LogSystem().critical(), "Not Run")
        self.assertNotEqual(JELogSystem.LogSystem().everything_broken(), "Not Run")


if __name__ == '__main__':
    suite = (unittest.TestLoader().loadTestsFromTestCase(TestLogSystem))
    unittest.TextTestRunner(verbosity=2).run(suite)
