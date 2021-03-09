import threading
import unittest

import JELogSystem


class TestLogSystem(unittest.TestCase):

    def test_set_broadcast_lv(self):
        for num in range(5):
            lock = threading.Lock()
            self.assertEqual(JELogSystem.LogSystem(lock).set_boardcast_lv(num), num)

    def test_log(self):
        boardcast = 0
        lock = threading.Lock()
        JELogSystem.LogSystem(lock).set_boardcast_lv(boardcast)
        self.assertNotEqual(JELogSystem.LogSystem(lock).log_normal(), "Not Run")
        self.assertNotEqual(JELogSystem.LogSystem(lock).log_info(), "Not Run")
        self.assertNotEqual(JELogSystem.LogSystem(lock).log_debug(), "Not Run")
        self.assertNotEqual(JELogSystem.LogSystem(lock).log_warning(), "Not Run")
        self.assertNotEqual(JELogSystem.LogSystem(lock).log_error(), "Not Run")
        self.assertNotEqual(JELogSystem.LogSystem(lock).log_critical(), "Not Run")
        self.assertNotEqual(JELogSystem.LogSystem(lock).log_everything_broken(), "Not Run")


if __name__ == '__main__':
    suite = (unittest.TestLoader().loadTestsFromTestCase(TestLogSystem))
    unittest.TextTestRunner(verbosity=2).run(suite)
