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

from docspace.api.rooms_api import RoomsApi


class TestRoomsApi(unittest.TestCase):
    """RoomsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = RoomsApi()

    def tearDown(self) -> None:
        pass

    def test_add_room_tags(self) -> None:
        """Test case for add_room_tags

        Add the room tags
        """
        pass

    def test_archive_room(self) -> None:
        """Test case for archive_room

        Archive a room
        """
        pass

    def test_change_room_cover(self) -> None:
        """Test case for change_room_cover

        Change the room cover
        """
        pass

    def test_create_room(self) -> None:
        """Test case for create_room

        Create a room
        """
        pass

    def test_create_room_from_template(self) -> None:
        """Test case for create_room_from_template

        Create a room from the template
        """
        pass

    def test_create_room_logo(self) -> None:
        """Test case for create_room_logo

        Create a room logo
        """
        pass

    def test_create_room_tag(self) -> None:
        """Test case for create_room_tag

        Create a tag
        """
        pass

    def test_create_room_template(self) -> None:
        """Test case for create_room_template

        Start creating room template
        """
        pass

    def test_create_room_third_party(self) -> None:
        """Test case for create_room_third_party

        Create a third-party room
        """
        pass

    def test_delete_custom_tags(self) -> None:
        """Test case for delete_custom_tags

        Delete tags
        """
        pass

    def test_delete_room(self) -> None:
        """Test case for delete_room

        Remove a room
        """
        pass

    def test_delete_room_logo(self) -> None:
        """Test case for delete_room_logo

        Remove a room logo
        """
        pass

    def test_delete_room_tags(self) -> None:
        """Test case for delete_room_tags

        Remove the room tags
        """
        pass

    def test_get_new_room_items(self) -> None:
        """Test case for get_new_room_items

        Get the new room items
        """
        pass

    def test_get_public_settings(self) -> None:
        """Test case for get_public_settings

        Get public settings
        """
        pass

    def test_get_room_covers(self) -> None:
        """Test case for get_room_covers

        Get covers
        """
        pass

    def test_get_room_creating_status(self) -> None:
        """Test case for get_room_creating_status

        Get the room creation progress
        """
        pass

    def test_get_room_index_export(self) -> None:
        """Test case for get_room_index_export

        Get the room index export
        """
        pass

    def test_get_room_info(self) -> None:
        """Test case for get_room_info

        Get room information
        """
        pass

    def test_get_room_links(self) -> None:
        """Test case for get_room_links

        Get the room links
        """
        pass

    def test_get_room_security_info(self) -> None:
        """Test case for get_room_security_info

        Get the room access rights
        """
        pass

    def test_get_room_tags_info(self) -> None:
        """Test case for get_room_tags_info

        Get tags
        """
        pass

    def test_get_room_template_creating_status(self) -> None:
        """Test case for get_room_template_creating_status

        Get status of room template creation
        """
        pass

    def test_get_rooms_folder(self) -> None:
        """Test case for get_rooms_folder

        Get rooms
        """
        pass

    def test_get_rooms_new_items(self) -> None:
        """Test case for get_rooms_new_items

        Get the room new items
        """
        pass

    def test_get_rooms_primary_external_link(self) -> None:
        """Test case for get_rooms_primary_external_link

        Get the room primary external link
        """
        pass

    def test_pin_room(self) -> None:
        """Test case for pin_room

        Pin a room
        """
        pass

    def test_reorder_room(self) -> None:
        """Test case for reorder_room

        Reorder the room
        """
        pass

    def test_resend_email_invitations(self) -> None:
        """Test case for resend_email_invitations

        Resend the room invitations
        """
        pass

    def test_set_public_settings(self) -> None:
        """Test case for set_public_settings

        Set public settings
        """
        pass

    def test_set_room_link(self) -> None:
        """Test case for set_room_link

        Set the room external or invitation link
        """
        pass

    def test_set_room_security(self) -> None:
        """Test case for set_room_security

        Set the room access rights
        """
        pass

    def test_start_room_index_export(self) -> None:
        """Test case for start_room_index_export

        Start the room index export
        """
        pass

    def test_terminate_room_index_export(self) -> None:
        """Test case for terminate_room_index_export

        Terminate the room index export
        """
        pass

    def test_unarchive_room(self) -> None:
        """Test case for unarchive_room

        Unarchive a room
        """
        pass

    def test_unpin_room(self) -> None:
        """Test case for unpin_room

        Unpin a room
        """
        pass

    def test_update_room(self) -> None:
        """Test case for update_room

        Update a room
        """
        pass

    def test_upload_room_logo(self) -> None:
        """Test case for upload_room_logo

        Upload a room logo image
        """
        pass


if __name__ == '__main__':
    unittest.main()
