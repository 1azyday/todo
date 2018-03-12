sudo su

source_root='/var/todo'

# 建立一个软连接
sudo ln -s -f ${source_root}/todo.conf /etc/supervisor/conf.d/todo.conf
# 不要再 sites-available 里面放任何东西


# 重启服务器
sudo service supervisor restart


# service supervisor status
# ls /var/log/supervisor/supervisord.log

sudo echo 'deploy success'
