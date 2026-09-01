# MentionWrapperArrayWrapper
The successful API response containing the list of MentionWrapper objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**List[MentionWrapper]**](MentionWrapper.md) | The list of MentionWrapper objects returned by the operation. | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.mention_wrapper_array_wrapper import MentionWrapperArrayWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of MentionWrapperArrayWrapper from a JSON string
mention_wrapper_array_wrapper_instance = MentionWrapperArrayWrapper.from_json(json)
# print the JSON string representation of the object
print(MentionWrapperArrayWrapper.to_json())

# convert the object into a dict
mention_wrapper_array_wrapper_dict = mention_wrapper_array_wrapper_instance.to_dict()
# create an instance of MentionWrapperArrayWrapper from a dict
mention_wrapper_array_wrapper_from_dict = MentionWrapperArrayWrapper.from_dict(mention_wrapper_array_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


