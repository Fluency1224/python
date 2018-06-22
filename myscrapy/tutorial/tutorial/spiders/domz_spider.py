#########################################################################
# File Name: domz_spider.py
# Author: fluency
# mail: 1005068694@qq.com
# Created Time: Tue 24 Apr 2018 05:08:40 PM CST
#########################################################################
#!/usr/bin/python
#!Coding:utf-8
import scrapy

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
		"http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
		"http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"]
	
	def parse(self, response):
		filename = response.url.split("/")[-2]
		with open(filename, 'wb') as f:
			f.write(reponse.body)
　　　　
