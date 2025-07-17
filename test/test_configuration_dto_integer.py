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

from docspace-api-python.models.configuration_dto_integer import ConfigurationDtoInteger

class TestConfigurationDtoInteger(unittest.TestCase):
    """ConfigurationDtoInteger unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ConfigurationDtoInteger:
        """Test ConfigurationDtoInteger
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ConfigurationDtoInteger`
        """
        model = ConfigurationDtoInteger()
        if include_optional:
            return ConfigurationDtoInteger(
                document = docspace-api-python.models.document_config_dto.DocumentConfigDto(
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
                        room_id = '9846', 
                        can_edit_room = True, ), 
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
                                ], ), ), ),
                document_type = 'some text',
                editor_config = docspace-api-python.models.editor_configuration_dto.EditorConfigurationDto(
                    callback_url = 'some text', 
                    co_editing = docspace-api-python.models.co_editing_config.CoEditingConfig(
                        change = True, 
                        fast = True, 
                        mode = 0, ), 
                    create_url = 'some text', 
                    customization = docspace-api-python.models.customization_config_dto.CustomizationConfigDto(
                        about = True, 
                        customer = docspace-api-python.models.customer_config_dto.CustomerConfigDto(
                            address = 'some text', 
                            logo = 'some text', 
                            logo_dark = 'some text', 
                            mail = 'some text', 
                            name = 'Winfield Upton', 
                            www = 'some text', ), 
                        anonymous = docspace-api-python.models.anonymous_config_dto.AnonymousConfigDto(
                            request = True, ), 
                        feedback = docspace-api-python.models.feedback_config.FeedbackConfig(
                            url = 'some text', 
                            visible = True, ), 
                        forcesave = True, 
                        goback = docspace-api-python.models.goback_config.GobackConfig(
                            url = 'some text', ), 
                        review = docspace-api-python.models.review_config.ReviewConfig(
                            review_display = 'some text', ), 
                        logo = docspace-api-python.models.logo_config_dto.LogoConfigDto(
                            image = 'some text', 
                            image_dark = 'some text', 
                            image_light = 'some text', 
                            image_embedded = 'some text', 
                            url = 'some text', 
                            visible = True, ), 
                        mention_share = True, 
                        submit_form = docspace-api-python.models.submit_form.SubmitForm(
                            visible = True, 
                            result_message = 'some text', ), 
                        start_filling_form = docspace-api-python.models.start_filling_form.StartFillingForm(
                            text = 'some text', ), ), 
                    embedded = docspace-api-python.models.embedded_config.EmbeddedConfig(
                        embed_url = 'some text', 
                        save_url = 'some text', 
                        share_link_param = 'some text', 
                        share_url = 'some text', 
                        toolbar_docked = 'some text', ), 
                    encryption_keys = docspace-api-python.models.encryption_keys_config.EncryptionKeysConfig(
                        crypto_engine_id = 'some text', 
                        private_key_enc = 'some text', 
                        public_key = 'some text', ), 
                    lang = 'some text', 
                    mode = 'some text', 
                    mode_write = True, 
                    plugins = docspace-api-python.models.plugins_config.PluginsConfig(
                        plugins_data = ["some text"], ), 
                    recent = [
                        docspace-api-python.models.recent_config.RecentConfig(
                            folder = 'some text', 
                            title = 'legacy_1080p_small_wooden_mouse', 
                            url = 'some text', )
                        ], 
                    templates = [
                        docspace-api-python.models.templates_config.TemplatesConfig(
                            image = 'some text', 
                            title = 'legacy_1080p_small_wooden_mouse', 
                            url = 'some text', )
                        ], 
                    user = docspace-api-python.models.user_config.UserConfig(
                        id = '9846', 
                        name = 'Winfield Upton', 
                        image = 'some text', 
                        roles = ["some text"], ), ),
                editor_type = 0,
                editor_url = 'some text',
                token = 'some text',
                type = 'some text',
                file = docspace-api-python.models.file_dto_integer.FileDtoInteger(
                    title = 'Some titile.txt/ Some title', 
                    access = 0, 
                    shared = False, 
                    created = docspace-api-python.models.api_date_time.ApiDateTime(
                        utc_time = '2008-04-10T06:30+04:00', 
                        time_zone_offset = '00:00:00', ), 
                    created_by = docspace-api-python.models.employee_dto.EmployeeDto(
                        id = '', 
                        display_name = 'Mike Zanyatski', 
                        title = 'Manager', 
                        avatar = 'some text', 
                        avatar_original = 'some text', 
                        avatar_max = 'some text', 
                        avatar_medium = 'some text', 
                        avatar_small = 'url to small avatar', 
                        profile_url = 'some text', 
                        has_avatar = True, 
                        is_anonim = True, ), 
                    updated = docspace-api-python.models.api_date_time.ApiDateTime(
                        utc_time = '2008-04-10T06:30+04:00', 
                        time_zone_offset = '00:00:00', ), 
                    auto_delete = , 
                    root_folder_type = 0, 
                    parent_room_type = 0, 
                    updated_by = docspace-api-python.models.employee_dto.EmployeeDto(
                        id = '', 
                        display_name = 'Mike Zanyatski', 
                        title = 'Manager', 
                        avatar = 'some text', 
                        avatar_original = 'some text', 
                        avatar_max = 'some text', 
                        avatar_medium = 'some text', 
                        avatar_small = 'url to small avatar', 
                        profile_url = 'some text', 
                        has_avatar = True, 
                        is_anonim = True, ), 
                    provider_item = True, 
                    provider_key = 'some text', 
                    provider_id = 1234, 
                    order = 'some text', 
                    id = 10, 
                    root_folder_id = 1234, 
                    origin_id = 1234, 
                    origin_room_id = 1234, 
                    origin_title = 'some text', 
                    origin_room_title = 'some text', 
                    can_share = True, 
                    security = [{"value":true}], 
                    request_token = 'some text', 
                    folder_id = 9846, 
                    version = 3, 
                    version_group = 1, 
                    content_length = '12345', 
                    pure_content_length = 1234, 
                    file_status = 0, 
                    mute = False, 
                    view_url = 'https://www.onlyoffice.com/viewfile?fileid=2221', 
                    web_url = 'some text', 
                    short_web_url = 'some text', 
                    file_type = 0, 
                    file_exst = '.txt', 
                    comment = 'some text', 
                    encrypted = False, 
                    thumbnail_url = 'some text', 
                    thumbnail_status = 0, 
                    locked = True, 
                    locked_by = 'some text', 
                    has_draft = False, 
                    form_filling_status = 0, 
                    is_form = False, 
                    custom_filter_enabled = True, 
                    custom_filter_enabled_by = 'some text', 
                    start_filling = False, 
                    in_process_folder_id = 1234, 
                    in_process_folder_title = 'some text', 
                    draft_location = docspace-api-python.models.draft_location_integer.DraftLocationInteger(
                        folder_id = 9846, 
                        folder_title = 'some text', 
                        file_id = 9846, 
                        file_title = 'some text', ), 
                    view_accessibility = [{"value":true}], 
                    available_external_rights = [{"key":"some text","value":true}], 
                    last_opened = , 
                    expired = , 
                    file_entry_type = 1, ),
                error_message = 'some text',
                start_filling = True,
                filling_status = True,
                start_filling_mode = 0,
                filling_session_id = 'some text'
            )
        else:
            return ConfigurationDtoInteger(
        )
        """

    def testConfigurationDtoInteger(self):
        """Test ConfigurationDtoInteger"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
