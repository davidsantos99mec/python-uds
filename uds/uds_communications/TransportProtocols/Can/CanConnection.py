#!/usr/bin/env python

__author__ = "David Hayward"
__copyrights__ = "Copyright 2019, the python-uds project"
__credits__ = ["David Hayward"]

__license__ = "MIT"
__maintainer__ = "Richard Clubb"
__email__ = "richard.clubb@embeduk.com"
__status__ = "Development"


import can

##
# @brief Small class to wrap the CAN Bus/Notifier/Listeners to allow multiple clients for each bus/connection
class CanConnection(object):

    def __init__(self, callback, filter, bus):
        self.__bus: can.interface.Bus = bus
        self.__notifier = can.Notifier(self.__bus, [callback], 1.0)
        self.__listeners = [callback]
        self.addFilter(filter)

    ##
    # @brief Adds call back (via additional listener) to the notifier which is attached to this bus
    def addCallback(self, callback):
        self.__notifier.add_listener(callback)
        self.__listeners.append(callback)

    ##
    # @brief Adds a filter (CAN Msg Id) to the bus to allow messages through to the callback
    def addFilter(self, filtersRaw):
        filtersProcessed=filtersRaw[1:-1].split(', ')
        filters = self.__bus.filters
        for i in filtersProcessed:
            filter=int(i)
            if filters is not None:
                if filter<=2047:
                    filters.append({"can_id": filter, "can_mask": 0xFFF, "extended": False})
                else:
                    filters.append({"can_id": filter, "can_mask": 0x1FFFFFFF, "extended": True})
            else:            
                if filter<=2047:
                    filters=[{"can_id": filter, "can_mask": 0xFFF, "extended": False}]
                else:
                    filters = [{"can_id": filter, "can_mask": 0x1FFFFFFF, "extended": True}]            
        self.__bus.set_filters(filters)

    ##
    # @brief transmits the data over can using can connection
    def transmit(self, data, reqId, extended=False):
        if reqId>2047:
            extended=True
        canMsg = can.Message(arbitration_id=reqId, is_extended_id=extended)
        canMsg.dlc = len(data)

        canMsg.data = data

        self.__bus.send(canMsg)

    def close(self):
        self.__notifier.stop()
        [listener.stop() for listener in self.__listeners]
        self.__bus.shutdown()

