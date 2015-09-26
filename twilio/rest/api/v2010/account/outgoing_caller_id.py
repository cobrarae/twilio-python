# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /       
"""

from twilio import values
from twilio.rest import deserialize
from twilio.rest.base import InstanceContext
from twilio.rest.base import InstanceResource
from twilio.rest.base import ListResource


class OutgoingCallerIdList(ListResource):

    def __init__(self, version, account_sid):
        """
        Initialize the OutgoingCallerIdList
        
        :param Version version: Version that contains the resource
        :param account_sid: Contextual account_sid
        
        :returns: OutgoingCallerIdList
        :rtype: OutgoingCallerIdList
        """
        super(OutgoingCallerIdList, self).__init__(version)
        
        # Path Solution
        self._kwargs = {
            'account_sid': account_sid,
        }
        self._uri = '/Accounts/{account_sid}/OutgoingCallerIds.json'.format(**self._kwargs)

    def stream(self, phone_number=values.unset, friendly_name=values.unset,
               limit=None, page_size=None, **kwargs):
        """
        Streams OutgoingCallerIdInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param str phone_number: Filter by phone number
        :param str friendly_name: Filter by friendly name
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)
        
        :returns: Generator that will yield up to limit results
        :rtype: generator
        """
        limits = self._version.read_limits(limit, page_size)
        
        params = values.of({
            'PhoneNumber': phone_number,
            'FriendlyName': friendly_name,
            'PageSize': limits['page_size'],
        })
        params.update(kwargs)
        
        return self._version.stream(
            self,
            OutgoingCallerIdInstance,
            self._kwargs,
            'GET',
            self._uri,
            limits['limit'],
            limits['page_limit'],
            params=params,
        )

    def read(self, phone_number=values.unset, friendly_name=values.unset,
             limit=None, page_size=None, **kwargs):
        """
        Reads OutgoingCallerIdInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param str phone_number: Filter by phone number
        :param str friendly_name: Filter by friendly name
        :param int limit: Upper limit for the number of records to return. read() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, read() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)
        
        :returns: Generator that will yield up to limit results
        :rtype: generator
        """
        return list(self.stream(
            phone_number=phone_number,
            friendly_name=friendly_name,
            limit=limit,
            page_size=page_size,
            **kwargs
        ))

    def page(self, phone_number=values.unset, friendly_name=values.unset,
             page_token=None, page_number=None, page_size=None, **kwargs):
        """
        Retrieve a single page of OutgoingCallerIdInstance records from the API.
        Request is executed immediately
        
        :param str phone_number: Filter by phone number
        :param str friendly_name: Filter by friendly name
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50
        
        :returns: Page of OutgoingCallerIdInstance
        :rtype: Page
        """
        params = values.of({
            'PhoneNumber': phone_number,
            'FriendlyName': friendly_name,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })
        params.update(kwargs)
        
        return self._version.page(
            self,
            OutgoingCallerIdInstance,
            self._kwargs,
            'GET',
            self._uri,
            params=params,
        )

    def create(self, phone_number, friendly_name=values.unset,
               call_delay=values.unset, extension=values.unset,
               status_callback=values.unset, status_callback_method=values.unset):
        """
        Create a new OutgoingCallerIdInstance
        
        :param str phone_number: The phone number to verify
        :param str friendly_name: A human readable description of the CallerID
        :param str call_delay: Number of seconds to delay before initiating verification
        :param str extension: Digits to dial after connecting the verification call
        :param str status_callback: URL Twilio will request with status of the verification
        :param str status_callback_method: HTTP method Twilio will use with the status callback
        
        :returns: Newly created OutgoingCallerIdInstance
        :rtype: OutgoingCallerIdInstance
        """
        data = values.of({
            'PhoneNumber': phone_number,
            'FriendlyName': friendly_name,
            'CallDelay': call_delay,
            'Extension': extension,
            'StatusCallback': status_callback,
            'StatusCallbackMethod': status_callback_method,
        })
        
        return self._version.create(
            OutgoingCallerIdInstance,
            self._kwargs,
            'POST',
            self._uri,
            data=data,
        )

    def __call__(self, sid):
        """
        Constructs a OutgoingCallerIdContext
        
        :param sid: Contextual sid
        
        :returns: OutgoingCallerIdContext
        :rtype: OutgoingCallerIdContext
        """
        return OutgoingCallerIdContext(self._version, sid=sid, **self._kwargs)

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.OutgoingCallerIdList>'


class OutgoingCallerIdContext(InstanceContext):

    def __init__(self, version, account_sid, sid):
        """
        Initialize the OutgoingCallerIdContext
        
        :param Version version
        :param account_sid: Contextual account_sid
        :param sid: Contextual sid
        
        :returns: OutgoingCallerIdContext
        :rtype: OutgoingCallerIdContext
        """
        super(OutgoingCallerIdContext, self).__init__(version)
        
        # Path Solution
        self._kwargs = {
            'account_sid': account_sid,
            'sid': sid,
        }
        self._uri = '/Accounts/{account_sid}/OutgoingCallerIds/{sid}.json'.format(**self._kwargs)

    def fetch(self):
        """
        Fetch a OutgoingCallerIdInstance
        
        :returns: Fetched OutgoingCallerIdInstance
        :rtype: OutgoingCallerIdInstance
        """
        params = values.of({})
        
        return self._version.fetch(
            OutgoingCallerIdInstance,
            self._kwargs,
            'GET',
            self._uri,
            params=params,
        )

    def update(self, friendly_name=values.unset):
        """
        Update the OutgoingCallerIdInstance
        
        :param str friendly_name: A human readable description of the caller ID
        
        :returns: Updated OutgoingCallerIdInstance
        :rtype: OutgoingCallerIdInstance
        """
        data = values.of({
            'FriendlyName': friendly_name,
        })
        
        return self._version.update(
            OutgoingCallerIdInstance,
            self._kwargs,
            'POST',
            self._uri,
            data=data,
        )

    def delete(self):
        """
        Deletes the OutgoingCallerIdInstance
        
        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete('delete', self._uri)

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._kwargs.items())
        return '<Twilio.Api.V2010.OutgoingCallerIdContext {}>'.format(context)


class OutgoingCallerIdInstance(InstanceResource):

    def __init__(self, version, payload, account_sid, sid=None):
        """
        Initialize the OutgoingCallerIdInstance
        
        :returns: OutgoingCallerIdInstance
        :rtype: OutgoingCallerIdInstance
        """
        super(OutgoingCallerIdInstance, self).__init__(version)
        
        # Marshaled Properties
        self._properties = {
            'account_sid': payload['account_sid'],
            'call_sid': payload['call_sid'],
            'date_created': deserialize.rfc2822_datetime(payload['date_created']),
            'date_updated': deserialize.rfc2822_datetime(payload['date_updated']),
            'friendly_name': payload['friendly_name'],
            'phone_number': payload['phone_number'],
            'sid': payload['sid'],
            'uri': payload['uri'],
            'validation_code': deserialize.integer(payload['validation_code']),
        }
        
        # Context
        self._instance_context = None
        self._kwargs = {
            'account_sid': account_sid,
            'sid': sid or self._properties['sid'],
        }

    @property
    def _context(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context
        
        :returns: OutgoingCallerIdContext for this OutgoingCallerIdInstance
        :rtype: OutgoingCallerIdContext
        """
        if self._instance_context is None:
            self._instance_context = OutgoingCallerIdContext(
                self._version,
                self._kwargs['account_sid'],
                self._kwargs['sid'],
            )
        return self._instance_context

    @property
    def account_sid(self):
        """
        :returns: The unique sid that identifies this account
        :rtype: str
        """
        return self._properties['account_sid']

    @property
    def call_sid(self):
        """
        :returns: The call_sid
        :rtype: str
        """
        return self._properties['call_sid']

    @property
    def date_created(self):
        """
        :returns: The date this resource was created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The date this resource was last updated
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def friendly_name(self):
        """
        :returns: A human readable description for this resource
        :rtype: str
        """
        return self._properties['friendly_name']

    @property
    def phone_number(self):
        """
        :returns: The incoming phone number
        :rtype: str
        """
        return self._properties['phone_number']

    @property
    def sid(self):
        """
        :returns: A string that uniquely identifies this outgoing-caller-ids
        :rtype: str
        """
        return self._properties['sid']

    @property
    def uri(self):
        """
        :returns: The URI for this resource
        :rtype: str
        """
        return self._properties['uri']

    @property
    def validation_code(self):
        """
        :returns: The validation_code
        :rtype: str
        """
        return self._properties['validation_code']

    def fetch(self):
        """
        Fetch a OutgoingCallerIdInstance
        
        :returns: Fetched OutgoingCallerIdInstance
        :rtype: OutgoingCallerIdInstance
        """
        return self._context.fetch()

    def update(self, friendly_name=values.unset):
        """
        Update the OutgoingCallerIdInstance
        
        :param str friendly_name: A human readable description of the caller ID
        
        :returns: Updated OutgoingCallerIdInstance
        :rtype: OutgoingCallerIdInstance
        """
        return self._context.update(
            friendly_name=friendly_name,
        )

    def delete(self):
        """
        Deletes the OutgoingCallerIdInstance
        
        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._context.delete()

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._kwargs.items())
        return '<Twilio.Api.V2010.OutgoingCallerIdInstance {}>'.format(context)
