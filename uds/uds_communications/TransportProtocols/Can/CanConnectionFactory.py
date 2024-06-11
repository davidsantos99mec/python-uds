import can
from can.interfaces import pcan, vector
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

        CanConnectionFactory.loadConfiguration(configPath)
        CanConnectionFactory.checkKwargs(**kwargs)

        # check config file and load
        connectionType = CanConnectionFactory.config['can']['interface']

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

        elif connectionType == 'peak_250':
            channel = CanConnectionFactory.config['peak']['device']
            if channel not in CanConnectionFactory.connections:
        #        baudrate = CanConnectionFactory.config['can']['baudrate']
                CanConnectionFactory.connections[channel] = CanConnection(callback, filter,
                                                                          pcan.PcanBus(channel='PCAN_USBBUS1',
                                                                          bitrate=250000))
            else:
                CanConnectionFactory.connections[channel].addCallback(callback)
                CanConnectionFactory.connections[channel].addFilter(filter)
                
            return CanConnectionFactory.connections[channel]
        elif connectionType == 'peak_500':
            channel = CanConnectionFactory.config['peak']['device']
            if channel not in CanConnectionFactory.connections:
        #        baudrate = CanConnectionFactory.config['can']['baudrate']
                CanConnectionFactory.connections[channel] = CanConnection(callback, filter,
                                                                          pcan.PcanBus(channel='PCAN_USBBUS1',
                                                                          bitrate=500000))
            else:
                CanConnectionFactory.connections[channel].addCallback(callback)
                CanConnectionFactory.connections[channel].addFilter(filter)
                
            return CanConnectionFactory.connections[channel]
        elif connectionType == 'peak_1000':
            channel = CanConnectionFactory.config['peak']['device']
            if channel not in CanConnectionFactory.connections:
        #        baudrate = CanConnectionFactory.config['can']['baudrate']
                CanConnectionFactory.connections[channel] = CanConnection(callback, filter,
                                                                          pcan.PcanBus(channel='PCAN_USBBUS1',
                                                                          bitrate=1000000))
            else:
                CanConnectionFactory.connections[channel].addCallback(callback)
                CanConnectionFactory.connections[channel].addFilter(filter)
                
            return CanConnectionFactory.connections[channel]
        
        #elif connectionType == 'peak':
        #    channel = CanConnectionFactory.config['peak']['device']
        #    if channel not in CanConnectionFactory.connections:
        #        baudrate = CanConnectionFactory.config['can']['baudrate']
        #        CanConnectionFactory.connections[channel] = CanConnection(callback, filter,
        #                                                                  pcan.PcanBus(channel,
        #                                                                  bitrate=baudrate))
        #    else:
        #        CanConnectionFactory.connections[channel].addCallback(callback)
        #        CanConnectionFactory.connections[channel].addFilter(filter)
                
        #    return CanConnectionFactory.connections[channel]

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
            CanConnectionFactory.config['can']['interface'] = kwargs['interface']

        if 'baudrate' in kwargs:
            CanConnectionFactory.config['can']['baudrate'] = kwargs['baudrate']

        if 'device' in kwargs:
            CanConnectionFactory.config['peak']['device'] = kwargs['device']

        if 'appName' in kwargs:
            CanConnectionFactory.config['vector']['appName'] = kwargs['appName']

        if 'channel' in kwargs:
            CanConnectionFactory.config['vector']['channel'] = kwargs['channel']
            CanConnectionFactory.config['socketcan']['channel'] = kwargs['channel']

