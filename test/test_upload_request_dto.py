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

from docspace-api-python.models.upload_request_dto import UploadRequestDto

class TestUploadRequestDto(unittest.TestCase):
    """UploadRequestDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UploadRequestDto:
        """Test UploadRequestDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UploadRequestDto`
        """
        model = UploadRequestDto()
        if include_optional:
            return UploadRequestDto(
                file = bytes(b'blah'),
                content_type = docspace-api-python.models.content_type.ContentType(
                    boundary = 'some text', 
                    char_set = 'some text', 
                    media_type = 'some text', 
                    name = 'Winfield Upton', 
                    parameters = [
                        null
                        ], ),
                content_disposition = docspace-api-python.models.content_disposition.ContentDisposition(
                    disposition_type = 'some text', 
                    parameters = [
                        null
                        ], 
                    file_name = 'some text', 
                    creation_date = '2008-04-10T06:30+04:00', 
                    modification_date = '2008-04-10T06:30+04:00', 
                    inline = True, 
                    read_date = '2008-04-10T06:30+04:00', 
                    size = 1234, ),
                files = [
                    bytes(b'blah')
                    ],
                create_new_if_exist = True,
                store_original_file_flag = True,
                keep_convert_status = True,
                stream = bytes(b'blah')
            )
        else:
            return UploadRequestDto(
        )
        """

    def testUploadRequestDto(self):
        """Test UploadRequestDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
