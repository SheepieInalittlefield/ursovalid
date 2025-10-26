nproc := $(shell nproc)
PROPERTY_FILE ?= properties/nutest.mcf
VERBOSE ?= 1

BUILD_DIR := out
BASENAME := $(subst  ,_,$(patsubst %.mcf,%,$(notdir $(PROPERTY_FILE))))

LPS_FILE          := $(BUILD_DIR)/model.lps
LTS_FILE          := $(BUILD_DIR)/model.lts
PBES_FILE         := $(BUILD_DIR)/$(BASENAME).pbes
EVIDENCE_LTS_FILE := $(BUILD_DIR)/$(BASENAME).evidence.lts

.PHONY: all lts pbes graph req clean

# Default: Build the LTS and solve the PBES, but don't show the graph.
all: lts pbes

# Generates the state space (LTS) from the mCRL2 specification.
lts:
	@$(MAKE) $(BUILD_DIR)
	mcrl22lps Model_spec.mcrl2 "$(LPS_FILE)" -lregular
	lps2lts $(if $(filter 1,$(VERBOSE)),-v) --threads=$(nproc) "$(LPS_FILE)" "$(LTS_FILE)" --cached
	ltsconvert $(if $(filter 1,$(VERBOSE)),-v) -ebranching-bisim "$(LTS_FILE)" "$(LTS_FILE)"

# Verifies the property and generates a counter-example.
pbes: 
	lts2pbes $(if $(filter 1,$(VERBOSE)),-v) --counter-example -f"$(PROPERTY_FILE)" "$(LTS_FILE)" "$(PBES_FILE)" -p
	pbessolve $(if $(filter 1,$(VERBOSE)),-v) "$(PBES_FILE)" -rjittyc --search-strategy=breadth-first --threads=$(nproc) -Q0 --file="$(LTS_FILE)" --evidence-file="$(EVIDENCE_LTS_FILE)"

pbesnoce: 
	lts2pbes $(if $(filter 1,$(VERBOSE)),-v) -f"$(PROPERTY_FILE)" "$(LTS_FILE)" "$(PBES_FILE)" -p
	pbessolve $(if $(filter 1,$(VERBOSE)),-v) "$(PBES_FILE)" -rjittyc --search-strategy=breadth-first --threads=$(nproc) -Q0 --file="$(LTS_FILE)"

# Displays the counter-example graph.
graph:
	ltsgraph "$(EVIDENCE_LTS_FILE)"

# Convenience target to run full verification AND show the graph.
req: pbes graph

$(BUILD_DIR):
	mkdir -p $(BUILD_DIR)

clean:
	rm -rf $(BUILD_DIR) jittyc* model.lps model.lts