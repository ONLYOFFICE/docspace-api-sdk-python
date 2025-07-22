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

from docspace-api-sdk.models.edit_history_data_wrapper import EditHistoryDataWrapper

class TestEditHistoryDataWrapper(unittest.TestCase):
    """EditHistoryDataWrapper unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EditHistoryDataWrapper:
        """Test EditHistoryDataWrapper
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EditHistoryDataWrapper`
        """
        model = EditHistoryDataWrapper()
        if include_optional:
            return EditHistoryDataWrapper(
                response = docspace-api-sdk.models.edit_history_data_dto.EditHistoryDataDto(
                    changes_url = 'some text', 
                    key = 'some text', 
                    previous = docspace-api-sdk.models.edit_history_url.EditHistoryUrl(
                        key = 'some text', 
                        url = 'some text', 
                        file_type = 'some text', ), 
                    token = 'some text', 
                    url = 'some text', 
                    version = 1234, 
                    file_type = 'some text', ),
                count = 56,
                links = [
                    docspace-api-sdk.models.active_connections_wrapper_links_inner.ActiveConnectionsWrapper_links_inner(
                        href = '', 
                        action = '', )
                    ],
                status = 56,
                status_code = 56
            )
        else:
            return EditHistoryDataWrapper(
        )
        """

    def testEditHistoryDataWrapper(self):
        """Test EditHistoryDataWrapper"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
