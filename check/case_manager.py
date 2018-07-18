class CaseManager :

    def __init__(self):
        pass
    @staticmethod
    def invoke(case,data):
        # call case class
        return getattr(case,'execute')(data)


def call_case(case,data):

    casemodule = __import__("cases." + case.lower() +".controller",
                      fromlist=["cases." + case.lower() +".controller"])

    CaseManager.invoke(casemodule.Client(),data)

#driver_manager
data = [['192.168.11.3', '192.168.11.31'],['stack', 'stack'],'ping -c 3 -q 192.168.11.3']
call_case('P2P',data)