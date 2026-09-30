# ExternalShareRequestParam
The password that unlocks a protected external share link.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** | The password chosen by the member who shared the entry, spelled exactly as they typed it. It is compared  against the stored value and never returned back; a mismatch is reported through the answer's status instead  of an error. | [optional] 

## Example

```python
from docspace_api_sdk.models.external_share_request_param import ExternalShareRequestParam

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalShareRequestParam from a JSON string
external_share_request_param_instance = ExternalShareRequestParam.from_json(json)
# print the JSON string representation of the object
print(ExternalShareRequestParam.to_json())

# convert the object into a dict
external_share_request_param_dict = external_share_request_param_instance.to_dict()
# create an instance of ExternalShareRequestParam from a dict
external_share_request_param_from_dict = ExternalShareRequestParam.from_dict(external_share_request_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


