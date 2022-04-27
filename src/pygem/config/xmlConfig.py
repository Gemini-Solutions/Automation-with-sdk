from typing import Dict
import lxml.etree as et
from pygem.config.baseConfig import abstarctBaseConfig
from pygem.libs.parsers import xmlToDict, xmlToList


class XmlConfig(abstarctBaseConfig):
    def __init__(self, filePath: str):
        super().__init__(filePath)
        # do any xml specific validatioins here

    def parse(self, filePath):
        print("-------- path", filePath)
        data = et.parse(filePath)
        self._CONFIG["SUITE_DATA"] = self._getSuiteData(data)
        self._CONFIG["TESTCASE_DATA"] = self._getTestCaseData(data)

    def _getSuiteData(self, data) -> Dict:

        suiteData = data.find("suite")

        suiteDict = xmlToDict(suiteData)
        # do your validations here

        return suiteDict

    def _getTestCaseData(self, data) -> Dict:

        testcaseData = data.find("testcases")

        testcaseList = xmlToList(testcaseData)

        testcaseDict = {k["NAME"]: k for k in testcaseList}
        # do your validation here

        return testcaseDict