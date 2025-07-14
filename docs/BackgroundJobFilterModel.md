# BackgroundJobFilterModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**types** | [**List[BackgroundJobType]**](BackgroundJobType.md) |  | [optional] 
**states** | [**List[BackgroundJobState]**](BackgroundJobState.md) |  | [optional] 
**is_deleted** | **bool** |  | [optional] 
**start_date** | [**DateTimeRangeSelectorModel**](DateTimeRangeSelectorModel.md) |  | [optional] 
**end_date** | [**DateTimeRangeSelectorModel**](DateTimeRangeSelectorModel.md) |  | [optional] 

## Example

```python
from testit_api_client.models.background_job_filter_model import BackgroundJobFilterModel

# TODO update the JSON string below
json = "{}"
# create an instance of BackgroundJobFilterModel from a JSON string
background_job_filter_model_instance = BackgroundJobFilterModel.from_json(json)
# print the JSON string representation of the object
print BackgroundJobFilterModel.to_json()

# convert the object into a dict
background_job_filter_model_dict = background_job_filter_model_instance.to_dict()
# create an instance of BackgroundJobFilterModel from a dict
background_job_filter_model_from_dict = BackgroundJobFilterModel.from_dict(background_job_filter_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


