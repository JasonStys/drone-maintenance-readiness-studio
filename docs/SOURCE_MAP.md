# Source declaration map

By Jason Stys. Headers link here for current exact physical lines.
Python/TypeScript ASTs index declarations, parameters and bindings; SQL lists non-comment schema lines. Lexical maps are navigation, not complete semantic symbol tables.

| File | Line | Declaration / variable |
| --- | ---: | --- |
| `tests/conftest.py` | 12 | `ORIGIN` |
| `tests/conftest.py` | 16 | `accounts()` |
| `tests/conftest.py` | 19 | `password` |
| `tests/conftest.py` | 20 | `role` |
| `tests/conftest.py` | 25 | `app(tmp_path, accounts)` |
| `tests/conftest.py` | 27 | `instance` |
| `tests/conftest.py` | 29 | `db` |
| `tests/conftest.py` | 30 | `_` |
| `tests/conftest.py` | 30 | `hashed` |
| `tests/conftest.py` | 30 | `role` |
| `tests/conftest.py` | 36 | `store(app)` |
| `tests/conftest.py` | 42 | `state(store)` |
| `tests/conftest.py` | 48 | `assumptions()` |
| `tests/conftest.py` | 54 | `client(app)` |
| `tests/conftest.py` | 56 | `connection` |
| `tests/conftest.py` | 61 | `login(client, accounts)` |
| `tests/conftest.py` | 64 | `enter(role)` |
| `tests/conftest.py` | 65 | `response` |
| `tests/conftest.py` | 74 | `post(client)` |
| `tests/conftest.py` | 77 | `submit(path)` |
| `tests/conftest.py` | 78 | `generation` |
| `tests/test_cli.py` | 11 | `test_init_provision_and_mismatch(tmp_path, monkeypatch, capsys)` |
| `tests/test_cli.py` | 13 | `db` |
| `tests/test_cli.py` | 20 | `answers` |
| `tests/test_cli.py` | 24 | `answers` |
| `tests/test_cli.py` | 29 | `test_serve_invalid_port_and_browser_fixture(tmp_path, monkeypatch)` |
| `tests/test_cli.py` | 31 | `seen` |
| `tests/test_cli.py` | 39 | `directory` |
| `tests/test_cli.py` | 40 | `first` |
| `tests/test_contracts.py` | 24 | `test_usage_contract_rejects_untrusted_attribution_or_clock(change)` |
| `tests/test_contracts.py` | 52 | `test_inspection_measurements_finite_and_strict(change)` |
| `tests/test_contracts.py` | 66 | `test_duplicate_and_incomplete_policy_rejected()` |
| `tests/test_contracts.py` | 68 | `policy` |
| `tests/test_contracts.py` | 77 | `model` |
| `tests/test_contracts.py` | 78 | `changes` |
| `tests/test_engine.py` | 12 | `result(state, assumptions, at)` |
| `tests/test_engine.py` | 14 | `report` |
| `tests/test_engine.py` | 15 | `p` |
| `tests/test_engine.py` | 18 | `test_three_realistic_synthetic_states(state, assumptions)` |
| `tests/test_engine.py` | 20 | `part` |
| `tests/test_engine.py` | 20 | `report` |
| `tests/test_engine.py` | 21 | `a` |
| `tests/test_engine.py` | 44 | `test_exact_life_and_warning_boundaries(state, assumptions, seconds, cycles, status, code)` |
| `tests/test_engine.py` | 46 | `p` |
| `tests/test_engine.py` | 46 | `part` |
| `tests/test_engine.py` | 48 | `_` |
| `tests/test_engine.py` | 48 | `actual` |
| `tests/test_engine.py` | 51 | `finding` |
| `tests/test_engine.py` | 54 | `test_inspection_expiry_equality_future_clock_and_evaluation_bounds(state, assumptions)` |
| `tests/test_engine.py` | 56 | `inspection` |
| `tests/test_engine.py` | 56 | `p` |
| `tests/test_engine.py` | 57 | `due` |
| `tests/test_engine.py` | 60 | `f` |
| `tests/test_engine.py` | 63 | `invalid` |
| `tests/test_engine.py` | 78 | `test_battery_measurement_boundaries(state, assumptions, capacity, resistance, status, code)` |
| `tests/test_engine.py` | 80 | `inspection` |
| `tests/test_engine.py` | 80 | `p` |
| `tests/test_engine.py` | 82 | `actual` |
| `tests/test_engine.py` | 85 | `f` |
| `tests/test_engine.py` | 88 | `test_missing_failed_retired_and_history_findings_accumulate(state, assumptions)` |
| `tests/test_engine.py` | 90 | `p` |
| `tests/test_engine.py` | 90 | `part` |
| `tests/test_engine.py` | 92 | `inspection` |
| `tests/test_engine.py` | 92 | `p` |
| `tests/test_engine.py` | 94 | `actual` |
| `tests/test_engine.py` | 96 | `f` |
| `tests/test_engine.py` | 101 | `i` |
| `tests/test_engine.py` | 102 | `f` |
| `tests/test_engine.py` | 105 | `test_configuration_drift_missing_slot_and_unmodeled_part(state, assumptions)` |
| `tests/test_engine.py` | 109 | `report` |
| `tests/test_engine.py` | 110 | `f` |
| `tests/test_engine.py` | 116 | `part` |
| `tests/test_engine.py` | 118 | `f` |
| `tests/test_engine.py` | 122 | `f` |
| `tests/test_engine.py` | 126 | `test_missing_limits_zero_rate_and_latest_inspection_order(state)` |
| `tests/test_engine.py` | 128 | `now` |
| `tests/test_engine.py` | 129 | `part` |
| `tests/test_engine.py` | 131 | `actual` |
| `tests/test_engine.py` | 146 | `latest` |
| `tests/test_engine.py` | 147 | `item` |
| `tests/test_engine.py` | 157 | `test_watch_and_empty_fleet_are_not_cleared(state, assumptions)` |
| `tests/test_evidence.py` | 12 | `NOTE` |
| `tests/test_evidence.py` | 15 | `test_immutable_assessment_current_stale_export_and_independent_ack(client, login, post)` |
| `tests/test_evidence.py` | 18 | `captured` |
| `tests/test_evidence.py` | 20 | `report` |
| `tests/test_evidence.py` | 27 | `reviewed` |
| `tests/test_evidence.py` | 40 | `stale` |
| `tests/test_evidence.py` | 48 | `test_readiness_review_self_and_role_change_no_bypass(client, login, post, store)` |
| `tests/test_evidence.py` | 51 | `report` |
| `tests/test_evidence.py` | 52 | `db` |
| `tests/test_evidence.py` | 60 | `test_clock_rollback_inspection_deadline_and_expiry(store, client, login, post, monkeypatch)` |
| `tests/test_evidence.py` | 63 | `report` |
| `tests/test_evidence.py` | 64 | `original` |
| `tests/test_evidence.py` | 76 | `test_actual_state_or_chain_tampering_fails_closed(store, client, login, tamper)` |
| `tests/test_evidence.py` | 79 | `db` |
| `tests/test_evidence.py` | 93 | `test_assessment_and_acknowledgement_hashes(store, client, login, post, target)` |
| `tests/test_evidence.py` | 96 | `report` |
| `tests/test_evidence.py` | 102 | `db` |
| `tests/test_evidence.py` | 105 | `content` |
| `tests/test_evidence.py` | 117 | `test_local_capacities_are_fail_closed(store, client, login, post, monkeypatch, cap)` |
| `tests/test_evidence.py` | 120 | `before` |
| `tests/test_evidence.py` | 123 | `asset` |
| `tests/test_evidence.py` | 133 | `response` |
| `tests/test_evidence.py` | 135 | `response` |
| `tests/test_evidence.py` | 137 | `response` |
| `tests/test_evidence.py` | 139 | `response` |
| `tests/test_evidence.py` | 143 | `response` |
| `tests/test_evidence.py` | 147 | `response` |
| `tests/test_evidence.py` | 149 | `response` |
| `tests/test_evidence.py` | 160 | `test_creation_and_policy_publication_preserve_counter_history(client, login, post)` |
| `tests/test_evidence.py` | 163 | `asset` |
| `tests/test_evidence.py` | 175 | `policy` |
| `tests/test_evidence.py` | 177 | `published` |
| `tests/test_impact.py` | 9 | `test_exact_hard_limit_and_deadline_deltas_preserve_lifetime_records(state, assumptions)` |
| `tests/test_impact.py` | 11 | `original` |
| `tests/test_impact.py` | 12 | `policy` |
| `tests/test_impact.py` | 13 | `battery` |
| `tests/test_impact.py` | 13 | `limit` |
| `tests/test_impact.py` | 15 | `at` |
| `tests/test_impact.py` | 15 | `row` |
| `tests/test_impact.py` | 16 | `result` |
| `tests/test_impact.py` | 17 | `row` |
| `tests/test_impact.py` | 23 | `finding` |
| `tests/test_impact.py` | 27 | `recorded` |
| `tests/test_impact.py` | 27 | `row` |
| `tests/test_impact.py` | 33 | `test_draft_cannot_erase_history_defects_or_missing_configuration(state, assumptions)` |
| `tests/test_impact.py` | 35 | `policy` |
| `tests/test_impact.py` | 36 | `limit` |
| `tests/test_impact.py` | 39 | `at` |
| `tests/test_impact.py` | 39 | `row` |
| `tests/test_impact.py` | 40 | `impact` |
| `tests/test_impact.py` | 41 | `row` |
| `tests/test_impact.py` | 41 | `statuses` |
| `tests/test_impact.py` | 44 | `changed` |
| `tests/test_impact.py` | 45 | `profile` |
| `tests/test_impact.py` | 47 | `unknown` |
| `tests/test_impact.py` | 49 | `row` |
| `tests/test_impact.py` | 54 | `finding` |
| `tests/test_impact.py` | 56 | `same` |
| `tests/test_impact.py` | 57 | `row` |
| `tests/test_impact.py` | 57 | `rows` |
| `tests/test_impact.py` | 60 | `test_actual_preview_api_roles_csrf_generation_immutability_and_race(store, state, assumptions, login, client, monkeypatch)` |
| `tests/test_impact.py` | 64 | `body` |
| `tests/test_impact.py` | 69 | `endpoint` |
| `tests/test_impact.py` | 70 | `role` |
| `tests/test_impact.py` | 74 | `original` |
| `tests/test_impact.py` | 75 | `token` |
| `tests/test_impact.py` | 78 | `result` |
| `tests/test_impact.py` | 86 | `concurrent()` |
| `tests/test_impact.py` | 88 | `result` |
| `tests/test_impact.py` | 99 | `test_tampered_source_ledger_cannot_be_previewed(store, state, assumptions, login, client)` |
| `tests/test_impact.py` | 102 | `db` |
| `tests/test_impact.py` | 104 | `response` |
| `tests/test_lifecycle.py` | 12 | `NOTE` |
| `tests/test_lifecycle.py` | 15 | `test_two_repairs_do_not_deadlock_or_close_other_defects(client, login, post)` |
| `tests/test_lifecycle.py` | 18 | `second` |
| `tests/test_lifecycle.py` | 19 | `second_id` |
| `tests/test_lifecycle.py` | 20 | `identifier` |
| `tests/test_lifecycle.py` | 29 | `first` |
| `tests/test_lifecycle.py` | 32 | `second` |
| `tests/test_lifecycle.py` | 37 | `by_id(values, identifier)` |
| `tests/test_lifecycle.py` | 39 | `value` |
| `tests/test_lifecycle.py` | 42 | `test_swap_keeps_component_life_and_usage_attribution(client, login, post)` |
| `tests/test_lifecycle.py` | 45 | `key` |
| `tests/test_lifecycle.py` | 46 | `response` |
| `tests/test_lifecycle.py` | 50 | `state` |
| `tests/test_lifecycle.py` | 59 | `swapped` |
| `tests/test_lifecycle.py` | 65 | `after` |
| `tests/test_lifecycle.py` | 76 | `evidence` |
| `tests/test_lifecycle.py` | 82 | `test_idempotency_retries_content_binding_and_concurrent_exactly_once(client, login, store)` |
| `tests/test_lifecycle.py` | 85 | `body` |
| `tests/test_lifecycle.py` | 93 | `first` |
| `tests/test_lifecycle.py` | 94 | `second` |
| `tests/test_lifecycle.py` | 99 | `command` |
| `tests/test_lifecycle.py` | 102 | `pool` |
| `tests/test_lifecycle.py` | 103 | `results` |
| `tests/test_lifecycle.py` | 108 | `result` |
| `tests/test_lifecycle.py` | 112 | `test_stale_concurrent_writes_and_failed_swap_rollback(client, login, post)` |
| `tests/test_lifecycle.py` | 115 | `initial` |
| `tests/test_lifecycle.py` | 116 | `component` |
| `tests/test_lifecycle.py` | 117 | `response` |
| `tests/test_lifecycle.py` | 132 | `stale` |
| `tests/test_lifecycle.py` | 140 | `unknown` |
| `tests/test_lifecycle.py` | 144 | `test_independent_work_fresh_inspection_and_preserved_warning(client, login, post)` |
| `tests/test_lifecycle.py` | 163 | `verified` |
| `tests/test_lifecycle.py` | 169 | `test_failed_inspection_cannot_be_erased_by_pass_and_self_review_denied(client, login, post, store)` |
| `tests/test_lifecycle.py` | 174 | `failed` |
| `tests/test_lifecycle.py` | 175 | `defect` |
| `tests/test_lifecycle.py` | 185 | `db` |
| `tests/test_lifecycle.py` | 190 | `test_retirement_is_irreversible_and_preserves_serial_and_life(client, login, post)` |
| `tests/test_lifecycle.py` | 200 | `retired` |
| `tests/test_lifecycle.py` | 222 | `part` |
| `tests/test_lifecycle.py` | 235 | `test_counter_overflow_and_bad_nonbattery_measurements(client, login, post)` |
| `tests/test_lifecycle.py` | 238 | `part` |
| `tests/test_lifecycle.py` | 279 | `test_records_and_ledger_are_immutable_sql_and_explicit_caps(store, client, login, post, monkeypatch)` |
| `tests/test_lifecycle.py` | 285 | `db` |
| `tests/test_lifecycle.py` | 288 | `before` |
| `tests/test_network.py` | 15 | `test_forwarded_headers_do_not_bypass_real_server_throttle(tmp_path, monkeypatch)` |
| `tests/test_network.py` | 17 | `reservation` |
| `tests/test_network.py` | 19 | `port` |
| `tests/test_network.py` | 20 | `app` |
| `tests/test_network.py` | 23 | `server` |
| `tests/test_network.py` | 33 | `thread` |
| `tests/test_network.py` | 36 | `_` |
| `tests/test_network.py` | 41 | `origin` |
| `tests/test_network.py` | 42 | `client` |
| `tests/test_network.py` | 43 | `index` |
| `tests/test_network.py` | 44 | `response` |
| `tests/test_osv_policy.py` | 12 | `lock()` |
| `tests/test_osv_policy.py` | 24 | `report()` |
| `tests/test_osv_policy.py` | 32 | `name` |
| `tests/test_osv_policy.py` | 32 | `version` |
| `tests/test_osv_policy.py` | 39 | `test_complete_inventory()` |
| `tests/test_osv_policy.py` | 41 | `expected` |
| `tests/test_osv_policy.py` | 55 | `test_invalid_lock(change)` |
| `tests/test_osv_policy.py` | 57 | `data` |
| `tests/test_osv_policy.py` | 82 | `test_incomplete_or_finding_never_passes(change)` |
| `tests/test_osv_policy.py` | 84 | `data` |
| `tests/test_publication_text.py` | 15 | `edition(root, name, main, text)` |
| `tests/test_publication_text.py` | 17 | `path` |
| `tests/test_publication_text.py` | 19 | `package` |
| `tests/test_publication_text.py` | 34 | `test_named_office_xml_remains_visible(tmp_path, name, main)` |
| `tests/test_publication_text.py` | 36 | `text` |
| `tests/test_publication_text.py` | 40 | `test_unknown_binary_is_not_an_exclusion(tmp_path)` |
| `tests/test_publication_text.py` | 42 | `path` |
| `tests/test_publication_text.py` | 47 | `test_missing_document_root_is_rejected(tmp_path)` |
| `tests/test_publication_text.py` | 53 | `test_invalid_zip_is_rejected(tmp_path)` |
| `tests/test_publication_text.py` | 55 | `path` |
| `tests/test_publication_text.py` | 62 | `test_invalid_utf8_xml_is_rejected(tmp_path)` |
| `tests/test_publication_text.py` | 68 | `test_expansion_budget_is_active(tmp_path)` |
| `tests/test_publication_text.py` | 70 | `path` |
| `tests/test_security.py` | 14 | `test_anonymous_boundary_and_private_static_files(client)` |
| `tests/test_security.py` | 16 | `path` |
| `tests/test_security.py` | 24 | `path` |
| `tests/test_security.py` | 33 | `response` |
| `tests/test_security.py` | 35 | `name` |
| `tests/test_security.py` | 35 | `value` |
| `tests/test_security.py` | 61 | `test_csrf_session_hash_expiry_revocation_and_live_roles(client, login, store)` |
| `tests/test_security.py` | 64 | `token` |
| `tests/test_security.py` | 65 | `db` |
| `tests/test_security.py` | 66 | `row` |
| `tests/test_security.py` | 71 | `db` |
| `tests/test_security.py` | 79 | `db` |
| `tests/test_security.py` | 87 | `test_roles_and_body_capacity(client, login, post, monkeypatch)` |
| `tests/test_security.py` | 90 | `body` |
| `tests/test_security.py` | 90 | `path` |
| `tests/test_security.py` | 113 | `test_login_limits_unknown_password_and_bounded_sessions(client, accounts, store, monkeypatch)` |
| `tests/test_security.py` | 115 | `body` |
| `tests/test_security.py` | 123 | `_` |
| `tests/test_security.py` | 124 | `response` |
| `tests/test_security.py` | 130 | `db` |
| `tests/test_security.py` | 132 | `db` |
| `tests/test_security.py` | 135 | `i` |
| `tests/test_security.py` | 140 | `test_provisioning_password_bounds_and_uniqueness(store)` |
| `tests/test_security.py` | 142 | `name` |
| `tests/test_security.py` | 142 | `password` |
| `tests/test_security.py` | 142 | `role` |
| `tests/test_security.py` | 155 | `test_invalid_port_and_unbuilt_ui(tmp_path, client, monkeypatch)` |
| `tools/audit_osv.py` | 17 | `ROOT` |
| `tools/audit_osv.py` | 18 | `VERSION` |
| `tools/audit_osv.py` | 19 | `BINARIES` |
| `tools/audit_osv.py` | 47 | `expected_packages(lock)` |
| `tools/audit_osv.py` | 51 | `expected` |
| `tools/audit_osv.py` | 52 | `location` |
| `tools/audit_osv.py` | 52 | `package` |
| `tools/audit_osv.py` | 55 | `name` |
| `tools/audit_osv.py` | 56 | `version` |
| `tools/audit_osv.py` | 73 | `verify_report(report, expected)` |
| `tools/audit_osv.py` | 81 | `scanned` |
| `tools/audit_osv.py` | 82 | `result` |
| `tools/audit_osv.py` | 83 | `source` |
| `tools/audit_osv.py` | 91 | `item` |
| `tools/audit_osv.py` | 92 | `package` |
| `tools/audit_osv.py` | 99 | `findings` |
| `tools/audit_osv.py` | 108 | `main()` |
| `tools/audit_osv.py` | 110 | `checksum` |
| `tools/audit_osv.py` | 110 | `name` |
| `tools/audit_osv.py` | 111 | `directory` |
| `tools/audit_osv.py` | 113 | `binary` |
| `tools/audit_osv.py` | 115 | `url` |
| `tools/audit_osv.py` | 116 | `output` |
| `tools/audit_osv.py` | 116 | `response` |
| `tools/audit_osv.py` | 117 | `chunk` |
| `tools/audit_osv.py` | 122 | `config` |
| `tools/audit_osv.py` | 125 | `expected` |
| `tools/audit_osv.py` | 128 | `report` |
| `tools/audit_osv.py` | 129 | `command` |
| `tools/audit_osv.py` | 139 | `result` |
| `tools/audit_osv.py` | 144 | `scanned` |
| `tools/benchmark.py` | 15 | `measure(action, count)` |
| `tools/benchmark.py` | 18 | `values` |
| `tools/benchmark.py` | 19 | `_` |
| `tools/benchmark.py` | 20 | `started` |
| `tools/benchmark.py` | 30 | `main()` |
| `tools/benchmark.py` | 32 | `directory` |
| `tools/benchmark.py` | 33 | `store` |
| `tools/benchmark.py` | 35 | `_` |
| `tools/benchmark.py` | 35 | `state` |
| `tools/benchmark.py` | 36 | `assumptions` |
| `tools/benchmark.py` | 37 | `at` |
| `tools/benchmark.py` | 38 | `report` |
| `tools/browser_server.py` | 15 | `prepare(directory)` |
| `tools/browser_server.py` | 18 | `db` |
| `tools/browser_server.py` | 19 | `store` |
| `tools/browser_server.py` | 21 | `credentials` |
| `tools/browser_server.py` | 23 | `values` |
| `tools/browser_server.py` | 25 | `role` |
| `tools/browser_server.py` | 27 | `record` |
| `tools/browser_server.py` | 27 | `role` |
| `tools/browser_server.py` | 33 | `main()` |
| `tools/browser_server.py` | 35 | `parser` |
| `tools/browser_server.py` | 38 | `args` |
| `tools/check_repo.py` | 14 | `main()` |
| `tools/check_repo.py` | 16 | `path` |
| `tools/check_repo.py` | 17 | `relative` |
| `tools/check_repo.py` | 18 | `content` |
| `tools/check_repo.py` | 36 | `ref` |
| `tools/check_repo.py` | 39 | `budget` |
| `tools/check_repo.py` | 39 | `suffix` |
| `tools/check_repo.py` | 40 | `size` |
| `tools/check_repo.py` | 41 | `p` |
| `tools/docs_index.py` | 18 | `ROOT` |
| `tools/docs_index.py` | 19 | `EXCLUDE` |
| `tools/docs_index.py` | 33 | `SPECIAL` |
| `tools/docs_index.py` | 50 | `files()` |
| `tools/docs_index.py` | 52 | `result` |
| `tools/docs_index.py` | 53 | `children` |
| `tools/docs_index.py` | 53 | `directory` |
| `tools/docs_index.py` | 53 | `names` |
| `tools/docs_index.py` | 54 | `child` |
| `tools/docs_index.py` | 55 | `name` |
| `tools/docs_index.py` | 61 | `render()` |
| `tools/docs_index.py` | 63 | `catalog` |
| `tools/docs_index.py` | 71 | `source` |
| `tools/docs_index.py` | 80 | `path` |
| `tools/docs_index.py` | 81 | `relative` |
| `tools/docs_index.py` | 82 | `content` |
| `tools/docs_index.py` | 83 | `description` |
| `tools/docs_index.py` | 86 | `line` |
| `tools/docs_index.py` | 94 | `records` |
| `tools/docs_index.py` | 96 | `node` |
| `tools/docs_index.py` | 98 | `args` |
| `tools/docs_index.py` | 101 | `a` |
| `tools/docs_index.py` | 109 | `line` |
| `tools/docs_index.py` | 109 | `value` |
| `tools/docs_index.py` | 112 | `line` |
| `tools/docs_index.py` | 112 | `name` |
| `tools/docs_index.py` | 113 | `node` |
| `tools/docs_index.py` | 127 | `main()` |
| `tools/docs_index.py` | 129 | `content` |
| `tools/docs_index.py` | 129 | `relative` |
| `tools/docs_index.py` | 130 | `path` |
| `tools/publication_text.py` | 11 | `EDITION_ROOTS` |
| `tools/publication_text.py` | 16 | `MAX_PACKAGE_BYTES` |
| `tools/publication_text.py` | 17 | `MAX_EXPANDED_BYTES` |
| `tools/publication_text.py` | 18 | `MAX_MEMBER_BYTES` |
| `tools/publication_text.py` | 19 | `MAX_MEMBERS` |
| `tools/publication_text.py` | 22 | `public_text(path, root)` |
| `tools/publication_text.py` | 24 | `relative` |
| `tools/publication_text.py` | 28 | `source` |
| `tools/publication_text.py` | 31 | `package` |
| `tools/publication_text.py` | 32 | `members` |
| `tools/publication_text.py` | 33 | `member` |
| `tools/publication_text.py` | 33 | `names` |
| `tools/publication_text.py` | 38 | `member` |
| `tools/publication_text.py` | 40 | `result` |
| `tools/publication_text.py` | 41 | `member` |
| `tools/publication_text.py` | 50 | `stream` |
| `tools/publication_text.py` | 51 | `payload` |
| `workbench/__main__.py` | 14 | `main()` |
| `workbench/__main__.py` | 16 | `parser` |
| `workbench/__main__.py` | 18 | `commands` |
| `workbench/__main__.py` | 19 | `init` |
| `workbench/__main__.py` | 21 | `user` |
| `workbench/__main__.py` | 26 | `serve` |
| `workbench/__main__.py` | 28 | `args` |
| `workbench/__main__.py` | 29 | `store` |
| `workbench/__main__.py` | 36 | `password` |
| `workbench/api.py` | 35 | `ROOT` |
| `workbench/api.py` | 36 | `BODY_GATE` |
| `workbench/api.py` | 37 | `HEADERS` |
| `workbench/api.py` | 47 | `create_app(database, port)` |
| `workbench/api.py` | 51 | `authority` |
| `workbench/api.py` | 51 | `origin` |
| `workbench/api.py` | 52 | `app` |
| `workbench/api.py` | 55 | `store` |
| `workbench/api.py` | 58 | `boundary(request, call_next)` |
| `workbench/api.py` | 60 | `acquired` |
| `workbench/api.py` | 80 | `acquired` |
| `workbench/api.py` | 81 | `data` |
| `workbench/api.py` | 83 | `chunk` |
| `workbench/api.py` | 88 | `response` |
| `workbench/api.py` | 90 | `response` |
| `workbench/api.py` | 92 | `response` |
| `workbench/api.py` | 100 | `invalid(_request, error)` |
| `workbench/api.py` | 105 | `e` |
| `workbench/api.py` | 111 | `conflict(_request, _error)` |
| `workbench/api.py` | 118 | `health()` |
| `workbench/api.py` | 123 | `login(body, request)` |
| `workbench/api.py` | 125 | `token` |
| `workbench/api.py` | 125 | `user` |
| `workbench/api.py` | 126 | `response` |
| `workbench/api.py` | 133 | `me(request)` |
| `workbench/api.py` | 138 | `logout(request)` |
| `workbench/api.py` | 141 | `response` |
| `workbench/api.py` | 146 | `workspace(request)` |
| `workbench/api.py` | 152 | `aircraft(body, request)` |
| `workbench/api.py` | 158 | `component(body, request)` |
| `workbench/api.py` | 164 | `publish(body, request)` |
| `workbench/api.py` | 170 | `preview_policy(body, request)` |
| `workbench/api.py` | 175 | `swap(body, request)` |
| `workbench/api.py` | 181 | `usage(body, request)` |
| `workbench/api.py` | 183 | `result` |
| `workbench/api.py` | 187 | `inspect(body, request)` |
| `workbench/api.py` | 193 | `defect(body, request)` |
| `workbench/api.py` | 199 | `work(body, request)` |
| `workbench/api.py` | 205 | `verify(body, request)` |
| `workbench/api.py` | 211 | `retire(body, request)` |
| `workbench/api.py` | 217 | `assess(body, request)` |
| `workbench/api.py` | 219 | `identifier` |
| `workbench/api.py` | 223 | `report(identifier, request)` |
| `workbench/api.py` | 229 | `review(identifier, body, request)` |
| `workbench/api.py` | 235 | `export(identifier, request)` |
| `workbench/api.py` | 244 | `evidence(request)` |
| `workbench/api.py` | 253 | `index()` |
| `workbench/auth.py` | 17 | `HASHER` |
| `workbench/auth.py` | 18 | `DUMMY` |
| `workbench/auth.py` | 19 | `VERIFY_GATE` |
| `workbench/auth.py` | 22 | `add_user(store, username, password, role)` |
| `workbench/auth.py` | 35 | `hashed` |
| `workbench/auth.py` | 36 | `db` |
| `workbench/auth.py` | 40 | `sign_in(request, username, password)` |
| `workbench/auth.py` | 42 | `store` |
| `workbench/auth.py` | 43 | `now` |
| `workbench/auth.py` | 44 | `client` |
| `workbench/auth.py` | 47 | `db` |
| `workbench/auth.py` | 49 | `row` |
| `workbench/auth.py` | 58 | `user` |
| `workbench/auth.py` | 69 | `csrf` |
| `workbench/auth.py` | 69 | `token` |
| `workbench/auth.py` | 70 | `db` |
| `workbench/auth.py` | 83 | `identity(request)` |
| `workbench/auth.py` | 85 | `token` |
| `workbench/auth.py` | 88 | `db` |
| `workbench/auth.py` | 89 | `row` |
| `workbench/auth.py` | 98 | `authorize(request, role)` |
| `workbench/auth.py` | 100 | `user` |
| `workbench/auth.py` | 110 | `sign_out(request)` |
| `workbench/auth.py` | 113 | `db` |
| `workbench/engine.py` | 10 | `RANK` |
| `workbench/engine.py` | 13 | `worst(statuses)` |
| `workbench/engine.py` | 18 | `active_policy(state)` |
| `workbench/engine.py` | 21 | `p` |
| `workbench/engine.py` | 25 | `indexes(state)` |
| `workbench/engine.py` | 27 | `defects` |
| `workbench/engine.py` | 27 | `inspections` |
| `workbench/engine.py` | 28 | `entry` |
| `workbench/engine.py` | 34 | `defect` |
| `workbench/engine.py` | 37 | `p` |
| `workbench/engine.py` | 40 | `component_result(part, limit, inspection, defects, policy, at, assumptions)` |
| `workbench/engine.py` | 42 | `findings` |
| `workbench/engine.py` | 44 | `add(code, status, message)` |
| `workbench/engine.py` | 52 | `remaining_cycles` |
| `workbench/engine.py` | 52 | `remaining_seconds` |
| `workbench/engine.py` | 53 | `due` |
| `workbench/engine.py` | 57 | `remaining_seconds` |
| `workbench/engine.py` | 58 | `remaining_cycles` |
| `workbench/engine.py` | 59 | `key` |
| `workbench/engine.py` | 59 | `maximum` |
| `workbench/engine.py` | 59 | `used` |
| `workbench/engine.py` | 81 | `due` |
| `workbench/engine.py` | 104 | `defect` |
| `workbench/engine.py` | 110 | `f` |
| `workbench/engine.py` | 110 | `status` |
| `workbench/engine.py` | 111 | `estimates` |
| `workbench/engine.py` | 133 | `evaluate(state, at, assumptions)` |
| `workbench/engine.py` | 141 | `policy` |
| `workbench/engine.py` | 142 | `defects` |
| `workbench/engine.py` | 142 | `inspections` |
| `workbench/engine.py` | 142 | `parts` |
| `workbench/engine.py` | 143 | `limit` |
| `workbench/engine.py` | 143 | `limits` |
| `workbench/engine.py` | 144 | `results` |
| `workbench/engine.py` | 154 | `key` |
| `workbench/engine.py` | 154 | `part` |
| `workbench/engine.py` | 156 | `installations` |
| `workbench/engine.py` | 158 | `item` |
| `workbench/engine.py` | 161 | `positions` |
| `workbench/engine.py` | 162 | `aircraft_id` |
| `workbench/engine.py` | 162 | `slot_id` |
| `workbench/engine.py` | 164 | `profile` |
| `workbench/engine.py` | 164 | `profiles` |
| `workbench/engine.py` | 165 | `aircraft` |
| `workbench/engine.py` | 166 | `asset` |
| `workbench/engine.py` | 167 | `findings` |
| `workbench/engine.py` | 167 | `slots` |
| `workbench/engine.py` | 176 | `profile` |
| `workbench/engine.py` | 186 | `slot` |
| `workbench/engine.py` | 187 | `identifier` |
| `workbench/engine.py` | 189 | `value` |
| `workbench/engine.py` | 198 | `value` |
| `workbench/engine.py` | 207 | `value` |
| `workbench/engine.py` | 213 | `known` |
| `workbench/engine.py` | 213 | `slot` |
| `workbench/engine.py` | 229 | `f` |
| `workbench/engine.py` | 229 | `s` |
| `workbench/engine.py` | 234 | `upcoming` |
| `workbench/engine.py` | 236 | `result` |
| `workbench/engine.py` | 244 | `a` |
| `workbench/examples.py` | 9 | `example_policy()` |
| `workbench/examples.py` | 28 | `cycles` |
| `workbench/examples.py` | 28 | `days` |
| `workbench/examples.py` | 28 | `kind` |
| `workbench/examples.py` | 28 | `seconds` |
| `workbench/examples.py` | 41 | `example_records(now)` |
| `workbench/examples.py` | 43 | `aircraft` |
| `workbench/examples.py` | 43 | `components` |
| `workbench/examples.py` | 43 | `inspections` |
| `workbench/examples.py` | 43 | `installations` |
| `workbench/examples.py` | 44 | `index` |
| `workbench/examples.py` | 44 | `key` |
| `workbench/examples.py` | 44 | `label` |
| `workbench/examples.py` | 51 | `base` |
| `workbench/examples.py` | 64 | `kind` |
| `workbench/examples.py` | 64 | `slot` |
| `workbench/examples.py` | 69 | `identifier` |
| `workbench/examples.py` | 70 | `cycles` |
| `workbench/examples.py` | 70 | `seconds` |
| `workbench/examples.py` | 140 | `defects` |
| `workbench/impact.py` | 13 | `policy_impact(state, policy, at, assumptions)` |
| `workbench/impact.py` | 15 | `hypothetical` |
| `workbench/impact.py` | 18 | `record` |
| `workbench/impact.py` | 21 | `after` |
| `workbench/impact.py` | 21 | `before` |
| `workbench/impact.py` | 22 | `changes` |
| `workbench/impact.py` | 23 | `kind` |
| `workbench/impact.py` | 24 | `previous` |
| `workbench/impact.py` | 24 | `row` |
| `workbench/impact.py` | 32 | `row` |
| `workbench/models.py` | 10 | `Key` |
| `workbench/models.py` | 11 | `Kind` |
| `workbench/models.py` | 12 | `Counter` |
| `workbench/models.py` | 13 | `Note` |
| `workbench/models.py` | 16 | `StrictModel(class)` |
| `workbench/models.py` | 19 | `model_config` |
| `workbench/models.py` | 22 | `Login(class)` |
| `workbench/models.py` | 25 | `username` |
| `workbench/models.py` | 26 | `password` |
| `workbench/models.py` | 29 | `Limit(class)` |
| `workbench/models.py` | 32 | `kind` |
| `workbench/models.py` | 33 | `seconds` |
| `workbench/models.py` | 34 | `cycles` |
| `workbench/models.py` | 35 | `inspection_days` |
| `workbench/models.py` | 38 | `Slot(class)` |
| `workbench/models.py` | 41 | `id` |
| `workbench/models.py` | 42 | `kind` |
| `workbench/models.py` | 45 | `Profile(class)` |
| `workbench/models.py` | 48 | `id` |
| `workbench/models.py` | 49 | `label` |
| `workbench/models.py` | 50 | `slots` |
| `workbench/models.py` | 53 | `unique(self)` |
| `workbench/models.py` | 55 | `slot` |
| `workbench/models.py` | 60 | `Policy(class)` |
| `workbench/models.py` | 63 | `label` |
| `workbench/models.py` | 64 | `reference` |
| `workbench/models.py` | 65 | `profiles` |
| `workbench/models.py` | 66 | `limits` |
| `workbench/models.py` | 67 | `warning_percent` |
| `workbench/models.py` | 68 | `battery_min_capacity_pct` |
| `workbench/models.py` | 69 | `battery_max_resistance_mohm` |
| `workbench/models.py` | 72 | `complete(self)` |
| `workbench/models.py` | 74 | `kinds` |
| `workbench/models.py` | 74 | `limit` |
| `workbench/models.py` | 75 | `p` |
| `workbench/models.py` | 79 | `profile` |
| `workbench/models.py` | 79 | `slot` |
| `workbench/models.py` | 84 | `Asset(class)` |
| `workbench/models.py` | 87 | `id` |
| `workbench/models.py` | 88 | `serial` |
| `workbench/models.py` | 89 | `label` |
| `workbench/models.py` | 90 | `opening_seconds` |
| `workbench/models.py` | 91 | `opening_cycles` |
| `workbench/models.py` | 92 | `history_complete` |
| `workbench/models.py` | 93 | `source_note` |
| `workbench/models.py` | 96 | `Aircraft(class)` |
| `workbench/models.py` | 99 | `profile` |
| `workbench/models.py` | 102 | `Component(class)` |
| `workbench/models.py` | 105 | `kind` |
| `workbench/models.py` | 108 | `Change(class)` |
| `workbench/models.py` | 111 | `expected_generation` |
| `workbench/models.py` | 114 | `Publish(class)` |
| `workbench/models.py` | 117 | `policy` |
| `workbench/models.py` | 120 | `NewAircraft(class)` |
| `workbench/models.py` | 123 | `aircraft` |
| `workbench/models.py` | 126 | `NewComponent(class)` |
| `workbench/models.py` | 129 | `component` |
| `workbench/models.py` | 132 | `Swap(class)` |
| `workbench/models.py` | 135 | `aircraft` |
| `workbench/models.py` | 136 | `slot` |
| `workbench/models.py` | 137 | `component` |
| `workbench/models.py` | 138 | `note` |
| `workbench/models.py` | 141 | `Usage(class)` |
| `workbench/models.py` | 144 | `aircraft` |
| `workbench/models.py` | 145 | `seconds` |
| `workbench/models.py` | 146 | `cycles` |
| `workbench/models.py` | 147 | `request_id` |
| `workbench/models.py` | 148 | `note` |
| `workbench/models.py` | 151 | `Inspection(class)` |
| `workbench/models.py` | 154 | `component` |
| `workbench/models.py` | 155 | `passed` |
| `workbench/models.py` | 156 | `capacity_pct` |
| `workbench/models.py` | 157 | `resistance_mohm` |
| `workbench/models.py` | 158 | `note` |
| `workbench/models.py` | 161 | `Defect(class)` |
| `workbench/models.py` | 164 | `component` |
| `workbench/models.py` | 165 | `severity` |
| `workbench/models.py` | 166 | `note` |
| `workbench/models.py` | 169 | `Work(class)` |
| `workbench/models.py` | 172 | `defect` |
| `workbench/models.py` | 173 | `note` |
| `workbench/models.py` | 176 | `Verify(class)` |
| `workbench/models.py` | 179 | `work` |
| `workbench/models.py` | 180 | `note` |
| `workbench/models.py` | 183 | `Retire(class)` |
| `workbench/models.py` | 186 | `component` |
| `workbench/models.py` | 187 | `note` |
| `workbench/models.py` | 190 | `Assumptions(class)` |
| `workbench/models.py` | 193 | `daily_seconds` |
| `workbench/models.py` | 194 | `daily_cycles` |
| `workbench/models.py` | 197 | `Assess(class)` |
| `workbench/models.py` | 200 | `assumptions` |
| `workbench/models.py` | 203 | `PolicyPreview(class)` |
| `workbench/models.py` | 206 | `assumptions` |
| `workbench/models.py` | 209 | `Review(class)` |
| `workbench/models.py` | 212 | `note` |
| `workbench/schema.sql` | 3 | `PRAGMA foreign_keys=ON;` |
| `workbench/schema.sql` | 4 | `CREATE TABLE IF NOT EXISTS users(name TEXT PRIMARY KEY,password_hash TEXT NOT NULL,role TEXT NOT NULL CHECK(role IN ('admin','operator','technician','reviewer')));` |
| `workbench/schema.sql` | 5 | `CREATE TABLE IF NOT EXISTS sessions(digest TEXT PRIMARY KEY,username TEXT NOT NULL REFERENCES users(name),csrf TEXT NOT NULL,expires REAL NOT NULL,created REAL NOT NULL);` |
| `workbench/schema.sql` | 6 | `CREATE INDEX IF NOT EXISTS sessions_user ON sessions(username);` |
| `workbench/schema.sql` | 7 | `CREATE TABLE IF NOT EXISTS attempts(client TEXT PRIMARY KEY,count INTEGER NOT NULL,started REAL NOT NULL);` |
| `workbench/schema.sql` | 8 | `CREATE TABLE IF NOT EXISTS policies(version INTEGER PRIMARY KEY,content TEXT NOT NULL);` |
| `workbench/schema.sql` | 9 | `CREATE TABLE IF NOT EXISTS workspace(id INTEGER PRIMARY KEY CHECK(id=1),generation INTEGER NOT NULL,policy INTEGER NOT NULL REFERENCES policies(version));` |
| `workbench/schema.sql` | 10 | `CREATE TABLE IF NOT EXISTS aircraft(id TEXT PRIMARY KEY,serial TEXT NOT NULL UNIQUE,content TEXT NOT NULL,seconds INTEGER NOT NULL CHECK(seconds BETWEEN 0 AND 1000000000000),cycles INTEGER NOT NULL CHECK(cycles BETWEEN 0 AND 1000000000000));` |
| `workbench/schema.sql` | 11 | `CREATE TABLE IF NOT EXISTS components(id TEXT PRIMARY KEY,serial TEXT NOT NULL UNIQUE,content TEXT NOT NULL,seconds INTEGER NOT NULL CHECK(seconds BETWEEN 0 AND 1000000000000),cycles INTEGER NOT NULL CHECK(cycles BETWEEN 0 AND 1000000000000),retired INTEGER NOT NULL CHECK(retired IN (0,1)));` |
| `workbench/schema.sql` | 12 | `CREATE TABLE IF NOT EXISTS installations(id INTEGER PRIMARY KEY,aircraft TEXT NOT NULL REFERENCES aircraft(id),slot TEXT NOT NULL,component TEXT NOT NULL REFERENCES components(id),installed INTEGER NOT NULL,removed INTEGER);` |
| `workbench/schema.sql` | 13 | `CREATE UNIQUE INDEX IF NOT EXISTS one_location ON installations(component) WHERE removed IS NULL;` |
| `workbench/schema.sql` | 14 | `CREATE UNIQUE INDEX IF NOT EXISTS one_part_per_slot ON installations(aircraft,slot) WHERE removed IS NULL;` |
| `workbench/schema.sql` | 15 | `CREATE TABLE IF NOT EXISTS inspections(id INTEGER PRIMARY KEY,component TEXT NOT NULL REFERENCES components(id),passed INTEGER NOT NULL CHECK(passed IN (0,1)),capacity REAL,resistance REAL,note TEXT NOT NULL,actor TEXT NOT NULL,at REAL NOT NULL,generation INTEGER NOT NULL);` |
| `workbench/schema.sql` | 16 | `CREATE INDEX IF NOT EXISTS inspections_latest ON inspections(component,id DESC);` |
| `workbench/schema.sql` | 17 | `CREATE TABLE IF NOT EXISTS defects(id INTEGER PRIMARY KEY,component TEXT NOT NULL REFERENCES components(id),severity TEXT NOT NULL CHECK(severity IN ('watch','blocking')),note TEXT NOT NULL,actor TEXT NOT NULL,at REAL NOT NULL,closed INTEGER NOT NULL CHECK(closed IN (0,1)));` |
| `workbench/schema.sql` | 18 | `CREATE TABLE IF NOT EXISTS work(id INTEGER PRIMARY KEY,defect INTEGER NOT NULL UNIQUE REFERENCES defects(id),note TEXT NOT NULL,technician TEXT NOT NULL,at REAL NOT NULL,completed_generation INTEGER NOT NULL,reviewer TEXT,review_note TEXT,verified REAL);` |
| `workbench/schema.sql` | 19 | `CREATE TABLE IF NOT EXISTS usage(id INTEGER PRIMARY KEY,request_id TEXT NOT NULL UNIQUE,request_digest TEXT NOT NULL,aircraft TEXT NOT NULL REFERENCES aircraft(id),seconds INTEGER NOT NULL,cycles INTEGER NOT NULL,components TEXT NOT NULL,note TEXT NOT NULL,actor TEXT NOT NULL,at REAL NOT NULL,generation INTEGER NOT NULL);` |
| `workbench/schema.sql` | 20 | `CREATE INDEX IF NOT EXISTS usage_aircraft ON usage(aircraft,id DESC);` |
| `workbench/schema.sql` | 21 | `CREATE TABLE IF NOT EXISTS ledger(generation INTEGER PRIMARY KEY,actor TEXT NOT NULL,event TEXT NOT NULL,at REAL NOT NULL,previous TEXT NOT NULL,state_digest TEXT NOT NULL,detail TEXT NOT NULL,digest TEXT NOT NULL);` |
| `workbench/schema.sql` | 22 | `CREATE TABLE IF NOT EXISTS assessments(id INTEGER PRIMARY KEY,creator TEXT NOT NULL,created REAL NOT NULL,generation INTEGER NOT NULL,content TEXT NOT NULL,digest TEXT NOT NULL);` |
| `workbench/schema.sql` | 23 | `CREATE TABLE IF NOT EXISTS reviews(assessment INTEGER PRIMARY KEY REFERENCES assessments(id),actor TEXT NOT NULL,note TEXT NOT NULL,at REAL NOT NULL,digest TEXT NOT NULL);` |
| `workbench/schema.sql` | 24 | `CREATE TRIGGER IF NOT EXISTS immutable_policy_update BEFORE UPDATE ON policies BEGIN SELECT RAISE(ABORT,'immutable policy'); END;` |
| `workbench/schema.sql` | 25 | `CREATE TRIGGER IF NOT EXISTS immutable_policy_delete BEFORE DELETE ON policies BEGIN SELECT RAISE(ABORT,'immutable policy'); END;` |
| `workbench/schema.sql` | 26 | `CREATE TRIGGER IF NOT EXISTS immutable_usage_update BEFORE UPDATE ON usage BEGIN SELECT RAISE(ABORT,'immutable usage'); END;` |
| `workbench/schema.sql` | 27 | `CREATE TRIGGER IF NOT EXISTS immutable_usage_delete BEFORE DELETE ON usage BEGIN SELECT RAISE(ABORT,'immutable usage'); END;` |
| `workbench/schema.sql` | 28 | `CREATE TRIGGER IF NOT EXISTS immutable_inspection_update BEFORE UPDATE ON inspections BEGIN SELECT RAISE(ABORT,'immutable inspection'); END;` |
| `workbench/schema.sql` | 29 | `CREATE TRIGGER IF NOT EXISTS immutable_ledger_update BEFORE UPDATE ON ledger BEGIN SELECT RAISE(ABORT,'immutable ledger'); END;` |
| `workbench/schema.sql` | 30 | `CREATE TRIGGER IF NOT EXISTS immutable_ledger_delete BEFORE DELETE ON ledger BEGIN SELECT RAISE(ABORT,'immutable ledger'); END;` |
| `workbench/schema.sql` | 31 | `CREATE TRIGGER IF NOT EXISTS immutable_assessment_update BEFORE UPDATE ON assessments BEGIN SELECT RAISE(ABORT,'immutable assessment'); END;` |
| `workbench/schema.sql` | 32 | `CREATE TRIGGER IF NOT EXISTS immutable_review_update BEFORE UPDATE ON reviews BEGIN SELECT RAISE(ABORT,'immutable review'); END;` |
| `workbench/store.py` | 20 | `QUERIES` |
| `workbench/store.py` | 30 | `CAPACITY` |
| `workbench/store.py` | 42 | `canonical(value)` |
| `workbench/store.py` | 47 | `digest(value)` |
| `workbench/store.py` | 52 | `Store(class)` |
| `workbench/store.py` | 55 | `__init__(self, path)` |
| `workbench/store.py` | 59 | `db` |
| `workbench/store.py` | 63 | `connect(self, write)` |
| `workbench/store.py` | 65 | `db` |
| `workbench/store.py` | 77 | `state(self, db)` |
| `workbench/store.py` | 79 | `workspace` |
| `workbench/store.py` | 82 | `result` |
| `workbench/store.py` | 83 | `query` |
| `workbench/store.py` | 83 | `table` |
| `workbench/store.py` | 84 | `rows` |
| `workbench/store.py` | 85 | `record` |
| `workbench/store.py` | 86 | `value` |
| `workbench/store.py` | 88 | `content` |
| `workbench/store.py` | 93 | `value` |
| `workbench/store.py` | 100 | `verify(self, db, state)` |
| `workbench/store.py` | 102 | `generation` |
| `workbench/store.py` | 102 | `previous` |
| `workbench/store.py` | 103 | `last` |
| `workbench/store.py` | 104 | `row` |
| `workbench/store.py` | 105 | `value` |
| `workbench/store.py` | 106 | `checksum` |
| `workbench/store.py` | 113 | `generation` |
| `workbench/store.py` | 113 | `last` |
| `workbench/store.py` | 113 | `previous` |
| `workbench/store.py` | 122 | `seal(self, db, actor, event, detail)` |
| `workbench/store.py` | 124 | `state` |
| `workbench/store.py` | 125 | `row` |
| `workbench/store.py` | 126 | `value` |
| `workbench/store.py` | 137 | `initialize(self, examples)` |
| `workbench/store.py` | 139 | `db` |
| `workbench/store.py` | 145 | `records` |
| `workbench/store.py` | 146 | `table` |
| `workbench/store.py` | 147 | `value` |
| `workbench/store.py` | 149 | `item` |
| `workbench/store.py` | 153 | `item` |
| `workbench/store.py` | 157 | `item` |
| `workbench/store.py` | 163 | `insert_asset(self, db, table, value)` |
| `workbench/store.py` | 167 | `content` |
| `workbench/store.py` | 167 | `k` |
| `workbench/store.py` | 167 | `v` |
| `workbench/store.py` | 168 | `values` |
| `workbench/store.py` | 182 | `snapshot(self)` |
| `workbench/store.py` | 184 | `db` |
| `workbench/store.py` | 186 | `state` |
| `workbench/store.py` | 187 | `tip` |
| `workbench/store.py` | 191 | `change(self, expected, user, event, roles, detail)` |
| `workbench/store.py` | 195 | `db` |
| `workbench/store.py` | 196 | `state` |
| `workbench/store.py` | 208 | `entity(self, state, table, identifier)` |
| `workbench/store.py` | 210 | `item` |
| `workbench/store.py` | 210 | `result` |
| `workbench/store.py` | 215 | `create(self, body, user, table)` |
| `workbench/store.py` | 217 | `value` |
| `workbench/store.py` | 219 | `db` |
| `workbench/store.py` | 220 | `state` |
| `workbench/store.py` | 221 | `_` |
| `workbench/store.py` | 226 | `p` |
| `workbench/store.py` | 231 | `publish(self, body, user)` |
| `workbench/store.py` | 234 | `db` |
| `workbench/store.py` | 235 | `state` |
| `workbench/store.py` | 236 | `_` |
| `workbench/store.py` | 238 | `version` |
| `workbench/store.py` | 244 | `swap(self, body, user)` |
| `workbench/store.py` | 248 | `db` |
| `workbench/store.py` | 248 | `generation` |
| `workbench/store.py` | 248 | `state` |
| `workbench/store.py` | 249 | `aircraft` |
| `workbench/store.py` | 250 | `profile` |
| `workbench/store.py` | 251 | `p` |
| `workbench/store.py` | 253 | `s` |
| `workbench/store.py` | 253 | `slot` |
| `workbench/store.py` | 257 | `part` |
| `workbench/store.py` | 262 | `i` |
| `workbench/store.py` | 275 | `usage(self, body, user)` |
| `workbench/store.py` | 280 | `request_digest` |
| `workbench/store.py` | 281 | `db` |
| `workbench/store.py` | 282 | `state` |
| `workbench/store.py` | 284 | `previous` |
| `workbench/store.py` | 297 | `aircraft` |
| `workbench/store.py` | 298 | `parts` |
| `workbench/store.py` | 300 | `i` |
| `workbench/store.py` | 303 | `key` |
| `workbench/store.py` | 303 | `value` |
| `workbench/store.py` | 313 | `identifier` |
| `workbench/store.py` | 318 | `generation` |
| `workbench/store.py` | 320 | `cursor` |
| `workbench/store.py` | 338 | `inspect(self, body, user)` |
| `workbench/store.py` | 341 | `db` |
| `workbench/store.py` | 342 | `state` |
| `workbench/store.py` | 343 | `generation` |
| `workbench/store.py` | 345 | `part` |
| `workbench/store.py` | 352 | `now` |
| `workbench/store.py` | 374 | `defect(self, body, user)` |
| `workbench/store.py` | 378 | `_` |
| `workbench/store.py` | 378 | `db` |
| `workbench/store.py` | 378 | `state` |
| `workbench/store.py` | 387 | `complete_work(self, body, user)` |
| `workbench/store.py` | 390 | `db` |
| `workbench/store.py` | 391 | `state` |
| `workbench/store.py` | 392 | `generation` |
| `workbench/store.py` | 394 | `defect` |
| `workbench/store.py` | 395 | `w` |
| `workbench/store.py` | 402 | `verify_work(self, body, user)` |
| `workbench/store.py` | 406 | `db` |
| `workbench/store.py` | 406 | `generation` |
| `workbench/store.py` | 406 | `state` |
| `workbench/store.py` | 407 | `work` |
| `workbench/store.py` | 410 | `defect` |
| `workbench/store.py` | 411 | `part` |
| `workbench/store.py` | 412 | `_` |
| `workbench/store.py` | 412 | `inspections` |
| `workbench/store.py` | 413 | `inspection` |
| `workbench/store.py` | 422 | `policy` |
| `workbench/store.py` | 423 | `limit` |
| `workbench/store.py` | 423 | `p` |
| `workbench/store.py` | 426 | `result` |
| `workbench/store.py` | 446 | `retire(self, body, user)` |
| `workbench/store.py` | 450 | `_` |
| `workbench/store.py` | 450 | `db` |
| `workbench/store.py` | 450 | `state` |
| `workbench/store.py` | 451 | `part` |
| `workbench/store.py` | 454 | `i` |
| `workbench/store.py` | 459 | `assess(self, body, user)` |
| `workbench/store.py` | 461 | `db` |
| `workbench/store.py` | 462 | `state` |
| `workbench/store.py` | 463 | `tip` |
| `workbench/store.py` | 470 | `now` |
| `workbench/store.py` | 471 | `content` |
| `workbench/store.py` | 478 | `cursor` |
| `workbench/store.py` | 484 | `preview_policy(self, body, user)` |
| `workbench/store.py` | 488 | `state` |
| `workbench/store.py` | 488 | `tip` |
| `workbench/store.py` | 491 | `result` |
| `workbench/store.py` | 503 | `report(self, identifier, db)` |
| `workbench/store.py` | 506 | `connection` |
| `workbench/store.py` | 509 | `state` |
| `workbench/store.py` | 511 | `row` |
| `workbench/store.py` | 514 | `content` |
| `workbench/store.py` | 522 | `review` |
| `workbench/store.py` | 525 | `record` |
| `workbench/store.py` | 527 | `checksum` |
| `workbench/store.py` | 530 | `now` |
| `workbench/store.py` | 542 | `review(self, identifier, body, user)` |
| `workbench/store.py` | 546 | `db` |
| `workbench/store.py` | 547 | `report` |
| `workbench/store.py` | 552 | `record` |
| `workbench/store.py` | 560 | `dashboard(self)` |
| `workbench/store.py` | 562 | `db` |
| `workbench/store.py` | 564 | `state` |
| `workbench/store.py` | 565 | `tip` |
| `workbench/store.py` | 574 | `r` |
| `workbench/store.py` | 580 | `r` |
| `workbench/store.py` | 586 | `evidence(self)` |
| `workbench/store.py` | 588 | `db` |
| `workbench/store.py` | 590 | `state` |
| `workbench/store.py` | 591 | `tip` |
| `workbench/store.py` | 598 | `row` |
| `ui/src/main.ts` | 10 | `User` |
| `ui/src/main.ts` | 15 | `Finding` |
| `ui/src/main.ts` | 20 | `Asset` |
| `ui/src/main.ts` | 31 | `PartResult` |
| `ui/src/main.ts` | 40 | `AircraftResult` |
| `ui/src/main.ts` | 46 | `Policy` |
| `ui/src/main.ts` | 50 | `State` |
| `ui/src/main.ts` | 78 | `Dashboard` |
| `ui/src/main.ts` | 85 | `Report` |
| `ui/src/main.ts` | 97 | `ApiError` |
| `ui/src/main.ts` | 99 | `message` |
| `ui/src/main.ts` | 100 | `status` |
| `ui/src/main.ts` | 105 | `user` |
| `ui/src/main.ts` | 106 | `dashboard` |
| `ui/src/main.ts` | 107 | `assessment` |
| `ui/src/main.ts` | 108 | `selectedAircraft` |
| `ui/src/main.ts` | 109 | `selectedComponent` |
| `ui/src/main.ts` | 110 | `epoch` |
| `ui/src/main.ts` | 111 | `busy` |
| `ui/src/main.ts` | 112 | `logoutPending` |
| `ui/src/main.ts` | 113 | `pendingUsage` |
| `ui/src/main.ts` | 114 | `Impact` |
| `ui/src/main.ts` | 133 | `impact` |
| `ui/src/main.ts` | 134 | `impactRevision` |
| `ui/src/main.ts` | 135 | `previewPolicy` |
| `ui/src/main.ts` | 139 | `downloadImpact` |
| `ui/src/main.ts` | 144 | `impactOutput` |
| `ui/src/main.ts` | 153 | `clearImpact` |
| `ui/src/main.ts` | 159 | `id` |
| `ui/src/main.ts` | 165 | `requested` |
| `ui/src/main.ts` | 166 | `result` |
| `ui/src/main.ts` | 179 | `heading` |
| `ui/src/main.ts` | 181 | `notice` |
| `ui/src/main.ts` | 184 | `list` |
| `ui/src/main.ts` | 185 | `row` |
| `ui/src/main.ts` | 186 | `item` |
| `ui/src/main.ts` | 190 | `row` |
| `ui/src/main.ts` | 191 | `item` |
| `ui/src/main.ts` | 192 | `finding` |
| `ui/src/main.ts` | 199 | `url` |
| `ui/src/main.ts` | 202 | `link` |
| `ui/src/main.ts` | 209 | `el` |
| `ui/src/main.ts` | 209 | `id` |
| `ui/src/main.ts` | 213 | `value` |
| `ui/src/main.ts` | 213 | `id` |
| `ui/src/main.ts` | 217 | `text` |
| `ui/src/main.ts` | 217 | `id` |
| `ui/src/main.ts` | 217 | `content` |
| `ui/src/main.ts` | 221 | `buttons` |
| `ui/src/main.ts` | 222 | `button` |
| `ui/src/main.ts` | 223 | `roles` |
| `ui/src/main.ts` | 232 | `api` |
| `ui/src/main.ts` | 232 | `path` |
| `ui/src/main.ts` | 232 | `body` |
| `ui/src/main.ts` | 233 | `generation` |
| `ui/src/main.ts` | 234 | `response` |
| `ui/src/main.ts` | 245 | `result` |
| `ui/src/main.ts` | 256 | `task` |
| `ui/src/main.ts` | 256 | `action` |
| `ui/src/main.ts` | 258 | `generation` |
| `ui/src/main.ts` | 266 | `error` |
| `ui/src/main.ts` | 274 | `reset` |
| `ui/src/main.ts` | 281 | `id` |
| `ui/src/main.ts` | 283 | `id` |
| `ui/src/main.ts` | 299 | `area` |
| `ui/src/main.ts` | 301 | `id` |
| `ui/src/main.ts` | 318 | `options` |
| `ui/src/main.ts` | 319 | `id` |
| `ui/src/main.ts` | 320 | `entries` |
| `ui/src/main.ts` | 321 | `selection` |
| `ui/src/main.ts` | 323 | `select` |
| `ui/src/main.ts` | 324 | `previous` |
| `ui/src/main.ts` | 326 | `[key, label]` |
| `ui/src/main.ts` | 327 | `option` |
| `ui/src/main.ts` | 332 | `[key]` |
| `ui/src/main.ts` | 335 | `findings` |
| `ui/src/main.ts` | 335 | `id` |
| `ui/src/main.ts` | 335 | `entries` |
| `ui/src/main.ts` | 336 | `root` |
| `ui/src/main.ts` | 338 | `finding` |
| `ui/src/main.ts` | 339 | `item` |
| `ui/src/main.ts` | 346 | `render` |
| `ui/src/main.ts` | 346 | `next` |
| `ui/src/main.ts` | 349 | `state` |
| `ui/src/main.ts` | 350 | `asset` |
| `ui/src/main.ts` | 352 | `part` |
| `ui/src/main.ts` | 354 | `metrics` |
| `ui/src/main.ts` | 356 | `status` |
| `ui/src/main.ts` | 362 | `div` |
| `ui/src/main.ts` | 364 | `count` |
| `ui/src/main.ts` | 366 | `asset` |
| `ui/src/main.ts` | 368 | `label` |
| `ui/src/main.ts` | 373 | `policy` |
| `ui/src/main.ts` | 374 | `record` |
| `ui/src/main.ts` | 419 | `part` |
| `ui/src/main.ts` | 424 | `part` |
| `ui/src/main.ts` | 433 | `d` |
| `ui/src/main.ts` | 433 | `work` |
| `ui/src/main.ts` | 435 | `d` |
| `ui/src/main.ts` | 443 | `work` |
| `ui/src/main.ts` | 444 | `work` |
| `ui/src/main.ts` | 453 | `record` |
| `ui/src/main.ts` | 462 | `defects` |
| `ui/src/main.ts` | 464 | `defect` |
| `ui/src/main.ts` | 464 | `entry` |
| `ui/src/main.ts` | 465 | `p` |
| `ui/src/main.ts` | 484 | `roster` |
| `ui/src/main.ts` | 485 | `root` |
| `ui/src/main.ts` | 488 | `asset` |
| `ui/src/main.ts` | 489 | `result` |
| `ui/src/main.ts` | 490 | `item` |
| `ui/src/main.ts` | 497 | `button` |
| `ui/src/main.ts` | 510 | `aircraftDesk` |
| `ui/src/main.ts` | 512 | `asset` |
| `ui/src/main.ts` | 513 | `item` |
| `ui/src/main.ts` | 515 | `result` |
| `ui/src/main.ts` | 516 | `item` |
| `ui/src/main.ts` | 533 | `policy` |
| `ui/src/main.ts` | 534 | `record` |
| `ui/src/main.ts` | 536 | `profile` |
| `ui/src/main.ts` | 536 | `entry` |
| `ui/src/main.ts` | 539 | `slot` |
| `ui/src/main.ts` | 545 | `slot` |
| `ui/src/main.ts` | 546 | `row` |
| `ui/src/main.ts` | 547 | `part` |
| `ui/src/main.ts` | 548 | `entry` |
| `ui/src/main.ts` | 550 | `status` |
| `ui/src/main.ts` | 551 | `entry` |
| `ui/src/main.ts` | 553 | `content` |
| `ui/src/main.ts` | 561 | `cell` |
| `ui/src/main.ts` | 570 | `componentDesk` |
| `ui/src/main.ts` | 572 | `part` |
| `ui/src/main.ts` | 573 | `entry` |
| `ui/src/main.ts` | 575 | `result` |
| `ui/src/main.ts` | 576 | `entry` |
| `ui/src/main.ts` | 588 | `cumulative` |
| `ui/src/main.ts` | 589 | `values` |
| `ui/src/main.ts` | 590 | `record` |
| `ui/src/main.ts` | 595 | `chart` |
| `ui/src/main.ts` | 597 | `line` |
| `ui/src/main.ts` | 608 | `refresh` |
| `ui/src/main.ts` | 614 | `mutate` |
| `ui/src/main.ts` | 615 | `path` |
| `ui/src/main.ts` | 616 | `fields` |
| `ui/src/main.ts` | 627 | `showReport` |
| `ui/src/main.ts` | 627 | `report` |
| `ui/src/main.ts` | 643 | `event` |
| `ui/src/main.ts` | 659 | `csrf` |
| `ui/src/main.ts` | 669 | `response` |
| `ui/src/main.ts` | 695 | `sendUsage` |
| `ui/src/main.ts` | 698 | `next` |
| `ui/src/main.ts` | 708 | `error` |
| `ui/src/main.ts` | 715 | `event` |
| `ui/src/main.ts` | 735 | `event` |
| `ui/src/main.ts` | 739 | `report` |
| `ui/src/main.ts` | 752 | `id` |
| `ui/src/main.ts` | 755 | `event` |
| `ui/src/main.ts` | 766 | `event` |
| `ui/src/main.ts` | 777 | `event` |
| `ui/src/main.ts` | 780 | `battery` |
| `ui/src/main.ts` | 781 | `part` |
| `ui/src/main.ts` | 796 | `event` |
| `ui/src/main.ts` | 806 | `event` |
| `ui/src/main.ts` | 815 | `event` |
| `ui/src/main.ts` | 833 | `event` |
| `ui/src/main.ts` | 839 | `event` |
| `ui/src/main.ts` | 845 | `event` |
| `ui/src/view.test.ts` | 17 | `value` |
| `ui/src/view.ts` | 5 | `statusLabel` |
| `ui/src/view.ts` | 5 | `status` |
| `ui/src/view.ts` | 14 | `minutes` |
| `ui/src/view.ts` | 14 | `seconds` |
| `ui/src/view.ts` | 18 | `reportId` |
| `ui/src/view.ts` | 18 | `value` |
| `ui/src/view.ts` | 19 | `number` |
| `ui/src/view.ts` | 23 | `sparkPoints` |
| `ui/src/view.ts` | 23 | `values` |
| `ui/src/view.ts` | 26 | `value` |
| `ui/src/view.ts` | 29 | `maximum` |
| `ui/src/view.ts` | 32 | `value` |
| `ui/src/view.ts` | 32 | `index` |
| `tests/browser/workspace.spec.ts` | 6 | `directory` |
| `tests/browser/workspace.spec.ts` | 8 | `signIn` |
| `tests/browser/workspace.spec.ts` | 8 | `page` |
| `tests/browser/workspace.spec.ts` | 8 | `role` |
| `tests/browser/workspace.spec.ts` | 9 | `account` |
| `tests/browser/workspace.spec.ts` | 19 | `ready` |
| `tests/browser/workspace.spec.ts` | 19 | `page` |
| `tests/browser/workspace.spec.ts` | 23 | `{ page, }` |
| `tests/browser/workspace.spec.ts` | 28 | `original` |
| `tests/browser/workspace.spec.ts` | 30 | `draft` |
| `tests/browser/workspace.spec.ts` | 32 | `limit` |
| `tests/browser/workspace.spec.ts` | 44 | `after` |
| `tests/browser/workspace.spec.ts` | 46 | `key` |
| `tests/browser/workspace.spec.ts` | 55 | `pending` |
| `tests/browser/workspace.spec.ts` | 59 | `file` |
| `tests/browser/workspace.spec.ts` | 60 | `saved` |
| `tests/browser/workspace.spec.ts` | 69 | `policy` |
| `tests/browser/workspace.spec.ts` | 81 | `{ page, }` |
| `tests/browser/workspace.spec.ts` | 94 | `route` |
| `tests/browser/workspace.spec.ts` | 95 | `response` |
| `tests/browser/workspace.spec.ts` | 116 | `workspace` |
| `tests/browser/workspace.spec.ts` | 120 | `p` |
| `tests/browser/workspace.spec.ts` | 125 | `download` |
| `tests/browser/workspace.spec.ts` | 127 | `report` |
| `tests/browser/workspace.spec.ts` | 146 | `{ page, }` |
| `tests/browser/workspace.spec.ts` | 185 | `workspace` |
| `tests/browser/workspace.spec.ts` | 187 | `d` |
| `tests/browser/workspace.spec.ts` | 191 | `a` |
| `tests/browser/workspace.spec.ts` | 195 | `{ page, }` |
| `tests/browser/workspace.spec.ts` | 201 | `policy` |
| `tests/browser/workspace.spec.ts` | 209 | `component` |
| `tests/browser/workspace.spec.ts` | 224 | `identity` |
| `tests/browser/workspace.spec.ts` | 225 | `state` |
| `tests/browser/workspace.spec.ts` | 226 | `changed` |
| `tests/browser/workspace.spec.ts` | 239 | `{ page, }` |
| `tests/browser/workspace.spec.ts` | 274 | `release` |
| `tests/browser/workspace.spec.ts` | 275 | `received` |
| `tests/browser/workspace.spec.ts` | 276 | `hold` |
| `tests/browser/workspace.spec.ts` | 276 | `resolve` |
| `tests/browser/workspace.spec.ts` | 279 | `responseReady` |
| `tests/browser/workspace.spec.ts` | 279 | `resolve` |
| `tests/browser/workspace.spec.ts` | 284 | `route` |
| `tests/browser/workspace.spec.ts` | 285 | `response` |
| `tools/browser_checks.mjs` | 8 | `project` |
| `tools/browser_checks.mjs` | 9 | `result` |
| `tools/source_index.mjs` | 7 | `collect` |
| `tools/source_index.mjs` | 7 | `root` |
| `tools/source_index.mjs` | 10 | `a` |
| `tools/source_index.mjs` | 10 | `b` |
| `tools/source_index.mjs` | 11 | `entry` |
| `tools/source_index.mjs` | 12 | `name` |
| `tools/source_index.mjs` | 20 | `file` |
| `tools/source_index.mjs` | 23 | `name` |
| `tools/source_index.mjs` | 27 | `source` |
| `tools/source_index.mjs` | 33 | `records` |
| `tools/source_index.mjs` | 35 | `visit` |
| `tools/source_index.mjs` | 35 | `node` |
| `tools/source_index.mjs` | 44 | `name` |
| `tools/source_index.mjs` | 48 | `line` |
| `tools/source_index.mjs` | 59 | `row` |
| `playwright.config.ts` | 5 | `directory` |
| `playwright.config.ts` | 8 | `local` |
| `playwright.config.ts` | 12 | `python` |
