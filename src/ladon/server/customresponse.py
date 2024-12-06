# -*- coding: utf-8 -*-


class CustomResponse(object):
    """
    In some cases it can be nessecary to override the normal response system and return
    something completely different - ie. 
    1. if a certain method should return a file as a http attachment response for
       browsers (Content-Disposition: attachment;).
    2. or a commandline tool that sends a SOAP request and should output raw text as
       result
    Objects of CustomResponse descendents are intercepted in the wsgi_application part
    so the service developer has full control over response headers and data.
    """

    def response_headers(self):
        """
        response_headers must return a list of tuple-pairs that will constitute the response
        headers. An example::
            return [
                ('Content-Disposition', 'attachment; filename="%s"' % self.filename),
                ('Content-Type', 'application/force-download'),
                ('Content-Length', str(self.filesize))
            ]
        """
        raise NotImplementedError(
            "CustomResponse.response_headers must be specialized")

    def response_data(self):
        """
        response_data is the data part of the response, and must be raw data (str in Python 2,
        bytes in Python 3). Iterator objects are also accepted and should be used when responses
        consist of very large data parts. For instance if the response data is a large file it
        should be returned as a iterator that is generated by reading chunks from a file object::
            self.output = open('/path/to/very/large/file.zip','rb')
            block_size = 4096
            return iter(lambda: output.read(block_size), '')

        """
        raise NotImplementedError(
            "CustomResponse.response_data must be specialized")