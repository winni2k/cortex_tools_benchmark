FIXTURE_PACKAGE := down/cortex-tools-fixtures.tar.bz2
FIXTURE_MANIFEST := fixtures/manifest.txt
PY_ENV := pipenv run
TEST_COMMAND := $(PY_ENV) pytest --benchmark-autosave
BENCHMARK_COMMAND := $(PY_ENV) pytest-benchmark

benchmark:
	$(TEST_COMMAND) benchmark

compare:
	$(BENCHMARK_COMMAND) compare

setup:
	scripts/setup

package-fixtures:
	tar -cjf $(FIXTURE_PACKAGE) $$(cat $FIXTURE_MANIFEST)

upload-fixtures:
	echo "do it manually!"

upload-results:
	tar -czf .benchmarks.tar.gz .benchmarks
	gdrive --service-account $(GDRIVE_ACCOUNT_CREDENTIALS_JSON) update '1W8z5a34gEs3kGyxfqIQ5_VBdP2F8iWYD' .benchmarks.tar.gz


.PHONY: setup benchmark
.DELETE_ON_ERROR:
