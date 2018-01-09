# MediaMath

Analytics Engineering Interview Task #1

•	Spin up a t1.micro instance on AWS (this is eligible for the AWS free tier – for 1 year)
•	Install Flask
o	Create a simple web application that performs two functions:
♣	1: Accepts input in a text-box called ‘delay’ that will then wait [delay] seconds before returning a CSV file (can be as a file download, not as plaintext if desired).. ex: 1.2.3.4:5000/csv_test
♣	2: Shows the number of csv downloaded, the delay, a timestamp of the download and any other useful information (client_ip, user agent, etc). ex: 1.2.3.4:5000/report
o	Enable this web application to return two requests concurrently. Ex: Open two tabs and load /csv_test at the same time. Both requests with delay = 10s return in 10s (not 20s).
♣	Please explain more than one approaches to tackle this problem – and the justification behind your choice.
•	Install MySQL (sqlite or mysql)
o	Record the number of times that the file is downloaded.
•	Explain possible sources of latency for the application above. What type of possible conditions may make latency better/worse?
•	[Bonus] What is the first thing you would do in order to “scale” this app up to 1MM possible users?


