# scaling-octo-chainsaw
BBC news headline scraper.
Currently the code scrapes the headlines with summaries and links and just outputs them with print. Using crontab the code is able to write to a separate log file which stores all of the headlines that have been scraped.
The headlines are separated according to importance with the classifications primary, secondary, tertiary and sport, used by the BBC.

In order to run automatically use crontab.
For OSX.
Using the nano text editor in terminal

"env EDITOR=nano crontab -e"

opens nano,
crontab takes five numbers (or *) and then the command

"0 9 * * * cd ~/Dropbox/Code/Python && ./bbc.py >> script_output.log 2>&1"

then to save the file press

"control+O, enter, control+x"

to write out the file, accept the file name and to exit nano.
The five numbers/asterisks determine when the script is run.
The first is for specifying the minute of the run (0-59), the second is for specifying the hour of the run (0-23), the third is for specifying the day of the month for the run (1-31), the fourth is for specifying the month of the run (1-12) and the fifth is for specifying the day of the week (where Sunday=0, up to Saturday=6)
In this case the application will run every day at 9:00am.

In order for terminal to run the file the permissions might need to be changed. 
Navigate to the folder containing the file and type the command

"chmod +x test.py"

in order to change permissions so terminal can run the file.
