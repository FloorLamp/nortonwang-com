Title: What I've learned from 1 year at a startup
Date: 2013-06-30 15:19
Tags: startup, django

Exactly 1 year ago, I started work at [Aggregift][]. Back then, I had
just graduated from college and didn't really know what I was doing.
Now, I still don't really know what I'm doing, but at least I have a
year of experience behind me. Here are some of the lessons I've learned
along the way, some tiny, and some significantly large.

## How to business

![business][]

I studied electrical engineering, so the closest I got
to business was maybe in a corporate finance class. But after working on
a 2-3 man team, one of them being the business manager, you sort of have
to know these things. Things like our revenue model (we were making
revenue from the day we launched. Not much, but it was more than 0),
combined with our user growth rate, would lead to break-even in x
months. Things like "we need to raise another round of funding because
our burn rate will lead us to death in y months". Things like "we have
potential acquisition interest from x company so we should also talk to
y and z companies about an acquisition". And finally, things like "we're
spending \$x on advertising every week and we're seeing y new users as a
result; y isn't big enough but at least we get pictures of cute animals
on our Facebook page". I'm not saying I could go and be a business
manager now, but at least I know that these are things you have to worry
about.

### Technical

After working with Python and Django for a year, you learn a little bit.

-   **Use South.** This is a given when using Django. And don't forget
    to migrate after deploying to production, goddamn.
-   **Fat models.** Give them a sandwich. Every single function that you
    can reuse, put it in the model.
-   **Try/catch every external service call.** Payment processors, email
    senders, Facebook api, Amazon api... everything will break
    eventually.
-   **Unicode support.** Our site had a major bug that was caused by a
    guy with an á in his name. If possible, specify a default encoding
    for your database. If not, make sure every time the field is used
    it's encoded.
-   **Use management commands.** Instead of writing random one off
    scripts, make them management commands so that you can just modify
    and reuse.
-   **Django admin is one of its best features.** You can embed html in
    each row/column for easy visual inspection.
-   **Test, and re-test. And then test again.** I broke user
    authentication when I modified one line and forgot to test with a
    new user. Oops.
-   **Use Django debug toolbar.** This is one of the tools I used for
    profiling and benchmarking. There are other tools, such
    as snippetscream and apache bench.
-   **Email templates suck.** If you weren't around in the early 2000s
    for table-based web design, then you'll have to relearn everything
    you thought you knew about HTML.

### Other

-   **Overcommunicate.** I'm still bad at this, but the idea is you always want more
    communication and not less. For example, when a production error
    happens, you need to explain the root cause, the severity, the fix,
    and prevention in the future.
-   **Don't fucking comment your fucking code like this.** Yeah, I've
    done this a few times when I was mad, but try not to use profanity
    in your comments/variable names. Especially not in client side Javascript.
-   **You don't always have to write perfect code.** If you're rushing
    to get a feature out tomorrow, just make it work. You can deal with
    refactoring later. Just don't forget to do it.
-   **Create a flowchart for complex processes.** Many times I would get
    confused about when the user's friends list was loaded. Then I made
    some pretty flowcharts and it was k.

  [Aggregift]: https://www.aggregift.com/
  [business]: http://i.imgur.com/DNFRd.jpg
