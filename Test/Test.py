import JELogSystem

if __name__ == '__main__':
    a = JELogSystem.LogSystem()
    a.set_board_cast_lv(2)
    a.normal("0")
    a.info("0")
    a.debug("0")
    a.warning("0")
    a.error("0")
    a.critical("0")
    a.everything_broken("0")
