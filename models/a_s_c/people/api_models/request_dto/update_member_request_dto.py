from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from ....api.core.api_date_time import ApiDateTime
    from ....web.api.models.contact import Contact

@dataclass
class UpdateMemberRequestDto(Parsable):
    """
    Request parameters for updating user information
    """
    # The birthday property
    birthday: Optional[ApiDateTime] = None
    # Comment
    comment: Optional[str] = None
    # List of user contacts
    contacts: Optional[List[Contact]] = None
    # Language
    culture_name: Optional[str] = None
    # List of user departments
    department: Optional[List[UUID]] = None
    # Specifies whether to disable a user or not
    disable: Optional[bool] = None
    # Email
    email: Optional[str] = None
    # Avatar photo URL
    files: Optional[str] = None
    # First name
    first_name: Optional[str] = None
    # Specifies if the user is added via the invitation link or not
    from_invite_link: Optional[bool] = None
    # Specifies if this is a guest or a user
    is_user: Optional[bool] = None
    # Key
    key: Optional[str] = None
    # Last name
    last_name: Optional[str] = None
    # Location
    location: Optional[str] = None
    # Password
    password: Optional[str] = None
    # Password hash
    password_hash: Optional[str] = None
    # [0 - Female, 1 - Male]
    sex: Optional[int] = None
    # Spam
    spam: Optional[bool] = None
    # Target
    target: Optional[UUID] = None
    # Title
    title: Optional[str] = None
    # [0 - All, 1 - Room admin, 2 - Guest, 3 - DocSpace admin, 4 - User]
    type: Optional[int] = None
    # User ID
    user_id: Optional[str] = None
    # The worksfrom property
    worksfrom: Optional[ApiDateTime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UpdateMemberRequestDto:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UpdateMemberRequestDto
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UpdateMemberRequestDto()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ....api.core.api_date_time import ApiDateTime
        from ....web.api.models.contact import Contact

        from ....api.core.api_date_time import ApiDateTime
        from ....web.api.models.contact import Contact

        fields: Dict[str, Callable[[Any], None]] = {
            "birthday": lambda n : setattr(self, 'birthday', n.get_object_value(ApiDateTime)),
            "comment": lambda n : setattr(self, 'comment', n.get_str_value()),
            "contacts": lambda n : setattr(self, 'contacts', n.get_collection_of_object_values(Contact)),
            "cultureName": lambda n : setattr(self, 'culture_name', n.get_str_value()),
            "department": lambda n : setattr(self, 'department', n.get_collection_of_primitive_values(UUID)),
            "disable": lambda n : setattr(self, 'disable', n.get_bool_value()),
            "email": lambda n : setattr(self, 'email', n.get_str_value()),
            "files": lambda n : setattr(self, 'files', n.get_str_value()),
            "firstName": lambda n : setattr(self, 'first_name', n.get_str_value()),
            "fromInviteLink": lambda n : setattr(self, 'from_invite_link', n.get_bool_value()),
            "isUser": lambda n : setattr(self, 'is_user', n.get_bool_value()),
            "key": lambda n : setattr(self, 'key', n.get_str_value()),
            "lastName": lambda n : setattr(self, 'last_name', n.get_str_value()),
            "location": lambda n : setattr(self, 'location', n.get_str_value()),
            "password": lambda n : setattr(self, 'password', n.get_str_value()),
            "passwordHash": lambda n : setattr(self, 'password_hash', n.get_str_value()),
            "sex": lambda n : setattr(self, 'sex', n.get_int_value()),
            "spam": lambda n : setattr(self, 'spam', n.get_bool_value()),
            "target": lambda n : setattr(self, 'target', n.get_uuid_value()),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_int_value()),
            "userId": lambda n : setattr(self, 'user_id', n.get_str_value()),
            "worksfrom": lambda n : setattr(self, 'worksfrom', n.get_object_value(ApiDateTime)),
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
        from ....web.api.models.contact import Contact

        writer.write_object_value("birthday", self.birthday)
        writer.write_str_value("comment", self.comment)
        writer.write_collection_of_object_values("contacts", self.contacts)
        writer.write_str_value("cultureName", self.culture_name)
        writer.write_collection_of_primitive_values("department", self.department)
        writer.write_bool_value("disable", self.disable)
        writer.write_str_value("email", self.email)
        writer.write_str_value("files", self.files)
        writer.write_str_value("firstName", self.first_name)
        writer.write_bool_value("fromInviteLink", self.from_invite_link)
        writer.write_bool_value("isUser", self.is_user)
        writer.write_str_value("key", self.key)
        writer.write_str_value("lastName", self.last_name)
        writer.write_str_value("location", self.location)
        writer.write_str_value("password", self.password)
        writer.write_str_value("passwordHash", self.password_hash)
        writer.write_int_value("sex", self.sex)
        writer.write_bool_value("spam", self.spam)
        writer.write_uuid_value("target", self.target)
        writer.write_str_value("title", self.title)
        writer.write_int_value("type", self.type)
        writer.write_str_value("userId", self.user_id)
        writer.write_object_value("worksfrom", self.worksfrom)
    

