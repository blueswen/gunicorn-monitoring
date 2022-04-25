TIMES=3
for i in $(eval echo "{1..$TIMES}")
do
    siege -c 1 -r 3 http://localhost:8000/
    siege -c 1 -r 5 http://localhost:8000/io_task
    siege -c 1 -r 5 http://localhost:8000/cpu_task
    siege -c 1 -r 5 http://localhost:8000/random_sleep
    siege -c 1 -r 20 http://localhost:8000/random_status
done
