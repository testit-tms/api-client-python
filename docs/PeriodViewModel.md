# PeriodViewModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** |  | [optional] 
**end_date** | **datetime** |  | [optional] 

## Example

```python
from testit_api_client.models.period_view_model import PeriodViewModel

# TODO update the JSON string below
json = "{}"
# create an instance of PeriodViewModel from a JSON string
period_view_model_instance = PeriodViewModel.from_json(json)
# print the JSON string representation of the object
print PeriodViewModel.to_json()

# convert the object into a dict
period_view_model_dict = period_view_model_instance.to_dict()
# create an instance of PeriodViewModel from a dict
period_view_model_from_dict = PeriodViewModel.from_dict(period_view_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


