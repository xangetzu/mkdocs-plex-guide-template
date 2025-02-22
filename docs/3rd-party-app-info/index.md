# How I set up deep.thought and manage the library

## The basics

Three years ago, I decided to get a little more serious with my Plex server. It had been up then then, running on an old windows machine that was formally a game rig with a bunch of USB attached drives. I wanted something more so I bought hardware to build a server. New to the concept, and realizing I wanted to be off of the windows environment, I looked at Unraid as an option as I was still nervous about learning something new but wanted the benefits of Linux stability. Three years later, the whole setup has evolved. I now have multiple Network Attached Storage boxes (NAS) both on Synology and TrueNAS operating systems and my suite of apps running on Unraid has grown to way more than just one docker container with plex on it. 

Unraid, acts as my application server. My NASs hold the library and the apps on Unraid are able to view that data and make changes to it. At its core, I have 5 levels of applications related to media. 

 1. **Plex apps**: These are apps related to plex directly, and interface with it directly. Things like Overseerr (for requesting new content), Tautulli (for viewing history, handling notifications), and server analytics, and finally Sync-Lounge (for watch together type stuff.)
 2. **Media Management apps**: Media Management and Download services work in tandom to each other. The ARR applications recieve notifications from Overseerr when a new request is made for Movies and TV. They then search various indexers for where the media can be found, and instruct my Download services to grab it. Then, once it is complete they move it and rename it to where it needs to be for Plex to ingest it and make it available to view. Some things are also managed by other connections outide of Overseerr such as Trakt or Spotify for music. 
 3. **Download services**: Pretty cut and dry with this one. These apps literally download the media and hold it until told to do otherwise.
 4. **Streaming services**: Something most people won't have access to, but I use an IPTV service that I pipe through Plex using a streaming application that simulates a cable card in my server for video.
 5. **Media Processing**: Media processing is something I do when I have a file I can't get in a formatt or size I want. Generally, I aim for something called H265, or HEVC as its also called. This stands for High Efficiancy Video Codec. It basically means for a smaller file size I can still get exceptionally good picture and audio quallity. But this takes a lot of computer to do so it's always best to try and find the media already in this format to begin with. 

These applications run 24/7 and are always adding new content, upgrading and replacing content, and whatever else is needed to make the Plex experience on deep.thought great. 

## Communication

Communication is also very important to me. To that end, I use both Tautulli and Overseerr to communicate a few things. 

1. When a request is approved via **Overseerr**, I send a notification to discord. If, the person that requested the content is a member of the discord and added to the server I set up for deep.thought, the message will be directed to them with a call out. 
2. Once media becomes available from Plex's point of view, meaning its finished processing, in the library and Plex has scanned it, another notification is sent out to the discord stating the content is in Plex. This message is meant for everyone so a user is not tagged in it. 
3. **Tautulli** also keeps tabs on whether the server is online or even reachible and will notificy when it is not. 

In the future, I plan on adding better communication around server availability becuase it suffers from being local to the actual plex server. Meaning, it can't report to discord if something outside of my home happens such as the internet going down. I need an external application to do that type of monitoring. 

!!! note
    It is highly recomended you reach out to me on [discord](https://discord.com/users/401938150877954048) in order to be added to the dedicated server I have set up for deep.thought. This will enable you to recieve notifications when media is added or when the server is down. 

## Maintenance and Updates

I generally keep everything up to date as much as possible. Plex enters its maintenance period based on a time I have selected that is best for most of my users however There are some over in the AU (Sorry mates) that this may effect. From 4 AM to 11 AM daily, Plex analyzes new media to create what it needs to operate more efficiantly which can sometimes slow it down. Every few days, it runs some database stuff that kills it for about 20 minutes but it usually comes back up reliably. 

Operating system updates and application updates are more manual and I try to warn people beforehand that they will be happening, sometimes even setting up an event in Discord so that everyone is aware if I expect it to take longer than normal. 