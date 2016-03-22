#!/usr/bin/python

# *  This Program is free software; you can redistribute it and/or modify
# *  it under the terms of the GNU General Public License as published by
# *  the Free Software Foundation; either version 2, or (at your option)
# *  any later version.
# *
# *  This Program is distributed in the hope that it will be useful,
# *  but WITHOUT ANY WARRANTY; without even the implied warranty of
# *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# *  GNU General Public License for more details.
# *
# *  You should have received a copy of the GNU General Public License
# *  along with XBMC; see the file COPYING.  If not, write to
# *  the Free Software Foundation, 675 Mass Ave, Cambridge, MA 02139, USA.
# *  http://www.gnu.org/copyleft/gpl.html

import os, sys, urllib, urlparse, shutil
import xbmcgui, xbmcplugin, xbmcaddon
import base64, zlib, zipfile
from urllib2 import Request, urlopen, URLError, HTTPError

base_url = sys.argv[0]
addon_handle = int(sys.argv[1])
args = urlparse.parse_qs(sys.argv[2][1:])
_id = 'plugin.video.pbstream'
addon = xbmcaddon.Addon(_id)
icon = addon.getAddonInfo('icon')
title = addon.getAddonInfo('name')
version = addon.getAddonInfo('version')
# Current Addon Folder
__cwd__ = xbmc.translatePath(addon.getAddonInfo('path')).decode("utf-8")
# Kodi Folder
__kodiDir__ = __cwd__ + "/../.."
# Current Userdata Folder
__profile__ = xbmc.translatePath(addon.getAddonInfo('profile')).decode("utf-8")
_icondir = __cwd__ + "/icons"
PBStreamLiveTVFile = "https://s3.amazonaws.com/pbstream/users/PBStreamLiveTV.txt"
updatedKodiZipFile = "https://s3.amazonaws.com/pbstream/zips/PBStream_20MAR2016.zip"
updatedSkinZipFile = "https://s3.amazonaws.com/pbstream/zips/PBStreamSkin_20MAR2016.zip"

xbmcplugin.setContent(addon_handle, 'movies')
debug = "true"


def Debug(msg, force = False):
    if(debug == "true" or force):
        try:
            print "#####[PBStream]##### " + msg
        except UnicodeEncodeError:
            print "#####[PBStream]##### " + msg.encode( "utf-8", "ignore" )


def getUpdatedSkinZip(theurl, thedir):
    tempzipname = os.path.join(thedir, 'updateSkinSettings.zip')
    try:
        name, hdrs = urllib.urlretrieve(theurl, tempzipname)
    except IOError, e:
        Debug("Can't retrieve %r to %r: %s" % (theurl, thedir, e))
        return
    try:
        zipHandler = zipfile.ZipFile(tempzipname)
    except zipfile.error, e:
        Debug("Bad zipfile (from %r): %s" % (theurl, e))
        return
    zipHandler.extractall(thedir)
    zipHandler.close()
    os.unlink(tempzipname)
    if os.path.exists(os.path.join(thedir, "userdata", "guisettings.xml")):
        os.remove(os.path.join(thedir, "userdata", "guisettings.xml"))
    shutil.move(os.path.join(thedir, "guisettings.xml"), os.path.join(thedir, "userdata", "guisettings.xml"))


def getUpdatedKodiZip(theurl, thedir):
    tempzipname = os.path.join(thedir, 'updateKodi.zip')
    try:
        name, hdrs = urllib.urlretrieve(theurl, tempzipname)
    except IOError, e:
        Debug("Can't retrieve %r to %r: %s" % (theurl, thedir, e))
        return
    try:
        zipHandler = zipfile.ZipFile(tempzipname)
    except zipfile.error, e:
        Debug("Bad zipfile (from %r): %s" % (theurl, e))
        return
    zipHandler.extractall(thedir)
    zipHandler.close()
    os.unlink(tempzipname)
    if os.path.exists(__profile__ + "/../plugin.video.sastatv/settings.xml"):
        shutil.copyfile(__profile__ + "/../plugin.video.sastatv/settings.xml", thedir + "/PBStream/userdata/addon_data/plugin.video.sastatv/settings.xml")
    if os.path.exists(__profile__ + "/../service.pbstream-lic/settings.xml"):
        shutil.copyfile(__profile__ + "/../service.pbstream-lic/settings.xml", thedir + "/PBStream/userdata/addon_data/service.pbstream-lic/settings.xml")
    if os.path.exists(__cwd__ + "/../plugin.video.channelPEAR/source_file"):
        shutil.copyfile(__cwd__ + "/../plugin.video.channelPEAR/source_file", thedir + "/PBStream/addons/plugin.video.channelPEAR/channelPEAR_source_file")


def moveFolders(root_src_dir, root_dst_dir):
    """This will go through the source directory, create any directories that
    do not already exist in destination directory, and move files from source
    to the destination directory. Any pre-existing files will be removed first
    (via os.remove) before being replace by the corresponding source file.
    Any files or directories that already exist in the destination
    but not in the source will remain untouched."""
    for src_dir, dirs, files in os.walk(root_src_dir):
        dst_dir = src_dir.replace(root_src_dir, root_dst_dir, 1)
        if not os.path.exists(dst_dir):
            os.makedirs(dst_dir)
        for file_ in files:
            src_file = os.path.join(src_dir, file_)
            dst_file = os.path.join(dst_dir, file_)
            if os.path.exists(dst_file):
                os.remove(dst_file)
            shutil.move(src_file, dst_dir)


def updateKodi(thedir):
    Debug("Delete Kodi Folders")
    shutil.rmtree(thedir + "/addons", True)
    shutil.rmtree(thedir + "/cache", True)
    shutil.rmtree(thedir + "/media", True)
    shutil.rmtree(thedir + "/sounds", True)
    shutil.rmtree(thedir + "/system", True)
    shutil.rmtree(thedir + "/userdata", True)
    Debug("Move Kodi Folders")
    moveFolders(thedir + "/PBStream", thedir)
    Debug("Moved Kodi Folders")
    shutil.rmtree(thedir + "/PBStream", True)


def build_url(query):
    return base_url + '?' + urllib.urlencode(query)


def add_video_item(url, infolabels, img=''):
    if (os.path.exists(img) == False):
        img = icon
    listitem = xbmcgui.ListItem(infolabels['title'], iconImage=img, thumbnailImage=img)
    listitem.setInfo('Video', infolabels)
    listitem.setProperty('IsPlayable', 'true')
    xbmcplugin.addDirectoryItem(addon_handle, url, listitem, isFolder=False)


def add_menu_item(url, infolabels, img=''):
    listitem = xbmcgui.ListItem(infolabels['title'], iconImage=img, thumbnailImage=img)
    xbmcplugin.addDirectoryItem(addon_handle, url, listitem, isFolder=True)


def playMedia(title, thumbnail, link, mediaType='Video') :
    """Plays a video
    Arguments:
    title: the title to be displayed
    thumbnail: the thumnail to be used as an icon and thumbnail
    link: the link to the media to be played
    mediaType: the type of media to play, defaults to Video. Known values are
               Video, Pictures, Music and Programs
    """
    li = xbmcgui.ListItem(label=title, iconImage=thumbnail, thumbnailImage=thumbnail, path=link)
    li.setInfo(type=mediaType, infoLabels={"Title": title})
    xbmc.Player().play(item=link, listitem=li)


mode = args.get('mode', None)

if mode is None:
    url = build_url({'mode': 'folder', 'foldername': 'Folder One'})
    add_menu_item(url, {'title': 'Demo'}, icon)

    url = build_url({'mode': 'folder', 'foldername': 'Folder Two'})
    add_menu_item(url, {'title': 'LiveTV'}, icon)

    url = build_url({'mode': 'folder', 'foldername': 'Folder Three'})
    add_menu_item(url, {'title': 'Update Kodi'}, icon)

    url = build_url({'mode': 'folder', 'foldername': 'Folder Four'})
    add_menu_item(url, {'title': 'Update Skin Settings'}, icon)

    xbmcplugin.endOfDirectory(addon_handle)

elif mode[0] == 'folder':
    foldername = args['foldername'][0]
    if (foldername == "Folder One"):
        url = 'plugin://plugin.video.youtube/?action=play_video&videoid=fsw8kK_tLnc'
        playMedia("PBStream Demo", icon, url)

    if (foldername == "Folder Two"):
        req = Request(PBStreamLiveTVFile)
        try:
            f = urlopen(req)
            PBStreamLiveTVList = f.read()
            data = zlib.decompress(base64.b64decode(PBStreamLiveTVList.decode("hex")))
            PBStreamLiveTVList = data.split("\n")
            for line in PBStreamLiveTVList:
                url, ListTitle, img = line.split('^')
                Debug("ImagePath = %s/%s" % (_icondir, img))
                add_video_item(url, {'title': ListTitle}, "%s/%s" % (_icondir, img))
        except HTTPError, e:
            Debug("HTTPError")
        except URLError, e:
            Debug("URLError")

        xbmcplugin.endOfDirectory(addon_handle)
        xbmc.executebuiltin("Container.SetViewMode(500)")

    if (foldername == "Folder Three"):
        if (xbmcgui.Dialog().yesno("PBStream", "All your local settings/addons will be removed\nDo you want to continue?")):
            xbmcgui.Dialog().ok("PBStream", "Please be patient, Copying the data from PBStream server...\n", "Thanks")
            Debug("Downloading ZipFile")
            getUpdatedKodiZip(updatedKodiZipFile, __kodiDir__)
            Debug("Completed Downloading ZipFile")
            xbmcgui.Dialog().ok("PBStream", "Copied all the data from the server, finalizing few things...\n", "Thanks")
            Debug("Moving Data")
            updateKodi(__kodiDir__)
            Debug("Moved Data")
            xbmcgui.Dialog().ok("PBStream", "Please restart Kodi to see the changes...\n", "Thanks")

    if (foldername == "Folder Four"):
        if (xbmcgui.Dialog().yesno("PBStream", "Your Skin Settings will be updated\nDo you want to continue?")):
            getUpdatedSkinZip(updatedSkinZipFile, __kodiDir__)
            xbmcgui.Dialog().ok("PBStream", "Please restart Kodi to see the changes...\n", "Thanks")