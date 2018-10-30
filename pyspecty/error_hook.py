import os
import inspect
import webbrowser
from singleton_decorator import singleton

@singleton
class PySpecty:
    """This class is responsible for all the management, data layer and processing."""

    def __init__(self):
        """This is main controller & hold data for whole pyspecty."""

        self.py_file = self.__get_caller_path()
        self.__code_executor()

    def __get_caller_path(self):
        """This function gets path of file which need inspection."""

        return os.path.abspath((inspect.stack()[3])[1])

    def __code_executor(self):
        """This function execute code hook all the errors and open browser with results."""

        try:
            exec(open(self.py_file).read())
        except Exception as e:
            url = "http://stackoverflow.com/search?q=[python]+" + str(e)
            webbrowser.open(url, new=2)
        else:
            print("Code Executed Successfully.")
