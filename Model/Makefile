
# Makefile for building the mCRL2 model

nproc := $(shell nproc)

PROPERTY_FILE := properties/Requirement\ 5.mcf
# PROPERTY_FILE := "properties/Gate1 can always get another sensor update from plane 1.mcf"

# Usage:
#   make quercus.lps
#   mcrl2lps -lregular2 Model_spec.mcrl2 qu
all:
# 	lpsrewr -v -psimplify -Q0 quercus.lps quercus.lps
# 	lpsparelm -v quercus.lps quercus.lps
# 	lpssumelm -v quercus.lps quercus.lps
# 	lpsconstelm -v quercus.lps quercus.lps
# 	lpssuminst -v quercus.lps quercus.lps

#	# LTS ROUTE!
	lts2pbes -v --counter-example -f$(PROPERTY_FILE) quercus.lts quercus.pbes -p
# 	lts2pbes -v -f$(PROPERTY_FILE) quercus.lts quercus.pbes
# 	pbessolve quercus.pbes -rjittyc --search-strategy=breadth-first -v --threads=$(nproc) -Q0

	pbessolve quercus.pbes -rjittyc --search-strategy=breadth-first -v --threads=$(nproc) -Q0 --file=quercus.lts --evidence-file=quercus.evidence.lts

# 	lps2pbes -v -c -f$(PROPERTY_FILE) quercus.lps quercus.pbes
# 	pbessolve quercus.pbes --search-strategy=breadth-first -v --threads=$(nproc) -Q0 --file=quercus.lps --evidence-file=quercus.evidence.lps -rjittyc

lts:
	mcrl22lps Model_spec.mcrl2 quercus.lps -lregular
	lps2lts -v --threads=$(nproc) quercus.lps quercus.lts --cached
	ltsconvert -v -ebranching-bisim quercus.lts quercus.lts


graph: 
	# lps2lts quercus.evidence.lps quercus.evidence.lts
	ltsgraph quercus.evidence.lts

# mcrl22lps abp.mcrl2 abp.lps
# lps2pbes -v -c -f infinitely_often_enabled_then_infinitely_often_taken.mcf abp.lps abp.pbes
# pbessolve -v --file=abp.lps abp.pbes
# lps2lts abp.pbes.evidence.lps abp.pbes.evidence.lts
# ltsgraph abp.pbes.evidence.lts
