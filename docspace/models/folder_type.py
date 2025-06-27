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



from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class FolderType(int, Enum):
    """
    [0 - Default, 1 - Coomon, 2 - Bunch, 3 - Trash, 5 - User, 6 - Share, 8 - Projects, 10 - Favourites, 11 - Recent, 12 - Templates, 13 - Privacy, 14 - Virtual rooms, 15 - Filling forms room, 16 - Editing room, 19 - Custom room, 20 - Archive, 21 - Thirdparty backup, 22 - Public room, 25 - Ready form folder, 26 - In process form folder, 27 - Form filling folder done, 28 - Form filling folder in progress, 29 - Virtual Data Room, 30 - Room templates folder]
    """

    """
    allowed enum values
    """
    DEFAULT = 0
    COMMON = 1
    BUNCH = 2
    TRASH = 3
    USER = 5
    SHARE = 6
    Projects = 8
    Favorites = 10
    Recent = 11
    Templates = 12
    Privacy = 13
    VirtualRooms = 14
    FillingFormsRoom = 15
    EditingRoom = 16
    CustomRoom = 19
    Archive = 20
    ThirdpartyBackup = 21
    PublicRoom = 22
    ReadyFormFolder = 25
    InProcessFormFolder = 26
    FormFillingFolderDone = 27
    FormFillingFolderInProgress = 28
    VirtualDataRoom = 29
    RoomTemplates = 30

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of FolderType from a JSON string"""
        return cls(json.loads(json_str))


