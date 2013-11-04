Title: Switching from Wordpress to Pelican
Date: 2013-11-04 14:00
Tags: pelican, python, wordpress

I was looking at my server memory the other day, and saw that mysql and apache were taking up way too much memory. I read about static site generators before, so I decided to try them out. The main ones were Jekyll (and Octopress), Hyde, and Pelican. I went with Pelican because it was Python based and seemed more popular than Hyde.

Switching to a static site would give me many benefits:

* No need to run mysql all the time, lowering memory consumption and reducing server errors when it randomly died
* I can finally get off of Wordpress!
* I can have all my content in plain text and version controlled

The Pelican documentation was pretty extensive, and the getting started guide got me started pretty fast. However, there were some unexpected things that I learned along the way:

* The wordpress importer tool, for some reason, escaped (with a backslash) some symbols in my posts: $, _, <, and >. I had to manually look through my posts and fix these occurrences.
* Since each post is a file, you have to create and name the files yourself. The recommended filename is just the slug, but I dislike manually writing slugs. It'd be cool if there was a tool that allowed users to input a title and then automatically create the file.
* Pelican supports both reStructuredText and Markdown, but prefers the former, while I prefer the latter. Markdown support feels like a second class citizen at times.

### Redesigning

After getting all my posts converted and formatted properly, I redesigned my theme completely. I switched from my boring old fonts to Google Web Fonts, got a new color scheme, and switched to a really simple one column layout. I also switched to Font Awesome for the social links. Pelican provides great Google Analytics and Disqus integration out of the box, so all I had to do was add my ids. After a bunch of css fiddling, it was done. Everything looked great on desktop and mobile, all the javascript worked, and I was ready to deploy.

### Nginx

I did go through the trouble of creating a static site, so I might as well serve it on nginx. I never used it before, but installation and configuration was relatively simple. The only difficulty I encountered was with my about link - I had the url set as `/about`, and the file was saved to `/about.html`. During testing, the python http server redirected correctly, but nginx doesn't unless you tell it to. So, I had to add this line to fix it:

    :::text
    rewrite /about$ /about.html;

Makes sense, but it would have saved me a lot of time if I had known this beforehand. After getting everything set up, I did a simple benchmark. I ran the following command on both my nginx and apache servers:

    :::text
    ab -n 1000 -c 10 nortonwang.com/

And the results:

    :::text
    Server Software:        Apache/2.2.22
    Time taken for tests:   22.574 seconds
    Requests per second:    44.30 [#/sec] (mean)
    Time per request:       225.737 [ms] (mean)
    Time per request:       22.574 [ms] (mean, across all concurrent requests)
    Transfer rate:          591.90 [Kbytes/sec] received

    Connection Times (ms)
                  min  mean[+/-sd] median   max
    Connect:       15  200 274.5    118    3667
    Processing:     0   19  60.8      0    1108
    Waiting:        0    9  34.7      0     335
    Total:         50  220 284.5    142    3670

    Percentage of the requests served within a certain time (ms)
      50%    142
      66%    230
      75%    288
      80%    325
      90%    410
      95%    511
      98%    812
      99%   1702
     100%   3670 (longest request)

    Server Software:        nginx/1.4.2
    Time taken for tests:   5.431 seconds
    Requests per second:    184.13 [#/sec] (mean)
    Time per request:       54.310 [ms] (mean)
    Time per request:       5.431 [ms] (mean, across all concurrent requests)
    Transfer rate:          2456.53 [Kbytes/sec] received

    Connection Times (ms)
                  min  mean[+/-sd] median   max
    Connect:       14   17   2.0     16      29
    Processing:    30   38  20.4     35     383
    Waiting:       15   19   3.3     18      58
    Total:         45   54  20.9     51     406

    Percentage of the requests served within a certain time (ms)
      50%     51
      66%     53
      75%     54
      80%     55
      90%     59
      95%     64
      98%     72
      99%     86
     100%    406 (longest request)

Nginx served requests **4.2x** faster than apache. Wow. On top of that, memory and cpu usage stayed low with nginx, whereas apache took cpu and memory to 100%. I think nginx was a good choice.

Overall, I think Pelican and static site generators are great for simple blogs like mine that don't change that often. Sure, the learning curve is steeper than Wordpress, but it's still relatively painless. And, of course, static sites are the cool thing to do nowadays.
