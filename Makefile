.PHONY: all

COG := cog
COG_FLAGS := -e -Icogs
COG_SRC := docs/Informers.rst

all .PHONY: $(COG_SRC)

$(COG_SRC):
	@$(COG) $(COG_FLAGS) -cr $@
