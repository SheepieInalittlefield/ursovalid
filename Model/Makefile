
# Makefile for building the mCRL2 model

nproc := $(shell nproc)

# PROPERTY_FILE := properties/landing_plane_reaches_gate.mcf
PROPERTY_FILE := "properties/No deadlocks.mcf"


# Usage:
#   make quercus.lps
#   mcrl2lps -lregular2 Model_spec.mcrl2 qu
all:
	mcrl22lps -lregular Model_spec.mcrl2 quercus.lps
# 	lpsrewr -v -psimplify -Q0 quercus.lps quercus.lps
# 	lpsparelm -v quercus.lps quercus.lps
# 	lpssumelm -v quercus.lps quercus.lps
# 	lpsconstelm -v quercus.lps quercus.lps
# 	lpssuminst -v quercus.lps quercus.lps

# 	lps2lts -v --threads=$(nproc) quercus.lps quercus.lts
# 	ltsconvert -v -ebranching-bisim quercus.lts quercus.lts
	lps2pbes -v --counter-example -f$(PROPERTY_FILE) quercus.lps quercus.pbes
	pbessolve quercus.pbes --search-strategy=breadth-first --solve-strategy=0 --verbose --threads=$(nproc) -Q0 --file=quercus.lps --evidence-file=quercus.evidence.lps

# 	pbessolve";
#     inputFile = fileSystem->pbesFilePath(property.name, evidence);
#     arguments << inputFile << "--in=pbes"
#               << "--search-strategy=breadth-first"
#               << "--solve-strategy=0"
#               << "--verbose"
#               << "--threads=" + QString::number(QThread::idealThreadCount())
#               << QString("-Q") + std::to_string(fileSystem->enumerationLimit()).c_str();
graph: 
	lps2lts quercus.evidence.lps quercus.evidence.lts
	ltsgraph quercus.evidence.lts

# mcrl22lps abp.mcrl2 abp.lps
# lps2pbes -v -c -f infinitely_often_enabled_then_infinitely_often_taken.mcf abp.lps abp.pbes
# pbessolve -v --file=abp.lps abp.pbes
# lps2lts abp.pbes.evidence.lps abp.pbes.evidence.lts
# ltsgraph abp.pbes.evidence.lts