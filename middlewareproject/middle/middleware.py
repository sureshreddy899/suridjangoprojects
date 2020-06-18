class ExecutionFlowMiddleware(object):
    """docstring for ExecutionFlowMiddleware."""

    def __init__(self, get_response):
        self.get_response=get_response

    def __call__(self,request):
        print('This is printed at pre-processing of request')
        response=self.get_response(request)
        print('This line printed at post-processing of request')
        return response


from django.http import HttpResponse

class AppMaintenanceMiddleware(object):

    def __init__(self,get_response):
        self.get_response=get_response

    def __call__(self,request):
        return HttpResponse('<h1> Application is Under Maintainance ... Please try after some time...</h1>')

class ErrorMessageMiddleware(object):

    def __init__(self,get_response):
        self.get_response=get_response

    def __call__(self,request):
        response=self.get_response(request)
        return response

    def process_exception(self,request,exception):
        s1='<h1> Currently we are experiencing some Error Please try after some time.....</h1>'
        s2='<h2> Raised Exception:{}</h2>'.format(exception.__class__.__name__)
        s3='<h3> Exception Description/Message:{}</h3>'.format(exception)
        return HttpResponse(s1+s2+s3)
