# IsDefaultWhiteLabelLogosWrapper
The successful API response containing the IsDefaultWhiteLabelLogosDto object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**IsDefaultWhiteLabelLogosDto**](IsDefaultWhiteLabelLogosDto.md) | The IsDefaultWhiteLabelLogosDto object returned by the operation. | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.is_default_white_label_logos_wrapper import IsDefaultWhiteLabelLogosWrapper

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


