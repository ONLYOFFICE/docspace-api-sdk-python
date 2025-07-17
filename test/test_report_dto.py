#
# (c) Copyright Ascensio System SIA 2025
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#



import unittest

from docspace-api-python.models.report_dto import ReportDto

class TestReportDto(unittest.TestCase):
    """ReportDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ReportDto:
        """Test ReportDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ReportDto`
        """
        model = ReportDto()
        if include_optional:
            return ReportDto(
                collection = [
                    docspace-api-python.models.operation_dto.OperationDto(
                        date = docspace-api-python.models.api_date_time.ApiDateTime(
                            utc_time = '2008-04-10T06:30+04:00', 
                            time_zone_offset = '00:00:00', ), 
                        service = 'some text', 
                        description = 'some text', 
                        service_unit = 'some text', 
                        quantity = 1234, 
                        currency = 'some text', 
                        credit = 1.337, 
                        withdrawal = 1.337, )
                    ],
                offset = 1234,
                limit = 1234,
                total_quantity = 1234,
                total_page = 1234,
                current_page = 1234
            )
        else:
            return ReportDto(
        )
        """

    def testReportDto(self):
        """Test ReportDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
