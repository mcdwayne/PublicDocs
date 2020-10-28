#!/usr/local/bin/python
# coding: latin-1
import os, sys

#written by Dwayne McDaniel (mcdwayne on twitter 1dwaynemcdaniel on Drupal.org)
# for internal Pantheon use only, no license or copyright implemented.  

#start

print "\t\tWelcome my friend!"
namecheck='fail'
while namecheck=="fail":
	name=raw_input( "Hello. Can I first of all have your name (press enter after inputting ANY data)?")
	if len(name)>1:
		namecheck="pass"
	else: "\nHey man, I said enter your name THEN press the enter key!.....sheeeezzzzz"
		
print '\nHello there', name, 'thank you for interacting with me! I am the Pantheon FAQ Quiz! \n No this is not going to get you out of your test with Scott, but it might help you study :) \n\n'



print \
	  """I am going to ask you random questions from the FAQ as multiple choice.
Please answer as best as you can with either a :  '1', '2','3' or '4'. (Remember to press enter after your entry)
"""
raw_input('\n\n\t\t\tPress enter to begin the test')

rightAnswerCounter = 0

# if I change q1 to: q1=raw_input, then it wont accept any value, num or lett, and be in a continous loop


#question section
print "Question #1"
print name, "What is the difference between Business and Enterprise? Why is it so much more?"
print \
	  """
Best answer:
1) Enterprise offers an SLA with guaranteed uptime, 24x7 support, our pre-launch concierge, Pantheon’s managed scaling for when your site gets huge amounts of traffic, and High availability in a Master/Slave DB and multiple DROPs (containers)
2) Business offers an SLA with guaranteed uptime, 24x7 support, our pre-launch concierge, Pantheon’s managed scaling for when your site gets huge amounts of traffic, and High availability in a Master/Slave DB and multiple DROPs (containers)
3) Enterprise offers an SLA with 2 hour fixes, 24x7 support, our pre-launch concierge, Pantheon’s managed scaling for when your site gets huge amounts of traffic, and High availability in a Master/Slave DB and multiple DROPs (containers)
4) Just have 'em buy Acquia
"""
ok='no'
while ok== 'no':
	q1=int(raw_input('\nPlease Answer 1, 2, 3 or 4?  '))
	if q1 ==1:
		ok='yes'
		print "\nYep, correct", name
		rightAnswerCounter += 1	
	elif q1 ==2:
		ok='yes'
		print "\nclose, but no", name	
	elif q1==3:
		ok='yes'
		print "\nwell, partly right, but reread it"
	elif q1==4:
		ok='yes'
		print "\nPack up your shit and go home, you are fired"


raw_input('\n\n\t\tPress enter to continue the test')



#question 2

print 'Question #2'
print"\n\nWhy is there no SSL option for the Personal plan?"
print \
'''
Best Answer:
1) Our personal plan is only for small sites without any security needs, like a wiki or blog.  Sites requiring SSL should find hosting elsewhere.
2) That option is available via third party tools.
3) Our personal plan is only intended for sites with modest requirements such as small blogs and low traffic sites. Sites requiring SSL such as ecommerce sites, etc., should consider a more robust plan.
4) Our personal plan is only intended for sites with modest requirements such as small blogs and low traffic sites. Sites requiring SSL such as ecommerce sites, etc., must choose an Enterprise plan.
'''
ok='no'
while ok== 'no':
	
	q2=int (raw_input('\nPlease Answer 1, 2, 3 or 4?  '))
	
	if q2 ==1:
		print "\nWRONG!"
		ok='yes'
	elif q2 ==2:
		print "\nThis is just not right"
		ok='yes'
	elif q2==3:
		print "\nThis is the best answer, good job"
		ok='yes'
		rightAnswerCounter += 1	
	elif q2==4:
		print "\nBusiness and Professional ofer this (at additional costs)"
		ok='yes'


raw_input('\n\n\t\tPress enter to continue the test')



#question 3
print "\nQuestion #3"
print"\n\nWhy do you charge based on pageviews?"
print \
'''
Best Answer:
1) We don't specifically charge for the pageviews.  We are charging for authenticated users hitting the DB layer, pageviews just is an easier number to get for initial pricing calls to estimate a ball park range.
2) We don’t specifically charge for the pageviews.  We simply use monthly pageviews and database size as proxies for how many containers your site will require, and what the support demands are likely to be.
3) We charge per Varnish cache hits and Redis cache hits, which can be worked out via an algorithm around the total pageviews for an average site.  
4)We don't specifically charge for pageviews but we do charge for page lookups, which is in part determined by the total number of pageviews minus the Varnish Edge Report per month.
'''
ok='no'
while ok== 'no':
	
	q2=int (raw_input('\nPlease Answer 1, 2, 3 or 4?  '))
	
	if q2 ==1:
		print "\nNope, not that one!"
		ok='yes'
	elif q2 ==2:
		print "\nGreat job, best answer!"
		ok='yes'
		rightAnswerCounter += 1	
	elif q2==3:
		print "\nAre you paying attention?  Wrong"
		ok='yes'
	elif q2==4:
		print "\nWow, no, just no...."
		ok='yes'


raw_input('\n\n\t\tPress enter to continue the test')


#question 4
print"\nOkay lets look at Question #4", name
print"\n\nIf my website(s) grow in usage, will you charge me more?"
print \
'''
Best Answer:
1) We will not charge for occasional spikes or increased usage.  When your growth reaches the point where you have sustained increased usage, we will contact you and discuss moving to an appropriate plan if needed. We have these limits in the contracts to clearly define reasonable use. If you are to exceed any one for a short period of time, that is not a problem.  We have yet to bill anyone for a short term overage. However, if you are consistently above the allotted amount of resources we will have to discuss moving your plan to a higher tier Enterprise plan.
2) We do not charge for overage.  To date we have never done so.  If your site traffic grows ater signing an annual contract we will bear the burden of the load until the end of the contract period.  
3) We charge for every pageview and charge at a rate of 1.5x per every page view over the cap that hits the cache and 1.75x for trips to the origin server.  See your contract for average overage scenarios.  
4) Only in extreme cases of overage will we charge for spikes in traffic or data.  These limits are expressed in our SLA and can be found at the support site for Enterprise Customers.  We rarely need to pursue such charges.  
'''
ok='no'
while ok== 'no':
	
	q2=int (raw_input('\nPlease Answer 1, 2, 3 or 4?  '))
	
	if q2 ==1:
		print "\nThis is exactly the correct answer from the FAQ!"
		rightAnswerCounter += 1	
		ok='yes'
	elif q2 ==2:
		print "\nPartially right, but overall not god enough, sorry"
		ok='yes'
	elif q2==3:
		print "Did you even read the question or answers?"
		ok='yes'
	elif q2==4:
		print "Not the right answer, but I see how you got there"
		ok='yes'


raw_input('\n\n\t\tPress enter to continue the test')

#question 5 
print"\nOkay lets look at Question #5", name
print"\n\nWhat is included in my SLA?"
print \
'''
Best Answer:
1) Guaranteed turnaround on all open tickets with resolutions in 2 hours or less with a 99% uptime guarantee.
2) 24/7/365 phone support in case of any major outage.  Best Efforts will be used to resolve all issues to try and target 99.9% uptime.
3) 99.99% uptime guarantee.  
4) 99.9% uptime guarantee.  
'''
ok='no'
while ok== 'no':
	
	q2=int (raw_input('\nPlease Answer 1, 2, 3 or 4?  '))
	
	if q2 ==1:
		print "\nNOT the correct answer from the FAQ!"
		ok='yes'
	elif q2 ==2:
		print "\nNope"
		ok='yes'
	elif q2==3:
		print "\nCorrect"
		rightAnswerCounter += 1	
		ok='yes'
	elif q2==4:
		print "Not the right answer"
		ok='yes'


raw_input('\n\n\t\tPress enter to continue the test')


#question 6
print"\nOkay lets look at Question #6", name
print"\n\nCan I change the SLA?"
print \
'''
Best Answer:
1) Not unless you are on the Enterprise Max plan and then only with Executive approval (Scott + one other manager).  
2) It dependes on the site and the support burden.  
3) Our SLA is standard for all of our customers, so we do not alter it.  
4) Our SLA is standard for all of our self serve customers, Enterprise and Pantheon One customers can negotiate depending on their needs.  
'''
ok='no'
while ok== 'no':
	
	q2=int (raw_input('\nPlease Answer 1, 2, 3 or 4?  '))
	
	if q2 ==1:
		print "\nThis is wrong"
		ok='yes'
	elif q2 ==2:
		print "\nNope"
		ok='yes'
	elif q2==3:
		print "Yes, this is right"
		rightAnswerCounter += 1	
		ok='yes'
	elif q2==4:
		print "Not the right answer"
		ok='yes'


raw_input('\n\n\t\tPress enter to continue the test')


#question 7
print"\nOkay lets look at Question #7", name
print"\n\nWhat if I want to get my site up in less than 30 days? Does it have to take that long for me to transition my site?"
print \
'''
Best Answer:
1) Going through our pre-launch concierge is optional - we recommend it though as you have at your disposal the team that is responsible for successfully launching hundreds of Drupal sites. Statistically, you will have far fewer emergencies and support requests as well due to this process - and that is good for all of us.  During the 30 days, we will do load testing and provide you with a performance report and discuss with you any improvements we see for your site. We help you with configurations, such as setting up caching correctly, and help on any specific services that you might be using on Pantheon like Solr and New Relic
2) Do what you want, after all you are the customer and we are merely your humble servants.  
3) Going through our pre-launch concierge means that you will have a very successful go-live on Pantheon - you have at your disposal the team that is responsible for successfully launching hundreds of Drupal sites. Statistically, you will have far fewer emergencies and support requests as well due to this process - and that is good for all of us.  Normally lasting 30 days (this can be sped up for a fee, talk to your manager before approval), we will do load testing and provide you with a performance report and discuss with you any improvements we see for your site. We help you with configurations, such as setting up caching correctly, and help on any specific services that you might be using on Pantheon like Solr and New Relic
4) Going through our pre-launch concierge means that you will have a very successful go-live on Pantheon - you have at your disposal the team that is responsible for successfully launching hundreds of Drupal sites. Statistically, you will have far fewer emergencies and support requests as well due to this process - and that is good for all of us.  During the 30 days, we will do load testing and provide you with a performance report and discuss with you any improvements we see for your site. We help you with configurations, such as setting up caching correctly, and help on any specific services that you might be using on Pantheon like Solr and New Relic.
'''
ok='no'
while ok== 'no':
	
	q2=int (raw_input('\nPlease Answer 1, 2, 3 or 4?  '))
	
	if q2 ==1:
		print "\nNO!"
		ok='yes'
	elif q2 ==2:
		print "\nHa ha!"
		ok='yes'
	elif q2==3:
		print "not right, but dang close, read more carefully"
		ok='yes'
	elif q2==4:
		print "Yes!  Great work!"
		rightAnswerCounter += 1	
		ok='yes'


raw_input('\n\n\t\tPress enter to continue the test')

#question 8
print"\nOkay lets look at Question #8", name
print"\n\nWhat do enterprise customers receive on the platform that self serve plans do not?"
print \
'''
Best Answer:
1) Enterprise accounts get more containers and other resource instances. For many layers, this redundancy provides automatic HA failover. We handle downtime for enterprise accounts first. If a resource isn't automatically HA, we migrate, restore, and verify enterprise accounts first. We track uptime for the enterprise tier independently. Often, we're hitting 99.99% across this level. Downtime on an enterprise site automatically escalates to engineering/ops pagers. Enterprise on-boarding. This process is more than just time spent "consulting"; we have strong evidence that it produces successful launches. 
2) Enterprise accounts get more containers and other resource instances. For many layers, this redundancy provides automatic HA failover. We handle downtime for enterprise accounts first. If a resource isn't automatically HA, we migrate, restore, and verify enterprise accounts first. We track uptime for the enterprise tier independently. Often, we're hitting 99.99% across this level. Downtime on an enterprise site automatically escalates to engineering/ops pagers. They also get a 24x7x365 toll-free phone number to talk to a real person in the Bay Area who has a direct line to get Individual containers (DROPs and otherwise) get individually provisioned larger shares of resources. Enterprise on-boarding. This process is more than just time spent "consulting"; we have strong evidence that it produces successful launches. A gong ring and internal featuring on our wall boards. We love our enterprise customers, and we like everyone at the company to know and appreciate the business they provide us.  
3) Enterprise accounts get more containers and other resource instances. For many layers, this redundancy provides automatic HA failover. If a resource isn't automatically HA, we migrate, restore, and verify enterprise accounts first. We track uptime for the enterprise tier independently. Often, we're hitting 99.99% across this level. They also get a 24x7x365 toll-free phone number to talk to a real person in the Bay Area who has a direct line to get Individual containers (DROPs and otherwise) get individually provisioned larger shares of resources. Enterprise on-boarding. This process is more than just time spent "consulting"; we have strong evidence that it produces successful launches. A gong ring and internal featuring on our wall boards. We love our enterprise customers, and we like everyone at the company to know and appreciate the business they provide us.  
4) Enterprise accounts get more containers and other resource instances. For many layers, this redundancy provides automatic HA failover. We handle downtime for enterprise accounts first. If a resource isn't automatically HA, we migrate, restore, and verify enterprise accounts first. We track uptime for the enterprise tier independently. Often, we're hitting 99.99% across this level. Downtime on an enterprise site automatically escalates to engineering/ops pagers. They also get a 24x7x365 toll-free phone number to talk to a real person in the Bay Area who has a direct line to get Individual containers (DROPs and otherwise) get individually provisioned larger shares of resources. A gong ring and internal featuring on our wall boards. We love our enterprise customers, and we like everyone at the company to know and appreciate the business they provide us.  
'''
ok='no'
while ok== 'no':
	
	q2=int (raw_input('\nPlease Answer 1, 2, 3 or 4?  '))
	
	if q2 ==1:
		print "\nThis is NOT the correct answer!"
		ok='yes'
	elif q2 ==2:
		print "\nThis is exactly the correct answer from the FAQ!"
		rightAnswerCounter += 1	
		ok='yes'
	elif q2==3:
		print "Did you even read the question or answers?"
		ok='yes'
	elif q2==4:
		print "Not the right answer."
		ok='yes'


raw_input('\n\n\t\tPress enter to continue the test')

#question 9
print"\nOkay lets look at Question #9", name
print"\n\nI totally get the value, I just need the pricing now.  I have 3 sites, a bog one with about 1/2 million monthly page views and a DB around 1 gig.  My other sites are tiny and less than 10K monthly page views.  Give me the 'best value' quote please"
print \
'''
Best Answer:
1) For the large site we would charge you for Enterprise Starter ($1,500 a month) but the other sites would be better off with the self serve Pro option (only $100 a month each).
2)For the large site we would charge you for Enterprise Standard ($2,500 a month) but the other sites would be better off with the self serve Pro option (only $100 a month each).  
3) For the large site we would charge you for Enterprise Standard ($2,500 a month) but the other sites would be charged at Enterprise Starter Add On pricing (only $150 a month each).  
4) For the large site we would charge you for Enterprise Starter ($1,500 a month) but the other sites would be charged at Enterprise Starter Add On pricing (only $150 a month each).  
'''
ok='no'
while ok== 'no':
	
	q2=int (raw_input('\nPlease Answer 1, 2, 3 or 4?  '))
	
	if q2 ==1:
		print "\nNo. Go reread the price levels...we will wait."
		ok='yes'
	elif q2 ==2:
		print "\nRight for the first part, but NEVER just send them to self serve"
		ok='yes'
	elif q2==3:
		print "Best fit and best value...Well Done"
		rightAnswerCounter += 1	
		ok='yes'
	elif q2==4:
		print "Not the right answer, but I see how you got there, slightly too big for the starter"
		ok='yes'


raw_input('\n\n\t\tPress enter to continue the test')

#question 10
print"\nOkay lets look at Question #10", name
print"\n\nDo you provide DDOS mitigation support?"
print \
'''
Best Answer:
1) Nope.
2) In case of a Distributed Denial of Service (DDoS) attack we can enforce Force Majore in the contract en dump you as  since Pantheon is blameless in such attacks and your poor business practices are a liability to us.  
3) We will work with customers of any size to mitigate Distributed Denial of Service (DDoS) attacks. Some attacks can only be mitigated at the upstream network level. We are a Rackspace Cloud Marquee Customer and Tool Provider, and have direct, 24x7 access to our provider to deal with issues such as a DDoS. For application-level and infrastructure-level DDoS attacks, our engineering and ops team will work with customers to address the issue.
4)We will work with some Enterprise customers to mitigate Distributed Denial of Service (DDoS) attacks. Some attacks can only be mitigated at the upstream network level. We are a Rackspace Cloud Marquee Customer and Tool Provider, and have direct, 24x7 access to our provider to deal with issues such as a DDoS. For application-level and infrastructure-level DDoS attacks, our engineering and ops team will work with customers to address the issue.   
'''
ok='no'
while ok== 'no':
	
	q2=int (raw_input('\nPlease Answer 1, 2, 3 or 4?  '))
	
	if q2 ==1:
		print "\nThis is wrong! Obviously wrong!  Boo!"
		ok='yes'
	elif q2 ==2:
		print "\nDDoS is not an act of nature or God (although 4chan could be argued as a diety in certain cases."
		ok='yes'
	elif q2==3:
		print "Yes, Correct!"
		rightAnswerCounter += 1	
		ok='yes'
	elif q2==4:
		print "Not the right answer, but close, reread it and compare to answer 3."
		ok='yes'


raw_input('\n\n\t\tPress enter to continue the test')

#question 11
print"\nOkay lets look at Question #11", name
print"\n\n Assume you have finished qualifying for this one: Custom says: I just need the pricing.  I have 10 sites, 1 is my flagship with 12Million monthly pageviews and a DB over 20GB, 3 really big ones with about 5 million monthly page views and DBs around 4 gigs.  My other sites are tiny and less than 100K monthly page views each and very small DBs (500MB at most).  Give me the 'best value' quote please"
print \
'''
Best Answer:
1)This fits into our standard Pantheon One pricing: for the largest site we would charge you for Enterprise Max ($10,000 a month) but the other sites would be charged at Enterprise Add On pricing (only $12,000 a month for the larger ones and $900 for the tiny 6 sites).
2)For the large site we would charge you for Enterprise Max ($10,000 a month) and Enterprise Standard for the next smallest ($7,500 for all 3 a month) but the other sites would be better off with the self serve Pro option (only $100 a month each).  
3) Rather than quote per site, you are in a good position for Pantheon One, let's talk value and see if it make sense to find a price.  
4) For the largest site we would charge you for Enterprise Max ($10,000 a month) but the other sites would be charged at Enterprise Add On pricing (only $12,000 a month for the larger ones and $900 for the tiny 6 sites).  
'''
ok='no'
while ok== 'no':
	
	q2=int (raw_input('\nPlease Answer 1, 2, 3 or 4?  '))
	
	if q2 ==1:
		print "\nNo. Go reread the price levels...we will wait."
		ok='yes'
	elif q2 ==2:
		print "\nDo you secretly work for Acquia?  Not the right answer."
		ok='yes'
	elif q2==3:
		print "Probably the best answer"
		rightAnswerCounter += 1	
		ok='yes'
	elif q2==4:
		print "Not the right answer.  :("
		ok='yes'
		
		
raw_input('\n\n\t\tPress enter to continue the test')

#question 12
print"\nOkay lets look at Question #12", name
print"\n\nDo I have access to my server?"
print \
'''
Best Answer:
1) You can't be trusted with that kind of access.  Only people who hate Pantheon and think we are no good at this would even suggest they should have SSH access.  Really it is a bad sign if they are asking this as they don't get what we even do here.
2) On Pantheon you do not have shell (SSH) access. We have a single platform running tens of thousands of sites. We manage the whole platform to be 100% Drupal optimized, 100% managed and monitored. We would not be able to do this if tens of thousands of websites meant tens of thousands of servers each with their own custom software stack. Companies doing that can’t provide high level Drupal and platform support because they are too busy troubleshooting issues with the software stack on each of the individual environments that have been created..  
3) On Pantheon you do have shell (SSH) access. We have a single platform running tens of thousands of sites. We manage the whole platform to be 100% Drupal optimized, 100% managed and monitored. We are only able to do this since tens of thousands of websites and the related tens of thousands of servers each have their own custom software stack.   
4) On Pantheon you do not have shell (SSH) access. We do this since we understand Drupal much better than you and you would only break something.  We would not be able to do our jobs if tens of thousands of websites meant tens of thousands of servers each with their own custom software stack. Companies doing that can’t provide high level Drupal and platform support because they are too busy troubleshooting issues with the software stack on each of the individual environments that have been created.  
'''
ok='no'
while ok== 'no':
	
	q2=int (raw_input('\nPlease Answer 1, 2, 3 or 4?  '))
	
	if q2 ==1:
		print "\nThis is exactly wrong.  "
		ok='yes'
	elif q2 ==2:
		print "\nRight, Perfect in fact"
		rightAnswerCounter += 1	
		ok='yes'
	elif q2==3:
		print "Did you even read the question or answers?"
		ok='yes'
	elif q2==4:
		print "Not the right answer, but I see how you got there"
		ok='yes'


raw_input('\n\n\t\tPress enter to continue the test')

#question 13
print"\nOkay lets look at Question #13", name
print"\n\nHow do you optimize my website?"
print \
'''
Best Answer:

1) There are a number of software tools you need to install for optimizing your site for the cloud including:  Varnish Caching: Pantheon integrates a Varnish reverse-proxy caching layer, which is a standard tool for reducing the load on a Drupal site’s database and speeding anonymous responses. Using Varnish may mean reconfiguring how your site uses cookies, and making minor changes to cache configuration; no modules are required. Redis Caching: If you’ve written custom queries, use Drupal’s cache_set and cache_get to store and retrieve caches. Code/Query Optimization using tools by New Relic (Additional purchase required ). After a response has been built by Drupal, it needs to be transferred and rendered in the client browser.  Tools like YSlow and Google's PageSpeed Insights will identify bottlenecks. 

2)There are a number of solutions for optimizing your site for the cloud. A site should be built with a clear idea of what an acceptable performance profile is for anonymous and logged in users. Establishing this first can drive the site architecture and caching strategy. Here are other important steps: Varnish Caching: Pantheon integrates a Varnish reverse-proxy caching layer, which is a standard tool for reducing the load on a Drupal site’s database and speeding anonymous responses. Using Varnish may mean reconfiguring how your site uses cookies, and making minor changes to cache configuration; no modules are required. Redis Caching: By offsetting database requests using redis as the caching backend, you can greatly reduce the number of round trips required to build a page. If you’ve written custom queries, use Drupal’s cache_set and cache_get to store and retrieve caches. Code/Query Optimization: This may require analysis and refactoring of unwieldy queries or code optimization. In these circumstances, tools such as New Relic (included with every site),Devel, and the site’s slow query log (in the /logs directory) are valuable in determining the root of degraded or inefficient performance.
Front End Optimization: After a response has been built by Drupal, it needs to be transferred and rendered in the client browser. Reducing unnecessary markup, aggregating and compressing JavaScript and CSS, using a CDN for static content can help improve browser rendering time. Tools like YSlow and Google's PageSpeed Insights will identify bottlenecks. Module Evaluation: Lowering the number of enabled modules will reduce the overhead required by Drupal to perform any operation.
In short, a lightweight site is a happy site. By taking steps to optimize your site to take advantage of a cloud architecture, you’ll improve your users site experience and satisfaction.

3) There is nothing special to do as you go to production because our concierge serve done it all for you.   For example, we provide a Varnish Caching. Further, Pantheon integrates a Varnish reverse-proxy caching layer, which is a standard tool for reducing the load on a Drupal site’s database and speeding anonymous responses. Using Varnish may mean reconfiguring how your site uses cookies, and making minor changes to cache configuration; no modules are required. Redis Caching: By offsetting database requests using redis as the caching backend, you can greatly reduce the number of round trips required to build a page. If you’ve written custom queries, use Drupal’s cache_set and cache_get to store and retrieve caches. Code/Query Optimization: This may require analysis and refactoring of unwieldy queries or code optimization. In these circumstances, tools such as New Relic (included with every site),Devel, and the site’s slow query log (in the /logs directory) are valuable in determining the root of degraded or inefficient performance. Front End Optimization: After a response has been built by Drupal, it needs to be transferred and rendered in the client browser. Reducing unnecessary markup, aggregating and compressing JavaScript and CSS, using a CDN for static content can help improve browser rendering time. Tools like YSlow and Google's PageSpeed Insights will identify bottlenecks. Module Evaluation: Lowering the number of enabled modules will reduce the overhead required by Drupal to perform any operation.  
  
4) There are a number of solutions for optimizing your site for the cloud. A site should be built with a clear idea of what is maximum performance going to cost. Establishing this first can drive the site architecture and caching strategy. Here are other important steps:  Varnish: Pantheon does not integrate a Varnish reverse-proxy caching layer, this is something you need to implement yourself. Using Varnish may mean reconfiguring how your site uses cookies, and making minor changes to cache configuration; 10 new modules are required. Redis Caching: Redis should always be turned off as the caching backend, you can greatly reduce the number of round trips required to build a page. If you’ve written custom queries, use Drupal’s DB_set and DB_get to store and retrieve caches. Code/Query Optimization: This may require analysis and refactoring of unwieldy queries or code optimization. In these circumstances, tools such as New Relic (included with every site),Devel, and the site’s slow query log (in the /logs directory) are valuable in determining the root of degraded or inefficient performance. Front End Optimization: After a response has been built by Drupal, it needs to be transferred and rendered in the client browser. Reducing unnecessary markup, aggregating and compressing JavaScript and CSS, using a CDN for static content can help improve browser rendering time. Tools like YSlow and Google's PageSpeed Insights will identify bottlenecks. Module Evaluation: Lowering the number of enabled modules will reduce the overhead required by Drupal to perform any operation.
.  
'''
ok='no'
while ok== 'no':
	q2=int (raw_input('\nPlease Answer 1, 2, 3 or 4?  '))
	
	if q2 ==1:
		print "\nWrong"
		ok='yes'
	elif q2 ==2:
		print "\nCorrect"
		rightAnswerCounter += 1	
		ok='yes'
	elif q2==3:
		print "\nWrong"
		ok='yes'
	elif q2==4:
		print "\nWrong"
		ok='yes'


raw_input('\n\n\t\tPress enter to continue the test')

#question 14
print"\nOkay lets look at Question #14", name
print"\n\nDo you run antivirus software?"
print \
'''
Best Answer:
1) Pantheon runs Norton Anti-Virus and therefore prevents the installation of malware using established vendor repositories for software, software package signature verification, cryptographic validation of Pantheon’s own platform code during deployment, and auditable change-management.  Pantheon also regularly rebuilds servers (the same way many providers only do after a known breach), ensuring even an undetected, one-time breach would not persist. The platform runs user-published site software in containers with multiple layers of isolation. We run configurations that prevent direct execution, even within the containers, of files uploaded through the website. Customers are responsible for ensuring the software they publish via git (whether through the dashboard or via remote pushes) meets their own security standards. Pantheon provides the ClamAV antivirus/anti-malware utility with up-to-date databases for the use of our customers. The ClamAV Drupal module can be installed in your application to verify that files uploaded to a site are not infected and prevent them from being saved if they are. This allows customers to reduce their chance of disseminating malware to vulnerable site visitors (even though such dissemination would not affect the site’s or Pantheon’s own security).

2)  Pantheon runs exclusively open source server operating systems and relies heavily on 3d party packet analysis, software package signature verification, cryptographic validation of Pantheon’s own platform code during deployment, and auditable change-management. We run configurations that prevent direct execution, even within the containers, of files uploaded through the website. Customers are responsible for ensuring the software they publish via SFTP (whether through the dashboard or via remote pushes) meets their own security standards. Pantheon does not provide users any type of malware protection, such as ClamAV antivirus/anti-malware utility with up-to-date databases. This allows customers to reduce their chance of disseminating malware to vulnerable site visitors (even though such dissemination would not affect the site’s or Pantheon’s own security).

3)  Pantheon runs exclusively Unix-based server operating systems and therefore prevents the installation of malware using established vendor repositories for software, cryptographic validation of Pantheon’s own platform code during deployment, and audible change-management. It’s safer to whitelist what’s allowed to run than blacklist software that’s known to cause trouble. Pantheon also regularly rebuilds servers (the same way many providers only do after a known breach), ensuring even an undetected, one-time breach would not persist. The platform runs user-published site software in containers with multiple layers of isolation. We run configurations that prevent direct execution, even within the containers, of files uploaded through the website. Customers are responsible for ensuring the software they publish via git (whether through the dashboard or via remote pushes) meets their own security standards. Pantheon provides the ClamAV antivirus/anti-malware utility with up-to-date databases for the use of our customers. The ClamAV Drupal module can be installed in your application to verify that files uploaded to a site are not infected and prevent them from being saved if they are. This allows customers to reduce their chance of disseminating malware to vulnerable site visitors (even though such dissemination would not affect the site’s or Pantheon’s own security).

4)  Pantheon runs exclusively Linux-based server operating systems and therefore prevents the installation of malware using established vendor repositories for software, software package signature verification, cryptographic validation of Pantheon’s own platform code during deployment, and auditable change-management. It’s safer to whitelist what’s allowed to run than blacklist software that’s known to cause trouble. Pantheon also regularly rebuilds servers (the same way many providers only do after a known breach), ensuring even an undetected, one-time breach would not persist. The platform runs user-published site software in containers with multiple layers of isolation. We run configurations that prevent direct execution, even within the containers, of files uploaded through the website. Customers are responsible for ensuring the software they publish via git (whether through the dashboard or via remote pushes) meets their own security standards. Pantheon provides the ClamAV antivirus/anti-malware utility with up-to-date databases for the use of our customers. The ClamAV Drupal module can be installed in your application to verify that files uploaded to a site are not infected and prevent them from being saved if they are. This allows customers to reduce their chance of disseminating malware to vulnerable site visitors (even though such dissemination would not affect the site’s or Pantheon’s own security).
'''
ok='no'
while ok== 'no':
	
	q2=int (raw_input('\nPlease Answer 1, 2, 3 or 4?  '))
	
	if q2 ==1:
		print "\nWrong"
		ok='yes'
	elif q2 ==2:
		print "\nWrong"
		ok='yes'
	elif q2==3:
		print "\nWrong"
		ok='yes'
	elif q2==4:
		print "\nCorrect"
		rightAnswerCounter += 1	
		ok='yes'


raw_input('\n\n\t\tPress enter to continue the test')

#question 15
print"\nOkay lets look at Question #15", name
print"\n\nI know that Pantheon basically ignores the core drupal files from client repos and uses a _clean_ version of core drupal. What about contrib modules? We have one contrib module that we've needed to patch for performance reasons and want to make sure that this will still be maintained in Pantheon's environment."
print \
'''
Best Answer:

1) We restrict the contrib module or theme code options. As we scale we can not account for all module issues and are forced to limit which modules can be used.  Patching these is fully supported, as is installing development versions or specific releases. That does also mean that deciding when to upgrade contribs (and to what version) is also not your responsibility — which makes sense given the somewhat uneven update habits of different contrib maintainers.  I should also point out that if you do have a need to patch Drupal core this can be supported: you'll just need to apply those patches after importing to Pantheon so that we can retain a record of the change in the git version control history. Most people never need to do this, but the capability is there if necessary.

2)We don't restrict or interfere with any of the contrib module or theme code. Patching these is fully supported, as is installing development versions or specific releases. That does also mean that deciding when to upgrade contribs (and to what version) is also your responsibility — which makes sense given the somewhat uneven update habits of different contrib maintainers.  I should also point out that if you do have a need to patch Drupal core this can be supported: you'll just need to apply those patches after importing to Pantheon so that we can retain a record of the change in the git version control history. Most people never need to do this, but the capability is there if necessary.  

3) We don't restrict or interfere with any of the contrib module or theme code. Patching these is not supported though, as the overhead is a support nightmare. That does also mean that deciding when to upgrade contribs (and to what version) is a shared responsibility — which makes sense given the somewhat uneven update habits of different contrib maintainers and our community requesting updates.  I should also point out that if you do have a need to patch Drupal core this can not be supported.  Most people wold want to do this, but the capability is there if necessary.  

4) We don't restrict or interfere with any of the core, contrib module or theme code.  Deciding when to upgrade contribs (and to what version) is completely our (Pantheon's) responsibility — which makes sense given the somewhat uneven update habits of different contrib maintainers makes this hard to individualy manage.  I should also point out that if you do have a need to patch Drupal core this can be supported: you'll just need to apply those patches after importing to Pantheon so that we can retain a record of the change in the git version control history. Most people never need to do this, but the capability is there if necessary..  
'''
ok='no'
while ok== 'no':
	
	q2=int (raw_input('\nPlease Answer 1, 2, 3 or 4?  '))
	
	if q2 ==1:
		print "\nWrong"
		ok='yes'
	elif q2 ==2:
		print "\nCorrect"
		rightAnswerCounter += 1	
		ok='yes'
	elif q2==3:
		print "\nWrong"
		ok='yes'
	elif q2==4:
		print "\nWrong"
		ok='yes'


raw_input('\n\n\t\tPress enter to continue the test')

#question 16
print"\nOkay lets look at Question #16", name
print"\n\nWhat’s the difference between containers and virtual machines?"
print \
'''
Best Answer:	
1) Virtual machines and Containers are essentially the same thing.  They are an entire stack starting with an operating system and all other related software components required to run the VM.  Each time a VM is needed, then entire software stack must be started, but leveraging only the essential part of a stack to run PHP code.  It requires an entire stack to boot up, therefore the overhead is significantly less, and the operations are faster when starting a new container.


2) Virtual machines are leveraging only the essential part of a stack to run PHP code.  It does not require an entire stack to boot up like a container would, therefore the overhead is significantly less, and the operations are faster when starting a new VM.
A container is an entire stack starting with an operating system and all other related software components required to run the container.  Each time a container is needed, then entire software stack must be started.  This takes time and adds overhead.  

3) Virtual machines are an entire dedicated piece of hardware and all the related software components required to run the VM.  Each time a VM is needed, then a new server must be started.  This takes time and adds overhead.
A container is leveraging only the essential part of a stack to run a new Operating System.  It does not require an entire stack to boot up like a new VM would, therefore the overhead is significantly less, and the operations are faster when starting a new container.
  
4) Virtual machines are an entire stack starting with an operating system and all other related software components required to run the VM.  Each time a VM is needed, then entire software stack must be started.  This takes time and adds overhead.
A container is leveraging only the essential part of a stack to run PHP code.  It does not require an entire stack to boot up like a new VM would, therefore the overhead is significantly less, and the operations are faster when starting a new container.  
'''
ok='no'
while ok== 'no':
	
	q2=int (raw_input('\nPlease Answer 1, 2, 3 or 4?  '))
	
	if q2 ==1:
		print "\nWrong"
		ok='yes'
	elif q2 ==2:
		print "\nWrong"
		ok='yes'
	elif q2==3:
		print "\nWrong"
		ok='yes'
	elif q2==4:
		print "\nCorrect"
		rightAnswerCounter += 1	
		ok='yes'


raw_input('\n\n\t\tPress enter to continue the test')

#question 17
print"\nOkay lets look at Question #17", name
print"\n\n•	What is Varnish?"
print \
'''
Best Answer:
1) Varnish is an HTTP accelerator designed for content-heavy dynamic web sites. In contrast to other web accelerators, such as Squid, which began life as a client-side cache, or Apache and nginx, which are primarily origin servers, Varnish was designed as an HTTP accelerator. Varnish is focused exclusively on HTTP, unlike other proxy servers that often support FTP, SMTP and other network protocols.
2) Varnish is a Drupal accelerator designed for content-heavy dynamic web sites. In contrast to other web accelerators, Varnish is focused exclusively on Drupal, unlike other proxy servers that often support WordPress, Joomla and other CMS frameworks.  
3) Varnish is something you paint onto wood to preserve the look and strength.  Pantheon started life as a woodworking shop and we kept the name since we had a giant barrel (which we still have in the supply closet, ask Aviva to see it).    
4) Varnish is an open source cache designed for content-heavy dynamic web sites. In contrast to other caches, such as Redis, which began life as a client-side cache, or Apache and nginx, which are primarily origin servers, Varnish was designed as Drupal specific site cache. Varnish is focused exclusively on Drupal, unlike other proxy servers that often support JavaScript, Ruby and other frameworks.  
'''
ok='no'
while ok== 'no':
	
	q2=int (raw_input('\nPlease Answer 1, 2, 3 or 4?  '))
	
	if q2 ==1:
		print "\nCorrect"
		rightAnswerCounter += 1	
		ok='yes'
	elif q2 ==2:
		print "\nWrong"
		ok='yes'
	elif q2==3:
		print "\nWrong"
		ok='yes'
	elif q2==4:
		print "\nWrong"
		ok='yes'


raw_input('\n\n\t\tPress enter to continue the test')

#question 18
print"\nOkay lets look at Question #18", name
print"\n\nWhat is Redis?"
print \
'''
Best Answer:
1) Redis is an open-source, networked, on-disk, DB value data store with optional durability. It is written in ANSI C. The development of Redis has been sponsored by Pivotal since May 2013;[1] until then, it was sponsored by VMWare.[2][3] According to the monthly ranking by DB-Engines.com, Redis is the most popular key-value store.
2) Redis is our proprietary, networked, in-memory, key-value data store with optional durability. It is written in ANSI C. The development of Redis has been sponsored by Pivotal since May 2013;[1] until then, it was sponsored by Microsoft. [2][3] According to the monthly ranking by DB-Engines.com, Redis is the least popular key-value store.
3) Redis is an open-source, networked, in-memory, key-value data store with optional durability. It is written in ANSI C. The development of Redis has been sponsored by Pivotal since May 2013;[1] until then, it was sponsored by VMWare.[2][3] According to the monthly ranking by DB-Engines.com, Redis is the most popular key-value store.  
4) Redis is our proprietary, networked, in-memory, key-value data store with optional durability. It is written in ANSI C. The development of Redis by Pantheon has gone on since May 2012;   
'''
ok='no'
while ok== 'no':
	
	q2=int (raw_input('\nPlease Answer 1, 2, 3 or 4?  '))
	
	if q2 ==1:
		print "\nWrong"
		ok='yes'
	elif q2 ==2:
		print "\nWrong"
		ok='yes'
	elif q2==3:
		print "\nCorrect"
		rightAnswerCounter += 1	
		ok='yes'
	elif q2==4:
		print "\nWrong"
		ok='yes'


raw_input('\n\n\t\tPress enter to continue the test')

#question 19
print"\nOkay lets look at Question #19", name
print"\n\nWhat is Valhalla? Is a distributed file system better and why?"
print \
'''
Best Answer:
1) Valhalla is Pantheon’s file system that duplicates the storage and retrieval of files used in websites for maximum H/A. If anyone cares to know the origin of the word: In Norse mythology, Valhalla (from Old Norse Valhöll "hall of the slain"[1]) is a majestic, enormous hall located in Asgard, ruled over by the godOdin.
2) Valhalla is Pantheon’s file system that optimizes the storage and retrieval of files used in websites. If anyone cares to know the origin of the word: In Norse mythology, Valhalla (from Old Norse Valhöll "hall of the slain"[1]) is a majestic, enormous hall located in Asgard, ruled over by the godOdin  
3)Valhalla is Pantheon’s DB system that optimizes the storage and retrieval of files used in websites. If anyone cares to know the origin of the word: In Norse mythology, Valhalla (from Old Norse Valhöll "hall of the slain"[1]) is a majestic, enormous hall located in Asgard, ruled over by the godOdin.  
4) Valhalla is Pantheon’s front end cache that optimizes the storage and retrieval of files used in websites. If anyone cares to know the origin of the word: In Norse mythology, Valhalla (from Old Norse Valhöll "hall of the slain"[1]) is a majestic, enormous hall located in Asgard, ruled over by the godOdin.  
'''
ok='no'
while ok== 'no':
	
	q2=int (raw_input('\nPlease Answer 1, 2, 3 or 4?  '))
	
	if q2 ==1:
		print "\nWrong"
		ok='yes'
	elif q2 ==2:
		print "\nCorrect"
		rightAnswerCounter += 1	
		ok='yes'
	elif q2==3:
		print "\nWrong"
		ok='yes'
	elif q2==4:
		print "\nWrong"
		ok='yes'


raw_input('\n\n\t\tPress enter to continue the test')

#question 20
print"\nOkay lets look at Question #20", name
print"\n\nWhat is Solr?"
print \
'''
Best Answer:
1) Solr (pronounced "solar") is a Windows specific enterprise search platform from the Microsoft Community project. Its major features include full-text search, hit highlighting, faceted search, dynamic clustering, database integration, and rich document (e.g., Word, PDF) handling. Providing distributed search and index replication, Solr is highly scalable.[1] Solr is the most popular enterprise search engine.
2) Solr (pronounced "solar") is an open source enterprise search platform from the Apache Lucene project. Its major features include partial-text search, hit commenting, dynamic clustering, database Duplication, and rich document (e.g., Word, PDF) handling. Providing distributed search and index replication, Solr is highly scalable.[1] Solr is the 3rd most popular enterprise search engine.  
3) Solr (pronounced "solar") is an open source enterprise search platform from the Apache Lucene project. Its major features include full-text search, hit highlighting, faceted search, static clustering, database integration, and rich document (e.g., Word, PDF) handling. Providing distributed search and index replication, Solr is meant for only single sites and only scales through our magic.[1] Solr is the most popular enterprise search engine.  
4) Solr (pronounced "solar") is an open source enterprise search platform from the Apache Lucene project. Its major features include full-text search, hit highlighting, faceted search, dynamic clustering, database integration, and rich document (e.g., Word, PDF) handling. Providing distributed search and index replication, Solr is highly scalable.[1] Solr is the most popular enterprise search engine.  
'''
ok='no'
while ok== 'no':
	
	q2=int (raw_input('\nPlease Answer 1, 2, 3 or 4?  '))
	
	if q2 ==1:
		print "\nWrong"
		ok='yes'
	elif q2 ==2:
		print "\nWrong"
		ok='yes'
	elif q2==3:
		print "\nWrong"
		ok='yes'
	elif q2==4:
		print "\nCorrect"
		rightAnswerCounter += 1	
		ok='yes'


raw_input('\n\n\t\tPress enter to continue the test')

#question 21
print"\nOkay lets look at Question #21", name
print"\n\nWhat is Git?"
print \
'''
Best Answer:
1) Git /ɡɪt/ is a distributed revision control and source code management (SCM) system with an emphasis on speed.[4] Git was initially designed and developed by Linus Torvalds for Linux kernel development in 2005. Based on a recent survey of Eclipse IDE users, Git is reported to have 30% adoption as of 2013. Every Git working directory is a full-fledged repository with complete history and full version tracking capabilities, not dependent on network access or a central server. Git is proprietary and owned by GitHub.
2) Git /ɡɪt/ is a distributed revision control and source code management (SCM) system with an emphasis on speed.[4] Git was initially designed and developed by Linus Torvalds for Linux kernel development in 2005. Based on a recent survey of Eclipse IDE users, Git is reported to have 30% adoption as of 2013. Every Git working directory is a full-fledged repository with complete history and full version tracking capabilities, not dependent on network access or a central server. Git is free software distributed under the terms of the GNU General Public License version 2.  
3) Git /ɡɪt/ is a distributed revision control and source code management (SCM) system with an emphasis on speed.[4] Git was initially designed and developed by Linus Torvalds for Linux kernel development in 2005. Based on a recent survey of Eclipse IDE users, Git is reported to have 70% adoption as of 2013. Every Git working directory is a full-fledged repository with complete history and full version tracking capabilities and is completely dependent on network access and a central server. Git is free software distributed under the terms of the GNU General Public License version 2.  
4) Git /ɡɪt/ is a central revision control and source code management (SCM) system with an emphasis on network connective correctness.[4] Git was initially designed and developed by Linus Torvalds for Linux kernel development in 2005. Based on a recent survey of Eclipse IDE users, Git is reported to have 30% adoption as of 2013. Every Git working directory is a full-fledged repository with complete history and full version tracking capabilities, not dependent on network access or a central server. Git is proprietary and owned by GitHub.  
'''
ok='no'
while ok== 'no':
	
	q2=int (raw_input('\nPlease Answer 1, 2, 3 or 4?  '))
	
	if q2 ==1:
		print "\nWrong"
		ok='yes'
	elif q2 ==2:
		print "\nCorrect"
		rightAnswerCounter += 1	
		ok='yes'
	elif q2==3:
		print "\nWrong"
		ok='yes'
	elif q2==4:
		print "\nWrong"
		ok='yes'


raw_input('\n\n\t\tPress enter to continue the test')

#question 22
print"\nOkay lets look at Question #22", name
print"\n\nWhat is Drush?"
print \
'''
Best Answer:
1) Drush is a shell-based application used to control, manipulate, and administer Drupal sites.
2) Drush is a shell-based application used to control, manipulate, and administer any CMS based sites.
3) Drush is a GUI application used to control, manipulate, and administer Linux sites.
4) Drush is a GUI application used to control, manipulate, and administer Drupal sites.
'''
ok='no'
while ok== 'no':
	
	q2=int (raw_input('\nPlease Answer 1, 2, 3 or 4?  '))
	
	if q2 ==1:
		print "\nCorrect"
		rightAnswerCounter += 1	
		ok='yes'
	elif q2 ==2:
		print "\nWrong"
		ok='yes'
	elif q2==3:
		print "\nWrong"
		ok='yes'
	elif q2==4:
		print "\nWrong"
		ok='yes'


raw_input('\n\n\t\tPress enter to continue the test')

#question 23
print"\nOkay lets look at Question #23", name
print"\n\nWhat is Nginx?"
print \
'''
Best Answer:
1) Nginx (pronounced "engine x") is an open source reverse proxy server for HTTP, HTTPS, SMTP, POP3, and IMAP protocols, as well as a load balancer, HTTP cache, and a web server (origin server). The nginx project started with a strong focus on high concurrency, high performance and low memory usage. It is licensed under the 2-clause BSD-like license and it only runs on Linux.  It will not run on BSD variants, Mac OS X, Solaris, AIX, HP-UX, as well as on other *nix flavors. There is rumor of port for Microsoft Windows.
2) Nginx (pronounced "engine x") is an open source reverse proxy server for HTTP, HTTPS, SMTP, POP3, and IMAP protocols, as well as a load balancer, HTTP cache, and a web server (origin server). The nginx project started with a strong focus on high concurrency, high performance and low memory usage. It is licensed under the 2-clause BSD-like license and it runs on Linux, BSD variants, Mac OS X, Solaris, AIX, HP-UX, as well as on other *nix flavors. It also has a proof of concept port for Microsoft Windows.
3) Nginx (pronounced "engine x") is our proprietary proxy server for HTTP, HTTPS, SMTP, POP3, and IMAP protocols, as well as a load balancer, HTTP cache, and a web server (origin server). The nginx project started with a strong focus on high concurrency, high performance and low memory usage. It is licensed under the 2-clause Pantheon license and it runs on Linux, BSD variants, Mac OS X, Solaris, AIX, HP-UX, as well as on other *nix flavors. It also has a proof of concept port for Microsoft Windows.
4) Nginx (pronounced "engine x") is our proprietary proxy server for HTTP and requires a  load balancer and HTTP cache. The nginx project started with a strong focus on high concurrency, high performance and low memory usage. It is licensed under the 2-clause Pantheon license and it runs on Linux, BSD variants, Mac OS X, Solaris, AIX, HP-UX, as well as on other *nix flavors. It also has a proof of concept port for Microsoft Windows.
'''
ok='no'
while ok== 'no':
	
	q2=int (raw_input('\nPlease Answer 1, 2, 3 or 4?  '))
	
	if q2 ==1:
		print "\nWrong"
		ok='yes'
	elif q2 ==2:
		print "\nCorrect"
		rightAnswerCounter += 1	
		ok='yes'
	elif q2==3:
		print "\nWrong"
		ok='yes'
	elif q2==4:
		print "\nWrong"
		ok='yes'


raw_input('\n\n\t\tPress enter to continue the test')

#question 24
print"\nOkay lets look at Question #24", name
print"\n\nWhat components are included in the initial setup (i.e. nginx + php-fpm + APC, redis, varnish, solr)"
print \
'''
Best Answer:
1) Some containers are created equally; free accounts are underpowered. Only Live environments use PHP 5.3 (PHP-FPM). For a comprehensive list of what's installed, use phpinfo()
•	Packages: APC (Alternative PHP Cache), LDAP, SOAP, GD, Mcrypt, MySQL, Imagick (ImageMagick), PDO, mbstring, XML, IMAP
•	Extensions: APC, New Relic, OAuth, redis
•	Maximum PHP execution time is 360 seconds
•	Maximum upload_max_filesize and post_max_size is 10MB
•	Each PHP process has 512MB of memory (independent on the plan)
 
2) All containers are created equally; free accounts are not underpowered. All environments use PHP 5.3 (PHP-FPM). For a comprehensive list of what's installed, use phpinfo()
•	Packages not allowed: APC (Alternative PHP Cache), LDAP, SOAP, GD, Mcrypt, MySQL, Imagick (ImageMagick), PDO, mbstring, XML, IMAP
•	Extensions not allowed: APC, New Relic
•	Maximum PHP execution time is 9 seconds
•	Maximum upload_max_filesize and post_max_size is 10KB
•	Each PHP process can either 256MB or 512MB of memory (depends on the plan)
   
3) Some containers are created equally; free accounts are sometimes underpowered. All environments use PHP 5.3 (PHP-FPM). For a comprehensive list of what's installed, use phpinfo()
•	Packages: APC (Alternative PHP Cache), LDAP, SOAP, GD, Mcrypt, MySQL, Imagick (ImageMagick), PDO, 
•	Extensions: redis
•	Maximum PHP execution time is 5000 seconds
•	Maximum upload_max_filesize and post_max_size is 100GB
•	Each PHP process can either 256MB or 512MB of memory (depends on the plan)
  
4) All containers are created equally; free accounts are not underpowered. All environments use PHP 5.3 (PHP-FPM). For a comprehensive list of what's installed, use phpinfo()
•	Packages: APC (Alternative PHP Cache), LDAP, SOAP, GD, Mcrypt, MySQL, Imagick (ImageMagick), PDO, mbstring, XML, IMAP
•	Extensions: APC, New Relic, OAuth, redis
•	Maximum PHP execution time is 90 seconds
•	Maximum upload_max_filesize and post_max_size is 100MB
•	Each PHP process can either 256MB or 512MB of memory (depends on the plan)
 
'''
ok='no'
while ok== 'no':
	
	q2=int (raw_input('\nPlease Answer 1, 2, 3 or 4?  '))
	
	if q2 ==1:
		print "\nWrong"
		ok='yes'
	elif q2 ==2:
		print "\nWrong"
		ok='yes'
	elif q2==3:
		print "\nWrong"
		ok='yes'
	elif q2==4:
		print "\nCorrect"
		rightAnswerCounter += 1	
		ok='yes'


raw_input('\n\n\t\tPress enter to continue the test')

#question 25
print"\nOkay lets look at Question #25", name
print"\n\nHow do you scale my site? Is it manual or automated?"
print \
'''
Best Answer:
1) Pantheon is the only Linux platform that scales entirely in software. Our infrastructure is more similar to the modern web and services like Craigslist and Google Search than it is to more stable legacy hosting that has been around since the dawn of web hosting.  The scaling process means that you are not punished for success. At the Enterprise level, we scale resources for you.  At the self-serve level, you can scale yourself by moving up plans. Manual scaling is best because we can provide exactly what you need, and detect and mitigate issues that you wouldn’t want automated scaling for (DDOS attack for example).

2) Pantheon is the only Drupal platform that scales entirely in software. Our infrastructure is more similar to the modern web and services like Heroku and Google App Engine than it is to the old school, legacy hosting that has been around since the dawn of web hosting.  The scaling process means that you are not punished for success. At the Enterprise level, we scale resources for you.  At the self-serve level, you can scale yourself by moving up plans. Manual scaling is best because we can provide exactly what you need, and detect and mitigate issues that you wouldn’t want automated scaling for (DDOS attack for example).

3) Pantheon is the only Drupal platform that scales entirely in software. Our infrastructure is more similar to the modern web and services like Heroku and Google App Engine than it is to the old school, legacy hosting that has been around since the dawn of web hosting.  At the all levels, you must scale yourself by moving up plans. Manual scaling is best because we can provide exactly what you need, and detect and mitigate issues that you wouldn’t want automated scaling for (DDOS attack for example).

4) Pantheon is the only Drupal platform that scales entirely in software. Our infrastructure is more similar to the modern web and services like Heroku and Google App Engine than it is to the old school, legacy hosting that has been around since the dawn of web hosting.  The scaling process means that you are not punished for success. At all levels, we scale resources for you. Automatic scaling is best because we can provide exactly what you need, and detect and mitigate issues that you wouldn’t want to manually scale for (DDOS attack for example).

'''
ok='no'
while ok== 'no':
	
	q2=int (raw_input('\nPlease Answer 1, 2, 3 or 4?  '))
	
	if q2 ==1:
		print "\nWrong"
		ok='yes'
	elif q2 ==2:
		print "\nCorrect"
		rightAnswerCounter += 1	
		ok='yes'
	elif q2==3:
		print "\nWrong"
		ok='yes'
	elif q2==4:
		print "\nWrong"
		ok='yes'


raw_input('\n\n\t\tPress enter to continue the test')

#question 26
print"\nOkay lets look at Question #26", name
print"\n\nWhat is your RPO (Recovery Point Objective)?"
print \
'''
Best Answer:
1) A recovery point objective, or “RPO”, is defined by business scale planning. It is the maximum concurrent users in case of a major incident.[1] The RPO gives systems designers a limit to work to. For instance, if the RPO is set to four million users, then in practice, off-site mirrored backups must be continuously maintained – a daily off-site backup on tape will not suffice. Care must be taken to avoid two common mistakes around the use and definition of RPO. Firstly, BC staff use business impact analysis to determine RPO for each service – RPO is not determined by the existent scale regime. Secondly, when any level of preparation of traffic surge is required, rather than at the planned spike time, the period during which data is lost very often starts near the time of the beginning of the work to prepare backups which are eventually SpikedUp
2)   A recovery point objective, or “RPO”, is defined by software availability. It involves the maximum tolerable period in which data might be lost from an IT service due to a major incident.[1] The RPO gives systems designers a limit to work to. For instance, if the RPO is set to four hours, then in practice, off-site mirrored backups must be continuously maintained – a daily off-site backup on tape will not suffice. Care must be taken to avoid two common mistakes around the use and definition of RPO. Firstly, BC hardware limitations are used to determine RPO for each service – RPO is not determined by the existent backup regime. Secondly, when any level of preparation of off-site data is required, rather than at the time the backups are offsited, the period during which data is lost very often starts near the time of the beginning of the work to prepare backups which are eventually offsited
3)  A robotic plotting objective, or “RPO”, is defined by robot continuity planning. It is the maximum tolerable period in which robots might be lost from an IT service due to a major incident.[1] The RPO gives systems designers a limit to work to. For instance, if the RPO is set to four hours, then in practice, off-site mirrored backups must be continuously maintained – a daily off-site backup on tape will not suffice. Care must be taken to avoid two common mistakes around the use and definition of RPO. Firstly, BC staff use business impact analysis to determine RPO for each service – RPO is not determined by the existent backup regime. Secondly, when any level of preparation of off-site data is required, rather than at the time the backups are offsited, the period during which data is lost very often starts near the time of the beginning of the work to prepare backups which are eventually offsited
4)A recovery point objective, or “RPO”, is defined by business continuity planning. It is the maximum tolerable period in which data might be lost from an IT service due to a major incident.[1] The RPO gives systems designers a limit to work to. For instance, if the RPO is set to four hours, then in practice, off-site mirrored backups must be continuously maintained – a daily off-site backup on tape will not suffice. Care must be taken to avoid two common mistakes around the use and definition of RPO. Firstly, BC staff use business impact analysis to determine RPO for each service – RPO is not determined by the existent backup regime. Secondly, when any level of preparation of off-site data is required, rather than at the time the backups are offsited, the period during which data is lost very often starts near the time of the beginning of the work to prepare backups which are eventually offsited
'''
ok='no'
while ok== 'no':
	
	q2=int (raw_input('\nPlease Answer 1, 2, 3 or 4?  '))
	
	if q2 ==1:
		print "\nWrong"
		ok='yes'
	elif q2 ==2:
		print "\nWrong"
		ok='yes'
	elif q2==3:
		print "\nWrong"
		ok='yes'
	elif q2==4:
		print "\nCorrect"
		rightAnswerCounter += 1	
		ok='yes'


raw_input('\n\n\t\tPress enter to continue the test')

#question 27
print"\nOkay lets look at Question #27", name
print"\n\nCan I get automatic daily backups?"
print \
'''
Best Answer:
1) Enterprise, and Pantheon One plans have access to the automated backup schedule functionality in the dashboard. To do so, navigate to the backup screen and click the "Backup Schedule" tab. Here, you can select the days and time when you would like the backups to occur, as well as the length of time the backup will be retained. Once the schedule has been selected, click the "Save Backup Schedule" button.
2)  Pro, Enterprise, and Pantheon One plans have access to the automated backup schedule functionality in the dashboard. To do so, navigate to the backup screen and click the "Backup Schedule" tab. Here, you can select the days and time when you would like the backups to occur, as well as the length of time the backup will be retained. Once the schedule has been selected, click the "Save Backup Schedule" button. 
3) Only the Pantheon One plan has access to the automated backup schedule functionality in the dashboard. To do so, navigate to the backup screen and click the "Backup Schedule" tab. Here, you can select the days and time when you would like the backups to occur, as well as the length of time the backup will be retained. Once the schedule has been selected, click the "Save Backup Schedule" button. 
4) Personal, Business, Pro, Enterprise, and Pantheon One plans have access to the automated backup schedule functionality in the dashboard. To do so, navigate to the backup screen and click the "Backup Schedule" tab. Here, you can select the days and time when you would like the backups to occur, as well as the length of time the backup will be retained. Once the schedule has been selected, click the "Save Backup Schedule" button.
'''
ok='no'
while ok== 'no':
	
	q2=int (raw_input('\nPlease Answer 1, 2, 3 or 4?  '))
	
	if q2 ==1:
		print "\nWrong"
		ok='yes'
	elif q2 ==2:
		print "\nCorrect"
		rightAnswerCounter += 1	
		ok='yes'
	elif q2==3:
		print "\nWrong"
		ok='yes'
	elif q2==4:
		print "\nWrong"
		ok='yes'


raw_input('\n\n\t\tPress enter to continue the test')

#question 28
print"\nOkay lets look at Question #28", name
print"\n\nCan I have custom rules for Varnish?"
print \
'''
Best Answer:
1) Pantheon provides a single platform to run all of the 50,000 sites on our platform. Because of the efficiencies we realize through our technology, every customer cannot customize anything and must accept our final version approval for their websites.
2)   Pantheon allows configuration options for any single instance for any of the 50,000 sites on our platform. Because of the efficiencies we realize through our technology, we can provide excellent top-tier support for success on our platform. However, this requires that every customer customize things like their Varnish rules.
3)  Pantheon provides a single platform to run all of the 50,000 sites on our platform. Because of the efficiencies we realize through our technology, we can provide excellent top-tier support for success on our platform. However, this means that every customer cannot customize things like their Varnish rules.
4) Pantheon provides multiple platform options to run all of the 5,000,000 sites on our platforms. Because of the efficiencies we realize through our technology, we can provide excellent top-tier support for success on our platform. However, this means that every customer cannot customize things like their Varnish rules.
'''
ok='no'
while ok== 'no':
	
	q2=int (raw_input('\nPlease Answer 1, 2, 3 or 4?  '))
	
	if q2 ==1:
		print "\nWrong"
		ok='yes'
	elif q2 ==2:
		print "\nWrong"
		ok='yes'
	elif q2==3:
		print "\nCorrect"
		rightAnswerCounter += 1	
		ok='yes'
	elif q2==4:
		print "\nWrong"
		ok='yes'


raw_input('\n\n\t\tPress enter to continue the test')

#question 29
print"\nOkay lets look at Question #29", name
print"\n\nHow do I handle DNS?"
print \
'''
Best Answer:
1) You can only use new DNS hosting service with IPv6 optimization. Pantheon does not manage your domain name or DNS for you. You will need to be sure to point your DNS records to Pantheon: http://helpdesk.getpantheon.com/customer/portal/articles/1319336 and add the domain names that you are pointing to Pantheon through your dashboard.
2)   You can not use your existing DNS hosting service. Pantheon will sell you your domain name and/or DNS. We will need to be sure to point your DNS records to Pantheon: http://helpdesk.getpantheon.com/customer/portal/articles/1319336 and add the domain names that you are pointing to Pantheon through your dashboard.
3)  You can use your existing DNS hosting service. Pantheon requires all admin rights so we can manage your domain name or DNS for you. You will need to be sure to point your DNS records to Pantheon: http://helpdesk.getpantheon.com/customer/portal/articles/1319336 and add the domain names that you are pointing to Pantheon through your dashboard.
4)You can use your existing DNS hosting service. Pantheon does not manage your domain name or DNS for you. You will need to be sure to point your DNS records to Pantheon: http://helpdesk.getpantheon.com/customer/portal/articles/1319336 and add the domain names that you are pointing to Pantheon through your dashboard.
'''
ok='no'
while ok== 'no':
	
	q2=int (raw_input('\nPlease Answer 1, 2, 3 or 4?  '))
	
	if q2 ==1:
		print "\nWrong"
		ok='yes'
	elif q2 ==2:
		print "\nWrong"
		ok='yes'
	elif q2==3:
		print "\nWrong"
		ok='yes'
	elif q2==4:
		print "\nCorrect"
		rightAnswerCounter += 1	
		ok='yes'


raw_input('\n\n\t\tPress enter to continue the test')

#question 30
print"\nOkay lets look at Question #30", name
print"\n\nHow do I set-up SSL?"
print \
'''
Best Answer:
1) Easy! An SSL certificate is required for any site that requires a secure https connection for their Drupal application. Pantheon will not sell you an SSL certificate. You will need to acquire your SSL elsewhere. But once you have it, it is extremely easy to add through your dashboard.  SSL support is part of any Enterprise plan. For our Business and Professional plans, support for SSL is $30/mo. SSL support is not available for the Personal plans. The $30/month is a literal pass through of the expense Pantheon incurs to create a VM for your dedicated IP address required for SSL support

2)   Easy! An SSL certificate is required for any site on Pantheon for their Drupal application. Pantheon will not sell you an SSL certificate. You will need to acquire your SSL elsewhere. But once you have it, it is extremely easy to add through your dashboard.  SSL support is part of any Enterprise plan. For our Business and Professional plans, support for SSL is $30/mo. SSL support is not available for the Personal plans. The $30/month is a literal pass through of the expense Pantheon incurs to create a VM for your dedicated IP address required for SSL support

3)  Easy! An SSL certificate is required for any site that requires a secure https connection for their Drupal application. Pantheon will sell you an SSL certificate. You will need to acquire your SSL via the dashboard. Once you have it, it is extremely easy to add through your dashboard.  SSL support is part of any plan. For our Business and Professional plans, support for SSL is $50/mo. SSL support is not available for the Personal plans. The $50/month is a literal pass through of the expense Pantheon incurs to create a VM for your dedicated IP address required for SSL support

4)Easy! An SSL certificate is required for any site that requires a secure https connection for their Drupal application. Pantheon will not sell you an SSL certificate. You will need to acquire your SSL elsewhere. But once you have it, it is extremely easy to add through direct support tickets.  SSL support is part of the Business and Enterprise plan. For our Business and Professional plans, support for SSL is $50/mo. SSL support is not available for the Personal plan. The $50/month is a literal pass through of the expense Pantheon incurs to create a VM for your dedicated IP address required for SSL support
'''
ok='no'
while ok== 'no':
	
	q2=int (raw_input('\nPlease Answer 1, 2, 3 or 4?  '))
	
	if q2 ==1:
		print "\nCorrect"
		rightAnswerCounter += 1	
		ok='yes'
	elif q2 ==2:
		print "\nWrong"
		ok='yes'
	elif q2==3:
		print "\nWrong"
		ok='yes'
	elif q2==4:
		print "\nWrong"
		ok='yes'


raw_input('\n\n\t\tPress enter to continue the test')

#question 31
print"\nOkay lets look at Question #31", name
print"\n\nDo you have European Customers?"
print \
'''
Best Answer:
1) Yes! Here is a partial list: https://www.getpantheon.com/blog/march-drupal-site-picks-pantheon-european-customers
2)   No! Here is a partial list of US customers though: https://www.getpantheon.com/blog/march-drupal-site-picks-pantheon-USA-customers
3)  Yes! Here is a list of all 10 of them: https://www.getpantheon.com/blog/march-drupal-site-picks-pantheon-european-customers
4) Yes! But only if you count Canada as part of the EU.  Here is a partial list: https://www.getpantheon.com/blog/march-drupal-site-picks-pantheon-canadian-customers
'''
ok='no'
while ok== 'no':
	
	q2=int (raw_input('\nPlease Answer 1, 2, 3 or 4?  '))
	
	if q2 ==1:
		print "\nCorrect"
		rightAnswerCounter += 1
		ok='yes'
	elif q2 ==2:
		print "\nWrong"	
		ok='yes'
	elif q2==3:
		print "\nWrong"
		ok='yes'
	elif q2==4:
		print "\nWrong"
		ok='yes'


raw_input('\n\n\t\tPress enter to continue the test')

#question 32
print"\nOkay lets look at Question #32", name
print"\n\nHow does support work?"
print \
'''
Best Answer:
1) To submit a ticket to support, send the required information to PantheonSupport@gmail.com.  Depending on your plan, we will respond accordingly. If you have Enterprise or Pantheon One, you have 24*7 emergency support, as well as priority and 2 hours business hour turnaround on support tickets.  Each CSE or employee is referred to as an “agent” within Desk.  The higher the number, the higher the priority. The priority is automatically set depending on the subscription level, but can be adjusted in special cases. for example default severe Free - 4 but non-crippling Enterprise - 10

2) To submit a ticket to support, go to our website and submit the required information.  Depending on your plan, we will respond accordingly. If you have Enterprise or Pantheon One, you have 24*7 emergency support, as well as priority and 4 hours business hour turnaround on support tickets.  Each CSE or employee is referred to as an “agent” within Desk.  The higher the number, the higher the priority. The priority is automatically set depending on the subscription level, but can be adjusted in special cases. for example default severe Free - 4 but non-crippling Enterprise - 10

3) To submit a ticket to support, go to our website and submit the required information.  Depending on your plan, we will respond accordingly. If you have Enterprise or Pantheon One, you have 24*7 emergency support, as well as priority and 2 hours business hour turnaround on support tickets.  Each CSE or employee is referred to as an “agent” within Desk.  The higher the number, the higher the priority. The priority is automatically set depending on the subscription level, but can be adjusted in special cases. for example default severe Free - 4 but non-crippling Enterprise - 10


4) To submit a ticket to support, go to our website  (or send a n email to getPantheonSupport@gmail.com and submit the required information.  Depending on your plan, we will respond accordingly. If you have Enterprise or Pantheon One, you have 12*5 emergency support, as well as priority and 6 hours business hour turnaround on support tickets.  Each CSE or employee is referred to as an “agent” within Desk.  The higher the number, the higher the priority. The priority is automatically set depending on the subscription level, but can be adjusted in special cases. for example default severe Free - 4 but non-crippling Enterprise - 10

'''
ok='no'
while ok== 'no':
	
	q2=int (raw_input('\nPlease Answer 1, 2, 3 or 4?  '))
	
	if q2 ==1:
		print "\nWrong"
		ok='yes'
	elif q2 ==2:
		print "\nWrong"
		ok='yes'
	elif q2==3:
		print "\nCorrect"
		rightAnswerCounter += 1	
		ok='yes'
	elif q2==4:
		print "\nWrong"
		ok='yes'


raw_input('\n\n\t\tPress enter to continue the test')

#question 33
print"\nOkay lets look at Question #33", name
print"\n\no	Status: What are the three statuses for Pantheon issues"
print \
'''
Best Answer:

1) A) Open - This is the default status. B) Pending - Use when solutions have been provided and waiting on customer response. If no response by end of business, close. B) Closed - The issue has been completely resolved. + When a customer responds to an issue for any reason - including praise and thanks, the issue status will be automatically changed to Open.

2) A) Open - This is the default status. B) Pending - Use when solutions have been provided and waiting on customer response. If no response by end of business, close. B) Closed - The issue has been completely resolved. + When a customer responds to an issue for any reason - including praise and thanks, the issue status will be automatically changed to Open.
 
3) A) Open - This is the default status. B) Pending - Use when solutions have been provided and waiting on customer response. If no response by end of business, close. B) Closed - The issue has been completely resolved. + When a customer responds to an issue for any reason - including praise and thanks, the issue status will be automatically changed to Open.

4) A) Open - This is the default status. B) Pending - Use when solutions have been provided and waiting on customer response. If no response by end of business, close. B) Closed - The issue has been completely resolved. + When a customer responds to an issue for any reason - including praise and thanks, the issue status will be automatically changed to Open.

'''
ok='no'
while ok== 'no':
	
	q2=int (raw_input('\nPlease Answer 1, 2, 3 or 4?  '))
	
	if q2 ==1:
		print "\nCorrect"
		rightAnswerCounter += 1	
		ok='yes'
	elif q2 ==2:
		print "\nWrong"
		ok='yes'
	elif q2==3:
		print "\nWrong"
		ok='yes'
	elif q2==4:
		print "\nWrong"
		ok='yes'


raw_input('\n\n\t\tPress enter to continue the test')

#question 34
print"\nOkay lets look at Question #34", name
print"\n\nDo I get a limited number of support tickets?"
print \
'''
Best Answer:
1) Depending on the package you select, the level of support varies.  

2) Depending on the package you select.  There is a hard cap for each level.  

3) This does not Depend on the package you select, the level of support is always infinite.  

4) Depending on the Enterprise package you select. There is a hard cap for each level inside Enterprise.

'''
ok='no'
while ok== 'no':
	
	q2=int (raw_input('\nPlease Answer 1, 2, 3 or 4?  '))
	
	if q2 ==1:
		print "\nCorrect"
		rightAnswerCounter += 1	
		ok='yes'
	elif q2 ==2:
		print "\n\nWrong"
		ok='yes'
	elif q2==3:
		print "\nWrong"
		ok='yes'
	elif q2==4:
		print "\nWrong"
		ok='yes'


raw_input('\n\n\t\tPress enter to continue the test')

#question 35
print"\nOkay lets look at Question #35", name
print"\n\nDo you handle Drupal upgrades?  How?  What about other distributions?"
print \
'''
Best Answer:
1) We provide all updates. The client does not perform contributed updates. For other distribution core updates we automatically update, while you need to download the contrib updates
2)   We provide core updates. The client performs contributed updates. For other distribution core updates are provided by the maintainers, while you need to download the contrib updates
3)  We do not provide any updates. The client performs both core and contributed updates. For other distribution core updates are provided by the maintainers, while you need to download the contrib updates
4) We provide core updates and enforce custom code patches to make our platform run faster. The client performs contributed updates. For other distribution core updates are provided by the maintainers, while you need to download the contrib updates
'''
ok='no'
while ok== 'no':
	
	q2=int (raw_input('\nPlease Answer 1, 2, 3 or 4?  '))
	
	if q2 ==1:
		print "\nWrong"
		ok='yes'
	elif q2 ==2:
		print "\nCorrect"
		rightAnswerCounter += 1	
		ok='yes'
	elif q2==3:
		print "\nWrong"
		ok='yes'
	elif q2==4:
		print "\nWrong"
		ok='yes'


raw_input('\n\n\t\tPress enter to continue the test')

#question 36
print"\nOkay lets look at Question #36", name
print"\n\nCan you tell me more about Multidev?  Why would I need it?"
print \
'''
Best Answer:
1) If you work with a team of web developers on several projects, Multidev is mandatory and an extra cost.  Think of it as Google Docs for website development.  Multidev supports feature-branching, per-developer sandboxes, dedicated QA environments, merging, easy experimentation, hotfix workflows, and more.  
2)  If you work with a team of web developers on a single projects, Multidev is a great way to get everyone on the same page.  Think of it as Google Docs for website development.  Multidev supports code forking, per-developer sandboxes, dedicated HA environments, merging, easy experimentation, hotfix workflows, and more.
3)  If you work with several projects, even as a single developer, Multidev is a great way to maintain everything from a single page.  Think of it as Google Docs for website development.  Multidev supports feature-branching, per-developer sandboxes, dedicated QA environments, merging, easy experimentation, hotfix workflows, and more.
4)If you work with a team of web developers on several projects, Multidev is a great way to get everyone on the same page.  Think of it as Google Docs for website development.  Multidev supports feature-branching, per-developer sandboxes, dedicated QA environments, merging, easy experimentation, hotfix workflows, and more.
'''
ok='no'
while ok== 'no':
	
	q2=int (raw_input('\nPlease Answer 1, 2, 3 or 4?  '))
	
	if q2 ==1:
		print "\nWrong"
		ok='yes'
	elif q2 ==2:
		print "\nWrong"
		ok='yes'
	elif q2==3:
		print "\nWrong"
		ok='yes'
	elif q2==4:
		print "\nCorrect"
		rightAnswerCounter += 1	
		ok='yes'


raw_input('\n\n\t\tPress enter to continue the test')

#question 37
print"\nOkay lets look at Question #37", name
print"\n\nWhat’s the typical response time to support tickets across all plans?"
print \
'''
Best Answer:
1) For Business, Enterprise and Pantheon One plans, we respond to your support tickets within two hours of submission, during business hours.  Support ticket response times for Sandbox and Personal accounts are made on a “Best Effort” basis.  Professional and Business plans will have “Priority” status with our support team.

2) For Enterprise and Pantheon One plans, we respond to your support tickets within two hours of submission, 24/7/365.  Support ticket response times for Sandbox and Personal accounts are made on a “Priority” basis.  Professional plans will have “Escalated” status with our support team.

3) For Enterprise and Pantheon One plans, we respond to your support tickets within two hours of submission, during business hours.  Support ticket response times for Sandbox and Personal accounts are made on a “Best Effort” basis.  Professional and Business plans will have “Priority” status with our support team.

4) For Enterprise and Pantheon One plans, we respond to your support tickets within 8 business hours of submission in the customer time zone.  Support ticket response times for Sandbox and Personal accounts are made on a “Some Effort” basis.  Professional and Business plans will have “High Priority” status with our support team.

'''
ok='no'
while ok== 'no':
	
	q2=int (raw_input('\nPlease Answer 1, 2, 3 or 4?  '))
	
	if q2 ==1:
		print "\nWrong"
		ok='yes'
	elif q2 ==2:
		print "\nWrong"
		ok='yes'
	elif q2==3:
		print "\nCorrect"
		rightAnswerCounter += 1	
		ok='yes'
	elif q2==4:
		print "\nWrong"
		ok='yes'


raw_input('\n\n\t\tPress enter to continue the test')

#question 38
print"\nOkay lets look at Question #38", name
print"\n\nWhat is a LAMP CMS?"
print \
'''
Best Answer:
1) Content Management Systems and LAMP standing for Linux, Apple, MSSQL and Python. Most systems use server side caching to improve performance. This works best when the CMS is changed often but visits happen irregularly.

2) Content Management Systems and LAMP standing for Lexus, Apache, MySQL and Python. Most systems use server side caching to improve performance. This works best when the CMS is not changed often but visits happen regularly.

3) Content Management Systems and LAMP standing for Linux, Apple, MySQL and PHP. Most systems use DB caching to improve performance. This works best when the CMS is changed often but visits happen irregularly.

4) Content Management Systems and LAMP standing for Linux, Apache, MySQL and PHP. Most systems use server side caching to improve performance. This works best when the CMS is not changed often but visits happen regularly.

'''
ok='no'
while ok== 'no':
	
	q2=int (raw_input('\nPlease Answer 1, 2, 3 or 4?  '))
	
	if q2 ==1:
		print "\nWrong"
		ok='yes'
	elif q2 ==2:
		print "\nWrong"
		ok='yes'
	elif q2==3:
		print "\nWrong"
		ok='yes'
	elif q2==4:
		print "\nCorrect"
		rightAnswerCounter += 1	
		ok='yes'


raw_input('\n\n\t\tPress enter to continue the test')

#question 39
print"\nOkay lets look at Question #39", name
print"\n\nHow do you differ from hosting?"
print \
'''
Best Answer:

1) Pantheon addresses the challenges of hosting: uptime, tuning, performance, lack of expertise to address, carrying the pager, and shared content. Our fundamental offering is a hosting service, but we offer much more and provide much greater value: Our software allows quick and easy setup of Drupal environments with great performance. Our support offers: SLA (100%), 24/7 Emergency support, Launch Concierge with guidance on best practices.

2) Pantheon addresses the challenges of hosting: uptime, performance, scalability, carrying the pager, and shared content. Our fundamental offering is a hosting service, but we offer much more and provide much greater value: Our software allows quick and easy setup of Drupal environments, our software provides the scalability, performance. Our support offers: SLA (100%), 24/7 Emergency support, and hosting best practices.

3) Pantheon addresses some of the challenges of hosting: uptime, tuning, scalability and shared content. Our fundamental offering is a hosting service, but we offer much more and provide much greater value: Our software allows quick and easy setup of Drupal environments, our software provides the scalability. Our support offers: SLA (99.9%) and launch Concierge with guidance on best practices.

4) Pantheon addresses the challenges of hosting: uptime, tuning, performance, scalability, carrying the pager, and shared content. Our fundamental offering is a hosting service, but we offer much more and provide much greater value: Our software allows quick and easy setup of Drupal environments, our software provides the scalability, performance. Our support offers: SLA (99.9%), 24/7 Emergency support, Launch Concierge with guidance on best practices.

'''
ok='no'
while ok== 'no':
	
	q2=int (raw_input('\nPlease Answer 1, 2, 3 or 4?  '))
	
	if q2 ==1:
		print "\nWrong"
		ok='yes'
	elif q2 ==2:
		print "\nWrong"
		ok='yes'
	elif q2==3:
		print "\nWrong"
		ok='yes'
	elif q2==4:
		print "\nCorrect"
		rightAnswerCounter += 1	
		ok='yes'


raw_input('\n\n\t\tPress enter to continue the test')

#question 40
print"\nOkay lets look at Question #40", name
print"\n\nHow do you differ from Acquia?:"
print \
'''
Best Answer:
1) While Acquia’s founder started Drupal, our founders have more combined experience in practical website and application development in Drupal than any company in this space.  With that hands on experience, we are not only able to understand Drupal itself, but more importantly, the challenges of installing, configuring and optimizing Drupal environments.  Add to that the market leading capabilities of our platform for developer and content manager experience, and we have a unique solution that nobody, includ Acquia, can touch.
Pantheon is completely different from Acquia. Their business model is largely built on support and services, not a focus on designing, developing and delivering the best solutions for managing Drupal website environments.  Pantheon’s focus is 100% dedicated to continuing to evolve and reinvent the way organizations build and manage web sites and applications.  Technologically, Acquia calls itself cloud, but that is misleading. They get the benefits of the cloud (spinning up VMs with Amazon via their API) and their customers get something that look a lot like legacy hosting: A Virtual machine, or cluster that needs to be maintained, has security issues with software that will become out of date. In contrast, Pantheon is true cloud, a single instance with multiple tenants, with a container approach which is more similar to google app engine and Heroku.  Pantheon is totally simple. Acquia is very complex Pantheon has one price and is simple and easy to budget for. Acquia will have many hidden fees and opportunities to upsell their customers.

2)  While Acquia’s founder owns Drupal, our founders have more combined experience in practical website and application development in Drupal than any company ever.  With that hands on experience, we are only able to understand Drupal itself.  Add to that the market leading capabilities of our platform for developer and content manager experience, and we have a unique solution that nobody, includ Acquia, can touch.
Pantheon is completely different from Acquia. Pantheon's business model is largely built on support and services, not a focus on designing, developing and delivering the best solutions for managing Drupal website environments.  Acquia’s focus is 100% dedicated to continuing to evolve and reinvent the way organizations build and manage web sites and applications.  Technologically, Acquia calls itself cloud, but that is misleading. They get the benefits of the cloud (spinning up VMs with Amazon via the API) and our customers get something that look a lot like legacy hosting: A Virtual machine, or cluster that needs to be maintained, has security issues with software that will become out of date. In contrast, Pantheon is true cloud, a single instance with multiple tenants, with a container approach which is more similar to google app engine and Heroku.  Pantheon is totally simple. Acquia is very complex Pantheon has one price and is simple and easy to budget for. Acquia will have many hidden fees and opportunities to upsell their customers.

3) Actually Acquia owns Pantheon and we are in fact the same company.  We seems to compete purely for marketing reasons.  Many of our best customers are maying much more to us than Acquia could charge, hence they being sent to us and us 'winning' them.  

4)While Acquia’s founder started Drupal and has more experience in practical website and application development in Drupal than any company in this space, we have a better user experience  With that hands on experience, they are not only able to understand Drupal itself, but more importantly, the challenges of installing, configuring and optimizing Drupal environments.  Add to that the market leading capabilities of their platform for developers and content managers' experience, and they have a unique solution that nobody, includ Pantheon, can touch.
Pantheon is completely different from Acquia. Acquia’s business model is largely built on support and services, not a focus on designing, developing and delivering the best solutions for managing Drupal website environments as Pantheon does.  Pantheon’s focus is 100% dedicated to continuing to evolve and reinvent the way users can see Drupal sites and reporting via a central dashboard.  Technologically, Acquia is a true cloud. They get the benefits of the cloud (spinning up VMs with Amazon via their API) and their customers get something that look a lot like futuristic hosting: A Virtual machine cluster that has no need to be maintained, has security with software that will never become out of date. In contrast, Pantheon is kind of a cloud, a million instances with single tenants, with a hard disk approach which is more similar to geocities or angelfire communities.  Pantheon is to simple for enterprise. Acquia is for sites that are very complex. Pantheon has one price and is impossible to budget for. Acquia will have many low fees and opportunities to discount to meet their customers' budgets.

'''
ok='no'
while ok== 'no':
	
	q2=int (raw_input('\nPlease Answer 1, 2, 3 or 4?  '))
	
	if q2 ==1:
		print "\nCorrect"
		rightAnswerCounter += 1	
		ok='yes'
	elif q2 ==2:
		print "\nWrong"
		ok='yes'
	elif q2==3:
		print "\nWrong"
		ok='yes'
	elif q2==4:
		print "\nWrong"
		ok='yes'


raw_input('\n\n\t\tPress enter to continue the test')

#question 41
print"\nOkay lets look at Question #41", name
print"\n\n•	Acquia says they provide professional services and you don’t."
print \
'''
Best Answer:
1) That is accurate.  Pantheon does not provide development, module or site building as a service, so we can not write code or develop the sites for you. We have a different approach to our customers where our total focus is providing: the best technology to address the challenges of installing and maintaining Drupal instances, software that can dynamically allocate resources to optimize your websites performance, offering our solution in a true SaaS which lowers our costs and provides much more flexibility in keeping our technology up to date for all customers, support services that provide access to the best support professionals in this space, and we believe any software company for that matter. We partner with some of the best Drupal focused web design and development firms to offer customers a complete solution when they require professional services. Also, there are a number of development firms and skilled contractors who are available if you do not have a developer available. See the Pantheon Partner Directory for more information.

2)   That is accurate.  Pantheon does not provide development, module or site building as a service, so we can not write code or develop the sites for you. We have a different approach to our customers where our total focus is providing: the best technology to address the challenges of installing and maintaining Drupal instances, software that can optimize your websites coding, offering our solution in a true SaaS which lowers our costs and provides much more flexibility in keeping our technology up to date for all customers, support services that provide access to the best developers in this space and, we believe any company for that matter. We partner with some of the best Linux focused web design and development firms to offer customers a complete solution when they require professional services. Also, there are a number of development firms and skilled contractors who are available if you do not have a developer available. See the Drupal.org for more information.

3)  That is a lie.  Pantheon does provide development, module or site building as a service, so we can write code or develop the sites for you. We have a different approach to our customers where our total focus is providing: The best technology to address the challenges of installing and maintaining Drupal instances, software that can dynamically allocate resources to optimize your websites performance, offering our solution in a true SaaS which lowers our costs and provides much more flexibility in keeping our technology up to date for all customers Support services that provide access to the best support professionals in this space, and we believe any software company for that matter. We are seen as one of the best Drupal focused web design and development firms and offer customers a complete solution when they require professional services.

4)That is accurate.  You as the customer are 100% responsible for setting up your own website.  Having someone else involved is immoral and illegal in most states.  Aquia is breaking the law 99.9% of the time they get involved.  

'''
ok='no'
while ok== 'no':
	
	q2=int (raw_input('\nPlease Answer 1, 2, 3 or 4?  '))
	
	if q2 ==1:
		print "\nCorrect"
		rightAnswerCounter += 1	
		ok='yes'
	elif q2 ==2:
		print "\nWrong"
		ok='yes'
	elif q2==3:
		print "\nWrong"
		ok='yes'
	elif q2==4:
		print "\nWrong"
		ok='yes'


raw_input('\n\n\t\tPress enter to continue the test')

#question 42
print"\nOkay lets look at Question #42", name
print"\n\n•	Are you as expensive as Acquia?"
print \
'''
Best Answer:
1) Certainly price is a component which you need to consider in your decision.  However, we believe that when you compare the bottom line price you receive from our solution and support, along with our partners if you engage in their professional services, you will see that Pantheon is the lowest cost option more often than not.

2) Certainly price is not the main component which you need to consider in your decision.  However, we believe that when you compare the value you receive from our solution and support, along with our partners if you engage in their professional services, you will see that Pantheon is the most expensive option for your project but a better fit if you need millions of page views.

3) Certainly price is a component which you need to consider in your decision.  However, we believe that when you compare the value you receive from our solution and support, along with our partners if you engage in their professional services, you will see that Pantheon is the best fit for your requirements decision making criteria.

4) Certainly price is a component which you need to consider in your decision.  However, we believe that when you compare the value you receive from our solution and support, along with our partners if you engage in their professional services, you will see that Pantheon is actually always cheaper in the short term.
'''
ok='no'
while ok== 'no':
	
	q2=int (raw_input('\nPlease Answer 1, 2, 3 or 4?  '))
	
	if q2 ==1:
		print "\nWrong"
		ok='yes'
	elif q2 ==2:
		print "\nWrong"
		ok='yes'
	elif q2==3:
		print "\nCorrect"
		rightAnswerCounter += 1	
		ok='yes'
	elif q2==4:
		print "\nWrong"
		ok='yes'


raw_input('\n\n\t\tPress enter to continue the test')
	
#question 43
print"\nOkay lets look at Question #43", name
print"\n\nOnly one of the following is false:"
print \
'''
Best Answer(remember you want False this time):
1) Pantheon pricing is simple - no hidden fees, we don’t nickel and dime for overages, no set-up fee, easy to budget for.	Acquia has set-up fees, hidden costs, a habit of drastically increasing your cost when your contract is up, and incredibly complex pricing.

2)  When you contact Pantheon Support, you get top-tier support - with unlimited tickets.	Acquia’s support is not nearly as good. Often you get somebody who doesn’t know much about Drupal, and you only get a certain number of tickets - they will charge you if you go over.  

3)  Pantheon’s technology is the only to offer true smooth scaling for when traffic goes through the roof	At Acquia, since your site resides on a virtual machine or cluster, when you exceed capacity, risky migration

4)  When you contact Acquia's Support, you get top-tier support - with unlimited tickets.	Pantheon’s support is not nearly as good yet. Often you get somebody who doesn’t know much about Drupal, and you only get a certain number of tickets - we have to charge you if you go over.  

'''
ok='no'
while ok== 'no':
	
	q2=int (raw_input('\nPlease Answer 1, 2, 3 or 4?  '))
	
	if q2 ==1:
		print "\nWrong"
		ok='yes'
	elif q2 ==2:
		print "\nCorrect"
		rightAnswerCounter += 1	
		ok='yes'
	elif q2==3:
		print "\nWrong"
		ok='yes'
	elif q2==4:
		print "\nWrong"
		ok='yes'


raw_input('\n\n\t\tPress enter to continue the test')
	
#question 44
print"\nOkay lets look at Question #44", name
print"\n\nDoes Pantheon allow for any sort of server configuration out side of settings.php?"
print \
'''
Best Answer:
1) Yes, you can have full access to your server and will be able to modify configuration files like php.ini.  Since most of the Drupal code base is going to remain the same we can easily
 
2)  No, we're a completely standardized hosting Drupal provider, we meet 99.99% of customer needs across our platform. There could not be a requirement for a specific library,so you won't be able to modify configuration files like php.ini

3)  No, we're a completely managed hosting Drupal provider, we try to meet 99.99% of customer needs across our platform. Sometimes there is a requirement for a specific library, which is often supported, but you won't be able to modify configuration files like php.ini

4) Yes, we're not a completely managed hosting Drupal provider, and although we try to meet 99.99% of customer needs across our platform, sometimes there is a requirement for a specific library which means you need to be able to modify configuration files like php.ini

'''
ok='no'
while ok== 'no':
	
	q2=int (raw_input('\nPlease Answer 1, 2, 3 or 4?  '))
	
	if q2 ==1:
		print "\nWrong"
		ok='yes'
	elif q2 ==2:
		print "\nWrong"
		ok='yes'
	elif q2==3:
		print "Correct"
		rightAnswerCounter += 1	
		ok='yes'
	elif q2==4:
		print "\nWrong"
		ok='yes'


raw_input('\n\n\t\tPress enter to continue the test')
	

#question 45
print"\nOkay lets look at Question #45", name
print"\n\nI have 1 small site, only about 10K pageviews a month, but it is selling high end commodities and a constantly updating product catalog means a larger DB than we would like, around 1GB. I absolutely need the best guarantees of uptime, cause if my site blinks I could lose a sale to the other guys, who are slightly cheaper.  I am doing my own hosting right now but I really need someone to look after all this for me.  How much is this going to cost."
print \
'''
Best Answer:
1) $2,500 a month for Enterprise Standard.  Perfect fir for your needs.
2) $1,500 a month for Enterprise Plus. Perfect fit for your needs. 
3) $1,500 total for Enterprise Starter.  One time up front payment is all we need.
4) $1,500 a month for Enterprise Starter. Perfect fit for your needs.  
'''
ok='no'
while ok== 'no':
	
	q2=int (raw_input('\nPlease Answer 1, 2, 3 or 4?  '))
	
	if q2 ==1:
		print "\nWrong"
		ok='yes'
	elif q2 ==2:
		print "\nWrong"
		ok='yes'
	elif q2==3:
		print "\nWrong"
		ok='yes'
	elif q2==4:
		print "\nCorrect"
		rightAnswerCounter += 1	
		ok='yes'


raw_input('\n\n\t\tPress enter to continue the test')
	

print"\n\nThankyou for your time"
print "\n\nYou got "+ str(rightAnswerCounter) +" out of 45 correct."
if rightAnswerCounter >= 43:
	print "\n\nYou Rock and have a good deal of Pantheon knowledge"
elif rightAnswerCounter >= 40:
	print "\n\nPretty good, but you could do a little bit better.  Keep studying"
elif rightAnswerCounter >= 35:
	print "\n\nGo back and review, you got most of them right and that is something!  Just press a little harder moving forward and you will get them all right!"
else:
	print"\n\nNot good.  Not good at all.  Read through the FAQ a few more times and get some help from your teammates if you need anything clarified.  I know you can get it, you just need to focus on it."


raw_input("\n\nPress the enter key to exit.")
