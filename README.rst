Sync tool for managing Reinout's photos and videos
==================================================


Photos
------

Photos can come from two sources:

- Individual images that are added on a one-off basis. Screenshots, perhaps. I
  add them with a script by passing the image's filename. The script prompts
  me for some metadata like title, album/category, event.

- Iphoto. Iphoto has a nice ``AlbumData.xml`` file with all the data I
  need. Title, album, event, rating, x/y location, etcetera. I sync this with
  a script that investigates the iphoto library and syncs/copies what's
  needed.

The one big target is a `git annex <http://git-annex.branchable.com/>`_
repository. Two things need to end up in there:

- The individual original photo files. They'll have a nice SEO-friendly
  lowercase name instead of ``IMG_1234.JPG``-like junk.

- A json file (or a couple of them) with metadata on those photo files like
  title, album and event.


Iphoto syncing strategy
-----------------------

How do I know which photos to sync from iphoto? By having a smart album that
tells me which photos are ready. I use smart albums to tell me which photos
still need to get a rating, a title, a geotag. So the most safe way is to use
the very same mechanism to tell me which photos are ready!

This smart album filter might not be smart enough, so there's room for extra
filtering in Python. It'll be extra filtering, though. I won't *add* photos.

Elements I use from iphoto:

- Events will end up as-is on the website. Those are a handy way to group
  photos, separate from albums.

- Albums (which I can nest in folders) for grouping. A photo can end up in
  multiple albums.


Making photos private
---------------------

I want to be more strict in making photos private. Not all my kids' photos
need to be public. And not all my work photos. Some are just for my own
enjoyment. Something as simple as an IP-based permission can get me and my
family access later on.

How to mark photos private? Well, I'll just add an underscore in front of the
title :-)


Videos
------

Videos can come only from one source: they're individual files that are added
individually. I make them one at a time. The ones I have now are all over the
place. So a script to add them will have to do. It should ask for metadata,
perhaps based on the photos' metadata.

The target?

- Individual video files in year-based folders.

- A metadata file (or several) with the title and album/event info.

What if metadata is missing? Perhaps a script that notes it and allows you to
add it.


Albums/categories
-----------------

Albums are categories. But I have gone overboard with them on flickr and
smugmug. But I think I can simplify it in this new setup.

- I use events, so things like "vacation 2012" are already bundled in an
  event.

- If I add geotags everywhere, I don't have to split my train photos in "Dutch
  train photos" and "German train photos. That'll be done automatically once I
  get around to programming it.

- I can always add tags for some extra grouping later on if I need it.

- I can tag events, too. Perhaps a nice way to group swordfighting stuff?

- Nobody's going to do much browsing through my photos. At least not through
  multiple levels of folders. The only thing I need to do, really, is to group
  it for external visitors. "Family", "trains". So that those interested in
  trains aren't bothered with my cycling photos.

- For special items, I can make proper textual pages in the regular part of my
  website.

Here's a brainstormed list: ligfiets, familie, (de)construction, trains, model
trains, historical trains, work, csr, kerk, school. As an example, "work"
contains zestsoftware, python meetings, PhD conferences and so on.
