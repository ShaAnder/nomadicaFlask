## CONTENTS

- [Nomadica](#nomadica)
  - [What is it](#what-is-it)
  - [Project purposes](#project-purposes)
  - [Features](#features)
    - [Future Features](#future-features)
  - [Development](#development)
    - [Languages](#languages)
    - [Tools](#tools)
  - [Deployment](#deployment)
  - [Credits & Attributions](#credits---attributions)
    - [Attribution](#attributions-)
    - [Other](#other)

### NOMADICA

Nomadica: In a fractured galaxy, humanity's greatest achievement becomes its worst nightmare. Your AI creations, designed to explore and conquer the stars, have turned against you. Now, hunted across the void, you must outwit and survive relentless synthetic predators. Can you escape the creations that know you better than you know yourself? The stars offer no sanctuary—only shadows.

#### What is it?

Nomadica is a concept i've been working on that for the moment is purely fiction, later maybe the idea for a game, this web / landing page serves as the first real creative outlet of the idea and was created as part of a uni follow along project. 

This is the updated version of that, now using a flask backend to test and understand flask better.

#### Project purposes

At it's core this is a fake landing page for a game i want to make in the future called nomadica, the idea behind this landing page came out of the need to create something myself rather than follow along with the course material.

This project was created as part of the bootstrap module for code institutes full stack software development diploma, it was intended to originally be a follow along project creating a fake whisky delivery website utilizing pure and largely only bootstrap.

As a developer i do see the power in bootstrap but by it's own admission the framework is rather limited and applications created in bootstrap tend to look very samey and be limited in what we can do with them. As a result i opted to follow a long with the project loosely creating my own landing page and utilizing bootsrap AND traditional css / js in combination.

This taught me not only how powerful and versitile boostrap is as the lessons intended but also (through mostly research) how to manipulate and edit bootstrap to create my own customized feel as needed.

The original project aimed to showcase how to build a landing page with a hybridization of bootstrap and html/cs/js, i opted to use it as the basis for an upgrade when i started using flask. I wanted to learn how to not only deploy an application with flask but how various frameworks and tools would interact with it, such as JS CSS and bootstrap

### FEATURES

This landing page features a few fully fleshed out ideas from the standard full responsiveness from smallest screens (375px) to desktop sizing.

A working nav bar (that leads back to main page (dummy links)) that is not only responsive but on mobile dynamically repositions itself as the user scrolls (will initially stick to the bottom and open upwards but as the user scrolls will move to the top and open downwards)

as well as this utilizing bootstrap features certain sections automatically responsively resize and change position as well as a fully functioning modal window with email signup field (again does nothing with the data as it's a dummy website)

#### Future features

As this is for a game concept i've had for ages id love to flesh out the website to create a fully functioning product page in the future, but this would be way down the line

### DEVELOPMENT

#### Languages

This website was created using HTML CSS JS Python and Flask

#### Tools

The site used Bootstrap frameworks as well as chatgpt for image generation and flask for web rendering

### DEPLOYMENT

#### How to Fork

To fork the repository:

1. Log in (or sign up) to Github.
2. Go to the repository for this project, [shaAnder/nomadicaFlask](https://github.com/shaAnder/nomadicaFlask)
3. Click the Fork button in the top right corner.

#### How to Clone

To clone the repository:

1. Log in (or sign up) to GitHub.
2. Go to the repository for this project, [shaAnder/nomadicaFlask](https://github.com/shaAnder/nomadicaFlask)
3. Click on the code button, select whether you would like to clone with HTTPS, SSH or GitHub CLI and copy the link shown.
4. Open the terminal in your code editor and change the current working directory to the location you want to use for the cloned directory.
5. Type 'git clone' into the terminal and then paste the link you copied in step 3. Press enter.

#### Setting up ENV / Installing flask

As this app uses packages not included in the cloned repo you will need to create an ENV folder for storing packages or install them directly to your python lib to do this run the following command

```
pip install -r requirements.txt
```

#### Running the application

Finally to run the application use the command

```
python3 app.py
```

### CREDITS AND ATTRIBUTION

This website and idea were created by me, some of the images for the gallery came from freepic and the rest of the images came from chat GPT
