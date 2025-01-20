from __future__ import annotations
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .changedeleteconfrim.changedeleteconfrim_request_builder import ChangedeleteconfrimRequestBuilder
    from .displayfileextension.displayfileextension_request_builder import DisplayfileextensionRequestBuilder
    from .docservice.docservice_request_builder import DocserviceRequestBuilder
    from .file.file_request_builder import FileRequestBuilder
    from .fileops.fileops_request_builder import FileopsRequestBuilder
    from .filesusedspace.filesusedspace_request_builder import FilesusedspaceRequestBuilder
    from .folder.folder_request_builder import FolderRequestBuilder
    from .forcesave.forcesave_request_builder import ForcesaveRequestBuilder
    from .info.info_request_builder import InfoRequestBuilder
    from .item.file_item_request_builder import FileItemRequestBuilder
    from .keepnewfilename.keepnewfilename_request_builder import KeepnewfilenameRequestBuilder
    from .logos.logos_request_builder import LogosRequestBuilder
    from .masterform.masterform_request_builder import MasterformRequestBuilder
    from .my.my_request_builder import MyRequestBuilder
    from .order.order_request_builder import OrderRequestBuilder
    from .privacy.privacy_request_builder import PrivacyRequestBuilder
    from .recent.recent_request_builder import RecentRequestBuilder
    from .rooms.rooms_request_builder import RoomsRequestBuilder
    from .root.root_request_builder import RootRequestBuilder
    from .settings.settings_request_builder import SettingsRequestBuilder
    from .storeforcesave.storeforcesave_request_builder import StoreforcesaveRequestBuilder
    from .storeoriginal.storeoriginal_request_builder import StoreoriginalRequestBuilder
    from .tags.tags_request_builder import TagsRequestBuilder
    from .templates.templates_request_builder import TemplatesRequestBuilder
    from .thirdparty.thirdparty_request_builder import ThirdpartyRequestBuilder
    from .thumbnails.thumbnails_request_builder import ThumbnailsRequestBuilder
    from .trash.trash_request_builder import TrashRequestBuilder
    from .updateifexist.updateifexist_request_builder import UpdateifexistRequestBuilder

class FilesRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/2.0/files
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new FilesRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/2.0/files", path_parameters)
    
    def by_file_id(self,file_id: int) -> FileItemRequestBuilder:
        """
        Gets an item from the client.api.TwoZero.files.item collection
        param file_id: Folder ID
        Returns: FileItemRequestBuilder
        """
        if file_id is None:
            raise TypeError("file_id cannot be null.")
        from .item.file_item_request_builder import FileItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["file%2Did"] = file_id
        return FileItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    @property
    def changedeleteconfrim(self) -> ChangedeleteconfrimRequestBuilder:
        """
        The changedeleteconfrim property
        """
        from .changedeleteconfrim.changedeleteconfrim_request_builder import ChangedeleteconfrimRequestBuilder

        return ChangedeleteconfrimRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def displayfileextension(self) -> DisplayfileextensionRequestBuilder:
        """
        The displayfileextension property
        """
        from .displayfileextension.displayfileextension_request_builder import DisplayfileextensionRequestBuilder

        return DisplayfileextensionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def docservice(self) -> DocserviceRequestBuilder:
        """
        The docservice property
        """
        from .docservice.docservice_request_builder import DocserviceRequestBuilder

        return DocserviceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def file(self) -> FileRequestBuilder:
        """
        The file property
        """
        from .file.file_request_builder import FileRequestBuilder

        return FileRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def fileops(self) -> FileopsRequestBuilder:
        """
        The fileops property
        """
        from .fileops.fileops_request_builder import FileopsRequestBuilder

        return FileopsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def filesusedspace(self) -> FilesusedspaceRequestBuilder:
        """
        The filesusedspace property
        """
        from .filesusedspace.filesusedspace_request_builder import FilesusedspaceRequestBuilder

        return FilesusedspaceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def folder(self) -> FolderRequestBuilder:
        """
        The folder property
        """
        from .folder.folder_request_builder import FolderRequestBuilder

        return FolderRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def forcesave(self) -> ForcesaveRequestBuilder:
        """
        The forcesave property
        """
        from .forcesave.forcesave_request_builder import ForcesaveRequestBuilder

        return ForcesaveRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def info(self) -> InfoRequestBuilder:
        """
        The info property
        """
        from .info.info_request_builder import InfoRequestBuilder

        return InfoRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def keepnewfilename(self) -> KeepnewfilenameRequestBuilder:
        """
        The keepnewfilename property
        """
        from .keepnewfilename.keepnewfilename_request_builder import KeepnewfilenameRequestBuilder

        return KeepnewfilenameRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def logos(self) -> LogosRequestBuilder:
        """
        The logos property
        """
        from .logos.logos_request_builder import LogosRequestBuilder

        return LogosRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def masterform(self) -> MasterformRequestBuilder:
        """
        The masterform property
        """
        from .masterform.masterform_request_builder import MasterformRequestBuilder

        return MasterformRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def my(self) -> MyRequestBuilder:
        """
        The My property
        """
        from .my.my_request_builder import MyRequestBuilder

        return MyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def order(self) -> OrderRequestBuilder:
        """
        The order property
        """
        from .order.order_request_builder import OrderRequestBuilder

        return OrderRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def privacy(self) -> PrivacyRequestBuilder:
        """
        The Privacy property
        """
        from .privacy.privacy_request_builder import PrivacyRequestBuilder

        return PrivacyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def recent(self) -> RecentRequestBuilder:
        """
        The recent property
        """
        from .recent.recent_request_builder import RecentRequestBuilder

        return RecentRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def rooms(self) -> RoomsRequestBuilder:
        """
        The rooms property
        """
        from .rooms.rooms_request_builder import RoomsRequestBuilder

        return RoomsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def root(self) -> RootRequestBuilder:
        """
        The Root property
        """
        from .root.root_request_builder import RootRequestBuilder

        return RootRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def settings(self) -> SettingsRequestBuilder:
        """
        The settings property
        """
        from .settings.settings_request_builder import SettingsRequestBuilder

        return SettingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def storeforcesave(self) -> StoreforcesaveRequestBuilder:
        """
        The storeforcesave property
        """
        from .storeforcesave.storeforcesave_request_builder import StoreforcesaveRequestBuilder

        return StoreforcesaveRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def storeoriginal(self) -> StoreoriginalRequestBuilder:
        """
        The storeoriginal property
        """
        from .storeoriginal.storeoriginal_request_builder import StoreoriginalRequestBuilder

        return StoreoriginalRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def tags(self) -> TagsRequestBuilder:
        """
        The tags property
        """
        from .tags.tags_request_builder import TagsRequestBuilder

        return TagsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def templates(self) -> TemplatesRequestBuilder:
        """
        The templates property
        """
        from .templates.templates_request_builder import TemplatesRequestBuilder

        return TemplatesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def thirdparty(self) -> ThirdpartyRequestBuilder:
        """
        The thirdparty property
        """
        from .thirdparty.thirdparty_request_builder import ThirdpartyRequestBuilder

        return ThirdpartyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def thumbnails(self) -> ThumbnailsRequestBuilder:
        """
        The thumbnails property
        """
        from .thumbnails.thumbnails_request_builder import ThumbnailsRequestBuilder

        return ThumbnailsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def trash(self) -> TrashRequestBuilder:
        """
        The Trash property
        """
        from .trash.trash_request_builder import TrashRequestBuilder

        return TrashRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def updateifexist(self) -> UpdateifexistRequestBuilder:
        """
        The updateifexist property
        """
        from .updateifexist.updateifexist_request_builder import UpdateifexistRequestBuilder

        return UpdateifexistRequestBuilder(self.request_adapter, self.path_parameters)
    

