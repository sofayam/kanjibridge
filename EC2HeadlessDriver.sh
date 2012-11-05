while [ "true" ]
do
	./Headless.sh
	msg="Restart on `date`"
	echo $msg
	touch "$msg"
	sleep 60
done
