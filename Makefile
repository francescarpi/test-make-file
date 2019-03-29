
SHELL:=/bin/bash

test_action_1:
	$(eval ORGANIZATION=$(shell echo $(json) | jq -r '.common.organization_slug'))
	@echo {\"output\": {\"key\": \"$(ORGANIZATION)\"}}

test_action_2:
	@echo $(json)

test_action_3:
	@echo {\"key_action_3\": \"value_action_3\"}

test_action_4:
	@echo 'action 4 result'

test_action_5:
	$(eval RETRY=$(shell echo $(json) | jq -r '.common.retries'))
	@echo {\"status\": \"success_at_retry_$(RETRY)\"}

