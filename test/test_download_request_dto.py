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

from docspace-api-python.models.download_request_dto import DownloadRequestDto

class TestDownloadRequestDto(unittest.TestCase):
    """DownloadRequestDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DownloadRequestDto:
        """Test DownloadRequestDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DownloadRequestDto`
        """
        model = DownloadRequestDto()
        if include_optional:
            return DownloadRequestDto(
                return_single_operation = True,
                folder_ids = [
                    null
                    ],
                file_ids = [
                    null
                    ],
                file_convert_ids = [
                    docspace-api-python.models.download_request_item_dto.DownloadRequestItemDto(
                        key = null, 
                        value = 'some text', 
                        password = 'vfmf2vO1Kp', )
                    ]
            )
        else:
            return DownloadRequestDto(
        )
        """

    def testDownloadRequestDto(self):
        """Test DownloadRequestDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
