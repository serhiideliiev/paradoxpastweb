PY?=python
PELICAN?=pelican
CONFIG_FILE=config.py

help:
	@echo 'Makefile for Project Paradox Past'
	@echo ''
	@echo 'Usage:'
	@echo '   make install          Install dependencies'
	@echo '   make dev              Start development server'
	@echo '   make build            Build production site'
	@echo '   make clean            Clean output directory'

install:
	$(PY) -m pip install -r requirements.txt

dev:
	PELICAN_ENV=development $(PELICAN) content -s $(CONFIG_FILE) -r -l

build:
	PELICAN_ENV=production $(PELICAN) content -s $(CONFIG_FILE)

clean:
	[ ! -d output ] || rm -rf output

.PHONY: help install dev build clean
