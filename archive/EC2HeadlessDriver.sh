while [ "true" ]
do
	./Headless.sh
	msg="Restart on `date`"
	echo $msg
	touch restarts/"$msg"
	sleep 60
done
