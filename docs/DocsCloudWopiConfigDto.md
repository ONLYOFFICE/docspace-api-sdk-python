# DocsCloudWopiConfigDto
Represents the WOPI configuration of a Docs Connect tenant.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **bool** | Whether WOPI is enabled. | [optional] 

## Example

```python
from docspace_api_sdk.models.docs_cloud_wopi_config_dto import DocsCloudWopiConfigDto

# TODO update the JSON string below
json = "{}"
# create an instance of DocsCloudWopiConfigDto from a JSON string
docs_cloud_wopi_config_dto_instance = DocsCloudWopiConfigDto.from_json(json)
# print the JSON string representation of the object
print(DocsCloudWopiConfigDto.to_json())

# convert the object into a dict
docs_cloud_wopi_config_dto_dict = docs_cloud_wopi_config_dto_instance.to_dict()
# create an instance of DocsCloudWopiConfigDto from a dict
docs_cloud_wopi_config_dto_from_dict = DocsCloudWopiConfigDto.from_dict(docs_cloud_wopi_config_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


