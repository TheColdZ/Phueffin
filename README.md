# Phueffin
This project will be an over-engineered Phillips Hue backend that will handle turning lights on and off, scheduling etc. 

It started as me just wanting to implement the brillinat "bindicator" light for myself as a coding project, finally having found something that was a bit silly and that would be fun to show off to the layman. 

The long term plan of this project then escelated to creating a matching frontend that can be accessed through a web-browser on the local network, that through this backend will control the lights. 
The "over" part of over-engineering, is that the project will use github actions, be designed using the hexagonal archtitucture design and of course be dockerized. 
Which should in the end make it more or less plug'n'playable for others wishing to also have this. 

Why? Because my phone is too old for the app and what if I have visitors over that don't want to download the app? 

Does such a project already exist? Maybe, but I don't care, this is for learning and being able to say I did something and knowing the code entirely. 

An important note: There will be heavy refactoring and since I have a somewhat busy life and this is a sparetime project: things will be made quick and dirty, "if it works it works".

Does that mean skipping tests? In the beginning, sure, stuff has to work so I don't forget trash collection. When having more than the bare minimum project? Heck no. 

If you are intrigued/want to use it/have an idea/want to offer me a high paying job, hit me up, I might answer at some point, maybe straightaway, maybe delayed. 

Rant over? 

Or yeah the name, part of my name can be translated to puffin. Maybe it has to change at some point, time will tell. 



Useful commands: 
Want to find the "username" for a server, use this curl command: 
curl --header "Content-Type: application/json"   --request POST   --data '{"devicetype":"app#some great name"}'   http://<IP-address>/api

Eventually (maybe) this should be faced out and be replaced with an auto detect upon startup.... low priority for now. 