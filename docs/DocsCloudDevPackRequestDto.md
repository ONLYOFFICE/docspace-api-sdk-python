# DocsCloudDevPackRequestDto
The request parameters for switch the DocsCloud subscription to DocsCloudDevPack.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quantity** | **int** | The number of users for DocsCloudDevPack subscription. | [optional] 

## Example

```python
from docspace_api_sdk.models.docs_cloud_dev_pack_request_dto import DocsCloudDevPackRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of DocsCloudDevPackRequestDto from a JSON string
docs_cloud_dev_pack_request_dto_instance = DocsCloudDevPackRequestDto.from_json(json)
# print the JSON string representation of the object
print(DocsCloudDevPackRequestDto.to_json())

# convert the object into a dict
docs_cloud_dev_pack_request_dto_dict = docs_cloud_dev_pack_request_dto_instance.to_dict()
# create an instance of DocsCloudDevPackRequestDto from a dict
docs_cloud_dev_pack_request_dto_from_dict = DocsCloudDevPackRequestDto.from_dict(docs_cloud_dev_pack_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


