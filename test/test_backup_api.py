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

from docspace-api-sdk.api.backup_api import BackupApi


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
