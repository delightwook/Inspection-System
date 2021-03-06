from check.cases import *
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))


class CaseManager :
    @staticmethod
    def invoke(case,data):
        # call case class
        return getattr(case,'execute')(data)


def call_case(case,data):
    casemodule = __import__("cases." + case.lower() +".controller",
                      fromlist=["cases." + case.lower() +".controller"])

    CaseManager.invoke(casemodule.Client(),data)


