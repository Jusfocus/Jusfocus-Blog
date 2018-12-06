## Jusfocus Blog

We are starting a challenge to write a blog post everyday talking about technology, books, philosophy, travel and other random musings.
We wish we would be able to stay truthful to the resolution. 

For want of better topic, today I'll write about the potential architecuture of the blog.

## Blog Technical Architecture

There are 2 different architecture options to compose and store the contents of the blog

* Use wagtail backed by Postgres DB
* Use static site generator and save the content in git

Option 1 is better for highly structured data. For a simple blog, static site generator looks better in terms of SEO, speed and storage.

### Which Static Site Generator.

Since python is our primary language, we will be using a SSG powered by python. There are couple of options,

1. Pelican
2. Lektor

While I have fiddled around with both in past, I'll try out both to decide on which one to use. Till then, I'll just use the Github edit
option.

### Hosting

S3 seems to be good place since we already have some AWS credits. 

That's it for today. I hope this is a humble beginnings of a long journey which would benifit lot of people on the way. 

See you tomorrow!!
