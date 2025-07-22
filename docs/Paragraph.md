# Paragraph
The paragraph parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**align** | **int** | The paragraph align. | [optional] 
**runs** | [**List[Run]**](Run.md) | The list of text runs from the paragraph. | [optional] 

## Example

```python
from docspace-api-sdk.models.paragraph import Paragraph

# TODO update the JSON string below
json = "{}"
# create an instance of Paragraph from a JSON string
paragraph_instance = Paragraph.from_json(json)
# print the JSON string representation of the object
print(Paragraph.to_json())

# convert the object into a dict
paragraph_dict = paragraph_instance.to_dict()
# create an instance of Paragraph from a dict
paragraph_from_dict = Paragraph.from_dict(paragraph_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


