# Randomcamp

The concept behind this project is to make a simple tool that allows people
to easily find new music through going to random Bandcamp pages. Also,
for me to learn stuff. Right now, it's just a simple Python script that
doesn't do much, but it would be cool to turn it into a webapp or
something, someday.

## 6/4/13

So the main dilemma right now is actually being able to get random
bandcamp pages. There isn't any sort of API for this, and if there was,
Bandcamp isn't giving out dev keys right now. The only other idea that
came to me was to essentially generate random band IDs and see if they
represent actual bands. The problem is that Bandcamp uses 32 bit
unsigned ints for band IDs and since there are significantly less
than 4,294,967,295 bands on Bandcamp, the probability of guessing one is
morbidly low, which seemingly dooms this project from the start. Oh well. If
I have any other ideas, this is where they'll go.
