import urllib
ALARM_NONE        = 0
ALARM_FOOD        = 1
ALARM_FIRE        = 2
CHANGE_NAME       = 'na'
CHANGE_ALARM      = 'al'
CHANGE_TEMP       = 'ta'
CHANGE_ALARM_HIGH = 'th'
CHANGE_ALARM_LOW  = 'tl'
CHANGE_BLOWER     = 'sw'

class Stoker:
  
  def __init__(self, stoker):
    """Constructor for the Stoker encapsulation.
    
    Args:
      stoker: The address (IP or hostname) of the stoker
    """
    self.stoker_address = stoker
    url = 'http://%s/index.html'
    stokerdata = urllib.urlopen(url)
    

  
  def ChangeStoker(self, action, serial, value):
    """Send a POST to the stoker to modify its configuration
  
    Args:
      action: The setting to change
      serial: The serial number of the sensor to change
      value:  The value that will be set
    Returns:
      a urllib request, which contains the response data
    """
    url = 'http://%s/stoker.Post_Handler' % (self.stoker_address)
    action = '%s%s' % (action, serial)
    data = urllib.urlencode([(action, value)])
    request = urllib.urlopen(url, data=data)
    return request
  