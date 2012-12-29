
This algorithm is simulated by Disalgo which is based on python, and through defining a series of functions for sending 
and receiving message from one site to another.It takes N processes and R requests for each processes, and mutual 
exclusion is guaranteed while accessing the CS.

Before implementing this algorithm, defined a Binary Tree class to organize all sites into a complete binary Tree.
Then to implement this algorithm, defined two queues and a variable called “pending_request”. One is waiting queue 
which collects the requests from other site. The second is replying queue which collects the replies send from other 
sites.
Assume the site i request to enter CS, and it sends out requests to all the other sites that belong to the same quorum. 
Defined the following functions to handle the whole process:
OnRequest:
When one site received a request from site I, put the request onto its waiting queue in order. Check if it has replied 
to other site before. If it did not, send Reply(self) message to site i. Then check if the request from site i comes 
earlier than the request from the site that it has replied before If it does, make the “pending_request” to be the 
request from site i, then send Inquire(self) message to the site it replied before.

OnReply:
When one site received reply message from site j. Put site j onto its replying queue.

OnInquire:
When one site received Inquire message from site j. First check if the number of reply message it received is equal to 
the number of sites belong to the same quorum. If it is not, then send Yield message to site j.
Otherwise, send Relinquish message to all the sites belong to the same quorum.

OnYield:
When one site received Yield message from site j. Put “pending_request” onto its waiting queue in order. Pop out the 
earliest request from its waiting queue, and send reply for the site which sent that request before.

OnRelinquish:
When one site received Relinquish message from site j. remove site j from its request queue. Then check if its waiting 
queue is empty or not. If it is not, pop the request which comes the earliest from the waiting queue, and send Reply 
message to the site which sent that request.

When the number of replied message in the replying queue of site i is equal to the number of sites that belong to the 
same quorum, it would enter the CS.
When site i wants to exit the CS, it would send Relinquish message to all the sites that belong to the same quorum. 
Then upon receiving this message, those sites would release their reply for site i and send Reply message to other site.
