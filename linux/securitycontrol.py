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
analyst@d4621645c026:~$ whatis cat
cat (1)              - concatenate files and print on the standard output
analyst@d4621645c026:~$ man cat
CAT(1)                        User Commands                       CAT(1)

NAME
       cat - concatenate files and print on the standard output

SYNOPSIS
       cat [OPTION]... [FILE]...

DESCRIPTION
       Concatenate FILE(s) to standard output.

       With no FILE, or when FILE is -, read standard input.

       -A, --show-all
              equivalent to -vET

       -b, --number-nonblank
              number nonempty output lines, overrides -n

       -e     equivalent to -vE

       -E, --show-ends
              display $ at end of each line

       -n, --number
              number all output lines

       -s, --squeeze-blank
              suppress repeated empty output lines

       -t     equivalent to -vT

       -T, --show-tabs
              display TAB characters as ^I

       -u     (ignored)

       -v, --show-nonprinting
              use ^ and M- notation, except for LFD and TAB

       --help display this help and exit

       --version
              output version information and exit

EXAMPLES
       cat f - g
              Output  f's  contents,  then standard input, then g's con-
              tents.

       cat    Copy standard input to standard output.

AUTHOR
       Written by Torbjorn Granlund and Richard M. Stallman.

REPORTING BUGS
       GNU coreutils  online  help:  <https://www.gnu.org/software/core-
       utils/>
       Report   cat   translation   bugs   to   <https://translationpro-
       ject.org/team/>

COPYRIGHT
       Copyright  (C)  2018  Free  Software  Foundation,  Inc.   License
       GPLv3+:   GNU   GPL   version  3  or  later  <https://gnu.org/li-
       censes/gpl.html>.
       This is free software: you are free to  change  and  redistribute
       it.  There is NO WARRANTY, to the extent permitted by law.

SEE ALSO
       tac(1)

       Full    documentation   at:   <https://www.gnu.org/software/core-
       utils/cat>
       or available locally via: info '(coreutils) cat invocation'

GNU coreutils 8.30            February 2019                       CAT(1)
analyst@d4621645c026:~$ 
analyst@d4621645c026:~$ 
analyst@d4621645c026:~$ 
analyst@d4621645c026:~$ 
analyst@d4621645c026:~$ 
analyst@d4621645c026:~$ 
analyst@d4621645c026:~$ 
analyst@d4621645c026:~$ 
analyst@d4621645c026:~$ 
analyst@d4621645c026:~$ 
analyst@d4621645c026:~$ 
analyst@d4621645c026:~$ 
analyst@d4621645c026:~$ 
analyst@d4621645c026:~$ 
analyst@d4621645c026:~$ 
analyst@d4621645c026:~$ 
analyst@d4621645c026:~$ 
analyst@d4621645c026:~$ 
analyst@d4621645c026:~$ 
analyst@d4621645c026:~$ 
analyst@d4621645c026:~$ 
analyst@d4621645c026:~$ 
analyst@d4621645c026:~$ 
analyst@d4621645c026:~$ 
analyst@d4621645c026:~$ 
analyst@d4621645c026:~$ 
analyst@d4621645c026:~$ 
analyst@d4621645c026:~$ 
analyst@d4621645c026:~$ 
analyst@d4621645c026:~$ 
analyst@d4621645c026:~$ 
analyst@d4621645c026:~$ 
analyst@d4621645c026:~$ 
analyst@d4621645c026:~$ 
analyst@d4621645c026:~$ 
analyst@d4621645c026:~$ 
analyst@d4621645c026:~$ 
analyst@d4621645c026:~$ 
analyst@d4621645c026:~$ 
analyst@d4621645c026:~$ 
analyst@d4621645c026:~$ 
analyst@d4621645c026:~$ apropos -a first part file
head (1)             - output the first part of files
analyst@d4621645c026:~$ man useradd
USERADD(8)             System Management Commands             USERADD(8)

NAME
       useradd - create a new user or update default new user
       information

SYNOPSIS
       useradd [options] LOGIN

       useradd -D

       useradd -D [options]

DESCRIPTION
       useradd is a low level utility for adding users. On Debian,
       administrators should usually use adduser(8) instead.

       When invoked without the -D option, the useradd command creates a
       new user account using the values specified on the command line
       plus the default values from the system. Depending on command
       line options, the useradd command will update system files and
       may also create the new user's home directory and copy initial
       files.

       By default, a group will also be created for the new user (see
       -g, -N, -U, and USERGROUPS_ENAB).

OPTIONS
       The options which apply to the useradd command are:

       -b, --base-dir BASE_DIR
           The default base directory for the system if -d HOME_DIR is
           not specified.  BASE_DIR is concatenated with the account
           name to define the home directory. If the -m option is not
           used, BASE_DIR must exist.

           If this option is not specified, useradd will use the base
           directory specified by the HOME variable in
           /etc/default/useradd, or /home by default.

       -c, --comment COMMENT
           Any text string. It is generally a short description of the
           login, and is currently used as the field for the user's full
           name.

       -d, --home-dir HOME_DIR
           The new user will be created using HOME_DIR as the value for
           the user's login directory. The default is to append the
           LOGIN name to BASE_DIR and use that as the login directory
           name. The directory HOME_DIR does not have to exist but will
           not be created if it is missing.

       -D, --defaults
           See below, the subsection "Changing the default values".

       -e, --expiredate EXPIRE_DATE
           The date on which the user account will be disabled. The date
           is specified in the format YYYY-MM-DD.

           If not specified, useradd will use the default expiry date
           specified by the EXPIRE variable in /etc/default/useradd, or
           an empty string (no expiry) by default.

       -f, --inactive INACTIVE
           The number of days after a password expires until the account
           is permanently disabled. A value of 0 disables the account as
           soon as the password has expired, and a value of -1 disables
           the feature.

           If not specified, useradd will use the default inactivity
           period specified by the INACTIVE variable in
           /etc/default/useradd, or -1 by default.

       -g, --gid GROUP
           The group name or number of the user's initial login group.
           The group name must exist. A group number must refer to an
           already existing group.

           If not specified, the behavior of useradd will depend on the
           USERGROUPS_ENAB variable in /etc/login.defs. If this variable
           is set to yes (or -U/--user-group is specified on the command
           line), a group will be created for the user, with the same
           name as her loginname. If the variable is set to no (or
           -N/--no-user-group is specified on the command line), useradd
           will set the primary group of the new user to the value
           specified by the GROUP variable in /etc/default/useradd, or
           100 by default.

       -G, --groups GROUP1[,GROUP2,...[,GROUPN]]]
           A list of supplementary groups which the user is also a
           member of. Each group is separated from the next by a comma,
           with no intervening whitespace. The groups are subject to the
           same restrictions as the group given with the -g option. The
           default is for the user to belong only to the initial group.

       -h, --help
           Display help message and exit.

       -k, --skel SKEL_DIR
           The skeleton directory, which contains files and directories
           to be copied in the user's home directory, when the home
           directory is created by useradd.

           This option is only valid if the -m (or --create-home) option
           is specified.

           If this option is not set, the skeleton directory is defined
           by the SKEL variable in /etc/default/useradd or, by default,
           /etc/skel.

           If possible, the ACLs and extended attributes are copied.

       -K, --key KEY=VALUE
           Overrides /etc/login.defs defaults (UID_MIN, UID_MAX, UMASK,
           PASS_MAX_DAYS and others).

           Example: -K PASS_MAX_DAYS=-1 can be used when creating system
           account to turn off password aging, even though system
           account has no password at all. Multiple -K options can be
           specified, e.g.: -K UID_MIN=100  -K UID_MAX=499

       -l, --no-log-init
           Do not add the user to the lastlog and faillog databases.

           By default, the user's entries in the lastlog and faillog
           databases are reset to avoid reusing the entry from a
           previously deleted user.

           For the compatibility with previous Debian's useradd, the -O
           option is also supported.

       -m, --create-home
           Create the user's home directory if it does not exist. The
           files and directories contained in the skeleton directory
           (which can be defined with the -k option) will be copied to
           the home directory.

           By default, if this option is not specified and CREATE_HOME
           is not enabled, no home directories are created.

       -M, --no-create-home
           Do no create the user's home directory, even if the system
           wide setting from /etc/login.defs (CREATE_HOME) is set to
           yes.

       -N, --no-user-group
           Do not create a group with the same name as the user, but add
           the user to the group specified by the -g option or by the
           GROUP variable in /etc/default/useradd.

           The default behavior (if the -g, -N, and -U options are not
           specified) is defined by the USERGROUPS_ENAB variable in
           /etc/login.defs.

       -o, --non-unique
           Allow the creation of a user account with a duplicate
           (non-unique) UID.

           This option is only valid in combination with the -u option.

       -p, --password PASSWORD
           The encrypted password, as returned by crypt(3). The default
           is to disable the password.

           Note: This option is not recommended because the password (or
           encrypted password) will be visible by users listing the
           processes.

           You should make sure the password respects the system's
           password policy.

       -r, --system
           Create a system account.

           System users will be created with no aging information in
           /etc/shadow, and their numeric identifiers are chosen in the
           SYS_UID_MIN-SYS_UID_MAX range, defined in /etc/login.defs,
           instead of UID_MIN-UID_MAX (and their GID counterparts for
           the creation of groups).

           Note that useradd will not create a home directory for such a
           user, regardless of the default setting in /etc/login.defs
           (CREATE_HOME). You have to specify the -m options if you want
           a home directory for a system account to be created.

       -R, --root CHROOT_DIR
           Apply changes in the CHROOT_DIR directory and use the
           configuration files from the CHROOT_DIR directory.

       -s, --shell SHELL
           The name of the user's login shell. The default is to leave
           this field blank, which causes the system to select the
           default login shell specified by the SHELL variable in
           /etc/default/useradd, or an empty string by default.

       -u, --uid UID
           The numerical value of the user's ID. This value must be
           unique, unless the -o option is used. The value must be
           non-negative. The default is to use the smallest ID value
           greater than or equal to UID_MIN and greater than every other
           user.

           See also the -r option and the UID_MAX description.

       -U, --user-group
           Create a group with the same name as the user, and add the
           user to this group.

           The default behavior (if the -g, -N, and -U options are not
           specified) is defined by the USERGROUPS_ENAB variable in
           /etc/login.defs.

       -Z, --selinux-user SEUSER
           The SELinux user for the user's login. The default is to
           leave this field blank, which causes the system to select the
           default SELinux user.

   Changing the default values
       When invoked with only the -D option, useradd will display the
       current default values. When invoked with -D plus other options,
       useradd will update the default values for the specified options.
       Valid default-changing options are:

       -b, --base-dir BASE_DIR
           The path prefix for a new user's home directory. The user's
           name will be affixed to the end of BASE_DIR to form the new
           user's home directory name, if the -d option is not used when
           creating a new account.

           This option sets the HOME variable in /etc/default/useradd.

       -e, --expiredate EXPIRE_DATE
           The date on which the user account is disabled.

           This option sets the EXPIRE variable in /etc/default/useradd.

       -f, --inactive INACTIVE
           The number of days after a password has expired before the
           account will be disabled.

           This option sets the INACTIVE variable in
           /etc/default/useradd.

       -g, --gid GROUP
           The group name or ID for a new user's initial group (when the
           -N/--no-user-group is used or when the USERGROUPS_ENAB
           variable is set to no in /etc/login.defs). The named group
           must exist, and a numerical group ID must have an existing
           entry.

           This option sets the GROUP variable in /etc/default/useradd.

       -s, --shell SHELL
           The name of a new user's login shell.

           This option sets the SHELL variable in /etc/default/useradd.

NOTES
       The system administrator is responsible for placing the default
       user files in the /etc/skel/ directory (or any other skeleton
       directory specified in /etc/default/useradd or on the command
       line).

CAVEATS
       You may not add a user to a NIS or LDAP group. This must be
       performed on the corresponding server.

       Similarly, if the username already exists in an external user
       database such as NIS or LDAP, useradd will deny the user account
       creation request.

       It is usually recommended to only use usernames that begin with a
       lower case letter or an underscore, followed by lower case
       letters, digits, underscores, or dashes. They can end with a
       dollar sign. In regular expression terms: [a-z_][a-z0-9_-]*[$]?

       On Debian, the only constraints are that usernames must neither
       start with a dash ('-') nor plus ('+') nor tilde ('~') nor
       contain a colon (':'), a comma (','), or a whitespace (space: '
       ', end of line: '\n', tabulation: '\t', etc.). Note that using a
       slash ('/') may break the default algorithm for the definition of
       the user's home directory.

       Usernames may only be up to 32 characters long.

CONFIGURATION
       The following configuration variables in /etc/login.defs change
       the behavior of this tool:

       CREATE_HOME (boolean)
           Indicate if a home directory should be created by default for
           new users.

           This setting does not apply to system users, and can be
           overridden on the command line.

       GID_MAX (number), GID_MIN (number)
           Range of group IDs used for the creation of regular groups by
           useradd, groupadd, or newusers.

           The default value for GID_MIN (resp.  GID_MAX) is 1000 (resp.
           60000).

       MAIL_DIR (string)
           The mail spool directory. This is needed to manipulate the
           mailbox when its corresponding user account is modified or
           deleted. If not specified, a compile-time default is used.

       MAIL_FILE (string)
           Defines the location of the users mail spool files relatively
           to their home directory.

       The MAIL_DIR and MAIL_FILE variables are used by useradd,
       usermod, and userdel to create, move, or delete the user's mail
       spool.

       MAX_MEMBERS_PER_GROUP (number)
           Maximum members per group entry. When the maximum is reached,
           a new group entry (line) is started in /etc/group (with the
           same name, same password, and same GID).

           The default value is 0, meaning that there are no limits in
           the number of members in a group.

           This feature (split group) permits to limit the length of
           lines in the group file. This is useful to make sure that
           lines for NIS groups are not larger than 1024 characters.

           If you need to enforce such limit, you can use 25.

           Note: split groups may not be supported by all tools (even in
           the Shadow toolsuite). You should not use this variable
           unless you really need it.

       PASS_MAX_DAYS (number)
           The maximum number of days a password may be used. If the
           password is older than this, a password change will be
           forced. If not specified, -1 will be assumed (which disables
           the restriction).

       PASS_MIN_DAYS (number)
           The minimum number of days allowed between password changes.
           Any password changes attempted sooner than this will be
           rejected. If not specified, -1 will be assumed (which
           disables the restriction).

       PASS_WARN_AGE (number)
           The number of days warning given before a password expires. A
           zero means warning is given only upon the day of expiration,
           a negative value means no warning is given. If not specified,
           no warning will be provided.

       SUB_GID_MIN (number), SUB_GID_MAX (number), SUB_GID_COUNT
       (number)
           If /etc/subuid exists, the commands useradd and newusers
           (unless the user already have subordinate group IDs) allocate
           SUB_GID_COUNT unused group IDs from the range SUB_GID_MIN to
           SUB_GID_MAX for each new user.

           The default values for SUB_GID_MIN, SUB_GID_MAX,
           SUB_GID_COUNT are respectively 100000, 600100000 and 10000.

       SUB_UID_MIN (number), SUB_UID_MAX (number), SUB_UID_COUNT
       (number)
           If /etc/subuid exists, the commands useradd and newusers
           (unless the user already have subordinate user IDs) allocate
           SUB_UID_COUNT unused user IDs from the range SUB_UID_MIN to
           SUB_UID_MAX for each new user.

           The default values for SUB_UID_MIN, SUB_UID_MAX,
           SUB_UID_COUNT are respectively 100000, 600100000 and 10000.

       SYS_GID_MAX (number), SYS_GID_MIN (number)
           Range of group IDs used for the creation of system groups by
           useradd, groupadd, or newusers.

           The default value for SYS_GID_MIN (resp.  SYS_GID_MAX) is 101
           (resp.  GID_MIN-1).

       SYS_UID_MAX (number), SYS_UID_MIN (number)
           Range of user IDs used for the creation of system users by
           useradd or newusers.

           The default value for SYS_UID_MIN (resp.  SYS_UID_MAX) is 101
           (resp.  UID_MIN-1).

       UID_MAX (number), UID_MIN (number)
           Range of user IDs used for the creation of regular users by
           useradd or newusers.

           The default value for UID_MIN (resp.  UID_MAX) is 1000 (resp.
           60000).

       UMASK (number)
           The file mode creation mask is initialized to this value. If
           not specified, the mask will be initialized to 022.

           useradd and newusers use this mask to set the mode of the
           home directory they create

           It is also used by pam_umask as the default umask value.

       USERGROUPS_ENAB (boolean)
           If set to yes, userdel will remove the user's group if it
           contains no more members, and useradd will create by default
           a group with the name of the user.

FILES
       /etc/passwd
           User account information.

       /etc/shadow
           Secure user account information.

       /etc/group
           Group account information.

       /etc/gshadow
           Secure group account information.

       /etc/default/useradd
           Default values for account creation.

       /etc/skel/
           Directory containing default files.

       /etc/subgid
           Per user subordinate group IDs.

       /etc/subuid
           Per user subordinate user IDs.

       /etc/login.defs
           Shadow password suite configuration.

EXIT VALUES
       The useradd command exits with the following values:

       0
           success

       1
           can't update password file

       2
           invalid command syntax

       3
           invalid argument to option

       4
           UID already in use (and no -o)

       6
           specified group doesn't exist

       9
           username already in use

       10
           can't update group file

       12
           can't create home directory

       14
           can't update SELinux user mapping

SEE ALSO
       chfn(1), chsh(1), passwd(1), crypt(3), groupadd(8), groupdel(8),
       groupmod(8), login.defs(5), newusers(8), subgid(5), subuid(5),
       userdel(8), usermod(8).

shadow-utils 4.5               07/27/2018                     USERADD(8)
analyst@d4621645c026:~$ 
analyst@d4621645c026:~$ 
analyst@d4621645c026:~$ 
analyst@d4621645c026:~$ 
analyst@d4621645c026:~$ 
analyst@d4621645c026:~$ 
analyst@d4621645c026:~$ 
analyst@d4621645c026:~$ 
analyst@d4621645c026:~$ 
analyst@d4621645c026:~$ 
analyst@d4621645c026:~$ 
analyst@d4621645c026:~$ 
analyst@d4621645c026:~$ 
analyst@d4621645c026:~$ 
analyst@d4621645c026:~$ 
analyst@d4621645c026:~$ 
analyst@d4621645c026:~$ 
analyst@d4621645c026:~$ 
analyst@d4621645c026:~$ 
analyst@d4621645c026:~$ 
analyst@d4621645c026:~$ 
analyst@d4621645c026:~$ 
analyst@d4621645c026:~$ 
analyst@d4621645c026:~$ 
analyst@d4621645c026:~$ 
analyst@d4621645c026:~$ 
analyst@d4621645c026:~$ whatis rm
rm (1)               - remove files or directories
analyst@d4621645c026:~$ whatis rmdir
rmdir (1)            - remove empty directories
rmdir (2)            - delete a directory
analyst@d4621645c026:~$ apropos -a create new group
groupadd (8)         - create a new group
analyst@d4621645c026:~$ ^C
analyst@d4621645c026:~$ 