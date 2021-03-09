import threading

import JELogSystem


def log(test):
    for i in range(1000):
        test.log_normal("0")
        test.log_info("0")
        test.log_debug("0")
        test.log_warning("0")
        test.log_error("0")
        test.log_critical("0")
        test.log_everything_broken("0")


if __name__ == '__main__':
    lock = threading.Lock()
    a = JELogSystem.LogSystem(lock)
    b = JELogSystem.LogSystem(lock)
    a.set_boardcast_lv(2)
    b.set_boardcast_lv(2)
    t1 = threading.Thread(target=log(a, ))
    t2 = threading.Thread(target=log(b, ))
