# LabelShortModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**global_id** | **int** | Global ID of the label | 
**name** | **str** | Name of the label | 

## Example

```python
from testit_api_client.models.label_short_model import LabelShortModel

# TODO update the JSON string below
json = "{}"
# create an instance of LabelShortModel from a JSON string
label_short_model_instance = LabelShortModel.from_json(json)
# print the JSON string representation of the object
print LabelShortModel.to_json()

# convert the object into a dict
label_short_model_dict = label_short_model_instance.to_dict()
# create an instance of LabelShortModel from a dict
label_short_model_from_dict = LabelShortModel.from_dict(label_short_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


