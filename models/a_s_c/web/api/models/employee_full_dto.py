from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from ....api.core.api_date_time import ApiDateTime
    from .contact import Contact
    from .employee_dto import EmployeeDto
    from .group_summary_dto import GroupSummaryDto

@dataclass
class EmployeeFullDto(Parsable):
    # [0 - Not activated, 1 - Activated, 2 - Pending, 4 - Auto generated]
    activation_status: Optional[int] = None
    # Avatar
    avatar: Optional[str] = None
    # Maximum size avatar
    avatar_max: Optional[str] = None
    # Medium size avatar
    avatar_medium: Optional[str] = None
    # Original size avatar
    avatar_original: Optional[str] = None
    # Small avatar
    avatar_small: Optional[str] = None
    # The birthday property
    birthday: Optional[ApiDateTime] = None
    # List of contacts
    contacts: Optional[List[Contact]] = None
    # The createdBy property
    created_by: Optional[EmployeeDto] = None
    # Language
    culture_name: Optional[str] = None
    # Department
    department: Optional[str] = None
    # Display name
    display_name: Optional[str] = None
    # Email
    email: Optional[str] = None
    # First name
    first_name: Optional[str] = None
    # List of groups
    groups: Optional[List[GroupSummaryDto]] = None
    # Specifies if the user has an avatar or not
    has_avatar: Optional[bool] = None
    # ID
    id: Optional[UUID] = None
    # Specifies if the user is an administrator or not
    is_admin: Optional[bool] = None
    # Specifies if the user is an anonim or not
    is_anonim: Optional[bool] = None
    # Specifies if the user is a portal collaborator or not
    is_collaborator: Optional[bool] = None
    # Specifies if the user has a custom quota or not
    is_custom_quota: Optional[bool] = None
    # Specifies if the LDAP settings are enabled for the user or not
    is_l_d_a_p: Optional[bool] = None
    # Specifies if the user is a portal owner or not
    is_owner: Optional[bool] = None
    # Specifies if the user is a room administrator or not
    is_room_admin: Optional[bool] = None
    # Specifies if the SSO settings are enabled for the user or not
    is_s_s_o: Optional[bool] = None
    # Specifies if the user is a portal visitor or not
    is_visitor: Optional[bool] = None
    # Last name
    last_name: Optional[str] = None
    # List of administrator modules
    list_admin_modules: Optional[List[str]] = None
    # Location
    location: Optional[str] = None
    # Current login event ID
    login_event_id: Optional[int] = None
    # Mobile phone number
    mobile_phone: Optional[str] = None
    # [0 - Not activated, 1 - Activated]
    mobile_phone_activation_status: Optional[int] = None
    # Notes
    notes: Optional[str] = None
    # Profile URL
    profile_url: Optional[str] = None
    # Quota limit
    quota_limit: Optional[int] = None
    # The registrationDate property
    registration_date: Optional[ApiDateTime] = None
    # Sex
    sex: Optional[str] = None
    # Shared
    shared: Optional[bool] = None
    # [1 - Active, 2 - Terminated, 4 - Pending, 5 - Default, 7 - All]
    status: Optional[int] = None
    # The terminated property
    terminated: Optional[ApiDateTime] = None
    # [0 - Base, 1 - Dark, 2 - System]
    theme: Optional[int] = None
    # Title
    title: Optional[str] = None
    # Portal used space
    used_space: Optional[float] = None
    # Username
    user_name: Optional[str] = None
    # The workFrom property
    work_from: Optional[ApiDateTime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EmployeeFullDto:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EmployeeFullDto
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EmployeeFullDto()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ....api.core.api_date_time import ApiDateTime
        from .contact import Contact
        from .employee_dto import EmployeeDto
        from .group_summary_dto import GroupSummaryDto

        from ....api.core.api_date_time import ApiDateTime
        from .contact import Contact
        from .employee_dto import EmployeeDto
        from .group_summary_dto import GroupSummaryDto

        fields: Dict[str, Callable[[Any], None]] = {
            "activationStatus": lambda n : setattr(self, 'activation_status', n.get_int_value()),
            "avatar": lambda n : setattr(self, 'avatar', n.get_str_value()),
            "avatarMax": lambda n : setattr(self, 'avatar_max', n.get_str_value()),
            "avatarMedium": lambda n : setattr(self, 'avatar_medium', n.get_str_value()),
            "avatarOriginal": lambda n : setattr(self, 'avatar_original', n.get_str_value()),
            "avatarSmall": lambda n : setattr(self, 'avatar_small', n.get_str_value()),
            "birthday": lambda n : setattr(self, 'birthday', n.get_object_value(ApiDateTime)),
            "contacts": lambda n : setattr(self, 'contacts', n.get_collection_of_object_values(Contact)),
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(EmployeeDto)),
            "cultureName": lambda n : setattr(self, 'culture_name', n.get_str_value()),
            "department": lambda n : setattr(self, 'department', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "email": lambda n : setattr(self, 'email', n.get_str_value()),
            "firstName": lambda n : setattr(self, 'first_name', n.get_str_value()),
            "groups": lambda n : setattr(self, 'groups', n.get_collection_of_object_values(GroupSummaryDto)),
            "hasAvatar": lambda n : setattr(self, 'has_avatar', n.get_bool_value()),
            "id": lambda n : setattr(self, 'id', n.get_uuid_value()),
            "isAdmin": lambda n : setattr(self, 'is_admin', n.get_bool_value()),
            "isAnonim": lambda n : setattr(self, 'is_anonim', n.get_bool_value()),
            "isCollaborator": lambda n : setattr(self, 'is_collaborator', n.get_bool_value()),
            "isCustomQuota": lambda n : setattr(self, 'is_custom_quota', n.get_bool_value()),
            "isLDAP": lambda n : setattr(self, 'is_l_d_a_p', n.get_bool_value()),
            "isOwner": lambda n : setattr(self, 'is_owner', n.get_bool_value()),
            "isRoomAdmin": lambda n : setattr(self, 'is_room_admin', n.get_bool_value()),
            "isSSO": lambda n : setattr(self, 'is_s_s_o', n.get_bool_value()),
            "isVisitor": lambda n : setattr(self, 'is_visitor', n.get_bool_value()),
            "lastName": lambda n : setattr(self, 'last_name', n.get_str_value()),
            "listAdminModules": lambda n : setattr(self, 'list_admin_modules', n.get_collection_of_primitive_values(str)),
            "location": lambda n : setattr(self, 'location', n.get_str_value()),
            "loginEventId": lambda n : setattr(self, 'login_event_id', n.get_int_value()),
            "mobilePhone": lambda n : setattr(self, 'mobile_phone', n.get_str_value()),
            "mobilePhoneActivationStatus": lambda n : setattr(self, 'mobile_phone_activation_status', n.get_int_value()),
            "notes": lambda n : setattr(self, 'notes', n.get_str_value()),
            "profileUrl": lambda n : setattr(self, 'profile_url', n.get_str_value()),
            "quotaLimit": lambda n : setattr(self, 'quota_limit', n.get_int_value()),
            "registrationDate": lambda n : setattr(self, 'registration_date', n.get_object_value(ApiDateTime)),
            "sex": lambda n : setattr(self, 'sex', n.get_str_value()),
            "shared": lambda n : setattr(self, 'shared', n.get_bool_value()),
            "status": lambda n : setattr(self, 'status', n.get_int_value()),
            "terminated": lambda n : setattr(self, 'terminated', n.get_object_value(ApiDateTime)),
            "theme": lambda n : setattr(self, 'theme', n.get_int_value()),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
            "usedSpace": lambda n : setattr(self, 'used_space', n.get_float_value()),
            "userName": lambda n : setattr(self, 'user_name', n.get_str_value()),
            "workFrom": lambda n : setattr(self, 'work_from', n.get_object_value(ApiDateTime)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        from ....api.core.api_date_time import ApiDateTime
        from .contact import Contact
        from .employee_dto import EmployeeDto
        from .group_summary_dto import GroupSummaryDto

        writer.write_int_value("activationStatus", self.activation_status)
        writer.write_str_value("avatar", self.avatar)
        writer.write_str_value("avatarMax", self.avatar_max)
        writer.write_str_value("avatarMedium", self.avatar_medium)
        writer.write_str_value("avatarOriginal", self.avatar_original)
        writer.write_str_value("avatarSmall", self.avatar_small)
        writer.write_object_value("birthday", self.birthday)
        writer.write_collection_of_object_values("contacts", self.contacts)
        writer.write_object_value("createdBy", self.created_by)
        writer.write_str_value("cultureName", self.culture_name)
        writer.write_str_value("department", self.department)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("email", self.email)
        writer.write_str_value("firstName", self.first_name)
        writer.write_collection_of_object_values("groups", self.groups)
        writer.write_bool_value("hasAvatar", self.has_avatar)
        writer.write_uuid_value("id", self.id)
        writer.write_bool_value("isAdmin", self.is_admin)
        writer.write_bool_value("isAnonim", self.is_anonim)
        writer.write_bool_value("isCollaborator", self.is_collaborator)
        writer.write_bool_value("isCustomQuota", self.is_custom_quota)
        writer.write_bool_value("isLDAP", self.is_l_d_a_p)
        writer.write_bool_value("isOwner", self.is_owner)
        writer.write_bool_value("isRoomAdmin", self.is_room_admin)
        writer.write_bool_value("isSSO", self.is_s_s_o)
        writer.write_bool_value("isVisitor", self.is_visitor)
        writer.write_str_value("lastName", self.last_name)
        writer.write_collection_of_primitive_values("listAdminModules", self.list_admin_modules)
        writer.write_str_value("location", self.location)
        writer.write_int_value("loginEventId", self.login_event_id)
        writer.write_str_value("mobilePhone", self.mobile_phone)
        writer.write_int_value("mobilePhoneActivationStatus", self.mobile_phone_activation_status)
        writer.write_str_value("notes", self.notes)
        writer.write_str_value("profileUrl", self.profile_url)
        writer.write_int_value("quotaLimit", self.quota_limit)
        writer.write_object_value("registrationDate", self.registration_date)
        writer.write_str_value("sex", self.sex)
        writer.write_bool_value("shared", self.shared)
        writer.write_int_value("status", self.status)
        writer.write_object_value("terminated", self.terminated)
        writer.write_int_value("theme", self.theme)
        writer.write_str_value("title", self.title)
        writer.write_float_value("usedSpace", self.used_space)
        writer.write_str_value("userName", self.user_name)
        writer.write_object_value("workFrom", self.work_from)
    

