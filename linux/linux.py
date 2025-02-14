apt
sudo apt install suricata
sudo apt remove suricata
suricata
sudo apt install tcpdump
sudo apt install suricata
echo hello
expr 32 - 8 

analyst@693f2db1c66b:~$ pwd
/home/analyst
analyst@693f2db1c66b:~$ ls -l
total 16
drwxr-xr-x 2 analyst root 4096 Jan 30 01:51 logs
drwxr-xr-x 2 analyst root 4096 Jan 30 01:51 projects
drwxr-xr-x 3 analyst root 4096 Jan 30 01:51 reports
drwxr-xr-x 2 analyst root 4096 Jan 30 01:51 temp
analyst@693f2db1c66b:~$ cd reports
analyst@693f2db1c66b:~/reports$ -d*/
-bash: -d*/: No such file or directory
analyst@693f2db1c66b:~/reports$ -d */
-bash: -d: command not found
analyst@693f2db1c66b:~/reports$ ls -d */
users/
analyst@693f2db1c66b:~/reports$ cd users
analyst@693f2db1c66b:~/reports/users$ cat Q1_added_users.txt
employee_id  username  department
1001         bmoreno   Marketing
1026         apatel    Human Resources
1041         cgriffin  Sales
1104         mreed     Information Technology
1177         aezra     Human Resources
1188         noshiro   Finance
analyst@693f2db1c66b:~/reports/users$ cd logs
-bash: cd: logs: No such file or directory
analyst@693f2db1c66b:~/reports/users$ cd /home/analyst/logs
analyst@693f2db1c66b:~/logs$ ls -l
total 4
-rw-r--r-- 1 root root 1044 Jan 30 01:51 server_logs.txt
analyst@693f2db1c66b:~/logs$ head -n -rw-r--r-- 1 root root 1044 Jan 30 01:51 server_logs.txt
head: invalid number of lines: 'rw-r--r--'
analyst@693f2db1c66b:~/logs$ head -n 1 root root 1044 Jan 30 01:51 server_logs.txt
head: cannot open 'root' for reading: No such file or directory
head: cannot open 'root' for reading: No such file or directory
head: cannot open '1044' for reading: No such file or directory
head: cannot open 'Jan' for reading: No such file or directory
head: cannot open '30' for reading: No such file or directory
head: cannot open '01:51' for reading: No such file or directory
==> server_logs.txt <==
2022-09-28 13:55:55 info    User logged on successfully
analyst@693f2db1c66b:~/logs$ head -n server_logs.txthead: invalid number of lines: 'server_logs.txt'
analyst@693f2db1c66b:~/logs$ head -n 10 server_logs.txt
2022-09-28 13:55:55 info    User logged on successfully
2022-09-28 13:56:22 error   The password is incorrect
2022-09-28 13:56:48 warning The file storage is 75% full
2022-09-28 15:55:55 info    User logged on successfully
2022-09-28 15:56:22 error   The username is incorrect
2022-09-28 15:56:48 warning The file storage is 90% full
2022-09-28 16:55:55 info    User navigated to settings page
2022-09-28 16:56:22 error   The password is incorrect
2022-09-28 16:56:48 warning The current user’s password expires in 15 days
2022-09-29 13:55:55 info    User logged on successfully
analyst@693f2db1c66b:~/logs$ 

cd logs
grep "error" server_logs.txt

2022-09-29 13:55:55 info    User logged on successfully
analyst@be37254e6899:~/logs$ grep "error" server_logs.txt
2022-09-28 13:56:22 error   The password is incorrect
2022-09-28 15:56:22 error   The username is incorrect
2022-09-28 16:56:22 error   The password is incorrect
2022-09-29 13:56:22 error   An unexpected error occurred
2022-09-29 15:56:22 error   Unauthorized access
2022-09-29 16:56:22 error   Unauthorized access
analyst@be37254e6899:~/logs$ cd /users
-bash: cd: /users: No such file or directory
analyst@be37254e6899:~/logs$ cd users
-bash: cd: users: No such file or directory
analyst@be37254e6899:~/logs$ pwd
/home/analyst/logs
analyst@be37254e6899:~/logs$ cd /home/analyst/users
-bash: cd: /home/analyst/users: No such file or directory
analyst@be37254e6899:~/logs$ cd /home/analyst/reports/users rs-bash: cd: too many arguments
analyst@be37254e6899:~/logs$ cd /home/analyst/reports/users   
analyst@be37254e6899:~/reports/users$ ls | grep "Q1"Q1_access.txt
Q1_added_users.txt
Q1_deleted_users.txt
analyst@be37254e6899:~/reports/users$ ls | grep "acess"
analyst@be37254e6899:~/reports/users$ ls | grep "access"
Q1_access.txt
Q2_access.txt
Q3_access.txt
Q4_access.txt
analyst@be37254e6899:~/reports/users$ grep "jhill" Q2_deleted_users.txt1025         jhill     Sales
analyst@be37254e6899:~/reports/users$ grep "Human Resources" Q4_added_users.txt
1151         sshah     Human Resources
1145         msosa     Human Resource
rcher2@fe10050be8f8:~$ cd projects
researcher2@fe10050be8f8:~/projects$ ls -l
total 20
drwx--x--- 2 researcher2 research_team 4096 Feb  9 00:50 drafts
-rw-rw-rw- 1 researcher2 research_team   46 Feb  9 00:50 project_k.txt
-rw-r----- 1 researcher2 research_team   46 Feb  9 00:50 project_m.txt
-rw-rw-r-- 1 researcher2 research_team   46 Feb  9 00:50 project_r.txt
-rw-rw-r-- 1 researcher2 research_team   46 Feb  9 00:50 project_t.txt
researcher2@fe10050be8f8:~/projects$ ls -la
total 32
drwxr-xr-x 3 researcher2 research_team 4096 Feb  9 00:50 .
drwxr-xr-x 3 researcher2 research_team 4096 Feb  9 01:37 ..
-rw--w---- 1 researcher2 research_team   46 Feb  9 00:50 .project_x.txt
drwx--x--- 2 researcher2 research_team 4096 Feb  9 00:50 drafts
-rw-rw-rw- 1 researcher2 research_team   46 Feb  9 00:50 project_k.txt
-rw-r----- 1 researcher2 research_team   46 Feb  9 00:50 project_m.txt
-rw-rw-r-- 1 researcher2 research_team   46 Feb  9 00:50 project_r.txt
-rw-rw-r-- 1 researcher2 research_team   46 Feb  9 00:50 project_t.txt
researcher2@fe10050be8f8:~/projects$ ls -l
total 20
drwx--x--- 2 researcher2 research_team 4096 Feb  9 00:50 drafts
-rw-rw-rw- 1 researcher2 research_team   46 Feb  9 00:50 project_k.txt
-rw-r----- 1 researcher2 research_team   46 Feb  9 00:50 project_m.txt
-rw-rw-r-- 1 researcher2 research_team   46 Feb  9 00:50 project_r.txt
-rw-rw-r-- 1 researcher2 research_team   46 Feb  9 00:50 project_t.txt
researcher2@fe10050be8f8:~/projects$ chmod o-w project_k.txt
researcher2@fe10050be8f8:~/projects$ ls -l
total 20
drwx--x--- 2 researcher2 research_team 4096 Feb  9 00:50 drafts
-rw-rw-r-- 1 researcher2 research_team   46 Feb  9 00:50 project_k.txt
-rw-r----- 1 researcher2 research_team   46 Feb  9 00:50 project_m.txt
-rw-rw-r-- 1 researcher2 research_team   46 Feb  9 00:50 project_r.txt
-rw-rw-r-- 1 researcher2 research_team   46 Feb  9 00:50 project_t.txt
researcher2@fe10050be8f8:~/projects$ chmod g-r project_m.txt
researcher2@fe10050be8f8:~/projects$ ls -la
total 32
drwxr-xr-x 3 researcher2 research_team 4096 Feb  9 00:50 .
drwxr-xr-x 3 researcher2 research_team 4096 Feb  9 01:37 ..
-rw--w---- 1 researcher2 research_team   46 Feb  9 00:50 .project_x.txt
drwx--x--- 2 researcher2 research_team 4096 Feb  9 00:50 drafts
-rw-rw-r-- 1 researcher2 research_team   46 Feb  9 00:50 project_k.txt
-rw------- 1 researcher2 research_team   46 Feb  9 00:50 project_m.txt
-rw-rw-r-- 1 researcher2 research_team   46 Feb  9 00:50 project_r.txt
-rw-rw-r-- 1 researcher2 research_team   46 Feb  9 00:50 project_t.txt
researcher2@fe10050be8f8:~/projects$ chmod u-w,g-w,g+r .project_x.txt
researcher2@fe10050be8f8:~/projects$ chmod g-r project_m.txt
researcher2@fe10050be8f8:~/projects$ ls -l
total 20
drwx--x--- 2 researcher2 research_team 4096 Feb  9 00:50 drafts
-rw-rw-r-- 1 researcher2 research_team   46 Feb  9 00:50 project_k.txt
-rw------- 1 researcher2 research_team   46 Feb  9 00:50 project_m.txt
-rw-rw-r-- 1 researcher2 research_team   46 Feb  9 00:50 project_r.txt
-rw-rw-r-- 1 researcher2 research_team   46 Feb  9 00:50 project_t.txt
researcher2@fe10050be8f8:~/projects$ chmod g-x drafts
sudo groupdel researcher9
analyst@33f308dd2afc:~$ sudo useradd researcher9
analyst@33f308dd2afc:~$ sudo usermod -g research_team researcher9
analyst@33f308dd2afc:~$ sudo useradd researcher9 -g research_team
useradd: user 'researcher9' already exists
analyst@33f308dd2afc:~$ sudo useradd researcher9 -g research_team
useradd: user 'researcher9' already exists
analyst@33f308dd2afc:~$ sudo chown researcher9 /home/researcher2/projects/project_r.txt
analyst@33f308dd2afc:~$ sudo usermod -a -G sales_team researcher9
analyst@33f308dd2afc:~$ sudo userdel researcher9
userdel: group researcher9 not removed because it is not the primary group of user researcher9.
analyst@33f308dd2afc:~$ sudo groupdel researcher9
sudo groupdel researcher9
analyst@50f1cc87d985:~$ sudo useradd researcher9
analyst@50f1cc87d985:~$ sudo usermod -g research_team researcher9
analyst@50f1cc87d985:~$ sudo useradd researcher9 -g research_team
useradd: user 'researcher9' already exists
analyst@50f1cc87d985:~$ sudo chown researcher9 /home/researcher2/projects/project_r.txt
analyst@50f1cc87d985:~$ sudo usermod -a -G sales_team researcher9
analyst@50f1cc87d985:~$ sudo userdel researcher9
userdel: group researcher9 not removed because it is not the primary group of user researcher9.
analyst@50f1cc87d985:~$ sudo groupdel researcher9
analyst@50f1cc87d985:~$ sudo chown researcher9 /home/researcher2/projects/project_r.txt
chown: invalid user: 'researcher9'
analyst@50f1cc87d985:~$ sudo useradd researcher9 -g research_teamanalyst@50f1cc87d985:~$ sudo chown researcher9 /home/researcher2/projects/project_r.txt
analyst@50f1cc87d985:~$ sudo usermod -a -G sales_team researcher9
analyst@50f1cc87d985:~$ sudo userdel researcher9
analyst@50f1cc87d985:~$ sudo groupdel researcher9
groupdel: group 'researcher9' does not exist
analyst@50f1cc87d985:~$ ^C
analyst@50f1cc87d985:~$ ^C
analyst@50f1cc87d985:~$ 