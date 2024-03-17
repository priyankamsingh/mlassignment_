#ssh to remote machine by using bobs redentials user@host
ssh bob@95.179.138.59 

#listing active job on machine 
crontab -l 

#now terminate the process first option 

kill <pid>


#edit scheduling cronjob (option 2)
crontab -e   # after editing save it

#get cat image 
#option 1 - search on bobs compute 
#assuming '`bae55978a5ef1f4790361f3b1d076b789a3027ee`' as image identifier then use scp to copy