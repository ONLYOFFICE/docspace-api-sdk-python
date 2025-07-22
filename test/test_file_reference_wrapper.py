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

from docspace-api-sdk.models.file_reference_wrapper import FileReferenceWrapper

class TestFileReferenceWrapper(unittest.TestCase):
    """FileReferenceWrapper unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FileReferenceWrapper:
        """Test FileReferenceWrapper
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FileReferenceWrapper`
        """
        model = FileReferenceWrapper()
        if include_optional:
            return FileReferenceWrapper(
                response = docspace-api-sdk.models.file_reference.FileReference(
                    reference_data = docspace-api-sdk.models.file_reference_data.FileReferenceData(
                        file_key = 'some text', 
                        instance_id = '9846', 
                        room_id = '9846', 
                        can_edit_room = True, ), 
                    error = 'some text', 
                    path = 'some text', 
                    url = 'some text', 
                    file_type = 'some text', 
                    key = 'some text', 
                    link = 'some text', 
                    token = 'some text', ),
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
            return FileReferenceWrapper(
        )
        """

    def testFileReferenceWrapper(self):
        """Test FileReferenceWrapper"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
