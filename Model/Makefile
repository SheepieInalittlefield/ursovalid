
# Makefile for building the mCRL2 model

nproc := $(shell nproc)

PROPERTY_FILE ?= properties/Requirement\ 9.mcf

lts:
	mcrl22lps Model_spec.mcrl2 quercus.lps -lregular
# 	lpsrewr -v -psimplify -Q0 quercus.lps quercus.lps
# 	lpsparelm -v quercus.lps quercus.lps
# 	lpssumelm -v quercus.lps quercus.lps
# 	lpsconstelm -v quercus.lps quercus.lps
# 	lpssuminst -v quercus.lps quercus.lps
	lps2lts -v --threads=$(nproc) quercus.lps quercus.lts --cached
	ltsconvert -v -ebranching-bisim quercus.lts quercus.lts

pbes:
	lts2pbes -v --counter-example -f"$(PROPERTY_FILE)" quercus.lts quercus.pbes -p
	pbessolve quercus.pbes -rjittyc --search-strategy=breadth-first -v --threads=$(nproc) -Q0 --file=quercus.lts --evidence-file=quercus.evidence.lts



graph: 
	# lps2lts quercus.evidence.lps quercus.evidence.lts
	ltsgraph quercus.evidence.lts

req: pbes graph

clean:
	rm -f quercus.lps quercus.lts quercus.pbes quercus.evidence.lts jittyc*