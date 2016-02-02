import sys
import xbmcgui
import xbmcplugin

addon_handle = int(sys.argv[1])

xbmcplugin.setContent(addon_handle, 'movies')
#CBA Television
url = 'http://cba.cdn.cur.watch/mystream.m3u8'
li = xbmcgui.ListItem('CBA Television', iconImage='https://cur.watch/images/kodi_icon.png')
fanart = "https://cur.watch/images/kodi_fanart.jpg"
li.setProperty('fanart_image', fanart)
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
# Telecuracao
url = 'http://tc.cdn.cur.watch/mystream.m3u8'
li = xbmcgui.ListItem('TeleCuracao', iconImage='https://cur.watch/images/kodi_icon.png')
fanart = "https://cur.watch/images/kodi_fanart.jpg"
li.setProperty('fanart_image', fanart)
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
# Rtv7
url = 'http://rtv7.cdn.cur.watch/mystream.m3u8'
li = xbmcgui.ListItem('Rtv-7', iconImage='https://cur.watch/images/kodi_icon.png')
fanart = "https://cur.watch/images/kodi_fanart.jpg"
li.setProperty('fanart_image', fanart)
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
#NOS TV
url = 'http://panchito13.flashmediacast.com:2087/live/livestream/playlist.m3u8'
li = xbmcgui.ListItem('NOS TV (Bonaire)', iconImage='https://cur.watch/images/kodi_icon.png')
fanart = "http://cur.watch/images/kodi_fanart.jpg"
li.setProperty('fanart_image', fanart)
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
# Telenotisia
url = 'https://cur.watch/api/last_episode/telenotisia/kodi.mp4'
li = xbmcgui.ListItem('VOD: Telenotisia', iconImage='https://cur.watch/roku/show_telenotisia.jpg')
fanart = "https://cur.watch/images/kodi_fanart.jpg"
li.setProperty('fanart_image', fanart)
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
# E Notisia
url = 'https://cur.watch/api/last_episode/e-notisia/kodi.mp4'
li = xbmcgui.ListItem('VOD: E Notisia', iconImage='https://cur.watch/roku/show_e-notisia.jpg')
fanart = "https://cur.watch/images/kodi_fanart.jpg"
li.setProperty('fanart_image', fanart)
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

xbmcplugin.endOfDirectory(addon_handle)