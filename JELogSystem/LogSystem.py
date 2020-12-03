import datetime


class LogSystem:
    """
    預設廣播等級 : 3
    預設紀錄時間
    Normal : 0
    Debug : Debug 1
    Info : Info 2
    Warning : 3
    Error : 4
    Critical : 5
    """

    def __init__(self):

        self.normal_lv = 0

        self.info_lv = 1

        self.debug_lv = 2

        self.warning_lv = 3

        self.error_lv = 4

        self.critical_lv = 5

        self.board_cast_lv = 3

        self.time = True

    # ----------------------------------------------------------------------------------------------
    '''
    Log 種類
    Normal : 普通訊息
    Debug : Debug 用訊息
    Info : Info 特殊訊息
    Warning : 警告訊息
    Error : 錯誤訊息
    Critical : 嚴重錯誤訊息
    '''

    def normal(self, *args):
        self.state(self.normal_lv, self.board_cast_lv, "Log", 'Normal', *args)

    def info(self, *args):
        self.state(self.info_lv, self.board_cast_lv, "Log", 'Info', *args)

    def debug(self, *args):
        self.state(self.debug_lv, self.board_cast_lv, "Log", 'Debug', *args)

    def warning(self, *args):
        self.state(self.warning_lv, self.board_cast_lv, "Log", 'Warning', *args)

    def error(self, *args):
        self.state(self.error_lv, self.board_cast_lv, "Log", 'Error', *args)

    def critical(self, *args):
        self.state(self.critical_lv, self.board_cast_lv, "Log", 'Critical', *args)

    # ----------------------------------------------------------------------------------------------
    # 設置需要廣播的等級
    def set_board_cast_lv(self, Lv):
        if (Lv <= -1):
            self.board_cast_lv = 3
        else:
            self.board_cast_lv = Lv

    # 設置是否顯示時間
    def set_time_able(self, Time_Able):
        self.time = Time_Able

    # ----------------------------------------------------------------------------------------------
    # 用來印出消息
    def state(self, lv1, lv2, log_file_name, error, *args):
        try:
            if lv1 >= lv2 and self.time is True:
                text = ''
                text += (datetime.datetime.now().strftime('%Y:%m:%d:%H:%M:%S') + '\t')
                text += ('\t' + str(error) + ': ' + str(args))
                print("Log in file " + text)
                self.save_log(text, log_file_name)
            elif self.critical_lv >= self.board_cast_lv:
                print("Not log in file ", str(error) + ': ' + str(args))
        except Exception as e:
            print(e)

    # ----------------------------------------------------------------------------------------------
    '''
    Log出消息
    '''

    @staticmethod
    def save_log(error_text, log_name):
        with open(log_name, 'a')as File:
            File.write(error_text + '\n')

    @staticmethod
    def clean_log(log_name):
        with open(log_name, 'w')as File:
            File.write('')
