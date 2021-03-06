# include root makefile
ifndef ROOT_MAKEFILE_MK
include ../../../../../../../Makefile
endif

# prevent rules from being evaluated/included multiple times
ifndef $(abspath $(lastword $(MAKEFILE_LIST)))_MK
$(abspath $(lastword $(MAKEFILE_LIST)))_MK := 1


# The following are control variables that determine what logic from `rules.mk` is enabled

# `true`/`false` to enable/disable the actual unit test command so it can be overridden (the targets are still created)
# applies to both the pony and elixir test targets
$(abspath $(lastword $(MAKEFILE_LIST)))_UNIT_TEST_COMMAND := false

# `true`/`false` to enable/disable generate pony related targets (build/test/clean) for pony sources in this directory
# otherwise targets only get created if there are pony sources (*.pony) in this directory.
$(abspath $(lastword $(MAKEFILE_LIST)))_PONY_TARGET := true

# `true`/`false` to enable/disable generate final file build target using ponyc command for the pony build target so
# it can be overridden manually
$(abspath $(lastword $(MAKEFILE_LIST)))_PONYC_TARGET := true

# `true`/`false` to enable/disable generate exs related targets (build/test/clean) for elixir sources in this directory
# otherwise targets only get created if there are elixir sources (*.exs) in this directory.
$(abspath $(lastword $(MAKEFILE_LIST)))_EXS_TARGET := true

# `true`/`false` to enable/disable generate docker related targets (build/push) for a Dockerfile in this directory
# otherwise targets only get created if there is a Dockerfile in this directory
$(abspath $(lastword $(MAKEFILE_LIST)))_DOCKER_TARGET := true

# `true`/`false` to enable/disable recursing into Makefiles of subdirectories if they exist
# (and by recursion every makefile in the tree that is referenced)
$(abspath $(lastword $(MAKEFILE_LIST)))_RECURSE_SUBMAKEFILES := true


SINGLE_STREAM_FILTERING_STATELESS_STATEFUL_FILTERED_APP_PATH := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))

# standard rules generation makefile
include $(rules_mk_path)

integration-tests-testing-correctness-topology_layouts-apps-single_stream-filtering_stateless-stateful_filtered_app: single_worker_filtering_stateless_stateful_filtered_app_test

single_worker_filtering_stateless_stateful_filtered_app_test:
	cd $(SINGLE_STREAM_FILTERING_STATELESS_STATEFUL_FILTERED_APP_PATH) && \
	integration_test \
	--framed-file-sender ../data_gen/_test.msg \
	--validation-cmp \
	--expected-file ../data_gen/_expected.msg \
	--log-level error \
	--command './stateful_filtered_app' \
	--sink-expect 50

# Multi-worker tests currently fail:
# Error initializing local topology
# This should never happen: failure in lib/wallaroo/initialization/local_topology.pony at line 1236
# See Issue: 947

# integration-tests-testing-correctness-topology_layouts-apps-single_stream-filtering_stateless-stateful_filtered_app: two_worker_single_worker_filtering_stateless_stateful_filtered_app_test

two_worker_single_worker_filtering_stateless_stateful_filtered_app_test:
	cd $(SINGLE_STREAM_FILTERING_STATELESS_STATEFUL_FILTERED_APP_PATH) && \
	integration_test \
	--framed-file-sender ../data_gen/_test.msg \
	--workers 2 \
	--validation-cmp \
	--expected-file ../data_gen/_expected.msg \
	--log-level error \
	--command './stateful_filtered_app' \
	--sink-expect 50

# integration-tests-testing-correctness-topology_layouts-apps-single_stream-filtering_stateless-stateful_filtered_app: three_worker_single_worker_filtering_stateless_stateful_filtered_app_test

three_worker_single_worker_filtering_stateless_stateful_filtered_app_test:
	cd $(SINGLE_STREAM_FILTERING_STATELESS_STATEFUL_FILTERED_APP_PATH) && \
	integration_test \
	--framed-file-sender ../data_gen/_test.msg \
	--workers 3 \
	--validation-cmp \
	--expected-file ../data_gen/_expected.msg \
	--log-level error \
	--command './stateful_filtered_app' \
	--sink-expect 50

# end of prevent rules from being evaluated/included multiple times
endif
