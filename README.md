# Demisto - Useful documentation
Some useful but not well documented stuff on Demisto aka Cortex XSOAR by Palo Alto Networks

# File System, Health Monitoring, and Logs
- Identify the file structure that Cortex XSOAR uses for software and data
- Define what to look for to confirm that the platform is working properly
- Describe the structure of the log file and the contents of the log bundle

## Primary Directory Locations
You should be aware of two primary directory locations.
### /var/lib/demisto/

![The /var/lib/demisto/ directory](/img/var-lib-demisto.png)

The **/var/lib/demisto/** directory contains system files and subdirectories that are variable, or subject to change. This 
directory is the root directory for artifacts, attachments, backups, the incidents database, downloads, jobs, version 
control data, and other dynamic data.

### /usr/local/demisto/

![The /usr/local/demisto/ directory](/img/usr-local-demisto.png)

The **/usr/local/demisto/** directory contains the application-server binary file, the private and public keys for the web 
interface, the license file, baseline platform content (resource files), and other distributed support files for running 
the web interface and other core functions.

## Cortex XSOAR Directory Locations for Key Assets
The following table lists several key assets and their directory locations for a standard Cortex XSOAR installation.

![Cortex XSOAR Directory Locations for Key Assets](/img/directories.png)

## Health Monitoring
To display high-level metrics for disk, CPU, and memory usage, navigate to the **Home [Dashboards] > System Health** page. 
The page displays updated information every 60 seconds. Look for yellow and red indicators for disk, CPU, or memory use. 
The default page refresh is every 10 minutes. 

The color for disk, CPU, and memory changes from green to yellow at 51% used and from yellow to red at 81% used. 

- Green indicates that baseline platform resources are sufficient for normal operation.
- Yellow indicates a condition to monitor relative to current performance and anticipated growth in system use and data 
storage.
- Red indicates that remediation steps should be assessed, especially with regard to disk use.

## Cortex XSOAR Troubleshooting Logs
You can use the Cortex XSOAR web interface to set the level of detail that the platform writes to its application log 
files. You also can use the web interface to download a copy of the log files. 

Log controls are located at the top of the **Settings > About > Troubleshooting** page.

### Debug
Debug causes the system to write many logs about the operational outcome of many procedural processes and subprocesses. 
The debug level is resource intensive. You typically should set the log level to debug only on advice from the technical 
support or customer success teams and/or problem-specific documentation.

### Info
Info is the default setting. It records events that are informative about general operational status and health. The 
info level includes all warning-level messages.

### Warning
Warning is the least active log level. It records only those events that indicate errors and failures or potential 
errors and failures.

## Log File Downloads
Perform the following steps to generate and download log files. 

![Log File Downloads](/img/logs-download.png)

### 1. Click Download logs.
Go to the **Settings > Troubleshooting** page and click **Download logs**. After you click **Download logs**, the 
browser makes a URL request to **https://<server-name-or-IP-address>/log/bundle**. 

### 2. Save the logs-bundle file and/or locate saved file. 
The URL request causes the application server to create a log bundle and return to the browser a tarball that contains 
the prepared logs. Your web browser will handle the download file based on its standard methods and your user settings.
The format of the name of the logs bundle is **logs-bundle-\<DD>\<MMM>\<YY>\<HH>_\<SS>\<ZZZ>.tar.gz**.

Note that the hours value <HH> directly follows the two-digit year value <YY>, which makes the combined values look 
like a four-digit year value.

The filename **logs-bundle-14Jul2004_50EDT.tar.gz** would be created for a Download logs request executed on 14 July, 
2020 at 04:50 AM Eastern Daylight Time.

### 3. Extract and review logs.
To display the contents of the tarball, use your preferred graphical archive manager or Linux CLI tools. Basic Linux 
commands are as follows:

- The **tar -tf \<filename>** command lists the filenames within the archive. 

- The **tar -xvzf \<filename>** command extracts the files and the **/var/lib/demist/temp/bundle<#########>/** directory 
structure to the current working directory.

## Files in the Logs Bundle
The Cortex XSOAR logs bundle contains over 20 individual log files. Some log files are copies of running logs to which 
the system writes operational information over time. Some logs provide copies of status output that the system generates 
at the time the log bundle is requested.

### Running Log Files
Some files in the log bundle are copies of log files that the system writes to continuously over time or for a period of 
time, such as during system boot or during an update.

![Running Log Files](/img/running-logs.png)

### Status Output Logs
Some files in the log bundle are copies of log files that the system writes to continuously over time or for a period of 
time, such as during system boot or during an update.

![Status Output Logs](/img/status-output-logs.png)
