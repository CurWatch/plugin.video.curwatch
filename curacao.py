import sys
import xbmcgui
import xbmcplugin

addon_handle = int(sys.argv[1])

xbmcplugin.setContent(addon_handle, 'movies')

url = 'http://cba.cdn.cur.watch/mystream.m3u8'
li = xbmcgui.ListItem('CBA Television', iconImage='http://cur.watch/images/kodi_icon.png')
fanart = "http://cur.watch/images/kodi_fanart.jpg"
li.setProperty('fanart_image', fanart)
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://tc.cdn.cur.watch/mystream.m3u8'
li = xbmcgui.ListItem('TeleCuracao', iconImage='http://cur.watch/images/kodi_icon.png')
fanart = "http://cur.watch/images/kodi_fanart.jpg"
li.setProperty('fanart_image', fanart)
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://rtv7.cdn.cur.watch/mystream.m3u8'
li = xbmcgui.ListItem('Rtv-7', iconImage='http://cur.watch/images/kodi_icon.png')
fanart = "http://cur.watch/images/kodi_fanart.jpg"
li.setProperty('fanart_image', fanart)
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

url = 'http://panchito13.flashmediacast.com:2087/live/livestream/playlist.m3u8'
li = xbmcgui.ListItem('NOS TV (Bonaire)', iconImage='http://cur.watch/images/kodi_icon.png')
fanart = "http://cur.watch/images/kodi_fanart.jpg"
li.setProperty('fanart_image', fanart)
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

xbmcplugin.endOfDirectory(addon_handle)