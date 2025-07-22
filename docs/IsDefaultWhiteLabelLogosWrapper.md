# IsDefaultWhiteLabelLogosWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**IsDefaultWhiteLabelLogosDto**](IsDefaultWhiteLabelLogosDto.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace-api-sdk.models.is_default_white_label_logos_wrapper import IsDefaultWhiteLabelLogosWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of IsDefaultWhiteLabelLogosWrapper from a JSON string
is_default_white_label_logos_wrapper_instance = IsDefaultWhiteLabelLogosWrapper.from_json(json)
# print the JSON string representation of the object
print(IsDefaultWhiteLabelLogosWrapper.to_json())

# convert the object into a dict
is_default_white_label_logos_wrapper_dict = is_default_white_label_logos_wrapper_instance.to_dict()
# create an instance of IsDefaultWhiteLabelLogosWrapper from a dict
is_default_white_label_logos_wrapper_from_dict = IsDefaultWhiteLabelLogosWrapper.from_dict(is_default_white_label_logos_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


