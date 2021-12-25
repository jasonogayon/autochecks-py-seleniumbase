ifeq ($(OS), Windows_NT)
	OSTYPE := Windows
else
	OSTYPE := $(shell sh -c 'uname -s 2>/dev/null || echo not')
endif

ORIG_PREFIX:= @
NEW_PREFIX:= -t @

help:
	@echo ""
	@echo "usage: make COMMAND"
	@echo ""
	@echo "Commands:"
	@echo ""
	@echo "    ui                  Run tests locally with browser"
	@echo "    h                   Run tests locally without browser (headless)"
	@echo "    demo                Run tests locally with browser on demo mode"
	@echo "    bs user={} key={}   Run tests on Browserstack, given a user and a key"
	@echo ""
	@echo "Git-Specific:"
	@echo ""
	@echo "    m                   Update local master branch with remote"
	@echo "    b tag={}            Create new local branch from latest remote master"
	@echo "    bu tag={}           Update local branch with remote master"
	@echo "    bn tag={}           Rename local branch"
	@echo "    d tag={}            Delete local branch"
	@echo "    dr tag={}           Delete remote branch"
	@echo ""


ui:
	@echo "Running tests ..."; echo "";
	@pytest tests/tests-todos.py -s --html=reports/report.html

uiv:
	@echo "Running tests ..."; echo "";
	@pytest tests/tests-todos.py  --data="V" -s --html=reports/report.html

h:
	@echo "Running tests ..."; echo "";
	@pytest tests/tests-todos.py -s --html=reports/report.html --headless

hv:
	@echo "Running tests ..."; echo "";
	@pytest tests/tests-todos.py --data="V" -s --html=reports/report.html --headless

ci:
	@echo "Running tests ..."; echo "";
	@pytest tests/tests-todos.py --data="CI" -s --html=reports/report.html --headless

demo:
	@echo "Running tests ..."; echo "";
	@pytest tests/tests-todos.py -s --html=reports/report.html --demo_mode

bs:
	@echo "Running tests ..."; echo ""
	@pytest tests/tests-todos.py --browser=remote --server=$(user):$(key)@hub.browserstack.com --port=80 --cap_file=capabilities/browserstack.py




m:
	@echo "Fetching master (remote) ..."; echo ""
	@git checkout master && git fetch -p origin
	@echo "Merging master (remote to local) ..."; echo ""
	@git merge origin/master
	@echo "Done"; echo ""

b:
	@make m
	@echo "Creating new feature branch ..."; echo ""
	@git checkout -b $(tag) master && git branch
	@echo "Done"; echo ""

bu:
	@make m
	@echo "Merging master to feature branch ..."; echo ""
	@git checkout $(tag) && git merge master && git branch
	@echo "Done"; echo ""

bn:
	@echo "Renaming branch ..."; echo ""
	@git branch -m $(old) $(new)
	@echo "Done"; echo ""

d:
	@echo "Deleting branch (local) ..."; echo ""
	@git checkout master && git branch -D $(tag) && git branch
	@echo "Done"; echo ""

dr:
	@echo "Deleting branch (remote) ..."; echo ""
	@git checkout master && git push origin --delete $(tag)
	@echo "Done"; echo ""


.PHONY: clean init
