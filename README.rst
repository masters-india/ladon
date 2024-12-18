Description
===========

Ladon is a framework for exposing python methods to several internet service
protocols. Once a method is ladonized it is automatically served through all
the interfaces that your ladon installation contains. Ladon is easily extendable.
Adding a new service interface is as easy as adding a single module containing
a class inheriting the BaseInterface class.

Documentation: http://ladon.readthedocs.io/en/latest/

Example
-------
::

	from ladon.ladonizer import ladonize

	class Calculator(object):
		"""
		This service does the math, and serves as example for new potential Ladon users.
		In-line documentation ends up in the web service online browsable API
		"""
		@ladonize(int,int,rtype=int)
		def add(self,a,b):
			"""
			Add two integers together and return the result

			@param a: 1st integer
			@param b: 2nd integer
			@rtype: The result of the addition
			"""
			return a+b
    
Features
--------
- Expose your existing Python code with the @ladonize decorator
- Support for Python 2 and Python 3
- Support for multiple web service protocols
- Autogenerated documetation based on in-line documentation
- Autogenerated service descriptions (WSDL, JSON-WSP/description)
- Web service API Browsing
	- Access your service and it's documentation via a web browser
	- Theming support for the API Browser by adding custom skins
	- Default skin "bluebox" supports direct web service method testing via the browser
- JSON-WSP support - ideal for AJAX backend
- Run web service methods in background with no effort by using Ladon tasks

What does Ladon mean?
---------------------
Ladon is a serpent-like dragon from Greek mythology which might be given multiple
heads, a hundred in Aristophanes' The Frogs (a passing remark in line 475). each
head might speak with different voices.

.. image:: https://github.com/masters-india/ladon/raw/master/logos/ladon2_button.jpg

Like Ladon the dragon has many heads that speak with different voices Ladon the
Web Service has many interfaces that communicate with different protocols. Ladon
the dragon only has one body - users only need to implement their service
classes once.
