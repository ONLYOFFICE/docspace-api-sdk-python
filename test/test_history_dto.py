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

from docspace-api-python.models.history_dto import HistoryDto

class TestHistoryDto(unittest.TestCase):
    """HistoryDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> HistoryDto:
        """Test HistoryDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `HistoryDto`
        """
        model = HistoryDto()
        if include_optional:
            return HistoryDto(
                action = docspace-api-python.models.history_action.HistoryAction(
                    id = 1000, 
                    key = 'some text', ),
                initiator = docspace-api-python.models.employee_dto.EmployeeDto(
                    id = '', 
                    display_name = 'Mike Zanyatski', 
                    title = 'Manager', 
                    avatar = 'some text', 
                    avatar_original = 'some text', 
                    avatar_max = 'some text', 
                    avatar_medium = 'some text', 
                    avatar_small = 'url to small avatar', 
                    profile_url = 'some text', 
                    has_avatar = True, 
                    is_anonim = True, ),
                var_date = docspace-api-python.models.api_date_time.ApiDateTime(
                    utc_time = '2008-04-10T06:30+04:00', 
                    time_zone_offset = '00:00:00', ),
                data = docspace-api-python.models.history_data.HistoryData(
                    initiator_name = 'some text', ),
                related = [
                    docspace-api-python.models.history_dto.HistoryDto(
                        action = docspace-api-python.models.history_action.HistoryAction(
                            id = 1000, 
                            key = 'some text', ), 
                        initiator = docspace-api-python.models.employee_dto.EmployeeDto(
                            display_name = 'Mike Zanyatski', 
                            title = 'Manager', 
                            avatar = 'some text', 
                            avatar_original = 'some text', 
                            avatar_max = 'some text', 
                            avatar_medium = 'some text', 
                            avatar_small = 'url to small avatar', 
                            profile_url = 'some text', 
                            has_avatar = True, 
                            is_anonim = True, ), 
                        date = docspace-api-python.models.api_date_time.ApiDateTime(
                            utc_time = '2008-04-10T06:30+04:00', 
                            time_zone_offset = '00:00:00', ), 
                        data = docspace-api-python.models.history_data.HistoryData(
                            initiator_name = 'some text', ), )
                    ]
            )
        else:
            return HistoryDto(
        )
        """

    def testHistoryDto(self):
        """Test HistoryDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
