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

        self.__normal_lv = 0

        self.__info_lv = 1

        self.__debug_lv = 2

        self.__warning_lv = 3

        self.__error_lv = 4

        self.__critical_lv = 5

        self.__everything_broken = 10

        self.__board_cast_lv = 3

        self.__time = True

    # ----------------------------------------------------------------------------------------------
    '''
    Log 種類
    Normal : 普通訊息 Normal Message
    Debug : Debug 用訊息 Debug Message
    Info : Info 特殊訊息 Info Message
    Warning : 警告訊息 Warning Message
    Error : 錯誤訊息 Error Message
    Critical : 嚴重錯誤訊息 Critical Message
    everything_broken : 甚麼都毀了 Never want Message
    '''

    def normal(self, *args) -> str:
        return self.state(self.__normal_lv, self.__board_cast_lv, "Log", 'Normal', *args)

    def info(self, *args) -> str:
        return self.state(self.__info_lv, self.__board_cast_lv, "Log", 'Info', *args)

    def debug(self, *args) -> str:
        return self.state(self.__debug_lv, self.__board_cast_lv, "Log", 'Debug', *args)

    def warning(self, *args) -> str:
        return self.state(self.__warning_lv, self.__board_cast_lv, "Log", 'Warning', *args)

    def error(self, *args) -> str:
        return self.state(self.__error_lv, self.__board_cast_lv, "Log", 'Error', *args)

    def critical(self, *args) -> str:
        return self.state(self.__critical_lv, self.__board_cast_lv, "Log", 'Critical', *args)

    def everything_broken(self, *args) -> str:
        return self.state(self.__everything_broken, self.__board_cast_lv, "Log", 'everything_broken', *args)

    # ----------------------------------------------------------------------------------------------
    # 設置需要廣播的等級
    def set_board_cast_lv(self, lv: int) -> int:
        if lv <= -1:
            self.__board_cast_lv = 3
            return -1
        else:
            self.__board_cast_lv = lv
            return self.__board_cast_lv

    # 設置是否顯示時間
    def set_time_able(self, time_able: bool) -> bool:
        self.__time = time_able
        return self.__time

        # ----------------------------------------------------------------------------------------------

    # 用來印出消息
    def state(self, lv1: int, lv2: int, log_file_name: str, error: str, *args) -> str:

        try:
            if lv1 >= lv2 and self.__time is True:
                text = ''
                text += (datetime.datetime.now().strftime('%Y:%m:%d:%H:%M:%S') + ':')
                text += (str(error) + ':' + str(args))
                print("Log in file " + text)
                self.save_log(text, log_file_name)
                return "Log in file " + text
            elif self.__critical_lv >= self.__board_cast_lv:
                print("Not log in file", str(error) + ':' + str(args))
                return "Not log in file " + str(error) + ':' + str(args)
        except Exception as e:
            print(e)
        return "Not Run"

    # ----------------------------------------------------------------------------------------------
    '''
    Log出消息
    '''

    @staticmethod
    def save_log(error_text: str, log_name: str) -> str:
        with open(log_name, 'a')as File:
            File.write(error_text + '\n')
        return error_text + log_name

    @staticmethod
    def clean_log(log_name: str) -> str:
        with open(log_name, 'w')as File:
            File.write('')
        return log_name
