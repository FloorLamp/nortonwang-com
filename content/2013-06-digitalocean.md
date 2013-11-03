Title: Switching to DigitalOcean
Date: 2013-06-20 16:00
Tags: aws, ec2, digitalocean

When I first started nortonwang.com, it was hosted on Heroku, since at
that time I was just really starting web development. We were learning
how to create a Facebook application using Heroku and Django, and since
I was familiar with it, I just started my website there. I quickly
realized that Heroku free tier comes with its disadvantages... namely,
the insane spin-up time. Each free Heroku dyno goes inactive after a
while, and when the next visitor comes, it has to spin up again, taking
around 5 seconds. Even for a small personal site like mine, 5 seconds
was a bit too much.

The other day I finally decided to switch to a virtual private server. I
started with AWS, creating a EC2 micro instance. This was a huge
difference from Heroku - you essentially own your own box in the cloud,
along with all the responsibilities of that. I had to install and
configure apache all by myself. It was a good learning experience,
although somewhat painful. Apache has tons of intricacies that aren't
apparent at first. I finally managed to get everything set up and
working, but EC2 was way too pricey for me. Even with the smallest instance,
it would have cost me over $175/year, which isn't worth it for such a low
traffic site.

Today I discovered [DigitalOcean][], which offers $5/month for their
smallest instance. After reading some reviews and comparisons, I decided
to try it out. Creating an instance was pretty easy, but for some reason
they don't allow you to add key-based ssh after it has been created. So,
I had to delete my first instance, add my ssh key, and then create
another instance using that key. Setting it up was far easier this time.
I did a simple apache bench on both EC2 and DO, and they gave
similar performance for low loads. As of now, the blog that you're
reading is hosted on DO, and will probably stay that way until I
suddenly become famous and need to scale up.

  [DigitalOcean]: https://www.digitalocean.com/
