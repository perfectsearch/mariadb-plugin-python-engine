Python Storage Engine for MariaDB and MySQL

This is a storage engine written for MariaDB and MySQL. I wanted to do some prototyping of a database storage engine, and thought it would be easier to accomplish the prototype using Python than writing it in C++. This code is not production ready and needs some additional work to make it so.

This was developed against MariaDB 5.5.42 and CentOS 6.6 (Final)

The following are my rough notes on how I've configured and used the driver.

I put the driver code in the storage folder.

mariadb-5.5.42/storage/python/

# https://mariadb.com/kb/en/mariadb/source-building-mariadb-on-centos/

yum install jemalloc-devel

cd build
cmake ../mariadb-5.5.42 -DBUILD_CONFIG=mysql_release -DWITH_JEMALLOC=yes -DRPM=centos
make -j 12 package

# We must install the debug build to use the debug share library

cd build_debug
cmake ../mariadb-5.5.42 -DBUILD_CONFIG=mysql_release -DWITH_JEMALLOC=yes -DRPM=centos -DCMAKE_BUILD_TYPE=Debug
make -j 12 package

# Add to my.cnf
[mariadb]
plugin-load=PYTHON=ha_python.so
python_python_script_path=/tmp/test.py

# Copy python.so to /usr/lib64/mysql/plugin if not installed with rpm

create database python;
use python;
create table `test` (`id` int, `data` text) ENGINE=PYTHON DEFAULT CHARSET=latin1 comment="Pass information to python engine.";
select * from `test`

