import pytz
from rest_framework import pagination, serializers
from rest_framework.renderers import JSONRenderer
from swimapp.models import Version
from datetime import datetime


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

        # Create a version dictionary to attach to response
        version = {}
        versionInfo = Version.objects.latest_version()
        version['version_number'] = versionInfo.version
        version['version_date'] = versionInfo.datetime

        resource = getattr(renderer_context.get('view').get_serializer().Meta,
                           'resource_name',
                           'data')

        #check if the results have been paginated
        #if data.get('paginated_results'):
            #add the resource key and copy the results
            #response_data['meta'] = data.get('meta')
            #response_data[resource] = data.get('paginated_results')
        #else:
        response_data[resource] = data
        response_data['version'] = version

        local_tz = pytz.timezone('America/New_York')

        response_data['timestamp'] = datetime.now(local_tz)

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
