from gempyp.engine.gempypHelper import Gempyp
from gempyp.libs.enums.status import status


class sample1(Gempyp):
    def main(self):
        self.verify("Gempyp", "testing")
        return self.reporter

    def verify(self, projectName, testcaseName):
        self.reporter = Gempyp(projectName, testcaseName).reporter

        self.reporter.addRow(
            "test step1", "hello world", status.PASS, extra_arg="1", extra_arg2="2"
        )
        self.reporter.addRow(
            "Warn Testing", "hello world", status.WARN, extra_arg="1", extra_arg2="2"
        )
        self.reporter.addRow(
            "test step2", "hello world", status.PASS, extra_arg3="3", extra_arg2="2"
        )
        self.reporter.addMisc("Reason_Of_Failure", "Missing")
        # self.reporter.finalize_report()
        # self.reporter.templateData.makeReport("test")
        # print(self.reporter.serialize())


if __name__ == "__main__":
    sample1().verify("testProject", "sampleTestcase1")
