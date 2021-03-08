import JELogSystem

if __name__ == '__main__':
    log = JELogSystem.LogSystem()
    log.load_setting('setting.je')
    log.log_critical("0")
    log.log_everything_broken("0")
