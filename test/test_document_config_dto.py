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

from docspace-api-sdk.models.document_config_dto import DocumentConfigDto

class TestDocumentConfigDto(unittest.TestCase):
    """DocumentConfigDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DocumentConfigDto:
        """Test DocumentConfigDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DocumentConfigDto`
        """
        model = DocumentConfigDto()
        if include_optional:
            return DocumentConfigDto(
                file_type = 'some text',
                info = docspace-api-sdk.models.info_config_dto.InfoConfigDto(
                    favorite = True, 
                    folder = 'some text', 
                    owner = 'some text', 
                    sharing_settings = [
                        docspace-api-sdk.models.ace_short_wrapper.AceShortWrapper(
                            user = 'some text', 
                            permissions = 'some text', 
                            is_link = True, )
                        ], 
                    type = 0, 
                    uploaded = 'some text', ),
                is_linked_for_me = True,
                key = 'some text',
                permissions = docspace-api-sdk.models.permissions_config.PermissionsConfig(
                    comment = True, 
                    chat = True, 
                    download = True, 
                    edit = True, 
                    fill_forms = True, 
                    modify_filter = True, 
                    protect = True, 
                    print = True, 
                    rename = True, 
                    review = True, 
                    copy = True, ),
                shared_link_param = 'some text',
                shared_link_key = 'some text',
                reference_data = docspace-api-sdk.models.file_reference_data.FileReferenceData(
                    file_key = 'some text', 
                    instance_id = '9846', 
                    room_id = '9846', 
                    can_edit_room = True, ),
                title = 'legacy_1080p_small_wooden_mouse',
                url = 'some text',
                is_form = True,
                options = docspace-api-sdk.models.options.Options(
                    watermark_on_draw = docspace-api-sdk.models.watermark_on_draw.WatermarkOnDraw(
                        width = -8.5, 
                        height = -8.5, 
                        margins = [1234], 
                        fill = 'some text', 
                        rotate = 1234, 
                        transparent = -8.5, 
                        paragraphs = [
                            docspace-api-sdk.models.paragraph.Paragraph(
                                align = 1234, 
                                runs = [
                                    docspace-api-sdk.models.run.Run(
                                        fill = [1234], 
                                        text = 'some text', 
                                        font_size = 'some text', )
                                    ], )
                            ], ), )
            )
        else:
            return DocumentConfigDto(
        )
        """

    def testDocumentConfigDto(self):
        """Test DocumentConfigDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
