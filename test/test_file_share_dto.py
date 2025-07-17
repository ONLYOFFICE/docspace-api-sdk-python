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

from docspace-api-python.models.file_share_dto import FileShareDto

class TestFileShareDto(unittest.TestCase):
    """FileShareDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FileShareDto:
        """Test FileShareDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FileShareDto`
        """
        model = FileShareDto()
        if include_optional:
            return FileShareDto(
                access = 0,
                shared_to = {"int":1234,"string":"some text","boolean":true},
                is_locked = False,
                is_owner = True,
                can_edit_access = True,
                subject_type = 0
            )
        else:
            return FileShareDto(
        )
        """

    def testFileShareDto(self):
        """Test FileShareDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
