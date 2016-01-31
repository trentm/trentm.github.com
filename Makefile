.PHONY: run
run:
	./_stuff/devserver

.PHONY: post
post:
	@./_stuff/mkpost.py


.PHONY: check-posts
check-posts:
	@./_stuff/lintpost.py _posts/????-??-??-*.markdown

.PHONY: check
check: check-posts

.PHONY: now
now:
	@node -e 'console.log(new Date().toISOString())'
