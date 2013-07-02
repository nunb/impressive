impressive
==========

------------------------------

Announcement!
=============

Hey guys, I rewrote the codebase of impressive a few times, so that I was able to figure out  
what user experience would be great for me... so I decided to write a "compiler". It'll be  
online in a few days (btw. I rewrote it in Hy, a Lisp Python dialect, use searchbar, do it!!!).   
The basic idea was using tools, I already use a lot. I write the most work related documentation  
in ReST and compile it with sphinx - so I thought writing something similiar would be great for  
impress.js :) My apprenticeship ends a few days with my final examinations - definetly more time  
to code :>

------------------------------

An impress.js presentation generator
  
I decided to code a small impress.js presentation generated, because I was tired  
of doing this odd redundant HTML stuff. Please let me know your improvements by  
opening an issue.  

You have to solve a few steps until your presentation is ready.  
First you'll have to create some content. Change into the cnt/ folder of exec/ by executing this command:  

    cd exec/cnt/  

Okay, after this you should create some content. For example you could create a start page, some content  
pages and an end page.  

    touch start.cnt content_a.cnt content_b.cnt end.cnt  

Well, fill it with some content you want to display and you are finished with this step. Your content  
will be parsed through a nl2br parser, so you can use this as your markdown :)  
Remember to name your .cnt and .json files [the generators will do this automatically, but maybe you  
want to change something in impressive.py itself] as your step id's. Here is an example:
        
    exec/
        cnt/
            content_a.cnt
            content_b.cnt
            end.cnt
            start.cnt
        json/
            content_a.json
            content_b.json
            end.json
            start.json
        
        HTML:  
        <div id="start" ... >  
        <div id="content_a" ... >
        <div id="content_b" ... >
        <div id="end" ... >
  
Okay, after you've added some content you are able to generate the json files which will be later  
converted into the steps. Start the impressive JSON generator with this lines:

    chmod u+x impressive_json-generator.py
    ./impressive_json-generator.py  

The generator asks you in a while-True-loop if you want to generate a new JSON slide,  
just answer the questions and generate the JSONs. The generator also keeps track on content  
updates (in cnt/$fileName.cnt) and patches them into the JSONs.  
  
As a last step you just have to run the run.py like this:
    
    chmod u+x run.py
    ./run.py json

The first argument is the folder where your JSONs are placed. They will be converted into  
impress.js steps.  
You are also able to run this script with a second argument, you can pass a config for the whole  
presentation, so you won't be ask for every single detail every time you run this script.  
