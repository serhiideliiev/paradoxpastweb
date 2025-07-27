# Makefile for Project Paradox Past Pelican site
# Following Pelican best practices and PEP-8 guidelines

# =============================================================================
# CONFIGURATION VARIABLES
# =============================================================================

PY?=python3
PELICAN?=pelican
PELICANOPTS=

BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/content
OUTPUTDIR=$(BASEDIR)/output
CONFFILE=$(BASEDIR)/pelicanconf.py
DEVCONFFILE=$(BASEDIR)/pelicanconf_dev.py
PUBLISHCONF=$(BASEDIR)/publishconf.py

GITHUB_PAGES_BRANCH=main

# Development server settings
SERVER=127.0.0.1
PORT=8000

# =============================================================================
# MAIN TARGETS
# =============================================================================

help:
	@echo 'Makefile for Project Paradox Past Pelican site'
	@echo ''
	@echo 'Usage:'
	@echo '   make help                Show this help message'
	@echo '   make html                Generate the website'
	@echo '   make clean               Remove the generated files'
	@echo '   make regenerate          Regenerate files upon modification'
	@echo '   make serve               Serve site at http://localhost:$(PORT)'
	@echo '   make devserver           Start development server with auto-reload'
	@echo '   make publish             Generate site using production settings'
	@echo '   make github              Deploy to GitHub Pages'
	@echo '   make lint                Run code quality checks'
	@echo '   make install             Install dependencies'
	@echo ''

html:
	"$(PELICAN)" "$(INPUTDIR)" -o "$(OUTPUTDIR)" -s "$(CONFFILE)" $(PELICANOPTS)

clean:
	[ ! -d "$(OUTPUTDIR)" ] || rm -rf "$(OUTPUTDIR)"

regenerate:
	"$(PELICAN)" -r "$(INPUTDIR)" -o "$(OUTPUTDIR)" -s "$(CONFFILE)" $(PELICANOPTS)

serve:
	"$(PELICAN)" -l "$(INPUTDIR)" -o "$(OUTPUTDIR)" -s "$(DEVCONFFILE)" \
		$(PELICANOPTS) -b $(SERVER) -p $(PORT)

devserver:
	"$(PELICAN)" -lr "$(INPUTDIR)" -o "$(OUTPUTDIR)" -s "$(DEVCONFFILE)" \
		$(PELICANOPTS) -b $(SERVER) -p $(PORT)

publish:
	"$(PELICAN)" "$(INPUTDIR)" -o "$(OUTPUTDIR)" -s "$(PUBLISHCONF)" $(PELICANOPTS)

# =============================================================================
# DEVELOPMENT TOOLS
# =============================================================================

lint:
	@echo "Running Python linting..."
	@if command -v pylint >/dev/null 2>&1; then \
		pylint pelicanconf_refactored.py publishconf.py pelicanconf_dev_refactored.py; \
	else \
		echo "pylint not found. Install with: pip install pylint"; \
	fi
	@echo "Running CSS linting..."
	@if command -v stylelint >/dev/null 2>&1; then \
		stylelint themes/custom/static/css/**/*.css; \
	else \
		echo "stylelint not found. Install with: npm install -g stylelint"; \
	fi

install:
	@echo "Installing Python dependencies..."
	pip install -r requirements.txt
	@echo "Installing development dependencies..."
	pip install pylint black isort

format:
	@echo "Formatting Python code..."
	@if command -v black >/dev/null 2>&1; then \
		black pelicanconf_refactored.py publishconf.py pelicanconf_dev_refactored.py; \
	else \
		echo "black not found. Install with: pip install black"; \
	fi
	@if command -v isort >/dev/null 2>&1; then \
		isort pelicanconf_refactored.py publishconf.py pelicanconf_dev_refactored.py; \
	else \
		echo "isort not found. Install with: pip install isort"; \
	fi

# =============================================================================
# DEPLOYMENT
# =============================================================================

github: publish
	@echo "Deploying to GitHub Pages..."
	@if command -v ghp-import >/dev/null 2>&1; then \
		ghp-import -m "Deploy site" -b $(GITHUB_PAGES_BRANCH) "$(OUTPUTDIR)"; \
		git push origin $(GITHUB_PAGES_BRANCH); \
	else \
		echo "ghp-import not found. Install with: pip install ghp-import"; \
	fi

# =============================================================================
# UTILITY TARGETS
# =============================================================================

check-content:
	@echo "Checking content structure..."
	@find content -name "*.md" -exec echo "Processing: {}" \;

new-post:
	@echo "Creating new post..."
	@read -p "Enter post title: " title; \
	slug=$$(echo "$$title" | tr '[:upper:]' '[:lower:]' | sed 's/[^a-z0-9]/-/g' | sed 's/--*/-/g' | sed 's/^-\|-$$//g'); \
	date=$$(date +"%Y-%m-%d %H:%M"); \
	filename="content/$$slug.md"; \
	echo "Title: $$title" > "$$filename"; \
	echo "Date: $$date" >> "$$filename"; \
	echo "Category: Blog" >> "$$filename"; \
	echo "Tags: " >> "$$filename"; \
	echo "Slug: $$slug" >> "$$filename"; \
	echo "Author: $(AUTHOR)" >> "$$filename"; \
	echo "" >> "$$filename"; \
	echo "Write your content here..." >> "$$filename"; \
	echo "Created: $$filename"

.PHONY: help html clean regenerate serve devserver publish lint install format github check-content new-post
