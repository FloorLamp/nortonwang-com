## [Nortonwang.com](nortonwang.com)

This site uses [Pelican](https://github.com/getpelican/pelican).

### Installation

    pip install -r requirements.txt
    make devserver
    
The site will be running at `localhost:8000`.

### Using the theme

To use the theme, you simply copy the `theme` folder to your Pelican folder and change the `THEME` variable to `theme`.

Alternatively, you can copy the folder to your Pelican directory:

    PYTHON_DIR/site-packages/pelican/themes

### Creating a new post

To create a new post about `name`, just do:

    ./create_post name
    
This will create the file in the `content` folder with the correct meta tags.