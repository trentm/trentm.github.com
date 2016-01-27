.PHONY: run
run:
	./_stuff/devserver

.PHONY: post
post:
	@./_stuff/mkpost.py
