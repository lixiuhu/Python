import sys
import wmi

if __name__ == "__main__":
    wmiService = wmi.WMI()
    colNicConfigs = wmiService.Win32_NetworkAdapterConfiguration(IPEnabled = True)

    if len(colNicConfigs) < 1:
        print "Can not get network configuration"
        exit()

    objNicConfig = colNicConfigs[0]

    val = objNicConfig.EnableDHCP()
    print val
    val = objNicConfig.SetDNSServerSearchOrder()
    print val

    print 'ip: ', ', '.join(objNicConfig.IPAddress)