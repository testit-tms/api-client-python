# CreateProjectsAttributeRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **bool, date, datetime, dict, float, int, list, str, none_type** | Type of attribute | 
**name** | **str** | Name of the attribute | 
**options** | [**[CustomAttributeOptionPostModel], none_type**](CustomAttributeOptionPostModel.md) | Collection of attribute options  &lt;br /&gt;  Available for attributes of type &#x60;options&#x60; and &#x60;multiple options&#x60; only | [optional] 
**is_enabled** | **bool** | Indicates if the attribute is enabled | [optional] 
**is_required** | **bool** | Indicates if the attribute value is mandatory to specify | [optional] 
**is_global** | **bool** | Indicates if the attribute is available across all projects | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


