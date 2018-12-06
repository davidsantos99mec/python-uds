#!/usr/bin/env python

__author__ = "Richard Clubb"
__copyrights__ = "Copyright 2018, the python-uds project"
__credits__ = ["Richard Clubb"]

__license__ = "MIT"
__maintainer__ = "Richard Clubb"
__email__ = "richard.clubb@embeduk.com"
__status__ = "Development"


from uds.uds_config_tool.SupportedServices.iContainer import iContainer
from types import MethodType


class ECUResetContainer(object):

    __metaclass__ = iContainer

    def __init__(self):
        self.requestFunctions = {}
        self.checkFunctions = {}
        self.negativeResponseFunctions = {}
        self.positiveResponseFunctions = {}

    ##
    # @brief this method is bound to an external Uds object, referenced by target, so that it can be called
    # as one of the in-built methods. uds.ecuReset("something","something else") It does not operate
    # on this instance of the container class.
    @staticmethod
    def __ecuReset(target, parameter, suppressResponse=False, **kwargs):

        # Note: ecuReset does not show support for multiple DIDs in the spec, so this is handling only a single DID with data record.
        requestFunction = target.ecuResetContainer.requestFunctions[parameter]
        checkFunction = target.ecuResetContainer.checkFunctions[parameter]
        negativeResponseFunction = target.ecuResetContainer.negativeResponseFunctions[parameter]
        positiveResponseFunction = target.ecuResetContainer.positiveResponseFunctions[parameter]

        # Call the sequence of functions to execute the ECU Reset request/response action ...
        # ==============================================================================

        # Create the request. Note: we do not have to pre-check the dataRecord as this action is performed by 
        # the recipient (the response codes 0x?? and 0x?? provide the necessary cover of errors in the request) ...
        request = requestFunction(suppressResponse)

        if checkFunction is None or positiveResponseFunction is None:
            suppressResponse = True

        if suppressResponse == False:
            # Send request and receive the response ...
            response = target.send(request,responseRequired=True) # ... this returns a single response
            negativeResponseFunction(response)  # ... throws an exception to be handled at a higher level if a negative response is received

            # We have a positive response so check that it makes sense to us ...
            checkFunction(response)

            # All is still good, so return the response (currently this function does nothing, but including it here as a hook in case that changes) ...
            return positiveResponseFunction(response)
			
		# ... else ...
        # Send request and receive the response ...
        response = target.send(request,responseRequired=False) # ... this suppresses any response handling (not expected)
        return

    def bind_function(self, bindObject):
        bindObject.ecuReset = MethodType(self.__ecuReset, bindObject)

    def add_requestFunction(self, aFunction, dictionaryEntry):
        self.requestFunctions[dictionaryEntry] = aFunction

    def add_checkFunction(self, aFunction, dictionaryEntry):
        self.checkFunctions[dictionaryEntry] = aFunction

    def add_negativeResponseFunction(self, aFunction, dictionaryEntry):
        self.negativeResponseFunctions[dictionaryEntry] = aFunction

    def add_positiveResponseFunction(self, aFunction, dictionaryEntry):
        self.positiveResponseFunctions[dictionaryEntry] = aFunction