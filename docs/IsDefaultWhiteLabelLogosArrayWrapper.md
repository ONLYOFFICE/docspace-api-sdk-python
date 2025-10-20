# IsDefaultWhiteLabelLogosArrayWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**List[IsDefaultWhiteLabelLogosDto]**](IsDefaultWhiteLabelLogosDto.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace_api_sdk.models.is_default_white_label_logos_array_wrapper import IsDefaultWhiteLabelLogosArrayWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of IsDefaultWhiteLabelLogosArrayWrapper from a JSON string
is_default_white_label_logos_array_wrapper_instance = IsDefaultWhiteLabelLogosArrayWrapper.from_json(json)
# print the JSON string representation of the object
print(IsDefaultWhiteLabelLogosArrayWrapper.to_json())

# convert the object into a dict
is_default_white_label_logos_array_wrapper_dict = is_default_white_label_logos_array_wrapper_instance.to_dict()
# create an instance of IsDefaultWhiteLabelLogosArrayWrapper from a dict
is_default_white_label_logos_array_wrapper_from_dict = IsDefaultWhiteLabelLogosArrayWrapper.from_dict(is_default_white_label_logos_array_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


