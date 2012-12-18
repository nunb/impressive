impressive
==========

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
  
  
  
# Tutorial short (long will follow)  
(Note: Do this all in your exec/ folder)  
1. Create your content files in exec/cnt/  
2. Create JSONs by using the impressive_json-generator.py  
    -> Remember to add the content first to exec/cnt/!  
3. execute run.py with json folder as argument (./run.py json)  
    -> If executed in exec/  

