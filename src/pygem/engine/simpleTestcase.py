from abc import ABC, abstractmethod
from typing import List, Union, Dict
from pygem.config import DefaultSettings
from pygem.engine.baseTemplate import testcaseReporter


class AbstarctSimpleTestcase(ABC):
    @abstractmethod
    def main(
        self, testcaseSettings: Dict, **kwargs
    ) -> Union[testcaseReporter, List[testcaseReporter]]:
        """
        extend the baseTemplate and implement this method.
        :param testcaseSettings: testcasesettings object created from the testcase config
        :return
        """
        pass

    def RUN(self, testcaseSettings: Dict, **kwargs) -> List:
        """
        the main function which will be called by the executor
        """
        # set the values from the report if not s et automatically
        Data = []
        reports = self.main(testcaseSettings, **kwargs)

        if isinstance(reports, testcaseReporter):
            reports = [reports]

        for index, report in enumerate(reports):
            if not report.projectName:
                report.projectName = testcaseSettings.get("PROJECTNAME", "PYGEM")

            if not report.testcaseName:
                report.testcaseName = testcaseSettings.get("NAME", "TESTCASE")
                report.testcaseName = f"{self.testcaseName}_{index}"

            # call the destructor if not already called.
            report.finalize_report()

            # if user has not provided its own resultfile
            if not report.resultFileName:
                report.jsonData = report.templateData.makeReport(
                    kwargs.get(
                        "OUTPUT_FOLDER", DefaultSettings.DEFAULT_PYGEM_FOLDER
                    ), testcaseSettings["NAME"])
            result = report.serialize()
            Data.append(result)

        return Data