
MARKDOWN2=python ~/tm/python-markdown2/lib/markdown2.py

all:
	$(MARKDOWN2) -x header-ids,code-friendly 2012-03-28-service-logging-in-json-with-bunyan.markdown > bunyan.html
	python fu-wordpress-i-want-my-styles.py bunyan.html
