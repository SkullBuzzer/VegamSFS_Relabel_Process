import inspect
import logging


class LogGen:
    @staticmethod
    def getLogger():
        name = inspect.stack()[1][3]
        logger = logging.getLogger(name)
        fileHandler = logging.FileHandler("C:\\Users\\Dell\\PycharmProjects\\VegamSFS_Relabel_Process\\Logs"
                                          "\\Automation_Relabel.log")
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.INFO)
        return logger
