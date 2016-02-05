import sys
import xbmcgui
import xbmcplugin

addon_handle = int(sys.argv[1])

xbmcplugin.setContent(addon_handle, 'movies')
#CBA Television
url = 'http://cba.cdn.cur.watch/mystream.m3u8'
li = xbmcgui.ListItem('[COLOR yellow]LIVE[/COLOR] CBA Television', iconImage='https://cur.watch/images/kodi_icon.png')
fanart = "https://cur.watch/images/kodi_fanart.jpg"
li.setProperty('fanart_image', fanart)
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
# Telecuracao
url = 'http://tc.cdn.cur.watch/mystream.m3u8'
li = xbmcgui.ListItem('[COLOR yellow]LIVE[/COLOR] Telecuracao', iconImage='https://cur.watch/images/kodi_icon.png')
fanart = "https://cur.watch/images/kodi_fanart.jpg"
li.setProperty('fanart_image', fanart)
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
# TCFM
url = 'http://cdn6.iviplanet.com:1935/UTS/myStream.sdp/playlist.m3u8'
li = xbmcgui.ListItem('[COLOR yellow]LIVE[/COLOR] TCFM (Telecuracao FM)', iconImage='https://cur.watch/images/kodi_icon.png')
fanart = "https://cur.watch/images/kodi_fanart.jpg"
li.setProperty('fanart_image', fanart)
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
# Rtv7
url = 'http://rtv7.cdn.cur.watch/mystream.m3u8'
li = xbmcgui.ListItem('[COLOR yellow]LIVE[/COLOR] Rtv-7', iconImage='https://cur.watch/images/kodi_icon.png')
fanart = "https://cur.watch/images/kodi_fanart.jpg"
li.setProperty('fanart_image', fanart)
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
# TV Direct 13
url = 'http://livestream.5centscdn.com/tvdirect13live_mbt/tvd13001.stream/playlist.m3u8'
li = xbmcgui.ListItem('[COLOR yellow]LIVE[/COLOR] TV Direct 13', iconImage='https://cur.watch/images/kodi_icon.png')
fanart = "https://cur.watch/images/kodi_fanart.jpg"
li.setProperty('fanart_image', fanart)
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
# TV Direct 13  HD
url = 'http://livestream.5centscdn.com/tvdirect13live/dfd4c30108856fab7a1b3ef38ca653b1.sdp/playlist.m3u8'
li = xbmcgui.ListItem('[COLOR yellow]LIVE[/COLOR] TV Direct 13 [COLOR red]HD[/COLOR] ', iconImage='https://cur.watch/images/kodi_icon.png')
fanart = "https://cur.watch/images/kodi_fanart.jpg"
li.setProperty('fanart_image', fanart)
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
#NOS TV
url = 'http://panchito13.flashmediacast.com:2087/live/livestream/playlist.m3u8'
li = xbmcgui.ListItem('[COLOR yellow]LIVE[/COLOR] NOS TV (Bonaire)', iconImage='https://cur.watch/images/kodi_icon.png')
fanart = "http://cur.watch/images/kodi_fanart.jpg"
li.setProperty('fanart_image', fanart)
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
# Telenotisia
url = 'https://cur.watch/api/last_episode/telenotisia/kodi.mp4'
li = xbmcgui.ListItem('[COLOR yellow]VOD[/COLOR] Telenotisia', iconImage='https://cur.watch/roku/show_telenotisia.jpg')
fanart = "https://cur.watch/images/kodi_fanart.jpg"
li.setProperty('fanart_image', fanart)
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)
# E Notisia
url = 'https://cur.watch/api/last_episode/e-notisia/kodi.mp4'
li = xbmcgui.ListItem('[COLOR yellow]VOD[/COLOR] E Notisia', iconImage='https://cur.watch/roku/show_e-notisia.jpg')
fanart = "https://cur.watch/images/kodi_fanart.jpg"
li.setProperty('fanart_image', fanart)
xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li)

xbmcplugin.endOfDirectory(addon_handle)