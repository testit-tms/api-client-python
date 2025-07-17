# AutoTestAverageDurationModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**passed_average_duration** | **float** |  | 
**failed_average_duration** | **float** |  | 

## Example

```python
from testit_api_client.models.auto_test_average_duration_model import AutoTestAverageDurationModel

# TODO update the JSON string below
json = "{}"
# create an instance of AutoTestAverageDurationModel from a JSON string
auto_test_average_duration_model_instance = AutoTestAverageDurationModel.from_json(json)
# print the JSON string representation of the object
print AutoTestAverageDurationModel.to_json()

# convert the object into a dict
auto_test_average_duration_model_dict = auto_test_average_duration_model_instance.to_dict()
# create an instance of AutoTestAverageDurationModel from a dict
auto_test_average_duration_model_from_dict = AutoTestAverageDurationModel.from_dict(auto_test_average_duration_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


