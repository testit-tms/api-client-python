# ApiV2CustomAttributesGlobalPostRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of attribute | 
**type** | [**CustomAttributeTypesEnum**](CustomAttributeTypesEnum.md) |  | 
**is_enabled** | **bool, none_type** | Indicates whether the attribute is available | [optional] 
**is_required** | **bool, none_type** | Indicates whether the attribute value is mandatory to specify | [optional] 
**options** | [**[CustomAttributeOptionPostModel], none_type**](CustomAttributeOptionPostModel.md) | Collection of attribute options  &lt;br /&gt;  Available for attributes of type &#x60;options&#x60; and &#x60;multiple options&#x60; only | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


