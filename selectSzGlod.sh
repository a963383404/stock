#!/bin/bash
start=`date +%s` # 定义脚本运行的开始时间

for ((i=508;i<=700;i++))
do
{
	sleep 1
	e=$[i+2]
	#echo 'success'$i'--'$e;
	./manage.py selectSzGlod $i $e
}&
done
wait
end=`date +%s`
echo "TIME:`expr $end - $start`"
