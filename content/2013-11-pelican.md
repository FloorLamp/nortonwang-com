Title: Switching from Wordpress to Pelican
Date: 2013-11-02 12:00
Tags: pelican, python, wordpress

I was looking at my server memory the other day, and saw that mysql and apache were taking up way too much memory. I read about static site generators before, so I decided to take a closer look. The main ones were Jekyll (and Octopress), Hyde, and Pelican. I went with Pelican because it was Python based and seemed more popular than Hyde.

Switching to a static site would give me many benefits:

* No need to run mysql all the time, lowering memory consumption and reducing server errors when it randomly died
* Nginx is faster and more memory efficient than Apache for serving static files
* I can finally get off of Wordpress!
* I can have all my content in plain text and version controlled

The Pelican documentation was pretty extensive, and the getting started guide got me started pretty fast. However, there were some unexpected things that I learned along the way:

* The wordpress importer tool, for some reason, escaped (with a backslash) some symbols in my posts: $, _, <, and >. I had to manually look through my posts and fix these occurrences.
* Since each post is a file, you have to create and name the files yourself. The recommended filename is just the slug, but I dislike manually writing slugs. It'd be cool if there was a tool that allowed users to input a title and then automatically create the file.
* Pelican supports both reStructuredText and Markdown, but prefers the former, while I prefer the latter. Markdown support feels like a second class citizen at times.