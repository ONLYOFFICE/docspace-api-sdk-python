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

from docspace-api-sdk.models.file_dto_integer_security import FileDtoIntegerSecurity

class TestFileDtoIntegerSecurity(unittest.TestCase):
    """FileDtoIntegerSecurity unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FileDtoIntegerSecurity:
        """Test FileDtoIntegerSecurity
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FileDtoIntegerSecurity`
        """
        model = FileDtoIntegerSecurity()
        if include_optional:
            return FileDtoIntegerSecurity(
                read = True,
                comment = True,
                fill_forms = True,
                review = True,
                create = True,
                create_from = True,
                edit = True,
                delete = True,
                custom_filter = True,
                edit_room = True,
                rename = True,
                read_history = True,
                lock = True,
                edit_history = True,
                copy_to = True,
                copy = True,
                move_to = True,
                move = True,
                pin = True,
                mute = True,
                edit_access = True,
                duplicate = True,
                submit_to_form_gallery = True,
                download = True,
                convert = True,
                copy_shared_link = True,
                read_links = True,
                reconnect = True,
                create_room_from = True,
                copy_link = True,
                embed = True,
                change_owner = True,
                index_export = True,
                start_filling = True,
                filling_status = True,
                reset_filling = True,
                stop_filling = True,
                open_form = True
            )
        else:
            return FileDtoIntegerSecurity(
        )
        """

    def testFileDtoIntegerSecurity(self):
        """Test FileDtoIntegerSecurity"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
