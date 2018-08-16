import abc
class BaseParser(abc.ABCMeta):

    @abc.abstractmethod
    def parsing(self,hosts,command,result):
        pass

