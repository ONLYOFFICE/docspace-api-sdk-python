# ReviewConfigDto
How tracked changes are displayed when the document opens.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**review_display** | **str** | How the editors render tracked changes at first: with the markup, in a simplified markup, as the final text,  or as the original text. A session that may not write opens on the final text. | [optional] [readonly] 

## Example

```python
from docspace_api_sdk.models.review_config_dto import ReviewConfigDto

# TODO update the JSON string below
json = "{}"
# create an instance of ReviewConfigDto from a JSON string
review_config_dto_instance = ReviewConfigDto.from_json(json)
# print the JSON string representation of the object
print(ReviewConfigDto.to_json())

# convert the object into a dict
review_config_dto_dict = review_config_dto_instance.to_dict()
# create an instance of ReviewConfigDto from a dict
review_config_dto_from_dict = ReviewConfigDto.from_dict(review_config_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


