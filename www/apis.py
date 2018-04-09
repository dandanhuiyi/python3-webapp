'''
JSON API definition
'''

import json, logging, inspect, functools

# class Page(object):
#     '''
#     Page object for display pages.
#     '''
#     def __init__(self, item_count, page_index=1, page_size=10):
#         '''
#         Init pagination by item_count, page_index, page_size.
#         '''
#         >>> p1 = Page(100,1)
#         >>> p1.page_count
#         10
#         >>> p1.offset


class APIError(Exception):
    '''
    the base APIError which contains error(required), data(optional) and message(optional).
    '''

    def __init__(self, error, data='', message=''):
        super(APIError, self).__init__(message)
        self.error = error
        self.data = data
        self.message = message

class APIValueError(APIError):
    '''
    Indicate the input value has error or invalid. The data specifies the resource name.
    '''
    def __init__(self, field, message=''):
        super(APIValueError, self).__init__('value:invalid',field, message)

class APIResourceNotFoundError(APIError):
    '''
    Indicate the resource was not found. The data specifies the resource name.
    '''
    def __init__(self, field, message=''):
        super(APIResourceNotFoundError, self).__init__('value:notfound', field, message)

class APIPermissionError(APIError):
    '''
    Indicate the api has no permission
    '''
    def __init__(self, message=''):
        super(APIPermissionError, self).__init__('permission:forbidden', 'permission', message)

if __name__ == '__main__':
    import doctest
    doctest.testmod()