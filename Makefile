include docs/Makefile

PYTHON_VER := $(word 1,$(wordlist 2,4,$(subst ., ,$(shell python --version 2>&1))))
PYTHON=python
ifeq ($(PYTHON_VER),3)
	PYTHON = python2
endif

.PHONY : all test test-series install clean

all: build test
test: test-series

build:
	@echo "»»» Building cairoplot..."
	@$(PYTHON) setup.py build

test-series:
	@echo "»»» Testing cairoplot with the series module..."
	@$(PYTHON) tests/series_tests.py

install:
	@echo "»»» Installing cairoplot..."
	@$(PYTHON) setup.py install

clean: 
	@echo "»»» Cleaning..."
	@rm -rf build

