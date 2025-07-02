# (c) Copyright Ascensio System SIA 2009-2025
# 
# This program is a free software product.
# You can redistribute it and/or modify it under the terms
# of the GNU Affero General Public License (AGPL) version 3 as published by the Free Software
# Foundation. In accordance with Section 7(a) of the GNU AGPL its Section 15 shall be amended
# to the effect that Ascensio System SIA expressly excludes the warranty of non-infringement of
# any third-party rights.
# 
# This program is distributed WITHOUT ANY WARRANTY, without even the implied warranty
# of MERCHANTABILITY or FITNESS FOR A PARTICULAR  PURPOSE. For details, see
# the GNU AGPL at: http://www.gnu.org/licenses/agpl-3.0.html
# 
# You can contact Ascensio System SIA at Lubanas st. 125a-25, Riga, Latvia, EU, LV-1021.
# 
# The  interactive user interfaces in modified source and object code versions of the Program must
# display Appropriate Legal Notices, as required under Section 5 of the GNU AGPL version 3.
# 
# Pursuant to Section 7(b) of the License you must retain the original Product logo when
# distributing the program. Pursuant to Section 7(e) we decline to grant you any rights under
# trademark law for use of our trademarks.
# 
# All the Product's GUI elements, including illustrations and icon sets, as well as technical writing
# content are licensed under the terms of the Creative Commons Attribution-ShareAlike 4.0
# International. See the License terms at http://creativecommons.org/licenses/by-sa/4.0/legalcode



import unittest

from docspace-api-python.models.document_config_dto import DocumentConfigDto

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
                info = docspace-api-python.models.info_config_dto.InfoConfigDto(
                    favorite = True, 
                    folder = 'some text', 
                    owner = 'some text', 
                    sharing_settings = [
                        docspace-api-python.models.ace_short_wrapper.AceShortWrapper(
                            user = 'some text', 
                            permissions = 'some text', 
                            is_link = True, )
                        ], 
                    type = 0, 
                    uploaded = 'some text', ),
                is_linked_for_me = True,
                key = 'some text',
                permissions = docspace-api-python.models.permissions_config.PermissionsConfig(
                    change_history = True, 
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
                reference_data = docspace-api-python.models.file_reference_data.FileReferenceData(
                    file_key = 'some text', 
                    instance_id = '9846', 
                    room_id = '9846', ),
                title = 'legacy_1080p_small_wooden_mouse',
                url = 'some text',
                is_form = True,
                options = docspace-api-python.models.options.Options(
                    watermark_on_draw = docspace-api-python.models.watermark_on_draw.WatermarkOnDraw(
                        width = -8.5, 
                        height = -8.5, 
                        margins = [1234], 
                        fill = 'some text', 
                        rotate = 1234, 
                        transparent = -8.5, 
                        paragraphs = [
                            docspace-api-python.models.paragraph.Paragraph(
                                align = 1234, 
                                runs = [
                                    docspace-api-python.models.run.Run(
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
