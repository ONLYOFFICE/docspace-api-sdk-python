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

from docspace-api-sdk.models.document_builder_task_dto import DocumentBuilderTaskDto

class TestDocumentBuilderTaskDto(unittest.TestCase):
    """DocumentBuilderTaskDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DocumentBuilderTaskDto:
        """Test DocumentBuilderTaskDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DocumentBuilderTaskDto`
        """
        model = DocumentBuilderTaskDto()
        if include_optional:
            return DocumentBuilderTaskDto(
                id = '9846',
                error = 'some text',
                percentage = 1234,
                is_completed = True,
                status = 0,
                result_file_id = {"int":1234,"string":"some text","boolean":true},
                result_file_name = 'some text',
                result_file_url = 'some text'
            )
        else:
            return DocumentBuilderTaskDto(
        )
        """

    def testDocumentBuilderTaskDto(self):
        """Test DocumentBuilderTaskDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
