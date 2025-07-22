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

from docspace-api-sdk.models.edit_history_array_wrapper import EditHistoryArrayWrapper

class TestEditHistoryArrayWrapper(unittest.TestCase):
    """EditHistoryArrayWrapper unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EditHistoryArrayWrapper:
        """Test EditHistoryArrayWrapper
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EditHistoryArrayWrapper`
        """
        model = EditHistoryArrayWrapper()
        if include_optional:
            return EditHistoryArrayWrapper(
                response = [
                    docspace-api-sdk.models.edit_history_dto.EditHistoryDto(
                        id = 1234, 
                        key = 'some text', 
                        version = 1234, 
                        version_group = 1234, 
                        user = docspace-api-sdk.models.edit_history_author.EditHistoryAuthor(
                            id = '9846', 
                            name = 'Winfield Upton', ), 
                        created = docspace-api-sdk.models.api_date_time.ApiDateTime(
                            utc_time = '2008-04-10T06:30+04:00', 
                            time_zone_offset = '00:00:00', ), 
                        changes_history = 'some text', 
                        changes = [
                            docspace-api-sdk.models.edit_history_changes_wrapper.EditHistoryChangesWrapper(
                                document_sha256 = 'some text', )
                            ], 
                        server_version = 'some text', )
                    ],
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
            return EditHistoryArrayWrapper(
        )
        """

    def testEditHistoryArrayWrapper(self):
        """Test EditHistoryArrayWrapper"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
