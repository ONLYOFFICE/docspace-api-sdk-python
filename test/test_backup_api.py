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

from docspace-api-python.api.backup_api import BackupApi


class TestBackupApi(unittest.TestCase):
    """BackupApi unit test stubs"""

    def setUp(self) -> None:
        self.api = BackupApi()

    def tearDown(self) -> None:
        pass

    def test_create_backup_schedule(self) -> None:
        """Test case for create_backup_schedule

        Create the backup schedule
        """
        pass

    def test_delete_backup(self) -> None:
        """Test case for delete_backup

        Delete the backup
        """
        pass

    def test_delete_backup_history(self) -> None:
        """Test case for delete_backup_history

        Delete the backup history
        """
        pass

    def test_delete_backup_schedule(self) -> None:
        """Test case for delete_backup_schedule

        Delete the backup schedule
        """
        pass

    def test_get_backup_history(self) -> None:
        """Test case for get_backup_history

        Get the backup history
        """
        pass

    def test_get_backup_progress(self) -> None:
        """Test case for get_backup_progress

        Get the backup progress
        """
        pass

    def test_get_backup_schedule(self) -> None:
        """Test case for get_backup_schedule

        Get the backup schedule
        """
        pass

    def test_get_restore_progress(self) -> None:
        """Test case for get_restore_progress

        Get the restoring progress
        """
        pass

    def test_start_backup(self) -> None:
        """Test case for start_backup

        Start the backup
        """
        pass

    def test_start_backup_restore(self) -> None:
        """Test case for start_backup_restore

        Start the restoring process
        """
        pass


if __name__ == '__main__':
    unittest.main()
