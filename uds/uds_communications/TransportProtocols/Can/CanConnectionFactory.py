import can
from can.interfaces import pcan
from uds.uds_configuration.Config import Config
from os import path
#from uds import CanConnection
from uds.uds_communications.TransportProtocols.Can.CanConnection import CanConnection

from typing import Dict
from platform import system
if system() == "Linux":
    from can.interfaces import socketcan

class CanConnectionFactory(object):

    connections = {}
    config = None

    @staticmethod
    def __call__(callback=None, filter=None, configPath=None, **kwargs):
        
        connectionType = 'can0_250'
        baudrate = 250000
        channel = "can0"
        interface = "socketcan"
        connectionName = "can0"
        
        #CanConnectionFactory.loadConfiguration(configPath)
        CanConnectionFactory.checkKwargs(**kwargs)
        #connectionType =  kwargs['interface']
        #baudrate = kwargs['baudrate']
        #channel = kwargs['channel']

        # check config file and load
        #connectionType = CanConnectionFactory.config['can']['interface']
        
        channel = CanConnectionFactory.channel
        baudrate = CanConnectionFactory.baudrate
        interface = CanConnectionFactory.interface
        connectionType = interface
        #if connectionType == 'virtual':
        #    connectionName = CanConnectionFactory.config['virtual']['interfaceName']
        #    if connectionName not in CanConnectionFactory.connections:
        #        CanConnectionFactory.connections[connectionName] = CanConnection(callback, filter,
        #                                                                         can.interface.Bus(connectionName,
        #                                                                             bustype='virtual'))
        #    else:
        #        CanConnectionFactory.connections[connectionName].addCallback(callback)
        #        CanConnectionFactory.connections[connectionName].addFilter(filter)
        #    return CanConnectionFactory.connections[connectionName]

        if connectionType == 'socketcan':
            connectionName = channel
            if connectionName not in CanConnectionFactory.connections:
                CanConnectionFactory.connections[connectionName] = CanConnection(callback, filter,
                                                                                 can.interface.Bus(connectionName,
                                                                                     interface = connectionType, bitrate = str(baudrate)))
            else:
                CanConnectionFactory.connections[connectionName].addCallback(callback)
                CanConnectionFactory.connections[connectionName].addFilter(filter)
            return CanConnectionFactory.connections[connectionName]
        
        if connectionType == 'can0_250':
            connectionName = CanConnectionFactory.config['can0_250']['channel']
            if connectionName not in CanConnectionFactory.connections:
                CanConnectionFactory.connections[connectionName] = CanConnection(callback, filter,
                                                                                 can.interface.Bus(connectionName,
                                                                                     interface = "socketcan", bitrate = "250000"))
            else:
                CanConnectionFactory.connections[connectionName].addCallback(callback)
                CanConnectionFactory.connections[connectionName].addFilter(filter)
            return CanConnectionFactory.connections[connectionName]

        elif connectionType == 'can0_500':
            connectionName = CanConnectionFactory.config['can0_500']['channel']
            if connectionName not in CanConnectionFactory.connections:
                CanConnectionFactory.connections[connectionName] = CanConnection(callback, filter,
                                                                                 can.interface.Bus(connectionName,
                                                                                     interface = "socketcan", bitrate = "500000"))
            else:
                CanConnectionFactory.connections[connectionName].addCallback(callback)
                CanConnectionFactory.connections[connectionName].addFilter(filter)
            return CanConnectionFactory.connections[connectionName]

        elif connectionType == 'can0_1000':
            connectionName = CanConnectionFactory.config['can0_1000']['channel']
            if connectionName not in CanConnectionFactory.connections:
                CanConnectionFactory.connections[connectionName] = CanConnection(callback, filter,
                                                                                 can.interface.Bus(connectionName,
                                                                                     interface = "socketcan", bitrate = "1000000"))
            else:
                CanConnectionFactory.connections[connectionName].addCallback(callback)
                CanConnectionFactory.connections[connectionName].addFilter(filter)
            return CanConnectionFactory.connections[connectionName]

        elif connectionType == 'can1_250':
            connectionName = CanConnectionFactory.config['can1_250']['channel']
            if connectionName not in CanConnectionFactory.connections:
                CanConnectionFactory.connections[connectionName] = CanConnection(callback, filter,
                                                                                 can.interface.Bus(connectionName,
                                                                                     interface = "socketcan", bitrate = "250000"))
            else:
                CanConnectionFactory.connections[connectionName].addCallback(callback)
                CanConnectionFactory.connections[connectionName].addFilter(filter)
            return CanConnectionFactory.connections[connectionName]

        elif connectionType == 'can1_500':
            connectionName = CanConnectionFactory.config['can1_500']['channel']
            if connectionName not in CanConnectionFactory.connections:
                CanConnectionFactory.connections[connectionName] = CanConnection(callback, filter,
                                                                                 can.interface.Bus(connectionName,
                                                                                     interface = "socketcan", bitrate = "500000"))
            else:
                CanConnectionFactory.connections[connectionName].addCallback(callback)
                CanConnectionFactory.connections[connectionName].addFilter(filter)
            return CanConnectionFactory.connections[connectionName]

        elif connectionType == 'can1_1000':
            connectionName = CanConnectionFactory.config['can1_1000']['channel']
            if connectionName not in CanConnectionFactory.connections:
                CanConnectionFactory.connections[connectionName] = CanConnection(callback, filter,
                                                                                 can.interface.Bus(connectionName,
                                                                                     interface = "socketcan", bitrate = "1000000"))
            else:
                CanConnectionFactory.connections[connectionName].addCallback(callback)
                CanConnectionFactory.connections[connectionName].addFilter(filter)
            return CanConnectionFactory.connections[connectionName]

        elif connectionType == 'pcan_250':
        #    channel = CanConnectionFactory.config['peak']['device']
            if channel not in CanConnectionFactory.connections:
        #        baudrate = CanConnectionFactory.config['can']['baudrate']
                CanConnectionFactory.connections[channel] = CanConnection(callback, filter,
                                                                          pcan.PcanBus(channel,
                                                                          bitrate=int(baudrate)))
            else:
                CanConnectionFactory.connections[channel].addCallback(callback)
                CanConnectionFactory.connections[channel].addFilter(filter)
                
            return CanConnectionFactory.connections[channel]
        elif connectionType == 'pcan_500':
        #    channel = CanConnectionFactory.config['peak']['device']
            if channel not in CanConnectionFactory.connections:
        #        baudrate = CanConnectionFactory.config['can']['baudrate']
                CanConnectionFactory.connections[channel] = CanConnection(callback, filter,
                                                                          pcan.PcanBus(channel='PCAN_USBBUS1',
                                                                          bitrate=500000))
            else:
                CanConnectionFactory.connections[channel].addCallback(callback)
                CanConnectionFactory.connections[channel].addFilter(filter)
                
            return CanConnectionFactory.connections[channel]
        elif connectionType == 'pcan_1000':
        #    channel = CanConnectionFactory.config['peak']['device']
            if channel not in CanConnectionFactory.connections:
        #        baudrate = CanConnectionFactory.config['can']['baudrate']
                CanConnectionFactory.connections[channel] = CanConnection(callback, filter,
                                                                          pcan.PcanBus(channel='PCAN_USBBUS1',
                                                                          bitrate=1000000))
            else:
                CanConnectionFactory.connections[channel].addCallback(callback)
                CanConnectionFactory.connections[channel].addFilter(filter)
                
            return CanConnectionFactory.connections[channel]
        
        elif connectionType == 'pcan':
            #channel = CanConnectionFactory.config['peak']['device']
            if channel not in CanConnectionFactory.connections:
            #    baudrate = CanConnectionFactory.config['can']['baudrate']
                CanConnectionFactory.connections[channel] = CanConnection(callback, filter,
                                                                          pcan.PcanBus(channel,
                                                                          bitrate=int(baudrate)))
            else:
                CanConnectionFactory.connections[channel].addCallback(callback)
                CanConnectionFactory.connections[channel].addFilter(filter)
                
            return CanConnectionFactory.connections[channel]
        
        #elif connectionType == 'pcan':
        #    #channel = CanConnectionFactory.config['peak']['device']
        #    if channel not in CanConnectionFactory.connections:
        #    #    baudrate = CanConnectionFactory.config['can']['baudrate']
        #        CanConnectionFactory.connections[channel] = CanConnection(callback, filter,
        #                                                                  can.ThreadSafeBus(connectionType,channel,
        #                                                                  bitrate=int(baudrate)))
        #    else:
        #        CanConnectionFactory.connections[channel].addCallback(callback)
        #        CanConnectionFactory.connections[channel].addFilter(filter)

        #elif connectionType == 'vector':
        #    channel = int(CanConnectionFactory.config['vector']['channel'])
        #    app_name = CanConnectionFactory.config['vector']['appName']
        #    connectionKey = str("{0}_{1}").format(app_name, channel)
        #    if connectionKey not in CanConnectionFactory.connections:
        #        baudrate = int(CanConnectionFactory.config['can']['baudrate'])
        #        CanConnectionFactory.connections[connectionKey] = CanConnection(callback, filter,
        #                                                                        vector.VectorBus(channel,
        #                                                                            app_name=app_name,
        #                                                                            data_bitrate=baudrate))
        #    else:
        #        CanConnectionFactory.connections[connectionKey].addCallback(callback)
        #        CanConnectionFactory.connections[connectionKey].addFilter(filter)
        #    return CanConnectionFactory.connections[connectionKey]

    @staticmethod
    def loadConfiguration(configPath=None):

        CanConnectionFactory.config = Config()

        localConfig = path.dirname(__file__) + "/config.ini"
        CanConnectionFactory.config.read(localConfig)

        if configPath is not None:
            if path.exists(configPath):
                CanConnectionFactory.config.read(configPath)
            else:
                raise FileNotFoundError("Can not find config file")

    @staticmethod
    def checkKwargs(**kwargs):

        if 'interface' in kwargs:
            #CanConnectionFactory.config['can']['interface'] = kwargs['interface']
            CanConnectionFactory.interface = kwargs['interface']

        if 'baudrate' in kwargs:
            #CanConnectionFactory.config['can']['baudrate'] = kwargs['baudrate']
            CanConnectionFactory.baudrate = kwargs['baudrate']

        #if 'device' in kwargs:
        #    CanConnectionFactory.config['peak']['device'] = kwargs['device']

        #if 'appName' in kwargs:
        #    CanConnectionFactory.config['vector']['appName'] = kwargs['appName']

        if 'channel' in kwargs:
            #CanConnectionFactory.config['vector']['channel'] = kwargs['channel']
            #CanConnectionFactory.config['socketcan']['channel'] = kwargs['channel']
            CanConnectionFactory.channel = kwargs['channel']

