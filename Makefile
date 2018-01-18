MCCORTEX := ../bin/mccortex 63
PIP := pip3
FIXTURE_PACKAGE := down/cortex-tools-fixtures.tar.bz2
PY_ENV := pipenv run
TEST_COMMAND := $(PY_ENV) pytest --benchmark-autosave
BENCHMARK_COMMAND := $(PY_ENV) pytest-benchmark

benchmark:
	$(TEST_COMMAND) benchmark

compare:
	$(BENCHMARK_COMMAND) compare

setup: python-dependencies
	$(MAKE) get-results
	$(MAKE) get-fixtures
	$(MAKE) fixtures

python-dependencies:
	pipenv install
	$(PY_ENV) $(PIP) install cortexpy

$(FIXTURE_PACKAGE):
	cd down; gdrive --service-account $(GDRIVE_ACCOUNT_CREDENTIALS_JSON) download $(FIXTURE_PACKAGE_GDRIVE_ID)

get-fixtures: $(FIXTURE_PACKAGE)
	tar -xf $^

package-fixtures:
	find fixtures -type f -name '*.fna' | xargs tar -cjf $(FIXTURE_PACKAGE)

fixtures: fixtures/Pabies_coding_sequence/Pabies1.0-all-cds.ctx

fixtures/Pabies_coding_sequence/Pabies1.0-all-cds.ctx: fixtures/Pabies_coding_sequence/Pabies1.0-all-cds.fna
	$(MCCORTEX) build --force --sort --memory 2G -k 47 --sample pabies_reference_cds --seq $< $@

get-results:
	gdrive --service-account $(GDRIVE_ACCOUNT_CREDENTIALS_JSON) download --force '1W8z5a34gEs3kGyxfqIQ5_VBdP2F8iWYD'
	tar -xf .benchmarks.tar.gz

upload-results:
	tar -czf .benchmarks.tar.gz .benchmarks
	gdrive --service-account $(GDRIVE_ACCOUNT_CREDENTIALS_JSON) update '1W8z5a34gEs3kGyxfqIQ5_VBdP2F8iWYD' .benchmarks.tar.gz



.PHONY: setup benchmark
.DELETE_ON_ERROR:
