import sys
import urllib
import urlparse
import xbmcgui
import xbmcplugin
import xbmcaddon, util

base_url = sys.argv[0]
addon_handle = int(sys.argv[1])
args = urlparse.parse_qs(sys.argv[2][1:])

addon = xbmcaddon.Addon('plugin.video.pbstream')
icon = addon.getAddonInfo('icon')
title = addon.getAddonInfo('name')
MyTVDemo_DBox = 'https://dl.dropboxusercontent.com/s/jn1o4c1y796x64m/MyTVDemo.mp4?dl=0'

#util.playMedia(title, icon, MyTVDemo_YTube)
#video_id = 'yBFXhPfVHmc&list=PLeXfhADycn_MONok_zviLmBk-YAWg0Ij6'
##MySongList = 'plugin://plugin.video.youtube/?action=play_video&videoid=%s' % video_id
#util.playMedia('MySongList', icon, MySongList)

xbmcplugin.setContent(addon_handle, 'movies')

def build_url(query):
    return base_url + '?' + urllib.urlencode(query)

mode = args.get('mode', None)

if mode is None:
    url = build_url({'mode': 'folder', 'foldername': 'Folder One'})
    li = xbmcgui.ListItem('Demo', iconImage='DefaultFolder.png')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True)

    url = build_url({'mode': 'folder', 'foldername': 'Folder Two'})
    li = xbmcgui.ListItem('My Songs', iconImage='DefaultFolder.png')
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=True)

    xbmcplugin.endOfDirectory(addon_handle)

elif mode[0] == 'folder':
    foldername = args['foldername'][0]
    if (foldername == "Folder One"):
    	video_id = 'fsw8kK_tLnc'
    	MyTVDemo_YTube = 'plugin://plugin.video.youtube/?action=play_video&videoid=%s' % video_id
    	util.playMedia("PBStream Demo", icon, MyTVDemo_YTube)
    	#li = xbmcgui.ListItem(label="PBStream Demo", iconImage=icon, thumbnailImage=icon, path=MyTVDemo_YTube)
    	#li.setInfo(type="Video", infoLabels={ "Title": "PBStream Demo" })
    	#xbmcplugin.addDirectoryItem(handle=addon_handle, url=MyTVDemo_YTube, listitem=li)
    	#xbmcplugin.endOfDirectory(addon_handle)
    if (foldername == "Folder Two"):
    	video_id = 'yBFXhPfVHmc&list=PLeXfhADycn_MONok_zviLmBk-YAWg0Ij6'
    	MySongList = 'plugin://plugin.video.youtube/?action=play_video&videoid=%s' % video_id
    	util.playMedia("MySongList", icon, MySongList)
    	#xbmcplugin.endOfDirectory(addon_handle)