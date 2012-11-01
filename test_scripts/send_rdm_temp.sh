#A test script that leverages CURL to send random temp measurements
#To the server to test out functionality
#This will send a random temperature to the server every 5 seconds

#Will create a random number between 1 and 100 to send to the server
#got a little help from http://islandlinux.org/howto/generate-random-numbers-bash-scripting


while true ; do
	RANDOM_TEMP=$[ ($RANDOM % 100) +1] 
	echo 'sending the tempurature:'$RANDOM_TEMP
	curl -H "Content-type: application/json" -X POST http://127.0.0.1:5000/devices/updates/temp -d '{"temperature":'$RANDOM_TEMP'}'
	sleep 5
	
done

