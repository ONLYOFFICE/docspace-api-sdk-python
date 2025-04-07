# Paragraph


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**align** | **int** |  | [optional] 
**runs** | [**List[Run]**](Run.md) |  | [optional] 

## Example

```python
from docspace.models.paragraph import Paragraph

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


