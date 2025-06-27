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

from docspace.models.editor_configuration_dto import EditorConfigurationDto

class TestEditorConfigurationDto(unittest.TestCase):
    """EditorConfigurationDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EditorConfigurationDto:
        """Test EditorConfigurationDto
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EditorConfigurationDto`
        """
        model = EditorConfigurationDto()
        if include_optional:
            return EditorConfigurationDto(
                callback_url = 'some text',
                co_editing = docspace.models.co_editing_config.CoEditingConfig(
                    change = True, 
                    fast = True, 
                    mode = 0, ),
                create_url = 'some text',
                customization = docspace.models.customization_config_dto.CustomizationConfigDto(
                    about = True, 
                    customer = docspace.models.customer_config_dto.CustomerConfigDto(
                        address = 'some text', 
                        logo = 'some text', 
                        logo_dark = 'some text', 
                        mail = 'some text', 
                        name = 'Winfield Upton', 
                        www = 'some text', ), 
                    anonymous = docspace.models.anonymous_config_dto.AnonymousConfigDto(
                        request = True, ), 
                    feedback = docspace.models.feedback_config.FeedbackConfig(
                        url = 'some text', 
                        visible = True, ), 
                    forcesave = True, 
                    goback = docspace.models.goback_config.GobackConfig(
                        url = 'some text', ), 
                    logo = docspace.models.logo_config_dto.LogoConfigDto(
                        image = 'some text', 
                        image_dark = 'some text', 
                        image_light = 'some text', 
                        image_embedded = 'some text', 
                        url = 'some text', 
                        visible = True, ), 
                    mention_share = True, 
                    review_display = 'some text', 
                    submit_form = docspace.models.submit_form.SubmitForm(
                        visible = True, 
                        result_message = 'some text', ), 
                    start_filling_form = docspace.models.start_filling_form.StartFillingForm(
                        text = 'some text', ), ),
                embedded = docspace.models.embedded_config.EmbeddedConfig(
                    embed_url = 'some text', 
                    save_url = 'some text', 
                    share_link_param = 'some text', 
                    share_url = 'some text', 
                    toolbar_docked = 'some text', ),
                encryption_keys = docspace.models.encryption_keys_config.EncryptionKeysConfig(
                    crypto_engine_id = 'some text', 
                    private_key_enc = 'some text', 
                    public_key = 'some text', ),
                lang = 'some text',
                mode = 'some text',
                mode_write = True,
                plugins = docspace.models.plugins_config.PluginsConfig(
                    plugins_data = ["some text"], ),
                recent = [
                    docspace.models.recent_config.RecentConfig(
                        folder = 'some text', 
                        title = 'legacy_1080p_small_wooden_mouse', 
                        url = 'some text', )
                    ],
                templates = [
                    docspace.models.templates_config.TemplatesConfig(
                        image = 'some text', 
                        title = 'legacy_1080p_small_wooden_mouse', 
                        url = 'some text', )
                    ],
                user = docspace.models.user_config.UserConfig(
                    id = '9846', 
                    name = 'Winfield Upton', 
                    image = 'some text', 
                    roles = ["some text"], )
            )
        else:
            return EditorConfigurationDto(
        )
        """

    def testEditorConfigurationDto(self):
        """Test EditorConfigurationDto"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
