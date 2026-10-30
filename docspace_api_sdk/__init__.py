# coding: utf-8

# flake8: noqa

#
# (c) Copyright Ascensio System SIA 2026
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



__version__ = "4.0.0"

# Define package exports
__all__ = [
    "AIApi",
    "AgentsApi",
    "AssignmentsApi",
    "AttachmentsApi",
    "ContextApi",
    "EditorToolsApi",
    "ExportApi",
    "MetadataApi",
    "OpenAIPassthroughApi",
    "PreferencesApi",
    "ProfilesApi",
    "PromptsApi",
    "SettingsApi",
    "ThreadsApi",
    "ToolsApi",
    "VectorizationApi",
    "WebSearchApi",
    "ApiKeysApi",
    "AppsApi",
    "AuthenticationApi",
    "BackupApi",
    "CapabilitiesApi",
    "DocsApi",
    "FilesApi",
    "FoldersApi",
    "MetadataApi",
    "OperationsApi",
    "QuotaApi",
    "SettingsApi",
    "SharingApi",
    "ThirdPartyIntegrationApi",
    "GroupApi",
    "SearchApi",
    "MigrationApi",
    "AuthorizationApi",
    "ClientManagementApi",
    "ClientQueryingApi",
    "DiscoveryApi",
    "ScopeManagementApi",
    "EmailApi",
    "GuestsApi",
    "PasswordApi",
    "PhotosApi",
    "ProfilesApi",
    "QuotaApi",
    "SearchApi",
    "ThemeApi",
    "ThirdPartyAccountsApi",
    "UserDataApi",
    "UserStatusApi",
    "UserTypeApi",
    "GuestsApi",
    "ModuleEventsApi",
    "PaymentApi",
    "QuotaApi",
    "SettingsApi",
    "UsersApi",
    "RoomsApi",
    "GroupsApi",
    "PrivacyRoomApi",
    "AccessToDevToolsApi",
    "ActiveConnectionsApi",
    "AuditTrailDataApi",
    "BannersVisibilityApi",
    "CSPApi",
    "FirebaseApi",
    "LoginHistoryApi",
    "OAuth2Api",
    "SMTPSettingsApi",
    "AccessToDevToolsApi",
    "AuthorizationApi",
    "BannersVisibilityApi",
    "CommonSettingsApi",
    "CookiesApi",
    "DocsCloudApi",
    "EncryptionApi",
    "GreetingSettingsApi",
    "IPRestrictionsApi",
    "LicenseApi",
    "LoginSettingsApi",
    "MessagesApi",
    "NotificationsApi",
    "OwnerApi",
    "QuotaApi",
    "RebrandingApi",
    "SSOApi",
    "SecurityApi",
    "StatisticsApi",
    "StorageApi",
    "TFASettingsApi",
    "TelegramApi",
    "WebhooksApi",
    "WebpluginsApi",
    "ThirdPartyApi",
    "ApiResponse",
    "ApiClient",
    "Configuration",
    "OpenApiException",
    "ApiTypeError",
    "ApiValueError",
    "ApiKeyError",
    "ApiAttributeError",
    "ApiException",
    "AccessRequestKeyDto",
    "AccountEntryArrayWrapper",
    "AccountEntryDto",
    "AccountInfoArrayWrapper",
    "AccountInfoDto",
    "AccountLoginType",
    "AccountSearchArea",
    "AceShortArrayWrapper",
    "AceShortDto",
    "ActionLinkActionRequest",
    "ActionLinkRequest",
    "ActionType",
    "ActiveConnectionsDto",
    "ActiveConnectionsItemDto",
    "ActiveConnectionsWrapper",
    "ActiveServiceArrayWrapper",
    "ActiveServiceDto",
    "AdditionalResourcesDto",
    "AdditionalResourcesWrapper",
    "AdditionalWhiteLabelSettingsDto",
    "AdditionalWhiteLabelSettingsRequestDto",
    "AdditionalWhiteLabelSettingsWrapper",
    "AdminMessageBaseSettingsRequestDto",
    "AdminMessageSettingsRequestDto",
    "AiActionArgs",
    "AiActionArgsPrompt",
    "AiActionType",
    "AiAgentNewItemsDto",
    "AiAgentsCreateRequest",
    "AiAgentsDeleteRequest",
    "AiAgentsGet200Response",
    "AiAgentsGet200ResponseAllOfResponse",
    "AiAgentsResetQuotaRequest",
    "AiAgentsUpdateQuotaRequest",
    "AiAgentsUpdateQuotaRequestRoomIdsInner",
    "AiAgentsUpdateRequest",
    "AiApiDateTime",
    "AiApproveToolCallRequest",
    "AiAssignmentMutationResult",
    "AiAssignmentsAssignRequest",
    "AiAssignmentsCascadeProfileDeleteRequest",
    "AiAttachment",
    "AiAttachmentFormKeysInner",
    "AiAttachmentsLinkToMessageRequest",
    "AiAttachmentsSaveFileRequest",
    "AiAttachmentsSaveFileRequestInput",
    "AiAttachmentsSaveFilesManyRequest",
    "AiBuiltinProviderType",
    "AiBulkAssignmentResult",
    "AiBulkAssignmentResultErrorsInner",
    "AiChatEvent",
    "AiChatPriceDto",
    "AiChatSettingsDto",
    "AiChatToolPermissionMode",
    "AiChatToolPrefsScope",
    "AiConfigDto",
    "AiCreateProfileInput",
    "AiCreatePromptInput",
    "AiDistributedTaskStatus",
    "AiEditorToolsCall200Response",
    "AiEditorToolsCallRequest",
    "AiEditorToolsList200Response",
    "AiEditorToolsList200ResponseToolsInner",
    "AiEmbeddingPriceDto",
    "AiEmbeddingProviderType",
    "AiEmployeeDto",
    "AiEntryMetadata",
    "AiEntryMetadataCustomFieldsInner",
    "AiEntryMetadataField",
    "AiEntryMetadataFieldOptionsInner",
    "AiEntryMetadataTemplatesInner",
    "AiEntryPricingDtoAiChatPriceDto",
    "AiEntryPricingDtoAiEmbeddingPriceDto",
    "AiEntryPricingDtoAiImagePriceDto",
    "AiEntryPricingDtoDecimal",
    "AiErrorCode",
    "AiErrorData",
    "AiErrorResponse",
    "AiExportTextToDocx202Response",
    "AiExportTextToDocxRequest",
    "AiExportTextToDocxRequestFolderId",
    "AiFileEntryBaseDto",
    "AiFileEntryDto",
    "AiFileEntryDtoAllOfAvailableShareRights",
    "AiFileEntryDtoAllOfSecurity",
    "AiFileEntryDtoAllOfShareSettings",
    "AiFileEntryType",
    "AiFileOperationDto",
    "AiFileOperationType",
    "AiFileOperationWrapper",
    "AiFileShare",
    "AiFolderArrayWrapper",
    "AiFolderContentDto",
    "AiFolderContentWrapper",
    "AiFolderDto",
    "AiFolderMutationResult",
    "AiFolderType",
    "AiFolderWrapper",
    "AiImagePriceDto",
    "AiImportError",
    "AiImportMode",
    "AiImportResult",
    "AiImportResultImported",
    "AiLogoCoverDto",
    "AiLogoDto",
    "AiMCPItem",
    "AiMetaFill200Response",
    "AiMetaFill200ResponseFilledInner",
    "AiMetaFill200ResponseFilledInnerValue",
    "AiMetaFill200ResponseSourcesInner",
    "AiMetaFill200ResponseUnresolvedInner",
    "AiMetaFillRequest",
    "AiMetaGenerate200Response",
    "AiMetaGenerate200ResponseFieldsInner",
    "AiMetaGenerate200ResponseSkippedInner",
    "AiMetaGenerate200ResponseSourcesInner",
    "AiMetaGenerate402Response",
    "AiMetaGenerateRequest",
    "AiMetaGenerateRequestId",
    "AiMetadataMatchDto",
    "AiMetadataValue",
    "AiModel",
    "AiNewItemsAgentNewItemsArrayWrapper",
    "AiNewItemsDtoAgentNewItemsDto",
    "AiOpenAIChatCompletionChunk",
    "AiOpenAIChoiceDelta",
    "AiOpenAIChunkChoice",
    "AiOpenAIFinishReason",
    "AiOpenAIStreamChunk",
    "AiOpenAIStreamError",
    "AiOpenAIStreamErrorError",
    "AiOpenAIToolCallDelta",
    "AiOpenAIToolCallDeltaFunction",
    "AiOpenOrCreateResult",
    "AiOpenaiChatCompletions403Response",
    "AiOpenaiChatCompletions403ResponseError",
    "AiOpenaiImagesGenerations403Response",
    "AiOpenaiImagesGenerations403ResponseError",
    "AiPreferencesSetDeepModeRequest",
    "AiPreferencesSetReasoningLevelRequest",
    "AiPreferencesSetToolPermissionModeRequest",
    "AiPriceCurrencyDto",
    "AiPricesDto",
    "AiPricesWrapper",
    "AiProfile",
    "AiProfileMutationResult",
    "AiProfilesCreate400Response",
    "AiProfilesGetById200Response",
    "AiProfilesListProviderModels400Response",
    "AiProfilesListProviderModels400ResponseAnyOf",
    "AiProfilesListProviderModelsRequest",
    "AiProfilesTestConnection200Response",
    "AiProfilesTestConnection200ResponseAnyOf",
    "AiPrompt",
    "AiPromptBundle",
    "AiPromptFolder",
    "AiPromptMutationResult",
    "AiPromptsImportBundleRequest",
    "AiPromptsImportBundleRequestOptions",
    "AiPromptsMoveRequest",
    "AiPromptsRenameFolderRequest",
    "AiPromptsUpdateRequest",
    "AiPromptsUpdateRequestUpdates",
    "AiProvider",
    "AiProviderType",
    "AiReasoningDepth",
    "AiReasoningLevel",
    "AiReasoningSupport",
    "AiRegenerateStreamRequest",
    "AiResolvedAssignment",
    "AiRoomDataLifetimeDto",
    "AiRoomDataLifetimePeriod",
    "AiRoomType",
    "AiSendCustomRequest",
    "AiSendRequest",
    "AiSendStreamBody",
    "AiSettingsDto",
    "AiSettingsWrapper",
    "AiSuccessResponse",
    "AiThread",
    "AiThreadMessageLike",
    "AiThreadMessageLikeContent",
    "AiThreadMessageLikeContentAnyOfInner",
    "AiThreadMessageLikeStatus",
    "AiThreadsAppendUserMessage200Response",
    "AiThreadsAppendUserMessageRequest",
    "AiThreadsCreateRequest",
    "AiThreadsOpenOrCreateRequest",
    "AiThreadsOpenOrCreateRequestEntityMeta",
    "AiThreadsRegenerateTitle200Response",
    "AiThreadsRegenerateTitleRequest",
    "AiThreadsRenameRequest",
    "AiThreadsTouchRequest",
    "AiThreadsUpdateMessageRequest",
    "AiToolAnnotations",
    "AiToolCallData",
    "AiToolPermissionMode",
    "AiToolsAddCustomServerRequest",
    "AiToolsBulkResult",
    "AiToolsBulkResultErrorsInner",
    "AiToolsListSystemTools200Response",
    "AiToolsMutationResult",
    "AiToolsRemoveCustomServerRequest",
    "AiToolsReplaceAllCustomServersRequest",
    "AiToolsSetAllowAlwaysRequest",
    "AiToolsSetDisabledRequest",
    "AiToolsUpdateCustomServerRequest",
    "AiUserSettingsDto",
    "AiUserSettingsWrapper",
    "AiVectorizationSettingsDto",
    "AiVectorizationSettingsWrapper",
    "AiVectorizationStartTask200Response",
    "AiVectorizationStartTaskRequest",
    "AiWatermarkAdditions",
    "AiWatermarkDto",
    "AiWebSearchConfig",
    "AiWebSearchConfigure400Response",
    "AiWebSearchConfigureRequest",
    "AiWebSearchMutationResult",
    "AiWebSearchSetActiveConfigRequest",
    "AmazonS3RegionArrayWrapper",
    "AmazonS3RegionDto",
    "AnonymousConfigDto",
    "ApiDateTime",
    "ApiKeyResponseArrayWrapper",
    "ApiKeyResponseDto",
    "ApiKeyResponseWrapper",
    "AppArrayWrapper",
    "AppDto",
    "AppWrapper",
    "ApplyFilterOption",
    "ArchiveRoomRequest",
    "ArrayArrayWrapper",
    "AssignMetadataTemplates",
    "AuditEventArrayWrapper",
    "AuditEventDto",
    "AuditReportFormat",
    "AuditTrailActionDto",
    "AuditTrailModuleDto",
    "AuditTrailProductArrayWrapper",
    "AuditTrailProductDto",
    "AuditTrailTypesDto",
    "AuditTrailTypesWrapper",
    "AuthKeyDto",
    "AuthKeyRequest",
    "AuthRequestDto",
    "AuthServiceArrayWrapper",
    "AuthServiceDto",
    "AuthWithCodeRequestDto",
    "AuthenticationTokenDto",
    "AuthenticationTokenWrapper",
    "AutoCleanUpDataDto",
    "AutoCleanUpDataWrapper",
    "AutoCleanupRequestDto",
    "BackupCronRequest",
    "BackupHistoryRecordArrayWrapper",
    "BackupHistoryRecordDto",
    "BackupPeriod",
    "BackupProgressDto",
    "BackupProgressEnum",
    "BackupProgressWrapper",
    "BackupServiceStateDto",
    "BackupServiceStateWrapper",
    "BackupStorageType",
    "BackupsCountResultDto",
    "BackupsCountResultWrapper",
    "BalanceDto",
    "BalanceWrapper",
    "BaseBatchRequestDto",
    "BaseBatchRequestDtoAllOfFileIds",
    "BaseBatchRequestDtoAllOfFolderIds",
    "BatchRequestDto",
    "BatchRequestDtoAllOfDestFolderId",
    "BatchRequestDtoAllOfFileIds",
    "BatchRequestDtoAllOfFolderIds",
    "BatchTagsRequestDto",
    "BooleanWrapper",
    "CapabilitiesDto",
    "CapabilitiesWrapper",
    "ChangeClientActivationRequest",
    "ChangeEmailRequest",
    "ChangeHistoryRequest",
    "ChangeOwnerRequestDto",
    "ChangePasswordRequest",
    "ChangeWalletServiceStateRequestDto",
    "ChatSettings",
    "ChatSettingsDto",
    "CheckConfirmRequestDto",
    "CheckConversionRequestDto",
    "CheckDestFolderDto",
    "CheckDestFolderResult",
    "CheckDestFolderWrapper",
    "CheckDocServiceUrlRequestDto",
    "CheckFillFormDraftRequest",
    "CheckUploadRequest",
    "ChunkedUploadSessionDto",
    "ChunkedUploadSessionResultDto",
    "ChunkedUploadSessionResultWrapper",
    "ChunkedUploadSessionWrapper",
    "ClientInfoResponse",
    "ClientResponse",
    "ClientSecretResponse",
    "CoEditingConfigDto",
    "CoEditingConfigMode",
    "ColorThemeColorsDto",
    "ColorThemeColorsRequestDto",
    "CompanyWhiteLabelSettingsDto",
    "CompanyWhiteLabelSettingsRequestDto",
    "CompanyWhiteLabelSettingsWrapper",
    "ConfigurationDto",
    "ConfigurationWrapper",
    "ConfirmData",
    "ConfirmDto",
    "ConfirmType",
    "ConfirmWrapper",
    "ConnectionTestResultDto",
    "ConnectionTestResultWrapper",
    "Contact",
    "ConversationResultArrayWrapper",
    "ConversationResultDto",
    "ConvertDocumentLayoutRequest",
    "ConvertDocumentRendererRequest",
    "ConvertFileRequestDto",
    "ConvertPdfRequest",
    "ConvertSpreadsheetLayoutRequest",
    "ConvertSpreadsheetMarginsRequest",
    "ConvertSpreadsheetPageSizeRequest",
    "ConvertThumbnailRequest",
    "CookieSettingsDto",
    "CookieSettingsRequestDto",
    "CookieSettingsWrapper",
    "CopyAsRequest",
    "CopyAsRequestDestFolderId",
    "CoverRequestDto",
    "CoversResultArrayWrapper",
    "CoversResultDto",
    "CreateApiKeyRequestDto",
    "CreateBackupScheduleRequestDto",
    "CreateClientRequest",
    "CreateFileRequest",
    "CreateFileRequestTemplateId",
    "CreateFolderRequest",
    "CreateMetadataTemplateRequestDto",
    "CreateRoomFromTemplateDto",
    "CreateRoomRequestDto",
    "CreateServiceLimitRequestDto",
    "CreateTagRequestDto",
    "CreateTextOrHtmlFileRequest",
    "CreateThirdPartyRoomRequest",
    "CreateWebhooksConfigRequestDto",
    "CronParamsDto",
    "CspDto",
    "CspRequestDto",
    "CspWrapper",
    "CurrenciesArrayWrapper",
    "CurrenciesDto",
    "CurrentLicenseInfo",
    "CustomColorThemeDto",
    "CustomColorThemeRequestDto",
    "CustomColorThemesSettingsDto",
    "CustomColorThemesSettingsRequestDto",
    "CustomColorThemesSettingsWrapper",
    "CustomFieldRequest",
    "CustomFieldValueArrayWrapper",
    "CustomFieldValueDto",
    "CustomFilterRequest",
    "CustomerConfigDto",
    "CustomerInfoDto",
    "CustomerInfoWrapper",
    "CustomerMonthlyUsageArrayWrapper",
    "CustomerMonthlyUsageDto",
    "CustomerMonthlyUsageReportRequestDto",
    "CustomerOperationsReportRequestDto",
    "CustomerServiceUsageDto",
    "CustomerServiceUsageReportDto",
    "CustomerServiceUsageReportRequestDto",
    "CustomerServiceUsageReportWrapper",
    "CustomizationConfigDto",
    "DarkThemeSettingsDto",
    "DarkThemeSettingsRequestDto",
    "DarkThemeSettingsType",
    "DarkThemeSettingsWrapper",
    "DateToAutoCleanUp",
    "DeepLinkConfigurationRequestDto",
    "DeepLinkDto",
    "DeepLinkHandlingMode",
    "DeepLinkSettingsRequestDto",
    "DefaultProductRequestDto",
    "DefaultTemplateItemDto",
    "DefaultTemplateSettingsDto",
    "DefaultTemplateSettingsRequestDto",
    "DefaultTemplateSettingsRequestDtoSelectedFile",
    "DefaultTemplateSettingsResetRequestDto",
    "DefaultTemplateSettingsWrapper",
    "DeleteBatchRequestDto",
    "DeleteBatchRequestDtoAllOfFileIds",
    "DeleteBatchRequestDtoAllOfFolderIds",
    "DeleteFileRequest",
    "DeleteFolderRequest",
    "DeleteRoomRequest",
    "DeleteVersionBatchRequestDto",
    "DepositDto",
    "DepositReportDto",
    "DepositReportWrapper",
    "DiscountCategoryDto",
    "DisplayRequestDto",
    "DistributedTaskStatus",
    "DnsSettingsRequestDto",
    "DocServiceUrlDto",
    "DocServiceUrlWrapper",
    "DocsCloudConfigDto",
    "DocsCloudConfigRequestDto",
    "DocsCloudConfigWrapper",
    "DocsCloudDevPackRequestDto",
    "DocsCloudIpFilterConfigDto",
    "DocsCloudIpFilterConfigRequest",
    "DocsCloudIpFilterRuleDto",
    "DocsCloudIpFilterRuleRequest",
    "DocsCloudLicenseInfoDto",
    "DocsCloudPaymentDto",
    "DocsCloudQuotaDto",
    "DocsCloudQuotaUserDto",
    "DocsCloudQuotaWrapper",
    "DocsCloudSecurityConfigDto",
    "DocsCloudSecurityConfigRequest",
    "DocsCloudServerConfigDto",
    "DocsCloudServerConfigRequest",
    "DocsCloudServerInfoDto",
    "DocsCloudStatsDto",
    "DocsCloudTenantDto",
    "DocsCloudTenantInfoDto",
    "DocsCloudTenantInfoWrapper",
    "DocsCloudTenantWrapper",
    "DocsCloudUsageDto",
    "DocsCloudUsageWrapper",
    "DocsCloudUserStatsDto",
    "DocsCloudUsersLimitDto",
    "DocsCloudWopiConfigDto",
    "DocsCloudWopiConfigRequest",
    "DocumentBuilderTaskDto",
    "DocumentBuilderTaskWrapper",
    "DocumentConfigDto",
    "DocumentOptionsDto",
    "DomainNameRulesDto",
    "DoubleNullableWrapper",
    "DoubleWrapper",
    "DownloadRequestDto",
    "DownloadRequestDtoAllOfFileIds",
    "DownloadRequestDtoAllOfFolderIds",
    "DownloadRequestItemDto",
    "DownloadRequestItemDtoKey",
    "DraftLocation",
    "DuplicateRequestDto",
    "DuplicateRequestDtoAllOfFileIds",
    "DuplicateRequestDtoAllOfFolderIds",
    "EditHistoryArrayWrapper",
    "EditHistoryAuthorDto",
    "EditHistoryChangesDto",
    "EditHistoryDataDto",
    "EditHistoryDataWrapper",
    "EditHistoryDto",
    "EditHistoryUrlDto",
    "EditorConfigurationDto",
    "EditorToolCallParametersDto",
    "EditorToolCallStateDto",
    "EditorType",
    "EmailActivationSettingsDto",
    "EmailActivationSettingsRequestDto",
    "EmailActivationSettingsWrapper",
    "EmailInvitationDto",
    "EmailMemberRequestDto",
    "EmbeddedConfigDto",
    "EmployeeActivationStatus",
    "EmployeeArrayWrapper",
    "EmployeeDto",
    "EmployeeFullArrayWrapper",
    "EmployeeFullDto",
    "EmployeeFullWrapper",
    "EmployeeStatus",
    "EmployeeType",
    "EmployeeWrapper",
    "EnabledModuleArrayWrapper",
    "EnabledModuleDto",
    "EncryptionKeyArrayWrapper",
    "EncryptionKeyDto",
    "EncryptionKeyRequestDto",
    "EncryptionSettingsDto",
    "EncryptionSettingsWrapper",
    "EncryptionStatus",
    "EntityQuotaDto",
    "EntityQuotaSettingsDto",
    "EntityQuotaSettingsWrapper",
    "EntryFieldDto",
    "EntryMetadataDto",
    "EntryMetadataWrapper",
    "EntryTemplateDto",
    "EntryType",
    "ErrorApiResponse",
    "ErrorApiResponseError",
    "ExchangeToken200Response",
    "ExternalDatabaseConnectionRequestDto",
    "ExternalDatabaseType",
    "ExternalDbSyncFormResultDto",
    "ExternalDbSyncTaskDto",
    "ExternalDbSyncTaskWrapper",
    "ExternalResourceDto",
    "ExternalResourcesDto",
    "ExternalShareDto",
    "ExternalShareRequestParam",
    "ExternalShareStatus",
    "ExternalShareWrapper",
    "ExternalSharingSettingsDto",
    "ExternalSharingSettingsRequestDto",
    "ExternalSharingSettingsWrapper",
    "FeatureUsedDto",
    "FeedbackConfigDto",
    "FieldError",
    "FileArrayWrapper",
    "FileConflictResolveType",
    "FileDto",
    "FileDtoAllOfViewAccessibility",
    "FileEncryptionInfoDto",
    "FileEncryptionInfoWrapper",
    "FileEntryArrayWrapper",
    "FileEntryBaseArrayWrapper",
    "FileEntryBaseDto",
    "FileEntryBaseWrapper",
    "FileEntryDto",
    "FileEntryType",
    "FileKeysDto",
    "FileLinkDto",
    "FileLinkRequest",
    "FileLinkWrapper",
    "FileOperationArrayWrapper",
    "FileOperationDto",
    "FileOperationRequestBaseDto",
    "FileOperationType",
    "FileOperationWrapper",
    "FileReferenceDataDto",
    "FileReferenceDto",
    "FileReferenceWrapper",
    "FileShare",
    "FileShareArrayWrapper",
    "FileShareDto",
    "FileShareLink",
    "FileShareParams",
    "FileShareResponseArrayWrapper",
    "FileShareWrapper",
    "FileStatus",
    "FileType",
    "FileUploadResultDto",
    "FileUploadResultWrapper",
    "FileWrapper",
    "FilesSettingsDto",
    "FilesSettingsDtoInternalFormats",
    "FilesSettingsWrapper",
    "FilesStatisticsFolder",
    "FilesStatisticsResultDto",
    "FilesStatisticsResultWrapper",
    "FillingFormResultDto",
    "FillingFormResultWrapper",
    "FilterType",
    "FinishDto",
    "FirebaseDeviceDto",
    "FirebaseDeviceWrapper",
    "FirebaseDto",
    "FirebaseRequestDto",
    "FolderArrayWrapper",
    "FolderContentArrayWrapper",
    "FolderContentDto",
    "FolderContentWrapper",
    "FolderDto",
    "FolderLinkRequest",
    "FolderMetadataSearch",
    "FolderType",
    "FolderWrapper",
    "FormFillingManageAction",
    "FormFillingStatus",
    "FormGalleryDto",
    "FormMetadataDto",
    "FormResultsDto",
    "FormRoleArrayWrapper",
    "FormRoleDto",
    "FormRoleRequest",
    "FormSubmissionsDto",
    "FormSubmissionsWrapper",
    "FormsItemArrayWrapper",
    "FormsItemDataDto",
    "FormsItemDto",
    "GenerateDocxToolCallParametersDto",
    "GenerateFormToolCallParametersDto",
    "GeneratePresentationToolCallParametersDto",
    "GetPortalPrices200Response",
    "GetPortalPrices200ResponseLinksInner",
    "GetReferenceDataDto",
    "GobackConfigDto",
    "GreetingSettingsRequestDto",
    "GroupArrayWrapper",
    "GroupDto",
    "GroupMemberSecurityArrayWrapper",
    "GroupMemberSecurityDto",
    "GroupRequestDto",
    "GroupSummaryArrayWrapper",
    "GroupSummaryDto",
    "GroupWrapper",
    "HideConfirmConvertRequestDto",
    "HistoryActionDto",
    "HistoryArrayWrapper",
    "HistoryDataDto",
    "HistoryDto",
    "ICompressWrapper",
    "IconRequest",
    "ImageSizeDto",
    "ImportableApiEntity",
    "InfoConfigDto",
    "Int32Wrapper",
    "Int64Wrapper",
    "InvitationLinkCreateRequestDto",
    "InvitationLinkDeleteRequestDto",
    "InvitationLinkDto",
    "InvitationLinkUpdateRequestDto",
    "InvitationLinkWrapper",
    "InviteUsersRequestDto",
    "IpRestrictionArrayWrapper",
    "IpRestrictionDto",
    "IpRestrictionEntryDto",
    "IpRestrictionsDto",
    "IpRestrictionsSettingsDto",
    "IpRestrictionsSettingsWrapper",
    "IpRestrictionsWrapper",
    "IsDefaultWhiteLabelLogosArrayWrapper",
    "IsDefaultWhiteLabelLogosDto",
    "IsDefaultWhiteLabelLogosWrapper",
    "ItemKeyValuePairBooleanString",
    "ItemKeyValuePairBooleanStringWrapper",
    "ItemKeyValuePairObjectObject",
    "ItemKeyValuePairStringBoolean",
    "ItemKeyValuePairStringLogoRequestDto",
    "ItemKeyValuePairStringString",
    "JsonValueWrapper",
    "LicensorDetailsArrayWrapper",
    "LicensorDetailsDto",
    "LicensorDetailsWrapper",
    "LinkAccountRequestDto",
    "LinkType",
    "LocationType",
    "LockFileRequest",
    "LoginEventArrayWrapper",
    "LoginEventDto",
    "LoginProvider",
    "LoginSettingsDto",
    "LoginSettingsRequestDto",
    "LoginSettingsWrapper",
    "LogoConfigDto",
    "LogoCoverDto",
    "LogoDto",
    "LogoRequest",
    "LogoRequestDto",
    "MailDomainSettingsRequestDto",
    "ManageFormFillingDto",
    "MemberRequestDto",
    "MembersRequest",
    "MentionArrayWrapper",
    "MentionDto",
    "MentionMessageRequest",
    "MessageAction",
    "MetadataConflictResolveType",
    "MetadataFieldDto",
    "MetadataFieldOptionDto",
    "MetadataFieldOptionRequest",
    "MetadataFieldRequest",
    "MetadataFieldType",
    "MetadataFieldWrapper",
    "MetadataFilterConditionRequest",
    "MetadataMatchDto",
    "MetadataOperationDto",
    "MetadataOperationWrapper",
    "MetadataTemplateArrayWrapper",
    "MetadataTemplateDto",
    "MetadataTemplateWrapper",
    "MetadataValueDto",
    "MetadataValueRequest",
    "MigratingApiFiles",
    "MigratingApiGroup",
    "MigratingApiUser",
    "MigrationApiInfo",
    "MigrationStatusDto",
    "MigrationStatusWrapper",
    "MobilePhoneActivationStatus",
    "MobileRequestDto",
    "Module",
    "ModuleWrapper",
    "MultiSizeLogoCoverDto",
    "NewItemsDtoFileEntryBaseDto",
    "NewItemsDtoRoomNewItemsDto",
    "NewItemsFileEntryBaseArrayWrapper",
    "NewItemsRoomNewItemsArrayWrapper",
    "NotificationChannelDto",
    "NotificationChannelStatusDto",
    "NotificationChannelStatusWrapper",
    "NotificationSettingsDto",
    "NotificationSettingsRequestDto",
    "NotificationSettingsWrapper",
    "NotificationType",
    "ObjectArrayWrapper",
    "OperationDto",
    "OperationOrderType",
    "OperationStatus",
    "OperationTokenUsageDto",
    "OperationType",
    "OrderByDto",
    "OrderRequestDto",
    "OrdersItemRequestDto",
    "OrdersRequestDto",
    "OwnerChangeInstructionsDto",
    "OwnerChangeInstructionsWrapper",
    "OwnerIdSettingsRequestDto",
    "PageableClientInfoResponse",
    "PageableClientResponse",
    "PageableModificationResponse",
    "PageableResponse",
    "PasswordHashSettingsDto",
    "PasswordSettingsDto",
    "PasswordSettingsRequestDto",
    "PasswordSettingsWrapper",
    "PaymentCalculationDto",
    "PaymentCalculationWrapper",
    "PaymentMethodStatus",
    "PaymentSettingsDto",
    "PaymentSettingsWrapper",
    "PaymentUrlRequestDto",
    "Payments",
    "PermissionsConfigDto",
    "PluginsConfigDto",
    "PluginsDto",
    "PortalUserDto",
    "PortalUserWrapper",
    "PriceDto",
    "PriceStatus",
    "PriceTimeUnit",
    "ProblemDetail",
    "ProductAdministratorDto",
    "ProductAdministratorWrapper",
    "ProductQuantityType",
    "ProductType",
    "ProviderArrayWrapper",
    "ProviderDto",
    "ProviderFilter",
    "QuantityRequestDto",
    "QuotaArrayWrapper",
    "QuotaDto",
    "QuotaFilter",
    "QuotaScope",
    "QuotaSettingsRequestDto",
    "QuotaSettingsRequestDtoDefaultQuota",
    "QuotaState",
    "QuotaWrapper",
    "RecaptchaType",
    "RecentConfigDto",
    "RegStatus",
    "ReportDto",
    "ReportWrapper",
    "RequestLocation",
    "RestrictedAiModelsDto",
    "RestrictedAiModelsWrapper",
    "ReviewConfigDto",
    "RoomDataLifetimeDto",
    "RoomDataLifetimePeriod",
    "RoomFromTemplateStatusDto",
    "RoomFromTemplateStatusWrapper",
    "RoomGroupArrayWrapper",
    "RoomGroupDto",
    "RoomGroupRequestDto",
    "RoomGroupWrapper",
    "RoomInvitation",
    "RoomInvitationRequest",
    "RoomLinkRequest",
    "RoomNewItemsDto",
    "RoomPrivacyFilter",
    "RoomSecurityDto",
    "RoomSecurityError",
    "RoomSecurityWrapper",
    "RoomTemplateDto",
    "RoomTemplateStatusDto",
    "RoomTemplateStatusWrapper",
    "RoomType",
    "RoomsMetadataSearchRequestDto",
    "RoomsNotificationSettingsDto",
    "RoomsNotificationSettingsWrapper",
    "RoomsNotificationsSettingsRequestDto",
    "RunBuilderScriptOutputRequest",
    "RunBuilderScriptRequestDto",
    "RunBuilderScriptRequestDtoArgument",
    "SalesRequestDto",
    "SaveAdditionalResourcesRequest",
    "SaveAsPdfRequest",
    "SaveAuthKeysRequestDto",
    "SaveCompanyInfoRequest",
    "SaveFormRoleMappingDto",
    "ScheduleDto",
    "ScheduleWrapper",
    "ScopeResponse",
    "SearchArea",
    "SecurityArrayWrapper",
    "SecurityDto",
    "SecurityInfoRequestDto",
    "SecurityInfoSimpleRequestDto",
    "SecurityRequestDto",
    "SendModuleEventRequest",
    "ServiceLimitDto",
    "ServiceLimitOrderBy",
    "ServiceLimitPeriod",
    "ServiceLimitReportDto",
    "ServiceLimitReportWrapper",
    "ServiceLimitScope",
    "ServiceLimitUsageDto",
    "ServiceLimitWrapper",
    "ServicePriceArrayWrapper",
    "ServicePriceDto",
    "SessionRequest",
    "SetAppEnabledRequest",
    "SetAppSettingsRequest",
    "SetAuditLifetimeSettingsRequest",
    "SetCustomFields",
    "SetManagerRequest",
    "SetMetadataValues",
    "SetParticipantServiceLimitsRequestDto",
    "SetPublicDto",
    "SetRestrictedAiModelsRequestDto",
    "SetWalletTopUpSettingsRequest",
    "SettingsDto",
    "SettingsRequestDto",
    "SettingsWrapper",
    "ShareFilterType",
    "SignupAccountRequestDto",
    "SmtpOperationStatusDto",
    "SmtpOperationStatusWrapper",
    "SmtpSettingsDto",
    "SmtpSettingsWrapper",
    "SocketSettingsDto",
    "SocketSettingsWrapper",
    "SortOrder",
    "SortedByType",
    "SsoBindingTypeDto",
    "SsoCertificateDto",
    "SsoEncryptAlgorithmTypeDto",
    "SsoFieldMappingDto",
    "SsoIdpCertificateActionTypeDto",
    "SsoIdpCertificateAdvancedDto",
    "SsoIdpSettingsDto",
    "SsoNameIdFormatTypeDto",
    "SsoSettingsConstantsDto",
    "SsoSettingsConstantsWrapper",
    "SsoSettingsDto",
    "SsoSettingsRequestDto",
    "SsoSettingsWrapper",
    "SsoSigningAlgorithmTypeDto",
    "SsoSpCertificateActionTypeDto",
    "SsoSpCertificateAdvancedDto",
    "StartBackupRequestDto",
    "StartBackupRestoreRequestDto",
    "StartEditRequest",
    "StartFillingForm",
    "StartFillingMode",
    "StartReassignRequestDto",
    "StartUpdateUserTypeDto",
    "StorageArrayWrapper",
    "StorageDto",
    "StorageEncryptionRequestDto",
    "StorageFilter",
    "StorageRequestDto",
    "StorageSettingsDto",
    "StorageSettingsWrapper",
    "StringArrayWrapper",
    "StringWrapper",
    "StudioDefaultPageSettingsDto",
    "StudioDefaultPageSettingsWrapper",
    "SubAccountDto",
    "SubjectType",
    "SubmitFormDto",
    "SubscriptionBalanceDto",
    "SubscriptionBalanceWrapper",
    "TariffDto",
    "TariffQuotaDto",
    "TariffState",
    "TariffWrapper",
    "TaskProgressResponseDto",
    "TaskProgressResponseWrapper",
    "TelegramStatusDto",
    "TelegramStatusWrapper",
    "TemplatesConfigDto",
    "TemplatesRequestDto",
    "TenantAiAccessSettingsDto",
    "TenantAiAccessSettingsRequestDto",
    "TenantAiAccessSettingsWrapper",
    "TenantAuditSettingsDto",
    "TenantAuditSettingsRequestDto",
    "TenantAuditSettingsWrapper",
    "TenantBannerSettingsDto",
    "TenantBannerSettingsRequestDto",
    "TenantBannerSettingsWrapper",
    "TenantDeepLinkSettingsDto",
    "TenantDeepLinkSettingsWrapper",
    "TenantDevToolsAccessSettingsDto",
    "TenantDevToolsAccessSettingsRequestDto",
    "TenantDevToolsAccessSettingsWrapper",
    "TenantDto",
    "TenantIndustry",
    "TenantQuotaDto",
    "TenantQuotaFeatureDto",
    "TenantQuotaSettingsDto",
    "TenantQuotaSettingsRequestDto",
    "TenantQuotaSettingsWrapper",
    "TenantQuotaWrapper",
    "TenantStatus",
    "TenantTrustedDomainsType",
    "TenantUserInvitationSettingsDto",
    "TenantUserInvitationSettingsRequestDto",
    "TenantUserInvitationSettingsWrapper",
    "TenantWalletService",
    "TenantWalletServiceSettingsDto",
    "TenantWalletServiceSettingsWrapper",
    "TenantWalletSettingsDto",
    "TenantWalletSettingsRequestDto",
    "TenantWalletSettingsWrapper",
    "TenantWrapper",
    "TerminateRequestDto",
    "TfaAppCodeArrayWrapper",
    "TfaAppCodeDto",
    "TfaConfirmDataDto",
    "TfaConfirmDataWrapper",
    "TfaRequestDto",
    "TfaSettingsArrayWrapper",
    "TfaSettingsDto",
    "TfaSetupCodeDto",
    "TfaSetupCodeWrapper",
    "TfaType",
    "TfaValidateRequestDto",
    "ThirdPartyAccountArrayWrapper",
    "ThirdPartyAccountDto",
    "ThirdPartyBackupRequestDto",
    "ThirdPartyCheckConversionRequestDto",
    "ThirdPartyChunkedUploadSessionDto",
    "ThirdPartyChunkedUploadSessionResultDto",
    "ThirdPartyChunkedUploadSessionResultWrapper",
    "ThirdPartyChunkedUploadSessionWrapper",
    "ThirdPartyConfigurationDto",
    "ThirdPartyConfigurationWrapper",
    "ThirdPartyDraftLocation",
    "ThirdPartyFileArrayWrapper",
    "ThirdPartyFileDto",
    "ThirdPartyFileEntryDto",
    "ThirdPartyFileWrapper",
    "ThirdPartyFolderArrayWrapper",
    "ThirdPartyFolderContentDto",
    "ThirdPartyFolderContentWrapper",
    "ThirdPartyFolderDto",
    "ThirdPartyFolderWrapper",
    "ThirdPartyRequestDto",
    "ThirdPartySaveAsPdfRequest",
    "ThirdPartyUploadSessionResponseDto",
    "ThirdPartyUploadSessionResponseWrapper",
    "Thumbnail",
    "ThumbnailsDataDto",
    "ThumbnailsDataWrapper",
    "ThumbnailsRequest",
    "TimeBoundDto",
    "TimezoneArrayWrapper",
    "TimezoneDto",
    "TokenDiagnosticsDto",
    "TokenDiagnosticsWrapper",
    "TopUpDepositRequestDto",
    "TransactionInfoDto",
    "TurnOnAdminMessageSettingsRequestDto",
    "UpcomingPaymentArrayWrapper",
    "UpcomingPaymentDto",
    "UpdateApiKeyRequest",
    "UpdateClientRequest",
    "UpdateCommentRequest",
    "UpdateFileRequest",
    "UpdateFolderMetadataTemplateRequest",
    "UpdateGroupRequest",
    "UpdateMemberCultureRequest",
    "UpdateMemberRequestDto",
    "UpdateMembersQuotaRequestDto",
    "UpdateMembersQuotaRequestDtoQuota",
    "UpdateMembersRequestDto",
    "UpdateMetadataFieldRequest",
    "UpdateMetadataTemplate",
    "UpdatePhotoMemberRequest",
    "UpdateRoomGroupRequest",
    "UpdateRoomRequest",
    "UpdateRoomsQuotaRequestDto",
    "UpdateRoomsRoomIdsRequestDto",
    "UpdateServiceLimitRequestDto",
    "UpdateTagRequestDto",
    "UpdateWebhooksConfigRequestDto",
    "UploadResultDto",
    "UploadResultWrapper",
    "UploadSessionResponseDto",
    "UploadSessionResponseWrapper",
    "UsageSpaceStatItemArrayWrapper",
    "UsageSpaceStatItemDto",
    "UserConfigDto",
    "UserExistsResponseDto",
    "UserExistsResponseWrapper",
    "UserInvitation",
    "UserInvitationRequestDto",
    "UserServiceLimitDto",
    "ValidationErrorResponse",
    "ValidationResult",
    "VectorizationStatus",
    "WalletQuantityRequestDto",
    "WalletServiceArrayWrapper",
    "WalletServiceDto",
    "WalletServiceWrapper",
    "WatermarkAdditions",
    "WatermarkDto",
    "WatermarkOnDrawDto",
    "WatermarkParagraphDto",
    "WatermarkRequestDto",
    "WatermarkTextRunDto",
    "WebItemSecurityRequestDto",
    "WebItemsSecurityRequestDto",
    "WebPluginArrayWrapper",
    "WebPluginDto",
    "WebPluginRequest",
    "WebPluginWrapper",
    "WebhookGroupStatus",
    "WebhookRetryRequestDto",
    "WebhookTrigger",
    "WebhookTriggerArrayWrapper",
    "WebhookTriggerDto",
    "WebhooksConfigDto",
    "WebhooksConfigWithStatusArrayWrapper",
    "WebhooksConfigWithStatusDto",
    "WebhooksConfigWrapper",
    "WebhooksLogArrayWrapper",
    "WebhooksLogDto",
    "WebhooksLogWrapper",
    "WhiteLabelItemArrayWrapper",
    "WhiteLabelItemDto",
    "WhiteLabelItemPathDto",
    "WhiteLabelItemSizeDto",
    "WhiteLabelLogoType",
    "WhiteLabelRequestDto",
    "WizardRequestDto",
    "WizardSettingsDto",
    "WizardSettingsWrapper",
    "XlsxReportResponseDto",
    "XlsxReportResponseWrapper",
]

# import apis into sdk package
from docspace_api_sdk.api.ai.ai_api import AIApi as AIApi
from docspace_api_sdk.api.ai.agents_api import AgentsApi as AgentsApi
from docspace_api_sdk.api.ai.assignments_api import AssignmentsApi as AssignmentsApi
from docspace_api_sdk.api.ai.attachments_api import AttachmentsApi as AttachmentsApi
from docspace_api_sdk.api.ai.context_api import ContextApi as ContextApi
from docspace_api_sdk.api.ai.editor_tools_api import EditorToolsApi as EditorToolsApi
from docspace_api_sdk.api.ai.export_api import ExportApi as ExportApi
from docspace_api_sdk.api.ai.metadata_api import MetadataApi as MetadataApi
from docspace_api_sdk.api.ai.open_ai_passthrough_api import OpenAIPassthroughApi as OpenAIPassthroughApi
from docspace_api_sdk.api.ai.preferences_api import PreferencesApi as PreferencesApi
from docspace_api_sdk.api.ai.profiles_api import ProfilesApi as ProfilesApi
from docspace_api_sdk.api.ai.prompts_api import PromptsApi as PromptsApi
from docspace_api_sdk.api.ai.settings_api import SettingsApi as SettingsApi
from docspace_api_sdk.api.ai.threads_api import ThreadsApi as ThreadsApi
from docspace_api_sdk.api.ai.tools_api import ToolsApi as ToolsApi
from docspace_api_sdk.api.ai.vectorization_api import VectorizationApi as VectorizationApi
from docspace_api_sdk.api.ai.web_search_api import WebSearchApi as WebSearchApi
from docspace_api_sdk.api.api_keys.api_keys_api import ApiKeysApi as ApiKeysApi
from docspace_api_sdk.api.apps.apps_api import AppsApi as AppsApi
from docspace_api_sdk.api.authentication.authentication_api import AuthenticationApi as AuthenticationApi
from docspace_api_sdk.api.backup.backup_api import BackupApi as BackupApi
from docspace_api_sdk.api.capabilities.capabilities_api import CapabilitiesApi as CapabilitiesApi
from docspace_api_sdk.api.docs.docs_api import DocsApi as DocsApi
from docspace_api_sdk.api.files.files_api import FilesApi as FilesApi
from docspace_api_sdk.api.files.folders_api import FoldersApi as FoldersApi
from docspace_api_sdk.api.files.metadata_api import MetadataApi as MetadataApi
from docspace_api_sdk.api.files.operations_api import OperationsApi as OperationsApi
from docspace_api_sdk.api.files.quota_api import QuotaApi as QuotaApi
from docspace_api_sdk.api.files.settings_api import SettingsApi as SettingsApi
from docspace_api_sdk.api.files.sharing_api import SharingApi as SharingApi
from docspace_api_sdk.api.files.third_party_integration_api import ThirdPartyIntegrationApi as ThirdPartyIntegrationApi
from docspace_api_sdk.api.group.group_api import GroupApi as GroupApi
from docspace_api_sdk.api.group.search_api import SearchApi as SearchApi
from docspace_api_sdk.api.migration.migration_api import MigrationApi as MigrationApi
from docspace_api_sdk.api.o_auth20.authorization_api import AuthorizationApi as AuthorizationApi
from docspace_api_sdk.api.o_auth20.client_management_api import ClientManagementApi as ClientManagementApi
from docspace_api_sdk.api.o_auth20.client_querying_api import ClientQueryingApi as ClientQueryingApi
from docspace_api_sdk.api.o_auth20.discovery_api import DiscoveryApi as DiscoveryApi
from docspace_api_sdk.api.o_auth20.scope_management_api import ScopeManagementApi as ScopeManagementApi
from docspace_api_sdk.api.people.email_api import EmailApi as EmailApi
from docspace_api_sdk.api.people.guests_api import GuestsApi as GuestsApi
from docspace_api_sdk.api.people.password_api import PasswordApi as PasswordApi
from docspace_api_sdk.api.people.photos_api import PhotosApi as PhotosApi
from docspace_api_sdk.api.people.profiles_api import ProfilesApi as ProfilesApi
from docspace_api_sdk.api.people.quota_api import QuotaApi as QuotaApi
from docspace_api_sdk.api.people.search_api import SearchApi as SearchApi
from docspace_api_sdk.api.people.theme_api import ThemeApi as ThemeApi
from docspace_api_sdk.api.people.third_party_accounts_api import ThirdPartyAccountsApi as ThirdPartyAccountsApi
from docspace_api_sdk.api.people.user_data_api import UserDataApi as UserDataApi
from docspace_api_sdk.api.people.user_status_api import UserStatusApi as UserStatusApi
from docspace_api_sdk.api.people.user_type_api import UserTypeApi as UserTypeApi
from docspace_api_sdk.api.portal.guests_api import GuestsApi as GuestsApi
from docspace_api_sdk.api.portal.module_events_api import ModuleEventsApi as ModuleEventsApi
from docspace_api_sdk.api.portal.payment_api import PaymentApi as PaymentApi
from docspace_api_sdk.api.portal.quota_api import QuotaApi as QuotaApi
from docspace_api_sdk.api.portal.settings_api import SettingsApi as SettingsApi
from docspace_api_sdk.api.portal.users_api import UsersApi as UsersApi
from docspace_api_sdk.api.rooms.rooms_api import RoomsApi as RoomsApi
from docspace_api_sdk.api.rooms.groups_api import GroupsApi as GroupsApi
from docspace_api_sdk.api.rooms.privacy_room_api import PrivacyRoomApi as PrivacyRoomApi
from docspace_api_sdk.api.security.access_to_dev_tools_api import AccessToDevToolsApi as AccessToDevToolsApi
from docspace_api_sdk.api.security.active_connections_api import ActiveConnectionsApi as ActiveConnectionsApi
from docspace_api_sdk.api.security.audit_trail_data_api import AuditTrailDataApi as AuditTrailDataApi
from docspace_api_sdk.api.security.banners_visibility_api import BannersVisibilityApi as BannersVisibilityApi
from docspace_api_sdk.api.security.csp_api import CSPApi as CSPApi
from docspace_api_sdk.api.security.firebase_api import FirebaseApi as FirebaseApi
from docspace_api_sdk.api.security.login_history_api import LoginHistoryApi as LoginHistoryApi
from docspace_api_sdk.api.security.o_auth2_api import OAuth2Api as OAuth2Api
from docspace_api_sdk.api.security.smtp_settings_api import SMTPSettingsApi as SMTPSettingsApi
from docspace_api_sdk.api.settings.access_to_dev_tools_api import AccessToDevToolsApi as AccessToDevToolsApi
from docspace_api_sdk.api.settings.authorization_api import AuthorizationApi as AuthorizationApi
from docspace_api_sdk.api.settings.banners_visibility_api import BannersVisibilityApi as BannersVisibilityApi
from docspace_api_sdk.api.settings.common_settings_api import CommonSettingsApi as CommonSettingsApi
from docspace_api_sdk.api.settings.cookies_api import CookiesApi as CookiesApi
from docspace_api_sdk.api.settings.docs_cloud_api import DocsCloudApi as DocsCloudApi
from docspace_api_sdk.api.settings.encryption_api import EncryptionApi as EncryptionApi
from docspace_api_sdk.api.settings.greeting_settings_api import GreetingSettingsApi as GreetingSettingsApi
from docspace_api_sdk.api.settings.ip_restrictions_api import IPRestrictionsApi as IPRestrictionsApi
from docspace_api_sdk.api.settings.license_api import LicenseApi as LicenseApi
from docspace_api_sdk.api.settings.login_settings_api import LoginSettingsApi as LoginSettingsApi
from docspace_api_sdk.api.settings.messages_api import MessagesApi as MessagesApi
from docspace_api_sdk.api.settings.notifications_api import NotificationsApi as NotificationsApi
from docspace_api_sdk.api.settings.owner_api import OwnerApi as OwnerApi
from docspace_api_sdk.api.settings.quota_api import QuotaApi as QuotaApi
from docspace_api_sdk.api.settings.rebranding_api import RebrandingApi as RebrandingApi
from docspace_api_sdk.api.settings.sso_api import SSOApi as SSOApi
from docspace_api_sdk.api.settings.security_api import SecurityApi as SecurityApi
from docspace_api_sdk.api.settings.statistics_api import StatisticsApi as StatisticsApi
from docspace_api_sdk.api.settings.storage_api import StorageApi as StorageApi
from docspace_api_sdk.api.settings.tfa_settings_api import TFASettingsApi as TFASettingsApi
from docspace_api_sdk.api.settings.telegram_api import TelegramApi as TelegramApi
from docspace_api_sdk.api.settings.webhooks_api import WebhooksApi as WebhooksApi
from docspace_api_sdk.api.settings.webplugins_api import WebpluginsApi as WebpluginsApi
from docspace_api_sdk.api.third_party.third_party_api import ThirdPartyApi as ThirdPartyApi

# import ApiClient
from docspace_api_sdk.api_response import ApiResponse as ApiResponse
from docspace_api_sdk.api_client import ApiClient as ApiClient
from docspace_api_sdk.configuration import Configuration as Configuration
from docspace_api_sdk.exceptions import OpenApiException as OpenApiException
from docspace_api_sdk.exceptions import ApiTypeError as ApiTypeError
from docspace_api_sdk.exceptions import ApiValueError as ApiValueError
from docspace_api_sdk.exceptions import ApiKeyError as ApiKeyError
from docspace_api_sdk.exceptions import ApiAttributeError as ApiAttributeError
from docspace_api_sdk.exceptions import ApiException as ApiException

# import models into sdk package
from docspace_api_sdk.models.access_request_key_dto import AccessRequestKeyDto as AccessRequestKeyDto
from docspace_api_sdk.models.account_entry_array_wrapper import AccountEntryArrayWrapper as AccountEntryArrayWrapper
from docspace_api_sdk.models.account_entry_dto import AccountEntryDto as AccountEntryDto
from docspace_api_sdk.models.account_info_array_wrapper import AccountInfoArrayWrapper as AccountInfoArrayWrapper
from docspace_api_sdk.models.account_info_dto import AccountInfoDto as AccountInfoDto
from docspace_api_sdk.models.account_login_type import AccountLoginType as AccountLoginType
from docspace_api_sdk.models.account_search_area import AccountSearchArea as AccountSearchArea
from docspace_api_sdk.models.ace_short_array_wrapper import AceShortArrayWrapper as AceShortArrayWrapper
from docspace_api_sdk.models.ace_short_dto import AceShortDto as AceShortDto
from docspace_api_sdk.models.action_link_action_request import ActionLinkActionRequest as ActionLinkActionRequest
from docspace_api_sdk.models.action_link_request import ActionLinkRequest as ActionLinkRequest
from docspace_api_sdk.models.action_type import ActionType as ActionType
from docspace_api_sdk.models.active_connections_dto import ActiveConnectionsDto as ActiveConnectionsDto
from docspace_api_sdk.models.active_connections_item_dto import ActiveConnectionsItemDto as ActiveConnectionsItemDto
from docspace_api_sdk.models.active_connections_wrapper import ActiveConnectionsWrapper as ActiveConnectionsWrapper
from docspace_api_sdk.models.active_service_array_wrapper import ActiveServiceArrayWrapper as ActiveServiceArrayWrapper
from docspace_api_sdk.models.active_service_dto import ActiveServiceDto as ActiveServiceDto
from docspace_api_sdk.models.additional_resources_dto import AdditionalResourcesDto as AdditionalResourcesDto
from docspace_api_sdk.models.additional_resources_wrapper import AdditionalResourcesWrapper as AdditionalResourcesWrapper
from docspace_api_sdk.models.additional_white_label_settings_dto import AdditionalWhiteLabelSettingsDto as AdditionalWhiteLabelSettingsDto
from docspace_api_sdk.models.additional_white_label_settings_request_dto import AdditionalWhiteLabelSettingsRequestDto as AdditionalWhiteLabelSettingsRequestDto
from docspace_api_sdk.models.additional_white_label_settings_wrapper import AdditionalWhiteLabelSettingsWrapper as AdditionalWhiteLabelSettingsWrapper
from docspace_api_sdk.models.admin_message_base_settings_request_dto import AdminMessageBaseSettingsRequestDto as AdminMessageBaseSettingsRequestDto
from docspace_api_sdk.models.admin_message_settings_request_dto import AdminMessageSettingsRequestDto as AdminMessageSettingsRequestDto
from docspace_api_sdk.models.ai_action_args import AiActionArgs as AiActionArgs
from docspace_api_sdk.models.ai_action_args_prompt import AiActionArgsPrompt as AiActionArgsPrompt
from docspace_api_sdk.models.ai_action_type import AiActionType as AiActionType
from docspace_api_sdk.models.ai_agent_new_items_dto import AiAgentNewItemsDto as AiAgentNewItemsDto
from docspace_api_sdk.models.ai_agents_create_request import AiAgentsCreateRequest as AiAgentsCreateRequest
from docspace_api_sdk.models.ai_agents_delete_request import AiAgentsDeleteRequest as AiAgentsDeleteRequest
from docspace_api_sdk.models.ai_agents_get200_response import AiAgentsGet200Response as AiAgentsGet200Response
from docspace_api_sdk.models.ai_agents_get200_response_all_of_response import AiAgentsGet200ResponseAllOfResponse as AiAgentsGet200ResponseAllOfResponse
from docspace_api_sdk.models.ai_agents_reset_quota_request import AiAgentsResetQuotaRequest as AiAgentsResetQuotaRequest
from docspace_api_sdk.models.ai_agents_update_quota_request import AiAgentsUpdateQuotaRequest as AiAgentsUpdateQuotaRequest
from docspace_api_sdk.models.ai_agents_update_quota_request_room_ids_inner import AiAgentsUpdateQuotaRequestRoomIdsInner as AiAgentsUpdateQuotaRequestRoomIdsInner
from docspace_api_sdk.models.ai_agents_update_request import AiAgentsUpdateRequest as AiAgentsUpdateRequest
from docspace_api_sdk.models.ai_api_date_time import AiApiDateTime as AiApiDateTime
from docspace_api_sdk.models.ai_approve_tool_call_request import AiApproveToolCallRequest as AiApproveToolCallRequest
from docspace_api_sdk.models.ai_assignment_mutation_result import AiAssignmentMutationResult as AiAssignmentMutationResult
from docspace_api_sdk.models.ai_assignments_assign_request import AiAssignmentsAssignRequest as AiAssignmentsAssignRequest
from docspace_api_sdk.models.ai_assignments_cascade_profile_delete_request import AiAssignmentsCascadeProfileDeleteRequest as AiAssignmentsCascadeProfileDeleteRequest
from docspace_api_sdk.models.ai_attachment import AiAttachment as AiAttachment
from docspace_api_sdk.models.ai_attachment_form_keys_inner import AiAttachmentFormKeysInner as AiAttachmentFormKeysInner
from docspace_api_sdk.models.ai_attachments_link_to_message_request import AiAttachmentsLinkToMessageRequest as AiAttachmentsLinkToMessageRequest
from docspace_api_sdk.models.ai_attachments_save_file_request import AiAttachmentsSaveFileRequest as AiAttachmentsSaveFileRequest
from docspace_api_sdk.models.ai_attachments_save_file_request_input import AiAttachmentsSaveFileRequestInput as AiAttachmentsSaveFileRequestInput
from docspace_api_sdk.models.ai_attachments_save_files_many_request import AiAttachmentsSaveFilesManyRequest as AiAttachmentsSaveFilesManyRequest
from docspace_api_sdk.models.ai_builtin_provider_type import AiBuiltinProviderType as AiBuiltinProviderType
from docspace_api_sdk.models.ai_bulk_assignment_result import AiBulkAssignmentResult as AiBulkAssignmentResult
from docspace_api_sdk.models.ai_bulk_assignment_result_errors_inner import AiBulkAssignmentResultErrorsInner as AiBulkAssignmentResultErrorsInner
from docspace_api_sdk.models.ai_chat_event import AiChatEvent as AiChatEvent
from docspace_api_sdk.models.ai_chat_price_dto import AiChatPriceDto as AiChatPriceDto
from docspace_api_sdk.models.ai_chat_settings_dto import AiChatSettingsDto as AiChatSettingsDto
from docspace_api_sdk.models.ai_chat_tool_permission_mode import AiChatToolPermissionMode as AiChatToolPermissionMode
from docspace_api_sdk.models.ai_chat_tool_prefs_scope import AiChatToolPrefsScope as AiChatToolPrefsScope
from docspace_api_sdk.models.ai_config_dto import AiConfigDto as AiConfigDto
from docspace_api_sdk.models.ai_create_profile_input import AiCreateProfileInput as AiCreateProfileInput
from docspace_api_sdk.models.ai_create_prompt_input import AiCreatePromptInput as AiCreatePromptInput
from docspace_api_sdk.models.ai_distributed_task_status import AiDistributedTaskStatus as AiDistributedTaskStatus
from docspace_api_sdk.models.ai_editor_tools_call200_response import AiEditorToolsCall200Response as AiEditorToolsCall200Response
from docspace_api_sdk.models.ai_editor_tools_call_request import AiEditorToolsCallRequest as AiEditorToolsCallRequest
from docspace_api_sdk.models.ai_editor_tools_list200_response import AiEditorToolsList200Response as AiEditorToolsList200Response
from docspace_api_sdk.models.ai_editor_tools_list200_response_tools_inner import AiEditorToolsList200ResponseToolsInner as AiEditorToolsList200ResponseToolsInner
from docspace_api_sdk.models.ai_embedding_price_dto import AiEmbeddingPriceDto as AiEmbeddingPriceDto
from docspace_api_sdk.models.ai_embedding_provider_type import AiEmbeddingProviderType as AiEmbeddingProviderType
from docspace_api_sdk.models.ai_employee_dto import AiEmployeeDto as AiEmployeeDto
from docspace_api_sdk.models.ai_entry_metadata import AiEntryMetadata as AiEntryMetadata
from docspace_api_sdk.models.ai_entry_metadata_custom_fields_inner import AiEntryMetadataCustomFieldsInner as AiEntryMetadataCustomFieldsInner
from docspace_api_sdk.models.ai_entry_metadata_field import AiEntryMetadataField as AiEntryMetadataField
from docspace_api_sdk.models.ai_entry_metadata_field_options_inner import AiEntryMetadataFieldOptionsInner as AiEntryMetadataFieldOptionsInner
from docspace_api_sdk.models.ai_entry_metadata_templates_inner import AiEntryMetadataTemplatesInner as AiEntryMetadataTemplatesInner
from docspace_api_sdk.models.ai_entry_pricing_dto_ai_chat_price_dto import AiEntryPricingDtoAiChatPriceDto as AiEntryPricingDtoAiChatPriceDto
from docspace_api_sdk.models.ai_entry_pricing_dto_ai_embedding_price_dto import AiEntryPricingDtoAiEmbeddingPriceDto as AiEntryPricingDtoAiEmbeddingPriceDto
from docspace_api_sdk.models.ai_entry_pricing_dto_ai_image_price_dto import AiEntryPricingDtoAiImagePriceDto as AiEntryPricingDtoAiImagePriceDto
from docspace_api_sdk.models.ai_entry_pricing_dto_decimal import AiEntryPricingDtoDecimal as AiEntryPricingDtoDecimal
from docspace_api_sdk.models.ai_error_code import AiErrorCode as AiErrorCode
from docspace_api_sdk.models.ai_error_data import AiErrorData as AiErrorData
from docspace_api_sdk.models.ai_error_response import AiErrorResponse as AiErrorResponse
from docspace_api_sdk.models.ai_export_text_to_docx202_response import AiExportTextToDocx202Response as AiExportTextToDocx202Response
from docspace_api_sdk.models.ai_export_text_to_docx_request import AiExportTextToDocxRequest as AiExportTextToDocxRequest
from docspace_api_sdk.models.ai_export_text_to_docx_request_folder_id import AiExportTextToDocxRequestFolderId as AiExportTextToDocxRequestFolderId
from docspace_api_sdk.models.ai_file_entry_base_dto import AiFileEntryBaseDto as AiFileEntryBaseDto
from docspace_api_sdk.models.ai_file_entry_dto import AiFileEntryDto as AiFileEntryDto
from docspace_api_sdk.models.ai_file_entry_dto_all_of_available_share_rights import AiFileEntryDtoAllOfAvailableShareRights as AiFileEntryDtoAllOfAvailableShareRights
from docspace_api_sdk.models.ai_file_entry_dto_all_of_security import AiFileEntryDtoAllOfSecurity as AiFileEntryDtoAllOfSecurity
from docspace_api_sdk.models.ai_file_entry_dto_all_of_share_settings import AiFileEntryDtoAllOfShareSettings as AiFileEntryDtoAllOfShareSettings
from docspace_api_sdk.models.ai_file_entry_type import AiFileEntryType as AiFileEntryType
from docspace_api_sdk.models.ai_file_operation_dto import AiFileOperationDto as AiFileOperationDto
from docspace_api_sdk.models.ai_file_operation_type import AiFileOperationType as AiFileOperationType
from docspace_api_sdk.models.ai_file_operation_wrapper import AiFileOperationWrapper as AiFileOperationWrapper
from docspace_api_sdk.models.ai_file_share import AiFileShare as AiFileShare
from docspace_api_sdk.models.ai_folder_array_wrapper import AiFolderArrayWrapper as AiFolderArrayWrapper
from docspace_api_sdk.models.ai_folder_content_dto import AiFolderContentDto as AiFolderContentDto
from docspace_api_sdk.models.ai_folder_content_wrapper import AiFolderContentWrapper as AiFolderContentWrapper
from docspace_api_sdk.models.ai_folder_dto import AiFolderDto as AiFolderDto
from docspace_api_sdk.models.ai_folder_mutation_result import AiFolderMutationResult as AiFolderMutationResult
from docspace_api_sdk.models.ai_folder_type import AiFolderType as AiFolderType
from docspace_api_sdk.models.ai_folder_wrapper import AiFolderWrapper as AiFolderWrapper
from docspace_api_sdk.models.ai_image_price_dto import AiImagePriceDto as AiImagePriceDto
from docspace_api_sdk.models.ai_import_error import AiImportError as AiImportError
from docspace_api_sdk.models.ai_import_mode import AiImportMode as AiImportMode
from docspace_api_sdk.models.ai_import_result import AiImportResult as AiImportResult
from docspace_api_sdk.models.ai_import_result_imported import AiImportResultImported as AiImportResultImported
from docspace_api_sdk.models.ai_logo_cover_dto import AiLogoCoverDto as AiLogoCoverDto
from docspace_api_sdk.models.ai_logo_dto import AiLogoDto as AiLogoDto
from docspace_api_sdk.models.ai_mcp_item import AiMCPItem as AiMCPItem
from docspace_api_sdk.models.ai_meta_fill200_response import AiMetaFill200Response as AiMetaFill200Response
from docspace_api_sdk.models.ai_meta_fill200_response_filled_inner import AiMetaFill200ResponseFilledInner as AiMetaFill200ResponseFilledInner
from docspace_api_sdk.models.ai_meta_fill200_response_filled_inner_value import AiMetaFill200ResponseFilledInnerValue as AiMetaFill200ResponseFilledInnerValue
from docspace_api_sdk.models.ai_meta_fill200_response_sources_inner import AiMetaFill200ResponseSourcesInner as AiMetaFill200ResponseSourcesInner
from docspace_api_sdk.models.ai_meta_fill200_response_unresolved_inner import AiMetaFill200ResponseUnresolvedInner as AiMetaFill200ResponseUnresolvedInner
from docspace_api_sdk.models.ai_meta_fill_request import AiMetaFillRequest as AiMetaFillRequest
from docspace_api_sdk.models.ai_meta_generate200_response import AiMetaGenerate200Response as AiMetaGenerate200Response
from docspace_api_sdk.models.ai_meta_generate200_response_fields_inner import AiMetaGenerate200ResponseFieldsInner as AiMetaGenerate200ResponseFieldsInner
from docspace_api_sdk.models.ai_meta_generate200_response_skipped_inner import AiMetaGenerate200ResponseSkippedInner as AiMetaGenerate200ResponseSkippedInner
from docspace_api_sdk.models.ai_meta_generate200_response_sources_inner import AiMetaGenerate200ResponseSourcesInner as AiMetaGenerate200ResponseSourcesInner
from docspace_api_sdk.models.ai_meta_generate402_response import AiMetaGenerate402Response as AiMetaGenerate402Response
from docspace_api_sdk.models.ai_meta_generate_request import AiMetaGenerateRequest as AiMetaGenerateRequest
from docspace_api_sdk.models.ai_meta_generate_request_id import AiMetaGenerateRequestId as AiMetaGenerateRequestId
from docspace_api_sdk.models.ai_metadata_match_dto import AiMetadataMatchDto as AiMetadataMatchDto
from docspace_api_sdk.models.ai_metadata_value import AiMetadataValue as AiMetadataValue
from docspace_api_sdk.models.ai_model import AiModel as AiModel
from docspace_api_sdk.models.ai_new_items_agent_new_items_array_wrapper import AiNewItemsAgentNewItemsArrayWrapper as AiNewItemsAgentNewItemsArrayWrapper
from docspace_api_sdk.models.ai_new_items_dto_agent_new_items_dto import AiNewItemsDtoAgentNewItemsDto as AiNewItemsDtoAgentNewItemsDto
from docspace_api_sdk.models.ai_open_ai_chat_completion_chunk import AiOpenAIChatCompletionChunk as AiOpenAIChatCompletionChunk
from docspace_api_sdk.models.ai_open_ai_choice_delta import AiOpenAIChoiceDelta as AiOpenAIChoiceDelta
from docspace_api_sdk.models.ai_open_ai_chunk_choice import AiOpenAIChunkChoice as AiOpenAIChunkChoice
from docspace_api_sdk.models.ai_open_ai_finish_reason import AiOpenAIFinishReason as AiOpenAIFinishReason
from docspace_api_sdk.models.ai_open_ai_stream_chunk import AiOpenAIStreamChunk as AiOpenAIStreamChunk
from docspace_api_sdk.models.ai_open_ai_stream_error import AiOpenAIStreamError as AiOpenAIStreamError
from docspace_api_sdk.models.ai_open_ai_stream_error_error import AiOpenAIStreamErrorError as AiOpenAIStreamErrorError
from docspace_api_sdk.models.ai_open_ai_tool_call_delta import AiOpenAIToolCallDelta as AiOpenAIToolCallDelta
from docspace_api_sdk.models.ai_open_ai_tool_call_delta_function import AiOpenAIToolCallDeltaFunction as AiOpenAIToolCallDeltaFunction
from docspace_api_sdk.models.ai_open_or_create_result import AiOpenOrCreateResult as AiOpenOrCreateResult
from docspace_api_sdk.models.ai_openai_chat_completions403_response import AiOpenaiChatCompletions403Response as AiOpenaiChatCompletions403Response
from docspace_api_sdk.models.ai_openai_chat_completions403_response_error import AiOpenaiChatCompletions403ResponseError as AiOpenaiChatCompletions403ResponseError
from docspace_api_sdk.models.ai_openai_images_generations403_response import AiOpenaiImagesGenerations403Response as AiOpenaiImagesGenerations403Response
from docspace_api_sdk.models.ai_openai_images_generations403_response_error import AiOpenaiImagesGenerations403ResponseError as AiOpenaiImagesGenerations403ResponseError
from docspace_api_sdk.models.ai_preferences_set_deep_mode_request import AiPreferencesSetDeepModeRequest as AiPreferencesSetDeepModeRequest
from docspace_api_sdk.models.ai_preferences_set_reasoning_level_request import AiPreferencesSetReasoningLevelRequest as AiPreferencesSetReasoningLevelRequest
from docspace_api_sdk.models.ai_preferences_set_tool_permission_mode_request import AiPreferencesSetToolPermissionModeRequest as AiPreferencesSetToolPermissionModeRequest
from docspace_api_sdk.models.ai_price_currency_dto import AiPriceCurrencyDto as AiPriceCurrencyDto
from docspace_api_sdk.models.ai_prices_dto import AiPricesDto as AiPricesDto
from docspace_api_sdk.models.ai_prices_wrapper import AiPricesWrapper as AiPricesWrapper
from docspace_api_sdk.models.ai_profile import AiProfile as AiProfile
from docspace_api_sdk.models.ai_profile_mutation_result import AiProfileMutationResult as AiProfileMutationResult
from docspace_api_sdk.models.ai_profiles_create400_response import AiProfilesCreate400Response as AiProfilesCreate400Response
from docspace_api_sdk.models.ai_profiles_get_by_id200_response import AiProfilesGetById200Response as AiProfilesGetById200Response
from docspace_api_sdk.models.ai_profiles_list_provider_models400_response import AiProfilesListProviderModels400Response as AiProfilesListProviderModels400Response
from docspace_api_sdk.models.ai_profiles_list_provider_models400_response_any_of import AiProfilesListProviderModels400ResponseAnyOf as AiProfilesListProviderModels400ResponseAnyOf
from docspace_api_sdk.models.ai_profiles_list_provider_models_request import AiProfilesListProviderModelsRequest as AiProfilesListProviderModelsRequest
from docspace_api_sdk.models.ai_profiles_test_connection200_response import AiProfilesTestConnection200Response as AiProfilesTestConnection200Response
from docspace_api_sdk.models.ai_profiles_test_connection200_response_any_of import AiProfilesTestConnection200ResponseAnyOf as AiProfilesTestConnection200ResponseAnyOf
from docspace_api_sdk.models.ai_prompt import AiPrompt as AiPrompt
from docspace_api_sdk.models.ai_prompt_bundle import AiPromptBundle as AiPromptBundle
from docspace_api_sdk.models.ai_prompt_folder import AiPromptFolder as AiPromptFolder
from docspace_api_sdk.models.ai_prompt_mutation_result import AiPromptMutationResult as AiPromptMutationResult
from docspace_api_sdk.models.ai_prompts_import_bundle_request import AiPromptsImportBundleRequest as AiPromptsImportBundleRequest
from docspace_api_sdk.models.ai_prompts_import_bundle_request_options import AiPromptsImportBundleRequestOptions as AiPromptsImportBundleRequestOptions
from docspace_api_sdk.models.ai_prompts_move_request import AiPromptsMoveRequest as AiPromptsMoveRequest
from docspace_api_sdk.models.ai_prompts_rename_folder_request import AiPromptsRenameFolderRequest as AiPromptsRenameFolderRequest
from docspace_api_sdk.models.ai_prompts_update_request import AiPromptsUpdateRequest as AiPromptsUpdateRequest
from docspace_api_sdk.models.ai_prompts_update_request_updates import AiPromptsUpdateRequestUpdates as AiPromptsUpdateRequestUpdates
from docspace_api_sdk.models.ai_provider import AiProvider as AiProvider
from docspace_api_sdk.models.ai_provider_type import AiProviderType as AiProviderType
from docspace_api_sdk.models.ai_reasoning_depth import AiReasoningDepth as AiReasoningDepth
from docspace_api_sdk.models.ai_reasoning_level import AiReasoningLevel as AiReasoningLevel
from docspace_api_sdk.models.ai_reasoning_support import AiReasoningSupport as AiReasoningSupport
from docspace_api_sdk.models.ai_regenerate_stream_request import AiRegenerateStreamRequest as AiRegenerateStreamRequest
from docspace_api_sdk.models.ai_resolved_assignment import AiResolvedAssignment as AiResolvedAssignment
from docspace_api_sdk.models.ai_room_data_lifetime_dto import AiRoomDataLifetimeDto as AiRoomDataLifetimeDto
from docspace_api_sdk.models.ai_room_data_lifetime_period import AiRoomDataLifetimePeriod as AiRoomDataLifetimePeriod
from docspace_api_sdk.models.ai_room_type import AiRoomType as AiRoomType
from docspace_api_sdk.models.ai_send_custom_request import AiSendCustomRequest as AiSendCustomRequest
from docspace_api_sdk.models.ai_send_request import AiSendRequest as AiSendRequest
from docspace_api_sdk.models.ai_send_stream_body import AiSendStreamBody as AiSendStreamBody
from docspace_api_sdk.models.ai_settings_dto import AiSettingsDto as AiSettingsDto
from docspace_api_sdk.models.ai_settings_wrapper import AiSettingsWrapper as AiSettingsWrapper
from docspace_api_sdk.models.ai_success_response import AiSuccessResponse as AiSuccessResponse
from docspace_api_sdk.models.ai_thread import AiThread as AiThread
from docspace_api_sdk.models.ai_thread_message_like import AiThreadMessageLike as AiThreadMessageLike
from docspace_api_sdk.models.ai_thread_message_like_content import AiThreadMessageLikeContent as AiThreadMessageLikeContent
from docspace_api_sdk.models.ai_thread_message_like_content_any_of_inner import AiThreadMessageLikeContentAnyOfInner as AiThreadMessageLikeContentAnyOfInner
from docspace_api_sdk.models.ai_thread_message_like_status import AiThreadMessageLikeStatus as AiThreadMessageLikeStatus
from docspace_api_sdk.models.ai_threads_append_user_message200_response import AiThreadsAppendUserMessage200Response as AiThreadsAppendUserMessage200Response
from docspace_api_sdk.models.ai_threads_append_user_message_request import AiThreadsAppendUserMessageRequest as AiThreadsAppendUserMessageRequest
from docspace_api_sdk.models.ai_threads_create_request import AiThreadsCreateRequest as AiThreadsCreateRequest
from docspace_api_sdk.models.ai_threads_open_or_create_request import AiThreadsOpenOrCreateRequest as AiThreadsOpenOrCreateRequest
from docspace_api_sdk.models.ai_threads_open_or_create_request_entity_meta import AiThreadsOpenOrCreateRequestEntityMeta as AiThreadsOpenOrCreateRequestEntityMeta
from docspace_api_sdk.models.ai_threads_regenerate_title200_response import AiThreadsRegenerateTitle200Response as AiThreadsRegenerateTitle200Response
from docspace_api_sdk.models.ai_threads_regenerate_title_request import AiThreadsRegenerateTitleRequest as AiThreadsRegenerateTitleRequest
from docspace_api_sdk.models.ai_threads_rename_request import AiThreadsRenameRequest as AiThreadsRenameRequest
from docspace_api_sdk.models.ai_threads_touch_request import AiThreadsTouchRequest as AiThreadsTouchRequest
from docspace_api_sdk.models.ai_threads_update_message_request import AiThreadsUpdateMessageRequest as AiThreadsUpdateMessageRequest
from docspace_api_sdk.models.ai_tool_annotations import AiToolAnnotations as AiToolAnnotations
from docspace_api_sdk.models.ai_tool_call_data import AiToolCallData as AiToolCallData
from docspace_api_sdk.models.ai_tool_permission_mode import AiToolPermissionMode as AiToolPermissionMode
from docspace_api_sdk.models.ai_tools_add_custom_server_request import AiToolsAddCustomServerRequest as AiToolsAddCustomServerRequest
from docspace_api_sdk.models.ai_tools_bulk_result import AiToolsBulkResult as AiToolsBulkResult
from docspace_api_sdk.models.ai_tools_bulk_result_errors_inner import AiToolsBulkResultErrorsInner as AiToolsBulkResultErrorsInner
from docspace_api_sdk.models.ai_tools_list_system_tools200_response import AiToolsListSystemTools200Response as AiToolsListSystemTools200Response
from docspace_api_sdk.models.ai_tools_mutation_result import AiToolsMutationResult as AiToolsMutationResult
from docspace_api_sdk.models.ai_tools_remove_custom_server_request import AiToolsRemoveCustomServerRequest as AiToolsRemoveCustomServerRequest
from docspace_api_sdk.models.ai_tools_replace_all_custom_servers_request import AiToolsReplaceAllCustomServersRequest as AiToolsReplaceAllCustomServersRequest
from docspace_api_sdk.models.ai_tools_set_allow_always_request import AiToolsSetAllowAlwaysRequest as AiToolsSetAllowAlwaysRequest
from docspace_api_sdk.models.ai_tools_set_disabled_request import AiToolsSetDisabledRequest as AiToolsSetDisabledRequest
from docspace_api_sdk.models.ai_tools_update_custom_server_request import AiToolsUpdateCustomServerRequest as AiToolsUpdateCustomServerRequest
from docspace_api_sdk.models.ai_user_settings_dto import AiUserSettingsDto as AiUserSettingsDto
from docspace_api_sdk.models.ai_user_settings_wrapper import AiUserSettingsWrapper as AiUserSettingsWrapper
from docspace_api_sdk.models.ai_vectorization_settings_dto import AiVectorizationSettingsDto as AiVectorizationSettingsDto
from docspace_api_sdk.models.ai_vectorization_settings_wrapper import AiVectorizationSettingsWrapper as AiVectorizationSettingsWrapper
from docspace_api_sdk.models.ai_vectorization_start_task200_response import AiVectorizationStartTask200Response as AiVectorizationStartTask200Response
from docspace_api_sdk.models.ai_vectorization_start_task_request import AiVectorizationStartTaskRequest as AiVectorizationStartTaskRequest
from docspace_api_sdk.models.ai_watermark_additions import AiWatermarkAdditions as AiWatermarkAdditions
from docspace_api_sdk.models.ai_watermark_dto import AiWatermarkDto as AiWatermarkDto
from docspace_api_sdk.models.ai_web_search_config import AiWebSearchConfig as AiWebSearchConfig
from docspace_api_sdk.models.ai_web_search_configure400_response import AiWebSearchConfigure400Response as AiWebSearchConfigure400Response
from docspace_api_sdk.models.ai_web_search_configure_request import AiWebSearchConfigureRequest as AiWebSearchConfigureRequest
from docspace_api_sdk.models.ai_web_search_mutation_result import AiWebSearchMutationResult as AiWebSearchMutationResult
from docspace_api_sdk.models.ai_web_search_set_active_config_request import AiWebSearchSetActiveConfigRequest as AiWebSearchSetActiveConfigRequest
from docspace_api_sdk.models.amazon_s3_region_array_wrapper import AmazonS3RegionArrayWrapper as AmazonS3RegionArrayWrapper
from docspace_api_sdk.models.amazon_s3_region_dto import AmazonS3RegionDto as AmazonS3RegionDto
from docspace_api_sdk.models.anonymous_config_dto import AnonymousConfigDto as AnonymousConfigDto
from docspace_api_sdk.models.api_date_time import ApiDateTime as ApiDateTime
from docspace_api_sdk.models.api_key_response_array_wrapper import ApiKeyResponseArrayWrapper as ApiKeyResponseArrayWrapper
from docspace_api_sdk.models.api_key_response_dto import ApiKeyResponseDto as ApiKeyResponseDto
from docspace_api_sdk.models.api_key_response_wrapper import ApiKeyResponseWrapper as ApiKeyResponseWrapper
from docspace_api_sdk.models.app_array_wrapper import AppArrayWrapper as AppArrayWrapper
from docspace_api_sdk.models.app_dto import AppDto as AppDto
from docspace_api_sdk.models.app_wrapper import AppWrapper as AppWrapper
from docspace_api_sdk.models.apply_filter_option import ApplyFilterOption as ApplyFilterOption
from docspace_api_sdk.models.archive_room_request import ArchiveRoomRequest as ArchiveRoomRequest
from docspace_api_sdk.models.array_array_wrapper import ArrayArrayWrapper as ArrayArrayWrapper
from docspace_api_sdk.models.assign_metadata_templates import AssignMetadataTemplates as AssignMetadataTemplates
from docspace_api_sdk.models.audit_event_array_wrapper import AuditEventArrayWrapper as AuditEventArrayWrapper
from docspace_api_sdk.models.audit_event_dto import AuditEventDto as AuditEventDto
from docspace_api_sdk.models.audit_report_format import AuditReportFormat as AuditReportFormat
from docspace_api_sdk.models.audit_trail_action_dto import AuditTrailActionDto as AuditTrailActionDto
from docspace_api_sdk.models.audit_trail_module_dto import AuditTrailModuleDto as AuditTrailModuleDto
from docspace_api_sdk.models.audit_trail_product_array_wrapper import AuditTrailProductArrayWrapper as AuditTrailProductArrayWrapper
from docspace_api_sdk.models.audit_trail_product_dto import AuditTrailProductDto as AuditTrailProductDto
from docspace_api_sdk.models.audit_trail_types_dto import AuditTrailTypesDto as AuditTrailTypesDto
from docspace_api_sdk.models.audit_trail_types_wrapper import AuditTrailTypesWrapper as AuditTrailTypesWrapper
from docspace_api_sdk.models.auth_key_dto import AuthKeyDto as AuthKeyDto
from docspace_api_sdk.models.auth_key_request import AuthKeyRequest as AuthKeyRequest
from docspace_api_sdk.models.auth_request_dto import AuthRequestDto as AuthRequestDto
from docspace_api_sdk.models.auth_service_array_wrapper import AuthServiceArrayWrapper as AuthServiceArrayWrapper
from docspace_api_sdk.models.auth_service_dto import AuthServiceDto as AuthServiceDto
from docspace_api_sdk.models.auth_with_code_request_dto import AuthWithCodeRequestDto as AuthWithCodeRequestDto
from docspace_api_sdk.models.authentication_token_dto import AuthenticationTokenDto as AuthenticationTokenDto
from docspace_api_sdk.models.authentication_token_wrapper import AuthenticationTokenWrapper as AuthenticationTokenWrapper
from docspace_api_sdk.models.auto_clean_up_data_dto import AutoCleanUpDataDto as AutoCleanUpDataDto
from docspace_api_sdk.models.auto_clean_up_data_wrapper import AutoCleanUpDataWrapper as AutoCleanUpDataWrapper
from docspace_api_sdk.models.auto_cleanup_request_dto import AutoCleanupRequestDto as AutoCleanupRequestDto
from docspace_api_sdk.models.backup_cron_request import BackupCronRequest as BackupCronRequest
from docspace_api_sdk.models.backup_history_record_array_wrapper import BackupHistoryRecordArrayWrapper as BackupHistoryRecordArrayWrapper
from docspace_api_sdk.models.backup_history_record_dto import BackupHistoryRecordDto as BackupHistoryRecordDto
from docspace_api_sdk.models.backup_period import BackupPeriod as BackupPeriod
from docspace_api_sdk.models.backup_progress_dto import BackupProgressDto as BackupProgressDto
from docspace_api_sdk.models.backup_progress_enum import BackupProgressEnum as BackupProgressEnum
from docspace_api_sdk.models.backup_progress_wrapper import BackupProgressWrapper as BackupProgressWrapper
from docspace_api_sdk.models.backup_service_state_dto import BackupServiceStateDto as BackupServiceStateDto
from docspace_api_sdk.models.backup_service_state_wrapper import BackupServiceStateWrapper as BackupServiceStateWrapper
from docspace_api_sdk.models.backup_storage_type import BackupStorageType as BackupStorageType
from docspace_api_sdk.models.backups_count_result_dto import BackupsCountResultDto as BackupsCountResultDto
from docspace_api_sdk.models.backups_count_result_wrapper import BackupsCountResultWrapper as BackupsCountResultWrapper
from docspace_api_sdk.models.balance_dto import BalanceDto as BalanceDto
from docspace_api_sdk.models.balance_wrapper import BalanceWrapper as BalanceWrapper
from docspace_api_sdk.models.base_batch_request_dto import BaseBatchRequestDto as BaseBatchRequestDto
from docspace_api_sdk.models.base_batch_request_dto_all_of_file_ids import BaseBatchRequestDtoAllOfFileIds as BaseBatchRequestDtoAllOfFileIds
from docspace_api_sdk.models.base_batch_request_dto_all_of_folder_ids import BaseBatchRequestDtoAllOfFolderIds as BaseBatchRequestDtoAllOfFolderIds
from docspace_api_sdk.models.batch_request_dto import BatchRequestDto as BatchRequestDto
from docspace_api_sdk.models.batch_request_dto_all_of_dest_folder_id import BatchRequestDtoAllOfDestFolderId as BatchRequestDtoAllOfDestFolderId
from docspace_api_sdk.models.batch_request_dto_all_of_file_ids import BatchRequestDtoAllOfFileIds as BatchRequestDtoAllOfFileIds
from docspace_api_sdk.models.batch_request_dto_all_of_folder_ids import BatchRequestDtoAllOfFolderIds as BatchRequestDtoAllOfFolderIds
from docspace_api_sdk.models.batch_tags_request_dto import BatchTagsRequestDto as BatchTagsRequestDto
from docspace_api_sdk.models.boolean_wrapper import BooleanWrapper as BooleanWrapper
from docspace_api_sdk.models.capabilities_dto import CapabilitiesDto as CapabilitiesDto
from docspace_api_sdk.models.capabilities_wrapper import CapabilitiesWrapper as CapabilitiesWrapper
from docspace_api_sdk.models.change_client_activation_request import ChangeClientActivationRequest as ChangeClientActivationRequest
from docspace_api_sdk.models.change_email_request import ChangeEmailRequest as ChangeEmailRequest
from docspace_api_sdk.models.change_history_request import ChangeHistoryRequest as ChangeHistoryRequest
from docspace_api_sdk.models.change_owner_request_dto import ChangeOwnerRequestDto as ChangeOwnerRequestDto
from docspace_api_sdk.models.change_password_request import ChangePasswordRequest as ChangePasswordRequest
from docspace_api_sdk.models.change_wallet_service_state_request_dto import ChangeWalletServiceStateRequestDto as ChangeWalletServiceStateRequestDto
from docspace_api_sdk.models.chat_settings import ChatSettings as ChatSettings
from docspace_api_sdk.models.chat_settings_dto import ChatSettingsDto as ChatSettingsDto
from docspace_api_sdk.models.check_confirm_request_dto import CheckConfirmRequestDto as CheckConfirmRequestDto
from docspace_api_sdk.models.check_conversion_request_dto import CheckConversionRequestDto as CheckConversionRequestDto
from docspace_api_sdk.models.check_dest_folder_dto import CheckDestFolderDto as CheckDestFolderDto
from docspace_api_sdk.models.check_dest_folder_result import CheckDestFolderResult as CheckDestFolderResult
from docspace_api_sdk.models.check_dest_folder_wrapper import CheckDestFolderWrapper as CheckDestFolderWrapper
from docspace_api_sdk.models.check_doc_service_url_request_dto import CheckDocServiceUrlRequestDto as CheckDocServiceUrlRequestDto
from docspace_api_sdk.models.check_fill_form_draft_request import CheckFillFormDraftRequest as CheckFillFormDraftRequest
from docspace_api_sdk.models.check_upload_request import CheckUploadRequest as CheckUploadRequest
from docspace_api_sdk.models.chunked_upload_session_dto import ChunkedUploadSessionDto as ChunkedUploadSessionDto
from docspace_api_sdk.models.chunked_upload_session_result_dto import ChunkedUploadSessionResultDto as ChunkedUploadSessionResultDto
from docspace_api_sdk.models.chunked_upload_session_result_wrapper import ChunkedUploadSessionResultWrapper as ChunkedUploadSessionResultWrapper
from docspace_api_sdk.models.chunked_upload_session_wrapper import ChunkedUploadSessionWrapper as ChunkedUploadSessionWrapper
from docspace_api_sdk.models.client_info_response import ClientInfoResponse as ClientInfoResponse
from docspace_api_sdk.models.client_response import ClientResponse as ClientResponse
from docspace_api_sdk.models.client_secret_response import ClientSecretResponse as ClientSecretResponse
from docspace_api_sdk.models.co_editing_config_dto import CoEditingConfigDto as CoEditingConfigDto
from docspace_api_sdk.models.co_editing_config_mode import CoEditingConfigMode as CoEditingConfigMode
from docspace_api_sdk.models.color_theme_colors_dto import ColorThemeColorsDto as ColorThemeColorsDto
from docspace_api_sdk.models.color_theme_colors_request_dto import ColorThemeColorsRequestDto as ColorThemeColorsRequestDto
from docspace_api_sdk.models.company_white_label_settings_dto import CompanyWhiteLabelSettingsDto as CompanyWhiteLabelSettingsDto
from docspace_api_sdk.models.company_white_label_settings_request_dto import CompanyWhiteLabelSettingsRequestDto as CompanyWhiteLabelSettingsRequestDto
from docspace_api_sdk.models.company_white_label_settings_wrapper import CompanyWhiteLabelSettingsWrapper as CompanyWhiteLabelSettingsWrapper
from docspace_api_sdk.models.configuration_dto import ConfigurationDto as ConfigurationDto
from docspace_api_sdk.models.configuration_wrapper import ConfigurationWrapper as ConfigurationWrapper
from docspace_api_sdk.models.confirm_data import ConfirmData as ConfirmData
from docspace_api_sdk.models.confirm_dto import ConfirmDto as ConfirmDto
from docspace_api_sdk.models.confirm_type import ConfirmType as ConfirmType
from docspace_api_sdk.models.confirm_wrapper import ConfirmWrapper as ConfirmWrapper
from docspace_api_sdk.models.connection_test_result_dto import ConnectionTestResultDto as ConnectionTestResultDto
from docspace_api_sdk.models.connection_test_result_wrapper import ConnectionTestResultWrapper as ConnectionTestResultWrapper
from docspace_api_sdk.models.contact import Contact as Contact
from docspace_api_sdk.models.conversation_result_array_wrapper import ConversationResultArrayWrapper as ConversationResultArrayWrapper
from docspace_api_sdk.models.conversation_result_dto import ConversationResultDto as ConversationResultDto
from docspace_api_sdk.models.convert_document_layout_request import ConvertDocumentLayoutRequest as ConvertDocumentLayoutRequest
from docspace_api_sdk.models.convert_document_renderer_request import ConvertDocumentRendererRequest as ConvertDocumentRendererRequest
from docspace_api_sdk.models.convert_file_request_dto import ConvertFileRequestDto as ConvertFileRequestDto
from docspace_api_sdk.models.convert_pdf_request import ConvertPdfRequest as ConvertPdfRequest
from docspace_api_sdk.models.convert_spreadsheet_layout_request import ConvertSpreadsheetLayoutRequest as ConvertSpreadsheetLayoutRequest
from docspace_api_sdk.models.convert_spreadsheet_margins_request import ConvertSpreadsheetMarginsRequest as ConvertSpreadsheetMarginsRequest
from docspace_api_sdk.models.convert_spreadsheet_page_size_request import ConvertSpreadsheetPageSizeRequest as ConvertSpreadsheetPageSizeRequest
from docspace_api_sdk.models.convert_thumbnail_request import ConvertThumbnailRequest as ConvertThumbnailRequest
from docspace_api_sdk.models.cookie_settings_dto import CookieSettingsDto as CookieSettingsDto
from docspace_api_sdk.models.cookie_settings_request_dto import CookieSettingsRequestDto as CookieSettingsRequestDto
from docspace_api_sdk.models.cookie_settings_wrapper import CookieSettingsWrapper as CookieSettingsWrapper
from docspace_api_sdk.models.copy_as_request import CopyAsRequest as CopyAsRequest
from docspace_api_sdk.models.copy_as_request_dest_folder_id import CopyAsRequestDestFolderId as CopyAsRequestDestFolderId
from docspace_api_sdk.models.cover_request_dto import CoverRequestDto as CoverRequestDto
from docspace_api_sdk.models.covers_result_array_wrapper import CoversResultArrayWrapper as CoversResultArrayWrapper
from docspace_api_sdk.models.covers_result_dto import CoversResultDto as CoversResultDto
from docspace_api_sdk.models.create_api_key_request_dto import CreateApiKeyRequestDto as CreateApiKeyRequestDto
from docspace_api_sdk.models.create_backup_schedule_request_dto import CreateBackupScheduleRequestDto as CreateBackupScheduleRequestDto
from docspace_api_sdk.models.create_client_request import CreateClientRequest as CreateClientRequest
from docspace_api_sdk.models.create_file_request import CreateFileRequest as CreateFileRequest
from docspace_api_sdk.models.create_file_request_template_id import CreateFileRequestTemplateId as CreateFileRequestTemplateId
from docspace_api_sdk.models.create_folder_request import CreateFolderRequest as CreateFolderRequest
from docspace_api_sdk.models.create_metadata_template_request_dto import CreateMetadataTemplateRequestDto as CreateMetadataTemplateRequestDto
from docspace_api_sdk.models.create_room_from_template_dto import CreateRoomFromTemplateDto as CreateRoomFromTemplateDto
from docspace_api_sdk.models.create_room_request_dto import CreateRoomRequestDto as CreateRoomRequestDto
from docspace_api_sdk.models.create_service_limit_request_dto import CreateServiceLimitRequestDto as CreateServiceLimitRequestDto
from docspace_api_sdk.models.create_tag_request_dto import CreateTagRequestDto as CreateTagRequestDto
from docspace_api_sdk.models.create_text_or_html_file_request import CreateTextOrHtmlFileRequest as CreateTextOrHtmlFileRequest
from docspace_api_sdk.models.create_third_party_room_request import CreateThirdPartyRoomRequest as CreateThirdPartyRoomRequest
from docspace_api_sdk.models.create_webhooks_config_request_dto import CreateWebhooksConfigRequestDto as CreateWebhooksConfigRequestDto
from docspace_api_sdk.models.cron_params_dto import CronParamsDto as CronParamsDto
from docspace_api_sdk.models.csp_dto import CspDto as CspDto
from docspace_api_sdk.models.csp_request_dto import CspRequestDto as CspRequestDto
from docspace_api_sdk.models.csp_wrapper import CspWrapper as CspWrapper
from docspace_api_sdk.models.currencies_array_wrapper import CurrenciesArrayWrapper as CurrenciesArrayWrapper
from docspace_api_sdk.models.currencies_dto import CurrenciesDto as CurrenciesDto
from docspace_api_sdk.models.current_license_info import CurrentLicenseInfo as CurrentLicenseInfo
from docspace_api_sdk.models.custom_color_theme_dto import CustomColorThemeDto as CustomColorThemeDto
from docspace_api_sdk.models.custom_color_theme_request_dto import CustomColorThemeRequestDto as CustomColorThemeRequestDto
from docspace_api_sdk.models.custom_color_themes_settings_dto import CustomColorThemesSettingsDto as CustomColorThemesSettingsDto
from docspace_api_sdk.models.custom_color_themes_settings_request_dto import CustomColorThemesSettingsRequestDto as CustomColorThemesSettingsRequestDto
from docspace_api_sdk.models.custom_color_themes_settings_wrapper import CustomColorThemesSettingsWrapper as CustomColorThemesSettingsWrapper
from docspace_api_sdk.models.custom_field_request import CustomFieldRequest as CustomFieldRequest
from docspace_api_sdk.models.custom_field_value_array_wrapper import CustomFieldValueArrayWrapper as CustomFieldValueArrayWrapper
from docspace_api_sdk.models.custom_field_value_dto import CustomFieldValueDto as CustomFieldValueDto
from docspace_api_sdk.models.custom_filter_request import CustomFilterRequest as CustomFilterRequest
from docspace_api_sdk.models.customer_config_dto import CustomerConfigDto as CustomerConfigDto
from docspace_api_sdk.models.customer_info_dto import CustomerInfoDto as CustomerInfoDto
from docspace_api_sdk.models.customer_info_wrapper import CustomerInfoWrapper as CustomerInfoWrapper
from docspace_api_sdk.models.customer_monthly_usage_array_wrapper import CustomerMonthlyUsageArrayWrapper as CustomerMonthlyUsageArrayWrapper
from docspace_api_sdk.models.customer_monthly_usage_dto import CustomerMonthlyUsageDto as CustomerMonthlyUsageDto
from docspace_api_sdk.models.customer_monthly_usage_report_request_dto import CustomerMonthlyUsageReportRequestDto as CustomerMonthlyUsageReportRequestDto
from docspace_api_sdk.models.customer_operations_report_request_dto import CustomerOperationsReportRequestDto as CustomerOperationsReportRequestDto
from docspace_api_sdk.models.customer_service_usage_dto import CustomerServiceUsageDto as CustomerServiceUsageDto
from docspace_api_sdk.models.customer_service_usage_report_dto import CustomerServiceUsageReportDto as CustomerServiceUsageReportDto
from docspace_api_sdk.models.customer_service_usage_report_request_dto import CustomerServiceUsageReportRequestDto as CustomerServiceUsageReportRequestDto
from docspace_api_sdk.models.customer_service_usage_report_wrapper import CustomerServiceUsageReportWrapper as CustomerServiceUsageReportWrapper
from docspace_api_sdk.models.customization_config_dto import CustomizationConfigDto as CustomizationConfigDto
from docspace_api_sdk.models.dark_theme_settings_dto import DarkThemeSettingsDto as DarkThemeSettingsDto
from docspace_api_sdk.models.dark_theme_settings_request_dto import DarkThemeSettingsRequestDto as DarkThemeSettingsRequestDto
from docspace_api_sdk.models.dark_theme_settings_type import DarkThemeSettingsType as DarkThemeSettingsType
from docspace_api_sdk.models.dark_theme_settings_wrapper import DarkThemeSettingsWrapper as DarkThemeSettingsWrapper
from docspace_api_sdk.models.date_to_auto_clean_up import DateToAutoCleanUp as DateToAutoCleanUp
from docspace_api_sdk.models.deep_link_configuration_request_dto import DeepLinkConfigurationRequestDto as DeepLinkConfigurationRequestDto
from docspace_api_sdk.models.deep_link_dto import DeepLinkDto as DeepLinkDto
from docspace_api_sdk.models.deep_link_handling_mode import DeepLinkHandlingMode as DeepLinkHandlingMode
from docspace_api_sdk.models.deep_link_settings_request_dto import DeepLinkSettingsRequestDto as DeepLinkSettingsRequestDto
from docspace_api_sdk.models.default_product_request_dto import DefaultProductRequestDto as DefaultProductRequestDto
from docspace_api_sdk.models.default_template_item_dto import DefaultTemplateItemDto as DefaultTemplateItemDto
from docspace_api_sdk.models.default_template_settings_dto import DefaultTemplateSettingsDto as DefaultTemplateSettingsDto
from docspace_api_sdk.models.default_template_settings_request_dto import DefaultTemplateSettingsRequestDto as DefaultTemplateSettingsRequestDto
from docspace_api_sdk.models.default_template_settings_request_dto_selected_file import DefaultTemplateSettingsRequestDtoSelectedFile as DefaultTemplateSettingsRequestDtoSelectedFile
from docspace_api_sdk.models.default_template_settings_reset_request_dto import DefaultTemplateSettingsResetRequestDto as DefaultTemplateSettingsResetRequestDto
from docspace_api_sdk.models.default_template_settings_wrapper import DefaultTemplateSettingsWrapper as DefaultTemplateSettingsWrapper
from docspace_api_sdk.models.delete_batch_request_dto import DeleteBatchRequestDto as DeleteBatchRequestDto
from docspace_api_sdk.models.delete_batch_request_dto_all_of_file_ids import DeleteBatchRequestDtoAllOfFileIds as DeleteBatchRequestDtoAllOfFileIds
from docspace_api_sdk.models.delete_batch_request_dto_all_of_folder_ids import DeleteBatchRequestDtoAllOfFolderIds as DeleteBatchRequestDtoAllOfFolderIds
from docspace_api_sdk.models.delete_file_request import DeleteFileRequest as DeleteFileRequest
from docspace_api_sdk.models.delete_folder_request import DeleteFolderRequest as DeleteFolderRequest
from docspace_api_sdk.models.delete_room_request import DeleteRoomRequest as DeleteRoomRequest
from docspace_api_sdk.models.delete_version_batch_request_dto import DeleteVersionBatchRequestDto as DeleteVersionBatchRequestDto
from docspace_api_sdk.models.deposit_dto import DepositDto as DepositDto
from docspace_api_sdk.models.deposit_report_dto import DepositReportDto as DepositReportDto
from docspace_api_sdk.models.deposit_report_wrapper import DepositReportWrapper as DepositReportWrapper
from docspace_api_sdk.models.discount_category_dto import DiscountCategoryDto as DiscountCategoryDto
from docspace_api_sdk.models.display_request_dto import DisplayRequestDto as DisplayRequestDto
from docspace_api_sdk.models.distributed_task_status import DistributedTaskStatus as DistributedTaskStatus
from docspace_api_sdk.models.dns_settings_request_dto import DnsSettingsRequestDto as DnsSettingsRequestDto
from docspace_api_sdk.models.doc_service_url_dto import DocServiceUrlDto as DocServiceUrlDto
from docspace_api_sdk.models.doc_service_url_wrapper import DocServiceUrlWrapper as DocServiceUrlWrapper
from docspace_api_sdk.models.docs_cloud_config_dto import DocsCloudConfigDto as DocsCloudConfigDto
from docspace_api_sdk.models.docs_cloud_config_request_dto import DocsCloudConfigRequestDto as DocsCloudConfigRequestDto
from docspace_api_sdk.models.docs_cloud_config_wrapper import DocsCloudConfigWrapper as DocsCloudConfigWrapper
from docspace_api_sdk.models.docs_cloud_dev_pack_request_dto import DocsCloudDevPackRequestDto as DocsCloudDevPackRequestDto
from docspace_api_sdk.models.docs_cloud_ip_filter_config_dto import DocsCloudIpFilterConfigDto as DocsCloudIpFilterConfigDto
from docspace_api_sdk.models.docs_cloud_ip_filter_config_request import DocsCloudIpFilterConfigRequest as DocsCloudIpFilterConfigRequest
from docspace_api_sdk.models.docs_cloud_ip_filter_rule_dto import DocsCloudIpFilterRuleDto as DocsCloudIpFilterRuleDto
from docspace_api_sdk.models.docs_cloud_ip_filter_rule_request import DocsCloudIpFilterRuleRequest as DocsCloudIpFilterRuleRequest
from docspace_api_sdk.models.docs_cloud_license_info_dto import DocsCloudLicenseInfoDto as DocsCloudLicenseInfoDto
from docspace_api_sdk.models.docs_cloud_payment_dto import DocsCloudPaymentDto as DocsCloudPaymentDto
from docspace_api_sdk.models.docs_cloud_quota_dto import DocsCloudQuotaDto as DocsCloudQuotaDto
from docspace_api_sdk.models.docs_cloud_quota_user_dto import DocsCloudQuotaUserDto as DocsCloudQuotaUserDto
from docspace_api_sdk.models.docs_cloud_quota_wrapper import DocsCloudQuotaWrapper as DocsCloudQuotaWrapper
from docspace_api_sdk.models.docs_cloud_security_config_dto import DocsCloudSecurityConfigDto as DocsCloudSecurityConfigDto
from docspace_api_sdk.models.docs_cloud_security_config_request import DocsCloudSecurityConfigRequest as DocsCloudSecurityConfigRequest
from docspace_api_sdk.models.docs_cloud_server_config_dto import DocsCloudServerConfigDto as DocsCloudServerConfigDto
from docspace_api_sdk.models.docs_cloud_server_config_request import DocsCloudServerConfigRequest as DocsCloudServerConfigRequest
from docspace_api_sdk.models.docs_cloud_server_info_dto import DocsCloudServerInfoDto as DocsCloudServerInfoDto
from docspace_api_sdk.models.docs_cloud_stats_dto import DocsCloudStatsDto as DocsCloudStatsDto
from docspace_api_sdk.models.docs_cloud_tenant_dto import DocsCloudTenantDto as DocsCloudTenantDto
from docspace_api_sdk.models.docs_cloud_tenant_info_dto import DocsCloudTenantInfoDto as DocsCloudTenantInfoDto
from docspace_api_sdk.models.docs_cloud_tenant_info_wrapper import DocsCloudTenantInfoWrapper as DocsCloudTenantInfoWrapper
from docspace_api_sdk.models.docs_cloud_tenant_wrapper import DocsCloudTenantWrapper as DocsCloudTenantWrapper
from docspace_api_sdk.models.docs_cloud_usage_dto import DocsCloudUsageDto as DocsCloudUsageDto
from docspace_api_sdk.models.docs_cloud_usage_wrapper import DocsCloudUsageWrapper as DocsCloudUsageWrapper
from docspace_api_sdk.models.docs_cloud_user_stats_dto import DocsCloudUserStatsDto as DocsCloudUserStatsDto
from docspace_api_sdk.models.docs_cloud_users_limit_dto import DocsCloudUsersLimitDto as DocsCloudUsersLimitDto
from docspace_api_sdk.models.docs_cloud_wopi_config_dto import DocsCloudWopiConfigDto as DocsCloudWopiConfigDto
from docspace_api_sdk.models.docs_cloud_wopi_config_request import DocsCloudWopiConfigRequest as DocsCloudWopiConfigRequest
from docspace_api_sdk.models.document_builder_task_dto import DocumentBuilderTaskDto as DocumentBuilderTaskDto
from docspace_api_sdk.models.document_builder_task_wrapper import DocumentBuilderTaskWrapper as DocumentBuilderTaskWrapper
from docspace_api_sdk.models.document_config_dto import DocumentConfigDto as DocumentConfigDto
from docspace_api_sdk.models.document_options_dto import DocumentOptionsDto as DocumentOptionsDto
from docspace_api_sdk.models.domain_name_rules_dto import DomainNameRulesDto as DomainNameRulesDto
from docspace_api_sdk.models.double_nullable_wrapper import DoubleNullableWrapper as DoubleNullableWrapper
from docspace_api_sdk.models.double_wrapper import DoubleWrapper as DoubleWrapper
from docspace_api_sdk.models.download_request_dto import DownloadRequestDto as DownloadRequestDto
from docspace_api_sdk.models.download_request_dto_all_of_file_ids import DownloadRequestDtoAllOfFileIds as DownloadRequestDtoAllOfFileIds
from docspace_api_sdk.models.download_request_dto_all_of_folder_ids import DownloadRequestDtoAllOfFolderIds as DownloadRequestDtoAllOfFolderIds
from docspace_api_sdk.models.download_request_item_dto import DownloadRequestItemDto as DownloadRequestItemDto
from docspace_api_sdk.models.download_request_item_dto_key import DownloadRequestItemDtoKey as DownloadRequestItemDtoKey
from docspace_api_sdk.models.draft_location import DraftLocation as DraftLocation
from docspace_api_sdk.models.duplicate_request_dto import DuplicateRequestDto as DuplicateRequestDto
from docspace_api_sdk.models.duplicate_request_dto_all_of_file_ids import DuplicateRequestDtoAllOfFileIds as DuplicateRequestDtoAllOfFileIds
from docspace_api_sdk.models.duplicate_request_dto_all_of_folder_ids import DuplicateRequestDtoAllOfFolderIds as DuplicateRequestDtoAllOfFolderIds
from docspace_api_sdk.models.edit_history_array_wrapper import EditHistoryArrayWrapper as EditHistoryArrayWrapper
from docspace_api_sdk.models.edit_history_author_dto import EditHistoryAuthorDto as EditHistoryAuthorDto
from docspace_api_sdk.models.edit_history_changes_dto import EditHistoryChangesDto as EditHistoryChangesDto
from docspace_api_sdk.models.edit_history_data_dto import EditHistoryDataDto as EditHistoryDataDto
from docspace_api_sdk.models.edit_history_data_wrapper import EditHistoryDataWrapper as EditHistoryDataWrapper
from docspace_api_sdk.models.edit_history_dto import EditHistoryDto as EditHistoryDto
from docspace_api_sdk.models.edit_history_url_dto import EditHistoryUrlDto as EditHistoryUrlDto
from docspace_api_sdk.models.editor_configuration_dto import EditorConfigurationDto as EditorConfigurationDto
from docspace_api_sdk.models.editor_tool_call_parameters_dto import EditorToolCallParametersDto as EditorToolCallParametersDto
from docspace_api_sdk.models.editor_tool_call_state_dto import EditorToolCallStateDto as EditorToolCallStateDto
from docspace_api_sdk.models.editor_type import EditorType as EditorType
from docspace_api_sdk.models.email_activation_settings_dto import EmailActivationSettingsDto as EmailActivationSettingsDto
from docspace_api_sdk.models.email_activation_settings_request_dto import EmailActivationSettingsRequestDto as EmailActivationSettingsRequestDto
from docspace_api_sdk.models.email_activation_settings_wrapper import EmailActivationSettingsWrapper as EmailActivationSettingsWrapper
from docspace_api_sdk.models.email_invitation_dto import EmailInvitationDto as EmailInvitationDto
from docspace_api_sdk.models.email_member_request_dto import EmailMemberRequestDto as EmailMemberRequestDto
from docspace_api_sdk.models.embedded_config_dto import EmbeddedConfigDto as EmbeddedConfigDto
from docspace_api_sdk.models.employee_activation_status import EmployeeActivationStatus as EmployeeActivationStatus
from docspace_api_sdk.models.employee_array_wrapper import EmployeeArrayWrapper as EmployeeArrayWrapper
from docspace_api_sdk.models.employee_dto import EmployeeDto as EmployeeDto
from docspace_api_sdk.models.employee_full_array_wrapper import EmployeeFullArrayWrapper as EmployeeFullArrayWrapper
from docspace_api_sdk.models.employee_full_dto import EmployeeFullDto as EmployeeFullDto
from docspace_api_sdk.models.employee_full_wrapper import EmployeeFullWrapper as EmployeeFullWrapper
from docspace_api_sdk.models.employee_status import EmployeeStatus as EmployeeStatus
from docspace_api_sdk.models.employee_type import EmployeeType as EmployeeType
from docspace_api_sdk.models.employee_wrapper import EmployeeWrapper as EmployeeWrapper
from docspace_api_sdk.models.enabled_module_array_wrapper import EnabledModuleArrayWrapper as EnabledModuleArrayWrapper
from docspace_api_sdk.models.enabled_module_dto import EnabledModuleDto as EnabledModuleDto
from docspace_api_sdk.models.encryption_key_array_wrapper import EncryptionKeyArrayWrapper as EncryptionKeyArrayWrapper
from docspace_api_sdk.models.encryption_key_dto import EncryptionKeyDto as EncryptionKeyDto
from docspace_api_sdk.models.encryption_key_request_dto import EncryptionKeyRequestDto as EncryptionKeyRequestDto
from docspace_api_sdk.models.encryption_settings_dto import EncryptionSettingsDto as EncryptionSettingsDto
from docspace_api_sdk.models.encryption_settings_wrapper import EncryptionSettingsWrapper as EncryptionSettingsWrapper
from docspace_api_sdk.models.encryption_status import EncryptionStatus as EncryptionStatus
from docspace_api_sdk.models.entity_quota_dto import EntityQuotaDto as EntityQuotaDto
from docspace_api_sdk.models.entity_quota_settings_dto import EntityQuotaSettingsDto as EntityQuotaSettingsDto
from docspace_api_sdk.models.entity_quota_settings_wrapper import EntityQuotaSettingsWrapper as EntityQuotaSettingsWrapper
from docspace_api_sdk.models.entry_field_dto import EntryFieldDto as EntryFieldDto
from docspace_api_sdk.models.entry_metadata_dto import EntryMetadataDto as EntryMetadataDto
from docspace_api_sdk.models.entry_metadata_wrapper import EntryMetadataWrapper as EntryMetadataWrapper
from docspace_api_sdk.models.entry_template_dto import EntryTemplateDto as EntryTemplateDto
from docspace_api_sdk.models.entry_type import EntryType as EntryType
from docspace_api_sdk.models.error_api_response import ErrorApiResponse as ErrorApiResponse
from docspace_api_sdk.models.error_api_response_error import ErrorApiResponseError as ErrorApiResponseError
from docspace_api_sdk.models.exchange_token200_response import ExchangeToken200Response as ExchangeToken200Response
from docspace_api_sdk.models.external_database_connection_request_dto import ExternalDatabaseConnectionRequestDto as ExternalDatabaseConnectionRequestDto
from docspace_api_sdk.models.external_database_type import ExternalDatabaseType as ExternalDatabaseType
from docspace_api_sdk.models.external_db_sync_form_result_dto import ExternalDbSyncFormResultDto as ExternalDbSyncFormResultDto
from docspace_api_sdk.models.external_db_sync_task_dto import ExternalDbSyncTaskDto as ExternalDbSyncTaskDto
from docspace_api_sdk.models.external_db_sync_task_wrapper import ExternalDbSyncTaskWrapper as ExternalDbSyncTaskWrapper
from docspace_api_sdk.models.external_resource_dto import ExternalResourceDto as ExternalResourceDto
from docspace_api_sdk.models.external_resources_dto import ExternalResourcesDto as ExternalResourcesDto
from docspace_api_sdk.models.external_share_dto import ExternalShareDto as ExternalShareDto
from docspace_api_sdk.models.external_share_request_param import ExternalShareRequestParam as ExternalShareRequestParam
from docspace_api_sdk.models.external_share_status import ExternalShareStatus as ExternalShareStatus
from docspace_api_sdk.models.external_share_wrapper import ExternalShareWrapper as ExternalShareWrapper
from docspace_api_sdk.models.external_sharing_settings_dto import ExternalSharingSettingsDto as ExternalSharingSettingsDto
from docspace_api_sdk.models.external_sharing_settings_request_dto import ExternalSharingSettingsRequestDto as ExternalSharingSettingsRequestDto
from docspace_api_sdk.models.external_sharing_settings_wrapper import ExternalSharingSettingsWrapper as ExternalSharingSettingsWrapper
from docspace_api_sdk.models.feature_used_dto import FeatureUsedDto as FeatureUsedDto
from docspace_api_sdk.models.feedback_config_dto import FeedbackConfigDto as FeedbackConfigDto
from docspace_api_sdk.models.field_error import FieldError as FieldError
from docspace_api_sdk.models.file_array_wrapper import FileArrayWrapper as FileArrayWrapper
from docspace_api_sdk.models.file_conflict_resolve_type import FileConflictResolveType as FileConflictResolveType
from docspace_api_sdk.models.file_dto import FileDto as FileDto
from docspace_api_sdk.models.file_dto_all_of_view_accessibility import FileDtoAllOfViewAccessibility as FileDtoAllOfViewAccessibility
from docspace_api_sdk.models.file_encryption_info_dto import FileEncryptionInfoDto as FileEncryptionInfoDto
from docspace_api_sdk.models.file_encryption_info_wrapper import FileEncryptionInfoWrapper as FileEncryptionInfoWrapper
from docspace_api_sdk.models.file_entry_array_wrapper import FileEntryArrayWrapper as FileEntryArrayWrapper
from docspace_api_sdk.models.file_entry_base_array_wrapper import FileEntryBaseArrayWrapper as FileEntryBaseArrayWrapper
from docspace_api_sdk.models.file_entry_base_dto import FileEntryBaseDto as FileEntryBaseDto
from docspace_api_sdk.models.file_entry_base_wrapper import FileEntryBaseWrapper as FileEntryBaseWrapper
from docspace_api_sdk.models.file_entry_dto import FileEntryDto as FileEntryDto
from docspace_api_sdk.models.file_entry_type import FileEntryType as FileEntryType
from docspace_api_sdk.models.file_keys_dto import FileKeysDto as FileKeysDto
from docspace_api_sdk.models.file_link_dto import FileLinkDto as FileLinkDto
from docspace_api_sdk.models.file_link_request import FileLinkRequest as FileLinkRequest
from docspace_api_sdk.models.file_link_wrapper import FileLinkWrapper as FileLinkWrapper
from docspace_api_sdk.models.file_operation_array_wrapper import FileOperationArrayWrapper as FileOperationArrayWrapper
from docspace_api_sdk.models.file_operation_dto import FileOperationDto as FileOperationDto
from docspace_api_sdk.models.file_operation_request_base_dto import FileOperationRequestBaseDto as FileOperationRequestBaseDto
from docspace_api_sdk.models.file_operation_type import FileOperationType as FileOperationType
from docspace_api_sdk.models.file_operation_wrapper import FileOperationWrapper as FileOperationWrapper
from docspace_api_sdk.models.file_reference_data_dto import FileReferenceDataDto as FileReferenceDataDto
from docspace_api_sdk.models.file_reference_dto import FileReferenceDto as FileReferenceDto
from docspace_api_sdk.models.file_reference_wrapper import FileReferenceWrapper as FileReferenceWrapper
from docspace_api_sdk.models.file_share import FileShare as FileShare
from docspace_api_sdk.models.file_share_array_wrapper import FileShareArrayWrapper as FileShareArrayWrapper
from docspace_api_sdk.models.file_share_dto import FileShareDto as FileShareDto
from docspace_api_sdk.models.file_share_link import FileShareLink as FileShareLink
from docspace_api_sdk.models.file_share_params import FileShareParams as FileShareParams
from docspace_api_sdk.models.file_share_response_array_wrapper import FileShareResponseArrayWrapper as FileShareResponseArrayWrapper
from docspace_api_sdk.models.file_share_wrapper import FileShareWrapper as FileShareWrapper
from docspace_api_sdk.models.file_status import FileStatus as FileStatus
from docspace_api_sdk.models.file_type import FileType as FileType
from docspace_api_sdk.models.file_upload_result_dto import FileUploadResultDto as FileUploadResultDto
from docspace_api_sdk.models.file_upload_result_wrapper import FileUploadResultWrapper as FileUploadResultWrapper
from docspace_api_sdk.models.file_wrapper import FileWrapper as FileWrapper
from docspace_api_sdk.models.files_settings_dto import FilesSettingsDto as FilesSettingsDto
from docspace_api_sdk.models.files_settings_dto_internal_formats import FilesSettingsDtoInternalFormats as FilesSettingsDtoInternalFormats
from docspace_api_sdk.models.files_settings_wrapper import FilesSettingsWrapper as FilesSettingsWrapper
from docspace_api_sdk.models.files_statistics_folder import FilesStatisticsFolder as FilesStatisticsFolder
from docspace_api_sdk.models.files_statistics_result_dto import FilesStatisticsResultDto as FilesStatisticsResultDto
from docspace_api_sdk.models.files_statistics_result_wrapper import FilesStatisticsResultWrapper as FilesStatisticsResultWrapper
from docspace_api_sdk.models.filling_form_result_dto import FillingFormResultDto as FillingFormResultDto
from docspace_api_sdk.models.filling_form_result_wrapper import FillingFormResultWrapper as FillingFormResultWrapper
from docspace_api_sdk.models.filter_type import FilterType as FilterType
from docspace_api_sdk.models.finish_dto import FinishDto as FinishDto
from docspace_api_sdk.models.firebase_device_dto import FirebaseDeviceDto as FirebaseDeviceDto
from docspace_api_sdk.models.firebase_device_wrapper import FirebaseDeviceWrapper as FirebaseDeviceWrapper
from docspace_api_sdk.models.firebase_dto import FirebaseDto as FirebaseDto
from docspace_api_sdk.models.firebase_request_dto import FirebaseRequestDto as FirebaseRequestDto
from docspace_api_sdk.models.folder_array_wrapper import FolderArrayWrapper as FolderArrayWrapper
from docspace_api_sdk.models.folder_content_array_wrapper import FolderContentArrayWrapper as FolderContentArrayWrapper
from docspace_api_sdk.models.folder_content_dto import FolderContentDto as FolderContentDto
from docspace_api_sdk.models.folder_content_wrapper import FolderContentWrapper as FolderContentWrapper
from docspace_api_sdk.models.folder_dto import FolderDto as FolderDto
from docspace_api_sdk.models.folder_link_request import FolderLinkRequest as FolderLinkRequest
from docspace_api_sdk.models.folder_metadata_search import FolderMetadataSearch as FolderMetadataSearch
from docspace_api_sdk.models.folder_type import FolderType as FolderType
from docspace_api_sdk.models.folder_wrapper import FolderWrapper as FolderWrapper
from docspace_api_sdk.models.form_filling_manage_action import FormFillingManageAction as FormFillingManageAction
from docspace_api_sdk.models.form_filling_status import FormFillingStatus as FormFillingStatus
from docspace_api_sdk.models.form_gallery_dto import FormGalleryDto as FormGalleryDto
from docspace_api_sdk.models.form_metadata_dto import FormMetadataDto as FormMetadataDto
from docspace_api_sdk.models.form_results_dto import FormResultsDto as FormResultsDto
from docspace_api_sdk.models.form_role_array_wrapper import FormRoleArrayWrapper as FormRoleArrayWrapper
from docspace_api_sdk.models.form_role_dto import FormRoleDto as FormRoleDto
from docspace_api_sdk.models.form_role_request import FormRoleRequest as FormRoleRequest
from docspace_api_sdk.models.form_submissions_dto import FormSubmissionsDto as FormSubmissionsDto
from docspace_api_sdk.models.form_submissions_wrapper import FormSubmissionsWrapper as FormSubmissionsWrapper
from docspace_api_sdk.models.forms_item_array_wrapper import FormsItemArrayWrapper as FormsItemArrayWrapper
from docspace_api_sdk.models.forms_item_data_dto import FormsItemDataDto as FormsItemDataDto
from docspace_api_sdk.models.forms_item_dto import FormsItemDto as FormsItemDto
from docspace_api_sdk.models.generate_docx_tool_call_parameters_dto import GenerateDocxToolCallParametersDto as GenerateDocxToolCallParametersDto
from docspace_api_sdk.models.generate_form_tool_call_parameters_dto import GenerateFormToolCallParametersDto as GenerateFormToolCallParametersDto
from docspace_api_sdk.models.generate_presentation_tool_call_parameters_dto import GeneratePresentationToolCallParametersDto as GeneratePresentationToolCallParametersDto
from docspace_api_sdk.models.get_portal_prices200_response import GetPortalPrices200Response as GetPortalPrices200Response
from docspace_api_sdk.models.get_portal_prices200_response_links_inner import GetPortalPrices200ResponseLinksInner as GetPortalPrices200ResponseLinksInner
from docspace_api_sdk.models.get_reference_data_dto import GetReferenceDataDto as GetReferenceDataDto
from docspace_api_sdk.models.goback_config_dto import GobackConfigDto as GobackConfigDto
from docspace_api_sdk.models.greeting_settings_request_dto import GreetingSettingsRequestDto as GreetingSettingsRequestDto
from docspace_api_sdk.models.group_array_wrapper import GroupArrayWrapper as GroupArrayWrapper
from docspace_api_sdk.models.group_dto import GroupDto as GroupDto
from docspace_api_sdk.models.group_member_security_array_wrapper import GroupMemberSecurityArrayWrapper as GroupMemberSecurityArrayWrapper
from docspace_api_sdk.models.group_member_security_dto import GroupMemberSecurityDto as GroupMemberSecurityDto
from docspace_api_sdk.models.group_request_dto import GroupRequestDto as GroupRequestDto
from docspace_api_sdk.models.group_summary_array_wrapper import GroupSummaryArrayWrapper as GroupSummaryArrayWrapper
from docspace_api_sdk.models.group_summary_dto import GroupSummaryDto as GroupSummaryDto
from docspace_api_sdk.models.group_wrapper import GroupWrapper as GroupWrapper
from docspace_api_sdk.models.hide_confirm_convert_request_dto import HideConfirmConvertRequestDto as HideConfirmConvertRequestDto
from docspace_api_sdk.models.history_action_dto import HistoryActionDto as HistoryActionDto
from docspace_api_sdk.models.history_array_wrapper import HistoryArrayWrapper as HistoryArrayWrapper
from docspace_api_sdk.models.history_data_dto import HistoryDataDto as HistoryDataDto
from docspace_api_sdk.models.history_dto import HistoryDto as HistoryDto
from docspace_api_sdk.models.i_compress_wrapper import ICompressWrapper as ICompressWrapper
from docspace_api_sdk.models.icon_request import IconRequest as IconRequest
from docspace_api_sdk.models.image_size_dto import ImageSizeDto as ImageSizeDto
from docspace_api_sdk.models.importable_api_entity import ImportableApiEntity as ImportableApiEntity
from docspace_api_sdk.models.info_config_dto import InfoConfigDto as InfoConfigDto
from docspace_api_sdk.models.int32_wrapper import Int32Wrapper as Int32Wrapper
from docspace_api_sdk.models.int64_wrapper import Int64Wrapper as Int64Wrapper
from docspace_api_sdk.models.invitation_link_create_request_dto import InvitationLinkCreateRequestDto as InvitationLinkCreateRequestDto
from docspace_api_sdk.models.invitation_link_delete_request_dto import InvitationLinkDeleteRequestDto as InvitationLinkDeleteRequestDto
from docspace_api_sdk.models.invitation_link_dto import InvitationLinkDto as InvitationLinkDto
from docspace_api_sdk.models.invitation_link_update_request_dto import InvitationLinkUpdateRequestDto as InvitationLinkUpdateRequestDto
from docspace_api_sdk.models.invitation_link_wrapper import InvitationLinkWrapper as InvitationLinkWrapper
from docspace_api_sdk.models.invite_users_request_dto import InviteUsersRequestDto as InviteUsersRequestDto
from docspace_api_sdk.models.ip_restriction_array_wrapper import IpRestrictionArrayWrapper as IpRestrictionArrayWrapper
from docspace_api_sdk.models.ip_restriction_dto import IpRestrictionDto as IpRestrictionDto
from docspace_api_sdk.models.ip_restriction_entry_dto import IpRestrictionEntryDto as IpRestrictionEntryDto
from docspace_api_sdk.models.ip_restrictions_dto import IpRestrictionsDto as IpRestrictionsDto
from docspace_api_sdk.models.ip_restrictions_settings_dto import IpRestrictionsSettingsDto as IpRestrictionsSettingsDto
from docspace_api_sdk.models.ip_restrictions_settings_wrapper import IpRestrictionsSettingsWrapper as IpRestrictionsSettingsWrapper
from docspace_api_sdk.models.ip_restrictions_wrapper import IpRestrictionsWrapper as IpRestrictionsWrapper
from docspace_api_sdk.models.is_default_white_label_logos_array_wrapper import IsDefaultWhiteLabelLogosArrayWrapper as IsDefaultWhiteLabelLogosArrayWrapper
from docspace_api_sdk.models.is_default_white_label_logos_dto import IsDefaultWhiteLabelLogosDto as IsDefaultWhiteLabelLogosDto
from docspace_api_sdk.models.is_default_white_label_logos_wrapper import IsDefaultWhiteLabelLogosWrapper as IsDefaultWhiteLabelLogosWrapper
from docspace_api_sdk.models.item_key_value_pair_boolean_string import ItemKeyValuePairBooleanString as ItemKeyValuePairBooleanString
from docspace_api_sdk.models.item_key_value_pair_boolean_string_wrapper import ItemKeyValuePairBooleanStringWrapper as ItemKeyValuePairBooleanStringWrapper
from docspace_api_sdk.models.item_key_value_pair_object_object import ItemKeyValuePairObjectObject as ItemKeyValuePairObjectObject
from docspace_api_sdk.models.item_key_value_pair_string_boolean import ItemKeyValuePairStringBoolean as ItemKeyValuePairStringBoolean
from docspace_api_sdk.models.item_key_value_pair_string_logo_request_dto import ItemKeyValuePairStringLogoRequestDto as ItemKeyValuePairStringLogoRequestDto
from docspace_api_sdk.models.item_key_value_pair_string_string import ItemKeyValuePairStringString as ItemKeyValuePairStringString
from docspace_api_sdk.models.json_value_wrapper import JsonValueWrapper as JsonValueWrapper
from docspace_api_sdk.models.licensor_details_array_wrapper import LicensorDetailsArrayWrapper as LicensorDetailsArrayWrapper
from docspace_api_sdk.models.licensor_details_dto import LicensorDetailsDto as LicensorDetailsDto
from docspace_api_sdk.models.licensor_details_wrapper import LicensorDetailsWrapper as LicensorDetailsWrapper
from docspace_api_sdk.models.link_account_request_dto import LinkAccountRequestDto as LinkAccountRequestDto
from docspace_api_sdk.models.link_type import LinkType as LinkType
from docspace_api_sdk.models.location_type import LocationType as LocationType
from docspace_api_sdk.models.lock_file_request import LockFileRequest as LockFileRequest
from docspace_api_sdk.models.login_event_array_wrapper import LoginEventArrayWrapper as LoginEventArrayWrapper
from docspace_api_sdk.models.login_event_dto import LoginEventDto as LoginEventDto
from docspace_api_sdk.models.login_provider import LoginProvider as LoginProvider
from docspace_api_sdk.models.login_settings_dto import LoginSettingsDto as LoginSettingsDto
from docspace_api_sdk.models.login_settings_request_dto import LoginSettingsRequestDto as LoginSettingsRequestDto
from docspace_api_sdk.models.login_settings_wrapper import LoginSettingsWrapper as LoginSettingsWrapper
from docspace_api_sdk.models.logo_config_dto import LogoConfigDto as LogoConfigDto
from docspace_api_sdk.models.logo_cover_dto import LogoCoverDto as LogoCoverDto
from docspace_api_sdk.models.logo_dto import LogoDto as LogoDto
from docspace_api_sdk.models.logo_request import LogoRequest as LogoRequest
from docspace_api_sdk.models.logo_request_dto import LogoRequestDto as LogoRequestDto
from docspace_api_sdk.models.mail_domain_settings_request_dto import MailDomainSettingsRequestDto as MailDomainSettingsRequestDto
from docspace_api_sdk.models.manage_form_filling_dto import ManageFormFillingDto as ManageFormFillingDto
from docspace_api_sdk.models.member_request_dto import MemberRequestDto as MemberRequestDto
from docspace_api_sdk.models.members_request import MembersRequest as MembersRequest
from docspace_api_sdk.models.mention_array_wrapper import MentionArrayWrapper as MentionArrayWrapper
from docspace_api_sdk.models.mention_dto import MentionDto as MentionDto
from docspace_api_sdk.models.mention_message_request import MentionMessageRequest as MentionMessageRequest
from docspace_api_sdk.models.message_action import MessageAction as MessageAction
from docspace_api_sdk.models.metadata_conflict_resolve_type import MetadataConflictResolveType as MetadataConflictResolveType
from docspace_api_sdk.models.metadata_field_dto import MetadataFieldDto as MetadataFieldDto
from docspace_api_sdk.models.metadata_field_option_dto import MetadataFieldOptionDto as MetadataFieldOptionDto
from docspace_api_sdk.models.metadata_field_option_request import MetadataFieldOptionRequest as MetadataFieldOptionRequest
from docspace_api_sdk.models.metadata_field_request import MetadataFieldRequest as MetadataFieldRequest
from docspace_api_sdk.models.metadata_field_type import MetadataFieldType as MetadataFieldType
from docspace_api_sdk.models.metadata_field_wrapper import MetadataFieldWrapper as MetadataFieldWrapper
from docspace_api_sdk.models.metadata_filter_condition_request import MetadataFilterConditionRequest as MetadataFilterConditionRequest
from docspace_api_sdk.models.metadata_match_dto import MetadataMatchDto as MetadataMatchDto
from docspace_api_sdk.models.metadata_operation_dto import MetadataOperationDto as MetadataOperationDto
from docspace_api_sdk.models.metadata_operation_wrapper import MetadataOperationWrapper as MetadataOperationWrapper
from docspace_api_sdk.models.metadata_template_array_wrapper import MetadataTemplateArrayWrapper as MetadataTemplateArrayWrapper
from docspace_api_sdk.models.metadata_template_dto import MetadataTemplateDto as MetadataTemplateDto
from docspace_api_sdk.models.metadata_template_wrapper import MetadataTemplateWrapper as MetadataTemplateWrapper
from docspace_api_sdk.models.metadata_value_dto import MetadataValueDto as MetadataValueDto
from docspace_api_sdk.models.metadata_value_request import MetadataValueRequest as MetadataValueRequest
from docspace_api_sdk.models.migrating_api_files import MigratingApiFiles as MigratingApiFiles
from docspace_api_sdk.models.migrating_api_group import MigratingApiGroup as MigratingApiGroup
from docspace_api_sdk.models.migrating_api_user import MigratingApiUser as MigratingApiUser
from docspace_api_sdk.models.migration_api_info import MigrationApiInfo as MigrationApiInfo
from docspace_api_sdk.models.migration_status_dto import MigrationStatusDto as MigrationStatusDto
from docspace_api_sdk.models.migration_status_wrapper import MigrationStatusWrapper as MigrationStatusWrapper
from docspace_api_sdk.models.mobile_phone_activation_status import MobilePhoneActivationStatus as MobilePhoneActivationStatus
from docspace_api_sdk.models.mobile_request_dto import MobileRequestDto as MobileRequestDto
from docspace_api_sdk.models.module import Module as Module
from docspace_api_sdk.models.module_wrapper import ModuleWrapper as ModuleWrapper
from docspace_api_sdk.models.multi_size_logo_cover_dto import MultiSizeLogoCoverDto as MultiSizeLogoCoverDto
from docspace_api_sdk.models.new_items_dto_file_entry_base_dto import NewItemsDtoFileEntryBaseDto as NewItemsDtoFileEntryBaseDto
from docspace_api_sdk.models.new_items_dto_room_new_items_dto import NewItemsDtoRoomNewItemsDto as NewItemsDtoRoomNewItemsDto
from docspace_api_sdk.models.new_items_file_entry_base_array_wrapper import NewItemsFileEntryBaseArrayWrapper as NewItemsFileEntryBaseArrayWrapper
from docspace_api_sdk.models.new_items_room_new_items_array_wrapper import NewItemsRoomNewItemsArrayWrapper as NewItemsRoomNewItemsArrayWrapper
from docspace_api_sdk.models.notification_channel_dto import NotificationChannelDto as NotificationChannelDto
from docspace_api_sdk.models.notification_channel_status_dto import NotificationChannelStatusDto as NotificationChannelStatusDto
from docspace_api_sdk.models.notification_channel_status_wrapper import NotificationChannelStatusWrapper as NotificationChannelStatusWrapper
from docspace_api_sdk.models.notification_settings_dto import NotificationSettingsDto as NotificationSettingsDto
from docspace_api_sdk.models.notification_settings_request_dto import NotificationSettingsRequestDto as NotificationSettingsRequestDto
from docspace_api_sdk.models.notification_settings_wrapper import NotificationSettingsWrapper as NotificationSettingsWrapper
from docspace_api_sdk.models.notification_type import NotificationType as NotificationType
from docspace_api_sdk.models.object_array_wrapper import ObjectArrayWrapper as ObjectArrayWrapper
from docspace_api_sdk.models.operation_dto import OperationDto as OperationDto
from docspace_api_sdk.models.operation_order_type import OperationOrderType as OperationOrderType
from docspace_api_sdk.models.operation_status import OperationStatus as OperationStatus
from docspace_api_sdk.models.operation_token_usage_dto import OperationTokenUsageDto as OperationTokenUsageDto
from docspace_api_sdk.models.operation_type import OperationType as OperationType
from docspace_api_sdk.models.order_by_dto import OrderByDto as OrderByDto
from docspace_api_sdk.models.order_request_dto import OrderRequestDto as OrderRequestDto
from docspace_api_sdk.models.orders_item_request_dto import OrdersItemRequestDto as OrdersItemRequestDto
from docspace_api_sdk.models.orders_request_dto import OrdersRequestDto as OrdersRequestDto
from docspace_api_sdk.models.owner_change_instructions_dto import OwnerChangeInstructionsDto as OwnerChangeInstructionsDto
from docspace_api_sdk.models.owner_change_instructions_wrapper import OwnerChangeInstructionsWrapper as OwnerChangeInstructionsWrapper
from docspace_api_sdk.models.owner_id_settings_request_dto import OwnerIdSettingsRequestDto as OwnerIdSettingsRequestDto
from docspace_api_sdk.models.pageable_client_info_response import PageableClientInfoResponse as PageableClientInfoResponse
from docspace_api_sdk.models.pageable_client_response import PageableClientResponse as PageableClientResponse
from docspace_api_sdk.models.pageable_modification_response import PageableModificationResponse as PageableModificationResponse
from docspace_api_sdk.models.pageable_response import PageableResponse as PageableResponse
from docspace_api_sdk.models.password_hash_settings_dto import PasswordHashSettingsDto as PasswordHashSettingsDto
from docspace_api_sdk.models.password_settings_dto import PasswordSettingsDto as PasswordSettingsDto
from docspace_api_sdk.models.password_settings_request_dto import PasswordSettingsRequestDto as PasswordSettingsRequestDto
from docspace_api_sdk.models.password_settings_wrapper import PasswordSettingsWrapper as PasswordSettingsWrapper
from docspace_api_sdk.models.payment_calculation_dto import PaymentCalculationDto as PaymentCalculationDto
from docspace_api_sdk.models.payment_calculation_wrapper import PaymentCalculationWrapper as PaymentCalculationWrapper
from docspace_api_sdk.models.payment_method_status import PaymentMethodStatus as PaymentMethodStatus
from docspace_api_sdk.models.payment_settings_dto import PaymentSettingsDto as PaymentSettingsDto
from docspace_api_sdk.models.payment_settings_wrapper import PaymentSettingsWrapper as PaymentSettingsWrapper
from docspace_api_sdk.models.payment_url_request_dto import PaymentUrlRequestDto as PaymentUrlRequestDto
from docspace_api_sdk.models.payments import Payments as Payments
from docspace_api_sdk.models.permissions_config_dto import PermissionsConfigDto as PermissionsConfigDto
from docspace_api_sdk.models.plugins_config_dto import PluginsConfigDto as PluginsConfigDto
from docspace_api_sdk.models.plugins_dto import PluginsDto as PluginsDto
from docspace_api_sdk.models.portal_user_dto import PortalUserDto as PortalUserDto
from docspace_api_sdk.models.portal_user_wrapper import PortalUserWrapper as PortalUserWrapper
from docspace_api_sdk.models.price_dto import PriceDto as PriceDto
from docspace_api_sdk.models.price_status import PriceStatus as PriceStatus
from docspace_api_sdk.models.price_time_unit import PriceTimeUnit as PriceTimeUnit
from docspace_api_sdk.models.problem_detail import ProblemDetail as ProblemDetail
from docspace_api_sdk.models.product_administrator_dto import ProductAdministratorDto as ProductAdministratorDto
from docspace_api_sdk.models.product_administrator_wrapper import ProductAdministratorWrapper as ProductAdministratorWrapper
from docspace_api_sdk.models.product_quantity_type import ProductQuantityType as ProductQuantityType
from docspace_api_sdk.models.product_type import ProductType as ProductType
from docspace_api_sdk.models.provider_array_wrapper import ProviderArrayWrapper as ProviderArrayWrapper
from docspace_api_sdk.models.provider_dto import ProviderDto as ProviderDto
from docspace_api_sdk.models.provider_filter import ProviderFilter as ProviderFilter
from docspace_api_sdk.models.quantity_request_dto import QuantityRequestDto as QuantityRequestDto
from docspace_api_sdk.models.quota_array_wrapper import QuotaArrayWrapper as QuotaArrayWrapper
from docspace_api_sdk.models.quota_dto import QuotaDto as QuotaDto
from docspace_api_sdk.models.quota_filter import QuotaFilter as QuotaFilter
from docspace_api_sdk.models.quota_scope import QuotaScope as QuotaScope
from docspace_api_sdk.models.quota_settings_request_dto import QuotaSettingsRequestDto as QuotaSettingsRequestDto
from docspace_api_sdk.models.quota_settings_request_dto_default_quota import QuotaSettingsRequestDtoDefaultQuota as QuotaSettingsRequestDtoDefaultQuota
from docspace_api_sdk.models.quota_state import QuotaState as QuotaState
from docspace_api_sdk.models.quota_wrapper import QuotaWrapper as QuotaWrapper
from docspace_api_sdk.models.recaptcha_type import RecaptchaType as RecaptchaType
from docspace_api_sdk.models.recent_config_dto import RecentConfigDto as RecentConfigDto
from docspace_api_sdk.models.reg_status import RegStatus as RegStatus
from docspace_api_sdk.models.report_dto import ReportDto as ReportDto
from docspace_api_sdk.models.report_wrapper import ReportWrapper as ReportWrapper
from docspace_api_sdk.models.request_location import RequestLocation as RequestLocation
from docspace_api_sdk.models.restricted_ai_models_dto import RestrictedAiModelsDto as RestrictedAiModelsDto
from docspace_api_sdk.models.restricted_ai_models_wrapper import RestrictedAiModelsWrapper as RestrictedAiModelsWrapper
from docspace_api_sdk.models.review_config_dto import ReviewConfigDto as ReviewConfigDto
from docspace_api_sdk.models.room_data_lifetime_dto import RoomDataLifetimeDto as RoomDataLifetimeDto
from docspace_api_sdk.models.room_data_lifetime_period import RoomDataLifetimePeriod as RoomDataLifetimePeriod
from docspace_api_sdk.models.room_from_template_status_dto import RoomFromTemplateStatusDto as RoomFromTemplateStatusDto
from docspace_api_sdk.models.room_from_template_status_wrapper import RoomFromTemplateStatusWrapper as RoomFromTemplateStatusWrapper
from docspace_api_sdk.models.room_group_array_wrapper import RoomGroupArrayWrapper as RoomGroupArrayWrapper
from docspace_api_sdk.models.room_group_dto import RoomGroupDto as RoomGroupDto
from docspace_api_sdk.models.room_group_request_dto import RoomGroupRequestDto as RoomGroupRequestDto
from docspace_api_sdk.models.room_group_wrapper import RoomGroupWrapper as RoomGroupWrapper
from docspace_api_sdk.models.room_invitation import RoomInvitation as RoomInvitation
from docspace_api_sdk.models.room_invitation_request import RoomInvitationRequest as RoomInvitationRequest
from docspace_api_sdk.models.room_link_request import RoomLinkRequest as RoomLinkRequest
from docspace_api_sdk.models.room_new_items_dto import RoomNewItemsDto as RoomNewItemsDto
from docspace_api_sdk.models.room_privacy_filter import RoomPrivacyFilter as RoomPrivacyFilter
from docspace_api_sdk.models.room_security_dto import RoomSecurityDto as RoomSecurityDto
from docspace_api_sdk.models.room_security_error import RoomSecurityError as RoomSecurityError
from docspace_api_sdk.models.room_security_wrapper import RoomSecurityWrapper as RoomSecurityWrapper
from docspace_api_sdk.models.room_template_dto import RoomTemplateDto as RoomTemplateDto
from docspace_api_sdk.models.room_template_status_dto import RoomTemplateStatusDto as RoomTemplateStatusDto
from docspace_api_sdk.models.room_template_status_wrapper import RoomTemplateStatusWrapper as RoomTemplateStatusWrapper
from docspace_api_sdk.models.room_type import RoomType as RoomType
from docspace_api_sdk.models.rooms_metadata_search_request_dto import RoomsMetadataSearchRequestDto as RoomsMetadataSearchRequestDto
from docspace_api_sdk.models.rooms_notification_settings_dto import RoomsNotificationSettingsDto as RoomsNotificationSettingsDto
from docspace_api_sdk.models.rooms_notification_settings_wrapper import RoomsNotificationSettingsWrapper as RoomsNotificationSettingsWrapper
from docspace_api_sdk.models.rooms_notifications_settings_request_dto import RoomsNotificationsSettingsRequestDto as RoomsNotificationsSettingsRequestDto
from docspace_api_sdk.models.run_builder_script_output_request import RunBuilderScriptOutputRequest as RunBuilderScriptOutputRequest
from docspace_api_sdk.models.run_builder_script_request_dto import RunBuilderScriptRequestDto as RunBuilderScriptRequestDto
from docspace_api_sdk.models.run_builder_script_request_dto_argument import RunBuilderScriptRequestDtoArgument as RunBuilderScriptRequestDtoArgument
from docspace_api_sdk.models.sales_request_dto import SalesRequestDto as SalesRequestDto
from docspace_api_sdk.models.save_additional_resources_request import SaveAdditionalResourcesRequest as SaveAdditionalResourcesRequest
from docspace_api_sdk.models.save_as_pdf_request import SaveAsPdfRequest as SaveAsPdfRequest
from docspace_api_sdk.models.save_auth_keys_request_dto import SaveAuthKeysRequestDto as SaveAuthKeysRequestDto
from docspace_api_sdk.models.save_company_info_request import SaveCompanyInfoRequest as SaveCompanyInfoRequest
from docspace_api_sdk.models.save_form_role_mapping_dto import SaveFormRoleMappingDto as SaveFormRoleMappingDto
from docspace_api_sdk.models.schedule_dto import ScheduleDto as ScheduleDto
from docspace_api_sdk.models.schedule_wrapper import ScheduleWrapper as ScheduleWrapper
from docspace_api_sdk.models.scope_response import ScopeResponse as ScopeResponse
from docspace_api_sdk.models.search_area import SearchArea as SearchArea
from docspace_api_sdk.models.security_array_wrapper import SecurityArrayWrapper as SecurityArrayWrapper
from docspace_api_sdk.models.security_dto import SecurityDto as SecurityDto
from docspace_api_sdk.models.security_info_request_dto import SecurityInfoRequestDto as SecurityInfoRequestDto
from docspace_api_sdk.models.security_info_simple_request_dto import SecurityInfoSimpleRequestDto as SecurityInfoSimpleRequestDto
from docspace_api_sdk.models.security_request_dto import SecurityRequestDto as SecurityRequestDto
from docspace_api_sdk.models.send_module_event_request import SendModuleEventRequest as SendModuleEventRequest
from docspace_api_sdk.models.service_limit_dto import ServiceLimitDto as ServiceLimitDto
from docspace_api_sdk.models.service_limit_order_by import ServiceLimitOrderBy as ServiceLimitOrderBy
from docspace_api_sdk.models.service_limit_period import ServiceLimitPeriod as ServiceLimitPeriod
from docspace_api_sdk.models.service_limit_report_dto import ServiceLimitReportDto as ServiceLimitReportDto
from docspace_api_sdk.models.service_limit_report_wrapper import ServiceLimitReportWrapper as ServiceLimitReportWrapper
from docspace_api_sdk.models.service_limit_scope import ServiceLimitScope as ServiceLimitScope
from docspace_api_sdk.models.service_limit_usage_dto import ServiceLimitUsageDto as ServiceLimitUsageDto
from docspace_api_sdk.models.service_limit_wrapper import ServiceLimitWrapper as ServiceLimitWrapper
from docspace_api_sdk.models.service_price_array_wrapper import ServicePriceArrayWrapper as ServicePriceArrayWrapper
from docspace_api_sdk.models.service_price_dto import ServicePriceDto as ServicePriceDto
from docspace_api_sdk.models.session_request import SessionRequest as SessionRequest
from docspace_api_sdk.models.set_app_enabled_request import SetAppEnabledRequest as SetAppEnabledRequest
from docspace_api_sdk.models.set_app_settings_request import SetAppSettingsRequest as SetAppSettingsRequest
from docspace_api_sdk.models.set_audit_lifetime_settings_request import SetAuditLifetimeSettingsRequest as SetAuditLifetimeSettingsRequest
from docspace_api_sdk.models.set_custom_fields import SetCustomFields as SetCustomFields
from docspace_api_sdk.models.set_manager_request import SetManagerRequest as SetManagerRequest
from docspace_api_sdk.models.set_metadata_values import SetMetadataValues as SetMetadataValues
from docspace_api_sdk.models.set_participant_service_limits_request_dto import SetParticipantServiceLimitsRequestDto as SetParticipantServiceLimitsRequestDto
from docspace_api_sdk.models.set_public_dto import SetPublicDto as SetPublicDto
from docspace_api_sdk.models.set_restricted_ai_models_request_dto import SetRestrictedAiModelsRequestDto as SetRestrictedAiModelsRequestDto
from docspace_api_sdk.models.set_wallet_top_up_settings_request import SetWalletTopUpSettingsRequest as SetWalletTopUpSettingsRequest
from docspace_api_sdk.models.settings_dto import SettingsDto as SettingsDto
from docspace_api_sdk.models.settings_request_dto import SettingsRequestDto as SettingsRequestDto
from docspace_api_sdk.models.settings_wrapper import SettingsWrapper as SettingsWrapper
from docspace_api_sdk.models.share_filter_type import ShareFilterType as ShareFilterType
from docspace_api_sdk.models.signup_account_request_dto import SignupAccountRequestDto as SignupAccountRequestDto
from docspace_api_sdk.models.smtp_operation_status_dto import SmtpOperationStatusDto as SmtpOperationStatusDto
from docspace_api_sdk.models.smtp_operation_status_wrapper import SmtpOperationStatusWrapper as SmtpOperationStatusWrapper
from docspace_api_sdk.models.smtp_settings_dto import SmtpSettingsDto as SmtpSettingsDto
from docspace_api_sdk.models.smtp_settings_wrapper import SmtpSettingsWrapper as SmtpSettingsWrapper
from docspace_api_sdk.models.socket_settings_dto import SocketSettingsDto as SocketSettingsDto
from docspace_api_sdk.models.socket_settings_wrapper import SocketSettingsWrapper as SocketSettingsWrapper
from docspace_api_sdk.models.sort_order import SortOrder as SortOrder
from docspace_api_sdk.models.sorted_by_type import SortedByType as SortedByType
from docspace_api_sdk.models.sso_binding_type_dto import SsoBindingTypeDto as SsoBindingTypeDto
from docspace_api_sdk.models.sso_certificate_dto import SsoCertificateDto as SsoCertificateDto
from docspace_api_sdk.models.sso_encrypt_algorithm_type_dto import SsoEncryptAlgorithmTypeDto as SsoEncryptAlgorithmTypeDto
from docspace_api_sdk.models.sso_field_mapping_dto import SsoFieldMappingDto as SsoFieldMappingDto
from docspace_api_sdk.models.sso_idp_certificate_action_type_dto import SsoIdpCertificateActionTypeDto as SsoIdpCertificateActionTypeDto
from docspace_api_sdk.models.sso_idp_certificate_advanced_dto import SsoIdpCertificateAdvancedDto as SsoIdpCertificateAdvancedDto
from docspace_api_sdk.models.sso_idp_settings_dto import SsoIdpSettingsDto as SsoIdpSettingsDto
from docspace_api_sdk.models.sso_name_id_format_type_dto import SsoNameIdFormatTypeDto as SsoNameIdFormatTypeDto
from docspace_api_sdk.models.sso_settings_constants_dto import SsoSettingsConstantsDto as SsoSettingsConstantsDto
from docspace_api_sdk.models.sso_settings_constants_wrapper import SsoSettingsConstantsWrapper as SsoSettingsConstantsWrapper
from docspace_api_sdk.models.sso_settings_dto import SsoSettingsDto as SsoSettingsDto
from docspace_api_sdk.models.sso_settings_request_dto import SsoSettingsRequestDto as SsoSettingsRequestDto
from docspace_api_sdk.models.sso_settings_wrapper import SsoSettingsWrapper as SsoSettingsWrapper
from docspace_api_sdk.models.sso_signing_algorithm_type_dto import SsoSigningAlgorithmTypeDto as SsoSigningAlgorithmTypeDto
from docspace_api_sdk.models.sso_sp_certificate_action_type_dto import SsoSpCertificateActionTypeDto as SsoSpCertificateActionTypeDto
from docspace_api_sdk.models.sso_sp_certificate_advanced_dto import SsoSpCertificateAdvancedDto as SsoSpCertificateAdvancedDto
from docspace_api_sdk.models.start_backup_request_dto import StartBackupRequestDto as StartBackupRequestDto
from docspace_api_sdk.models.start_backup_restore_request_dto import StartBackupRestoreRequestDto as StartBackupRestoreRequestDto
from docspace_api_sdk.models.start_edit_request import StartEditRequest as StartEditRequest
from docspace_api_sdk.models.start_filling_form import StartFillingForm as StartFillingForm
from docspace_api_sdk.models.start_filling_mode import StartFillingMode as StartFillingMode
from docspace_api_sdk.models.start_reassign_request_dto import StartReassignRequestDto as StartReassignRequestDto
from docspace_api_sdk.models.start_update_user_type_dto import StartUpdateUserTypeDto as StartUpdateUserTypeDto
from docspace_api_sdk.models.storage_array_wrapper import StorageArrayWrapper as StorageArrayWrapper
from docspace_api_sdk.models.storage_dto import StorageDto as StorageDto
from docspace_api_sdk.models.storage_encryption_request_dto import StorageEncryptionRequestDto as StorageEncryptionRequestDto
from docspace_api_sdk.models.storage_filter import StorageFilter as StorageFilter
from docspace_api_sdk.models.storage_request_dto import StorageRequestDto as StorageRequestDto
from docspace_api_sdk.models.storage_settings_dto import StorageSettingsDto as StorageSettingsDto
from docspace_api_sdk.models.storage_settings_wrapper import StorageSettingsWrapper as StorageSettingsWrapper
from docspace_api_sdk.models.string_array_wrapper import StringArrayWrapper as StringArrayWrapper
from docspace_api_sdk.models.string_wrapper import StringWrapper as StringWrapper
from docspace_api_sdk.models.studio_default_page_settings_dto import StudioDefaultPageSettingsDto as StudioDefaultPageSettingsDto
from docspace_api_sdk.models.studio_default_page_settings_wrapper import StudioDefaultPageSettingsWrapper as StudioDefaultPageSettingsWrapper
from docspace_api_sdk.models.sub_account_dto import SubAccountDto as SubAccountDto
from docspace_api_sdk.models.subject_type import SubjectType as SubjectType
from docspace_api_sdk.models.submit_form_dto import SubmitFormDto as SubmitFormDto
from docspace_api_sdk.models.subscription_balance_dto import SubscriptionBalanceDto as SubscriptionBalanceDto
from docspace_api_sdk.models.subscription_balance_wrapper import SubscriptionBalanceWrapper as SubscriptionBalanceWrapper
from docspace_api_sdk.models.tariff_dto import TariffDto as TariffDto
from docspace_api_sdk.models.tariff_quota_dto import TariffQuotaDto as TariffQuotaDto
from docspace_api_sdk.models.tariff_state import TariffState as TariffState
from docspace_api_sdk.models.tariff_wrapper import TariffWrapper as TariffWrapper
from docspace_api_sdk.models.task_progress_response_dto import TaskProgressResponseDto as TaskProgressResponseDto
from docspace_api_sdk.models.task_progress_response_wrapper import TaskProgressResponseWrapper as TaskProgressResponseWrapper
from docspace_api_sdk.models.telegram_status_dto import TelegramStatusDto as TelegramStatusDto
from docspace_api_sdk.models.telegram_status_wrapper import TelegramStatusWrapper as TelegramStatusWrapper
from docspace_api_sdk.models.templates_config_dto import TemplatesConfigDto as TemplatesConfigDto
from docspace_api_sdk.models.templates_request_dto import TemplatesRequestDto as TemplatesRequestDto
from docspace_api_sdk.models.tenant_ai_access_settings_dto import TenantAiAccessSettingsDto as TenantAiAccessSettingsDto
from docspace_api_sdk.models.tenant_ai_access_settings_request_dto import TenantAiAccessSettingsRequestDto as TenantAiAccessSettingsRequestDto
from docspace_api_sdk.models.tenant_ai_access_settings_wrapper import TenantAiAccessSettingsWrapper as TenantAiAccessSettingsWrapper
from docspace_api_sdk.models.tenant_audit_settings_dto import TenantAuditSettingsDto as TenantAuditSettingsDto
from docspace_api_sdk.models.tenant_audit_settings_request_dto import TenantAuditSettingsRequestDto as TenantAuditSettingsRequestDto
from docspace_api_sdk.models.tenant_audit_settings_wrapper import TenantAuditSettingsWrapper as TenantAuditSettingsWrapper
from docspace_api_sdk.models.tenant_banner_settings_dto import TenantBannerSettingsDto as TenantBannerSettingsDto
from docspace_api_sdk.models.tenant_banner_settings_request_dto import TenantBannerSettingsRequestDto as TenantBannerSettingsRequestDto
from docspace_api_sdk.models.tenant_banner_settings_wrapper import TenantBannerSettingsWrapper as TenantBannerSettingsWrapper
from docspace_api_sdk.models.tenant_deep_link_settings_dto import TenantDeepLinkSettingsDto as TenantDeepLinkSettingsDto
from docspace_api_sdk.models.tenant_deep_link_settings_wrapper import TenantDeepLinkSettingsWrapper as TenantDeepLinkSettingsWrapper
from docspace_api_sdk.models.tenant_dev_tools_access_settings_dto import TenantDevToolsAccessSettingsDto as TenantDevToolsAccessSettingsDto
from docspace_api_sdk.models.tenant_dev_tools_access_settings_request_dto import TenantDevToolsAccessSettingsRequestDto as TenantDevToolsAccessSettingsRequestDto
from docspace_api_sdk.models.tenant_dev_tools_access_settings_wrapper import TenantDevToolsAccessSettingsWrapper as TenantDevToolsAccessSettingsWrapper
from docspace_api_sdk.models.tenant_dto import TenantDto as TenantDto
from docspace_api_sdk.models.tenant_industry import TenantIndustry as TenantIndustry
from docspace_api_sdk.models.tenant_quota_dto import TenantQuotaDto as TenantQuotaDto
from docspace_api_sdk.models.tenant_quota_feature_dto import TenantQuotaFeatureDto as TenantQuotaFeatureDto
from docspace_api_sdk.models.tenant_quota_settings_dto import TenantQuotaSettingsDto as TenantQuotaSettingsDto
from docspace_api_sdk.models.tenant_quota_settings_request_dto import TenantQuotaSettingsRequestDto as TenantQuotaSettingsRequestDto
from docspace_api_sdk.models.tenant_quota_settings_wrapper import TenantQuotaSettingsWrapper as TenantQuotaSettingsWrapper
from docspace_api_sdk.models.tenant_quota_wrapper import TenantQuotaWrapper as TenantQuotaWrapper
from docspace_api_sdk.models.tenant_status import TenantStatus as TenantStatus
from docspace_api_sdk.models.tenant_trusted_domains_type import TenantTrustedDomainsType as TenantTrustedDomainsType
from docspace_api_sdk.models.tenant_user_invitation_settings_dto import TenantUserInvitationSettingsDto as TenantUserInvitationSettingsDto
from docspace_api_sdk.models.tenant_user_invitation_settings_request_dto import TenantUserInvitationSettingsRequestDto as TenantUserInvitationSettingsRequestDto
from docspace_api_sdk.models.tenant_user_invitation_settings_wrapper import TenantUserInvitationSettingsWrapper as TenantUserInvitationSettingsWrapper
from docspace_api_sdk.models.tenant_wallet_service import TenantWalletService as TenantWalletService
from docspace_api_sdk.models.tenant_wallet_service_settings_dto import TenantWalletServiceSettingsDto as TenantWalletServiceSettingsDto
from docspace_api_sdk.models.tenant_wallet_service_settings_wrapper import TenantWalletServiceSettingsWrapper as TenantWalletServiceSettingsWrapper
from docspace_api_sdk.models.tenant_wallet_settings_dto import TenantWalletSettingsDto as TenantWalletSettingsDto
from docspace_api_sdk.models.tenant_wallet_settings_request_dto import TenantWalletSettingsRequestDto as TenantWalletSettingsRequestDto
from docspace_api_sdk.models.tenant_wallet_settings_wrapper import TenantWalletSettingsWrapper as TenantWalletSettingsWrapper
from docspace_api_sdk.models.tenant_wrapper import TenantWrapper as TenantWrapper
from docspace_api_sdk.models.terminate_request_dto import TerminateRequestDto as TerminateRequestDto
from docspace_api_sdk.models.tfa_app_code_array_wrapper import TfaAppCodeArrayWrapper as TfaAppCodeArrayWrapper
from docspace_api_sdk.models.tfa_app_code_dto import TfaAppCodeDto as TfaAppCodeDto
from docspace_api_sdk.models.tfa_confirm_data_dto import TfaConfirmDataDto as TfaConfirmDataDto
from docspace_api_sdk.models.tfa_confirm_data_wrapper import TfaConfirmDataWrapper as TfaConfirmDataWrapper
from docspace_api_sdk.models.tfa_request_dto import TfaRequestDto as TfaRequestDto
from docspace_api_sdk.models.tfa_settings_array_wrapper import TfaSettingsArrayWrapper as TfaSettingsArrayWrapper
from docspace_api_sdk.models.tfa_settings_dto import TfaSettingsDto as TfaSettingsDto
from docspace_api_sdk.models.tfa_setup_code_dto import TfaSetupCodeDto as TfaSetupCodeDto
from docspace_api_sdk.models.tfa_setup_code_wrapper import TfaSetupCodeWrapper as TfaSetupCodeWrapper
from docspace_api_sdk.models.tfa_type import TfaType as TfaType
from docspace_api_sdk.models.tfa_validate_request_dto import TfaValidateRequestDto as TfaValidateRequestDto
from docspace_api_sdk.models.third_party_account_array_wrapper import ThirdPartyAccountArrayWrapper as ThirdPartyAccountArrayWrapper
from docspace_api_sdk.models.third_party_account_dto import ThirdPartyAccountDto as ThirdPartyAccountDto
from docspace_api_sdk.models.third_party_backup_request_dto import ThirdPartyBackupRequestDto as ThirdPartyBackupRequestDto
from docspace_api_sdk.models.third_party_check_conversion_request_dto import ThirdPartyCheckConversionRequestDto as ThirdPartyCheckConversionRequestDto
from docspace_api_sdk.models.third_party_chunked_upload_session_dto import ThirdPartyChunkedUploadSessionDto as ThirdPartyChunkedUploadSessionDto
from docspace_api_sdk.models.third_party_chunked_upload_session_result_dto import ThirdPartyChunkedUploadSessionResultDto as ThirdPartyChunkedUploadSessionResultDto
from docspace_api_sdk.models.third_party_chunked_upload_session_result_wrapper import ThirdPartyChunkedUploadSessionResultWrapper as ThirdPartyChunkedUploadSessionResultWrapper
from docspace_api_sdk.models.third_party_chunked_upload_session_wrapper import ThirdPartyChunkedUploadSessionWrapper as ThirdPartyChunkedUploadSessionWrapper
from docspace_api_sdk.models.third_party_configuration_dto import ThirdPartyConfigurationDto as ThirdPartyConfigurationDto
from docspace_api_sdk.models.third_party_configuration_wrapper import ThirdPartyConfigurationWrapper as ThirdPartyConfigurationWrapper
from docspace_api_sdk.models.third_party_draft_location import ThirdPartyDraftLocation as ThirdPartyDraftLocation
from docspace_api_sdk.models.third_party_file_array_wrapper import ThirdPartyFileArrayWrapper as ThirdPartyFileArrayWrapper
from docspace_api_sdk.models.third_party_file_dto import ThirdPartyFileDto as ThirdPartyFileDto
from docspace_api_sdk.models.third_party_file_entry_dto import ThirdPartyFileEntryDto as ThirdPartyFileEntryDto
from docspace_api_sdk.models.third_party_file_wrapper import ThirdPartyFileWrapper as ThirdPartyFileWrapper
from docspace_api_sdk.models.third_party_folder_array_wrapper import ThirdPartyFolderArrayWrapper as ThirdPartyFolderArrayWrapper
from docspace_api_sdk.models.third_party_folder_content_dto import ThirdPartyFolderContentDto as ThirdPartyFolderContentDto
from docspace_api_sdk.models.third_party_folder_content_wrapper import ThirdPartyFolderContentWrapper as ThirdPartyFolderContentWrapper
from docspace_api_sdk.models.third_party_folder_dto import ThirdPartyFolderDto as ThirdPartyFolderDto
from docspace_api_sdk.models.third_party_folder_wrapper import ThirdPartyFolderWrapper as ThirdPartyFolderWrapper
from docspace_api_sdk.models.third_party_request_dto import ThirdPartyRequestDto as ThirdPartyRequestDto
from docspace_api_sdk.models.third_party_save_as_pdf_request import ThirdPartySaveAsPdfRequest as ThirdPartySaveAsPdfRequest
from docspace_api_sdk.models.third_party_upload_session_response_dto import ThirdPartyUploadSessionResponseDto as ThirdPartyUploadSessionResponseDto
from docspace_api_sdk.models.third_party_upload_session_response_wrapper import ThirdPartyUploadSessionResponseWrapper as ThirdPartyUploadSessionResponseWrapper
from docspace_api_sdk.models.thumbnail import Thumbnail as Thumbnail
from docspace_api_sdk.models.thumbnails_data_dto import ThumbnailsDataDto as ThumbnailsDataDto
from docspace_api_sdk.models.thumbnails_data_wrapper import ThumbnailsDataWrapper as ThumbnailsDataWrapper
from docspace_api_sdk.models.thumbnails_request import ThumbnailsRequest as ThumbnailsRequest
from docspace_api_sdk.models.time_bound_dto import TimeBoundDto as TimeBoundDto
from docspace_api_sdk.models.timezone_array_wrapper import TimezoneArrayWrapper as TimezoneArrayWrapper
from docspace_api_sdk.models.timezone_dto import TimezoneDto as TimezoneDto
from docspace_api_sdk.models.token_diagnostics_dto import TokenDiagnosticsDto as TokenDiagnosticsDto
from docspace_api_sdk.models.token_diagnostics_wrapper import TokenDiagnosticsWrapper as TokenDiagnosticsWrapper
from docspace_api_sdk.models.top_up_deposit_request_dto import TopUpDepositRequestDto as TopUpDepositRequestDto
from docspace_api_sdk.models.transaction_info_dto import TransactionInfoDto as TransactionInfoDto
from docspace_api_sdk.models.turn_on_admin_message_settings_request_dto import TurnOnAdminMessageSettingsRequestDto as TurnOnAdminMessageSettingsRequestDto
from docspace_api_sdk.models.upcoming_payment_array_wrapper import UpcomingPaymentArrayWrapper as UpcomingPaymentArrayWrapper
from docspace_api_sdk.models.upcoming_payment_dto import UpcomingPaymentDto as UpcomingPaymentDto
from docspace_api_sdk.models.update_api_key_request import UpdateApiKeyRequest as UpdateApiKeyRequest
from docspace_api_sdk.models.update_client_request import UpdateClientRequest as UpdateClientRequest
from docspace_api_sdk.models.update_comment_request import UpdateCommentRequest as UpdateCommentRequest
from docspace_api_sdk.models.update_file_request import UpdateFileRequest as UpdateFileRequest
from docspace_api_sdk.models.update_folder_metadata_template_request import UpdateFolderMetadataTemplateRequest as UpdateFolderMetadataTemplateRequest
from docspace_api_sdk.models.update_group_request import UpdateGroupRequest as UpdateGroupRequest
from docspace_api_sdk.models.update_member_culture_request import UpdateMemberCultureRequest as UpdateMemberCultureRequest
from docspace_api_sdk.models.update_member_request_dto import UpdateMemberRequestDto as UpdateMemberRequestDto
from docspace_api_sdk.models.update_members_quota_request_dto import UpdateMembersQuotaRequestDto as UpdateMembersQuotaRequestDto
from docspace_api_sdk.models.update_members_quota_request_dto_quota import UpdateMembersQuotaRequestDtoQuota as UpdateMembersQuotaRequestDtoQuota
from docspace_api_sdk.models.update_members_request_dto import UpdateMembersRequestDto as UpdateMembersRequestDto
from docspace_api_sdk.models.update_metadata_field_request import UpdateMetadataFieldRequest as UpdateMetadataFieldRequest
from docspace_api_sdk.models.update_metadata_template import UpdateMetadataTemplate as UpdateMetadataTemplate
from docspace_api_sdk.models.update_photo_member_request import UpdatePhotoMemberRequest as UpdatePhotoMemberRequest
from docspace_api_sdk.models.update_room_group_request import UpdateRoomGroupRequest as UpdateRoomGroupRequest
from docspace_api_sdk.models.update_room_request import UpdateRoomRequest as UpdateRoomRequest
from docspace_api_sdk.models.update_rooms_quota_request_dto import UpdateRoomsQuotaRequestDto as UpdateRoomsQuotaRequestDto
from docspace_api_sdk.models.update_rooms_room_ids_request_dto import UpdateRoomsRoomIdsRequestDto as UpdateRoomsRoomIdsRequestDto
from docspace_api_sdk.models.update_service_limit_request_dto import UpdateServiceLimitRequestDto as UpdateServiceLimitRequestDto
from docspace_api_sdk.models.update_tag_request_dto import UpdateTagRequestDto as UpdateTagRequestDto
from docspace_api_sdk.models.update_webhooks_config_request_dto import UpdateWebhooksConfigRequestDto as UpdateWebhooksConfigRequestDto
from docspace_api_sdk.models.upload_result_dto import UploadResultDto as UploadResultDto
from docspace_api_sdk.models.upload_result_wrapper import UploadResultWrapper as UploadResultWrapper
from docspace_api_sdk.models.upload_session_response_dto import UploadSessionResponseDto as UploadSessionResponseDto
from docspace_api_sdk.models.upload_session_response_wrapper import UploadSessionResponseWrapper as UploadSessionResponseWrapper
from docspace_api_sdk.models.usage_space_stat_item_array_wrapper import UsageSpaceStatItemArrayWrapper as UsageSpaceStatItemArrayWrapper
from docspace_api_sdk.models.usage_space_stat_item_dto import UsageSpaceStatItemDto as UsageSpaceStatItemDto
from docspace_api_sdk.models.user_config_dto import UserConfigDto as UserConfigDto
from docspace_api_sdk.models.user_exists_response_dto import UserExistsResponseDto as UserExistsResponseDto
from docspace_api_sdk.models.user_exists_response_wrapper import UserExistsResponseWrapper as UserExistsResponseWrapper
from docspace_api_sdk.models.user_invitation import UserInvitation as UserInvitation
from docspace_api_sdk.models.user_invitation_request_dto import UserInvitationRequestDto as UserInvitationRequestDto
from docspace_api_sdk.models.user_service_limit_dto import UserServiceLimitDto as UserServiceLimitDto
from docspace_api_sdk.models.validation_error_response import ValidationErrorResponse as ValidationErrorResponse
from docspace_api_sdk.models.validation_result import ValidationResult as ValidationResult
from docspace_api_sdk.models.vectorization_status import VectorizationStatus as VectorizationStatus
from docspace_api_sdk.models.wallet_quantity_request_dto import WalletQuantityRequestDto as WalletQuantityRequestDto
from docspace_api_sdk.models.wallet_service_array_wrapper import WalletServiceArrayWrapper as WalletServiceArrayWrapper
from docspace_api_sdk.models.wallet_service_dto import WalletServiceDto as WalletServiceDto
from docspace_api_sdk.models.wallet_service_wrapper import WalletServiceWrapper as WalletServiceWrapper
from docspace_api_sdk.models.watermark_additions import WatermarkAdditions as WatermarkAdditions
from docspace_api_sdk.models.watermark_dto import WatermarkDto as WatermarkDto
from docspace_api_sdk.models.watermark_on_draw_dto import WatermarkOnDrawDto as WatermarkOnDrawDto
from docspace_api_sdk.models.watermark_paragraph_dto import WatermarkParagraphDto as WatermarkParagraphDto
from docspace_api_sdk.models.watermark_request_dto import WatermarkRequestDto as WatermarkRequestDto
from docspace_api_sdk.models.watermark_text_run_dto import WatermarkTextRunDto as WatermarkTextRunDto
from docspace_api_sdk.models.web_item_security_request_dto import WebItemSecurityRequestDto as WebItemSecurityRequestDto
from docspace_api_sdk.models.web_items_security_request_dto import WebItemsSecurityRequestDto as WebItemsSecurityRequestDto
from docspace_api_sdk.models.web_plugin_array_wrapper import WebPluginArrayWrapper as WebPluginArrayWrapper
from docspace_api_sdk.models.web_plugin_dto import WebPluginDto as WebPluginDto
from docspace_api_sdk.models.web_plugin_request import WebPluginRequest as WebPluginRequest
from docspace_api_sdk.models.web_plugin_wrapper import WebPluginWrapper as WebPluginWrapper
from docspace_api_sdk.models.webhook_group_status import WebhookGroupStatus as WebhookGroupStatus
from docspace_api_sdk.models.webhook_retry_request_dto import WebhookRetryRequestDto as WebhookRetryRequestDto
from docspace_api_sdk.models.webhook_trigger import WebhookTrigger as WebhookTrigger
from docspace_api_sdk.models.webhook_trigger_array_wrapper import WebhookTriggerArrayWrapper as WebhookTriggerArrayWrapper
from docspace_api_sdk.models.webhook_trigger_dto import WebhookTriggerDto as WebhookTriggerDto
from docspace_api_sdk.models.webhooks_config_dto import WebhooksConfigDto as WebhooksConfigDto
from docspace_api_sdk.models.webhooks_config_with_status_array_wrapper import WebhooksConfigWithStatusArrayWrapper as WebhooksConfigWithStatusArrayWrapper
from docspace_api_sdk.models.webhooks_config_with_status_dto import WebhooksConfigWithStatusDto as WebhooksConfigWithStatusDto
from docspace_api_sdk.models.webhooks_config_wrapper import WebhooksConfigWrapper as WebhooksConfigWrapper
from docspace_api_sdk.models.webhooks_log_array_wrapper import WebhooksLogArrayWrapper as WebhooksLogArrayWrapper
from docspace_api_sdk.models.webhooks_log_dto import WebhooksLogDto as WebhooksLogDto
from docspace_api_sdk.models.webhooks_log_wrapper import WebhooksLogWrapper as WebhooksLogWrapper
from docspace_api_sdk.models.white_label_item_array_wrapper import WhiteLabelItemArrayWrapper as WhiteLabelItemArrayWrapper
from docspace_api_sdk.models.white_label_item_dto import WhiteLabelItemDto as WhiteLabelItemDto
from docspace_api_sdk.models.white_label_item_path_dto import WhiteLabelItemPathDto as WhiteLabelItemPathDto
from docspace_api_sdk.models.white_label_item_size_dto import WhiteLabelItemSizeDto as WhiteLabelItemSizeDto
from docspace_api_sdk.models.white_label_logo_type import WhiteLabelLogoType as WhiteLabelLogoType
from docspace_api_sdk.models.white_label_request_dto import WhiteLabelRequestDto as WhiteLabelRequestDto
from docspace_api_sdk.models.wizard_request_dto import WizardRequestDto as WizardRequestDto
from docspace_api_sdk.models.wizard_settings_dto import WizardSettingsDto as WizardSettingsDto
from docspace_api_sdk.models.wizard_settings_wrapper import WizardSettingsWrapper as WizardSettingsWrapper
from docspace_api_sdk.models.xlsx_report_response_dto import XlsxReportResponseDto as XlsxReportResponseDto
from docspace_api_sdk.models.xlsx_report_response_wrapper import XlsxReportResponseWrapper as XlsxReportResponseWrapper

