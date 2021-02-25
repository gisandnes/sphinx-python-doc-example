from typing import Optional

class SimpleBleDevice(object):
    """This is a conceptual class representation of a simple BLE device
    (GATT Server). It is essentially an extended combination of the
    :class:`bluepy.btle.Peripheral` and :class:`bluepy.btle.ScanEntry` classes

    Args:
        client:     A handle to the :class:`simpleble.SimpleBleClient` client
                    object that detected the device
        addr:       Device MAC address, defaults to None`
        addrType:   Device address type - one of ADDR_TYPE_PUBLIC or
                    ADDR_TYPE_RANDOM, defaults to ADDR_TYPE_PUBLIC
        iface:      Bluetooth interface number (0 = `/dev/hci0`) used for the
                    connection, defaults to 0
        data:
        rssi:
        connectable:
        updateCount:
    """


    def __init__(self, client, addr: Optional[str] = None, addrType: Optional[str] = None, iface: Optional[int] = 0,
                 data=None, rssi=0, connectable=False, updateCount=0):
        """Constructor method
        """
        super().__init__(deviceAddr=None, addrType=addrType, iface=iface)
        self.addr = addr
        self.addrType = addrType
        self.iface = iface
        self.rssi = rssi
        self.connectable = connectable
        self.updateCount = updateCount
        self.data = data
        self._connected = False
        self._services = []
        self._characteristics = []
        self._client = client


