This repo is the student resources required to partcipate in the "Your code brightens the room" workshop

To Get Started click the following link sandbox link to create a workspace on Gitpod.
You're required to have a github user account to verify user/email in order to use the Gitpod service. 

[Sandbox environment for this Workshop/Repo](https://gitpod.io/#https://github.com/draco2003/hackher413)

[Presentation Slides](https://docs.google.com/presentation/d/1DMbn1_U7t8sulNTfID0-JmK_EtUKRi6L0MgjR9SWafU/edit?usp=sharing)

## Files in this repo to checkout

[mqtt_cli.py](mqtt_cli.py) : demo python cli app for subscribing to a topic as well as sending a message

[webui.py](webui.py) : example python web app for subscribing to a topic as well as sending a message


## mqtt_cli.py example commands:
Off:
`python mqtt_cli.py --message off --topic cmnd/<yourdevicename>/power`

On:
`python mqtt_cli.py --message on --topic cmnd/<yourdevicename>/power`

Subscrbie to a topic
`python mqtt_cli.py --topic stat/<yourdevicename>/POWER`

## webui.py example command:
Start webserver:
`python webui.py`
