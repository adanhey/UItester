import datetime
import logging


class TestLogger:
    def __init__(self):
        self.nowTime = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        self.logger = logging.getLogger("uweb_reference")
        self.logger.setLevel(logging.DEBUG)
        self.file_url = logging.FileHandler("./%stestLog.log" % self.nowTime, mode="a+",
                                            encoding="utf8")
        self.logger.addHandler(self.file_url)

    def log_event(self, title, data=""):
        self.logger.debug(f"-->{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        self.logger.debug(f"{title}：{data}")

