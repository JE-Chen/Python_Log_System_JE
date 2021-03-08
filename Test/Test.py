import JELogSystem

if __name__ == '__main__':
    a = JELogSystem.LogSystem()
    a.set_boardcast_lv(2)
    for i in range(1000):
        a.log_normal("0")
        a.log_info("0")
        a.log_debug("0")
        a.log_warning("0")
        a.log_error("0")
        a.log_critical("0")
        a.log_everything_broken("0")
