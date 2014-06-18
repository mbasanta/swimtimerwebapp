from rest_framework import pagination, serializers
from rest_framework.renderers import JSONRenderer


class SwimAppJSONRenderer(JSONRenderer):
    """
    Override the render method of the django rest framework JSONRenderer to
    allow the following:
    * adding a resource_name root element to all GET requests formatted
        with JSON
    * reformatting paginated results to the following structure
        {meta: {}, resource_name: [{},{}]}

    NB: This solution requires a custom pagination serializer and an attribute
        of 'resource_name' defined in the serializer
    """

    def render(self, data, accepted_media_type=None, renderer_context=None):
        response_data = {}

        resource = getattr(renderer_context.get('view').get_serializer().Meta,
                           'resource_name',
                           'objects')

        #check if the results have been paginated
        #if data.get('paginated_results'):
            #add the resource key and copy the results
            #response_data['meta'] = data.get('meta')
            #response_data[resource] = data.get('paginated_results')
        #else:
        response_data[resource] = data

        #call super to render the response
        response = super(SwimAppJSONRenderer, self).render(response_data,
                                                           accepted_media_type,
                                                           renderer_context)

        return response


class SwimAppMetaSerializer(serializers.Serializer):
    next_page = pagination.NextPageField(source='*')
    prev_page = pagination.PreviousPageField(source='*')
    record_count = serializers.Field(source='paginator.count')


class SwimAppPaginationSerializer(pagination.BasePaginationSerializer):
    # Takes the page object as the source
    meta = SwimAppMetaSerializer(source='*')
    results_field = 'paginated_results'
