# LabelApiResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the label | 
**global_id** | **int** | Global ID of the label | 

## Example

```python
from testit_api_client.models.label_api_result import LabelApiResult

# TODO update the JSON string below
json = "{}"
# create an instance of LabelApiResult from a JSON string
label_api_result_instance = LabelApiResult.from_json(json)
# print the JSON string representation of the object
print LabelApiResult.to_json()

# convert the object into a dict
label_api_result_dict = label_api_result_instance.to_dict()
# create an instance of LabelApiResult from a dict
label_api_result_from_dict = LabelApiResult.from_dict(label_api_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


