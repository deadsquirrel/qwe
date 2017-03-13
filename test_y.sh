#!/bin/bash
#проверяем не пустой ли параметр на входе
if [ "$1" == "" ]; then
    echo "You must define project's name"
    exit 1
fi

PROJECT_NAME="$1"
#проверяем наличие домашней директории
if [ -d "/home/projects/${PROJECT_NAME}/" ]; then
	echo 'directory exist'
	exit 1
fi

#проверяем наличие пользователя
grep "u_${PROJECT_NAME}:" /etc/passwd >/dev/null
if ! [ $? -ne 0 ]; then
	echo 'username exist'
	exit 1
fi

#проверяем наличие репозитория
if ! [ -f "/home/horoshop/repos/${PROJECT_NAME}.git" ]; then 
	echo 'repos not found'
	exit 1
fi

#содаетм пользователя и добавляем его в группы
useradd  u_${PROJECT_NAME} -G git,www-data -d /home/projects/${PROJECT_NAME} -m -s /bin/bash

#создает директорию для бекапа БД
mkdir "/home/projects/${PROJECT_NAME}/db_backup"

#почему мы меняем права тут сейчас?
chown "git:www-data -R /home/horoshop/repos/${PROJECT_NAME}.git"

#содаем симлинки

ln -s /var/www/${PROJECT_NAME}.horoshop.com.ua/content/ /home/projects/${PROJECT_NAME}/content/
ln -s /home/horoshop/repos/${PROJECT_NAME}.git /home/project/${PROJECT_NAME}/repository.git

#делаем дамп БД
mysqldump --user=root --password=nCzALHXOa2 $SUB_DOMAIN_NAME > /home/projects/${PROJECT_NAME}/db_backup/last.sql


#чиним репозиторий
sh /var/www/ds.horoshop.com.ua/shell_scripts/project/fix-git.sh /var/www/${PROJECT_NAME}.horoshop.com.ua ${PROJECT_NAME}

#меняем права доступа на директорию
chown  u_${PROJECT_NAME}:u_${PROJECT_NAME}  /home/projects/${PROJECT_NAME}