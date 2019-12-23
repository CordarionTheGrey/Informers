.PHONY: all README.rst

COG := cog
COG_FLAGS := -e

all: README.rst

README.rst:
	@$(COG) $(COG_FLAGS) -cr $@
