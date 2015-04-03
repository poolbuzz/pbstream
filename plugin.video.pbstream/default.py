import xbmcaddon, util

addon = xbmcaddon.Addon('plugin.video.pbstream')

util.playMedia(addon.getAddonInfo('name'), addon.getAddonInfo('icon'), 'https://dl.dropboxusercontent.com/s/jn1o4c1y796x64m/MyTVDemo.mp4?dl=0')