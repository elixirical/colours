# colours

This little webapp generates 16 colours based on a text input. With unified palette checked, it tries to select a small subset of the palette, and using those selected colours, adds some amount of jitter to fill out the remaining colours. The colours are sorted according to a nearest neighbour algorithm, however because of the three dimensional nature of HTML colourspaces, the colour order doesnt always makes sense to our human eyes. <br><br>
I created this largely for the hell of it. It was inspired by (or it is a direct copy of ¯\\_(ツ)_/¯) [this](https://farbecolore.com/) wonderful generator. I'm unsure of the exact method the linked site uses to generate colours, however this site hashes the given text input using the x64 128-bit [MurmurHash](https://en.wikipedia.org/wiki/MurmurHash") algorithm, and utilizes the resulting hash as an initial seed to generate all the colours. <br><br>
The app itself is built using [flask](https://flask.palletsprojects.com/en/2.3.x/) as the framework, and the [mmh3](https://github.com/hajimes/mmh3) implementation of MurmurHash. It also utilizes [numpy](https://numpy.org/) and [scipy](https://scipy.org/) to calculate the nearest neighbour of each colour. The specific implementation of the nearest neighbour algorithm is sourced from [this article](https://www.alanzucconi.com/2015/09/30/colour-sorting/), which was of tremendous help while building this app. Lastly, the favicon was obtained from [flaticon](https://www.flaticon.com/free-icon/paint_2997270), which provides a license stipulating that it may be used for commercial or personal projects with attribution. <br><br>

The source code for this project can be found [here](https://github.com/elixirical/colours/tree/master). Feel free to clone it and modify it however you want (sorry in advance for the godawful documentation). If you do, please credit me ([elixirical](https://github.com/elixirical)) as the original creator, and please credit farbecolore.com as the original inspiration. I am using and highly recommend [Render](https://render.com/) to host this. I found Render as an alternative to Heroku after they deleted my account and removed their free tier, and have found it to be much easier to use, especially with the ability to conect your git repository directly to your Render account and then deploy from there.

Try it out at [colours.ennuic.com](https://colours.ennuic.com/).