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
| `tools/check_repo.py` | 9 | `main()` |
| `tools/check_repo.py` | 11 | `path` |
| `tools/check_repo.py` | 12 | `relative` |
| `tools/check_repo.py` | 13 | `content` |
| `tools/check_repo.py` | 31 | `ref` |
| `tools/check_repo.py` | 34 | `budget` |
| `tools/check_repo.py` | 34 | `suffix` |
| `tools/check_repo.py` | 35 | `size` |
| `tools/check_repo.py` | 36 | `p` |
| `tools/docs_index.py` | 13 | `ROOT` |
| `tools/docs_index.py` | 14 | `EXCLUDE` |
| `tools/docs_index.py` | 28 | `SPECIAL` |
| `tools/docs_index.py` | 40 | `files()` |
| `tools/docs_index.py` | 42 | `result` |
| `tools/docs_index.py` | 43 | `children` |
| `tools/docs_index.py` | 43 | `directory` |
| `tools/docs_index.py` | 43 | `names` |
| `tools/docs_index.py` | 44 | `child` |
| `tools/docs_index.py` | 45 | `name` |
| `tools/docs_index.py` | 51 | `render()` |
| `tools/docs_index.py` | 53 | `catalog` |
| `tools/docs_index.py` | 61 | `source` |
| `tools/docs_index.py` | 70 | `path` |
| `tools/docs_index.py` | 71 | `relative` |
| `tools/docs_index.py` | 72 | `content` |
| `tools/docs_index.py` | 73 | `description` |
| `tools/docs_index.py` | 76 | `line` |
| `tools/docs_index.py` | 84 | `records` |
| `tools/docs_index.py` | 86 | `node` |
| `tools/docs_index.py` | 88 | `args` |
| `tools/docs_index.py` | 91 | `a` |
| `tools/docs_index.py` | 99 | `line` |
| `tools/docs_index.py` | 99 | `value` |
| `tools/docs_index.py` | 102 | `line` |
| `tools/docs_index.py` | 102 | `name` |
| `tools/docs_index.py` | 103 | `node` |
| `tools/docs_index.py` | 117 | `main()` |
| `tools/docs_index.py` | 119 | `content` |
| `tools/docs_index.py` | 119 | `relative` |
| `tools/docs_index.py` | 120 | `path` |
| `workbench/__main__.py` | 14 | `main()` |
| `workbench/__main__.py` | 16 | `parser` |
| `workbench/__main__.py` | 18 | `commands` |
| `workbench/__main__.py` | 19 | `init` |
| `workbench/__main__.py` | 21 | `user` |
| `workbench/__main__.py` | 26 | `serve` |
| `workbench/__main__.py` | 28 | `args` |
| `workbench/__main__.py` | 29 | `store` |
| `workbench/__main__.py` | 36 | `password` |
| `workbench/api.py` | 34 | `ROOT` |
| `workbench/api.py` | 35 | `BODY_GATE` |
| `workbench/api.py` | 36 | `HEADERS` |
| `workbench/api.py` | 46 | `create_app(database, port)` |
| `workbench/api.py` | 50 | `authority` |
| `workbench/api.py` | 50 | `origin` |
| `workbench/api.py` | 51 | `app` |
| `workbench/api.py` | 54 | `store` |
| `workbench/api.py` | 57 | `boundary(request, call_next)` |
| `workbench/api.py` | 59 | `acquired` |
| `workbench/api.py` | 79 | `acquired` |
| `workbench/api.py` | 80 | `data` |
| `workbench/api.py` | 82 | `chunk` |
| `workbench/api.py` | 87 | `response` |
| `workbench/api.py` | 89 | `response` |
| `workbench/api.py` | 91 | `response` |
| `workbench/api.py` | 99 | `invalid(_request, error)` |
| `workbench/api.py` | 104 | `e` |
| `workbench/api.py` | 110 | `conflict(_request, _error)` |
| `workbench/api.py` | 117 | `health()` |
| `workbench/api.py` | 122 | `login(body, request)` |
| `workbench/api.py` | 124 | `token` |
| `workbench/api.py` | 124 | `user` |
| `workbench/api.py` | 125 | `response` |
| `workbench/api.py` | 132 | `me(request)` |
| `workbench/api.py` | 137 | `logout(request)` |
| `workbench/api.py` | 140 | `response` |
| `workbench/api.py` | 145 | `workspace(request)` |
| `workbench/api.py` | 151 | `aircraft(body, request)` |
| `workbench/api.py` | 157 | `component(body, request)` |
| `workbench/api.py` | 163 | `publish(body, request)` |
| `workbench/api.py` | 169 | `swap(body, request)` |
| `workbench/api.py` | 175 | `usage(body, request)` |
| `workbench/api.py` | 177 | `result` |
| `workbench/api.py` | 181 | `inspect(body, request)` |
| `workbench/api.py` | 187 | `defect(body, request)` |
| `workbench/api.py` | 193 | `work(body, request)` |
| `workbench/api.py` | 199 | `verify(body, request)` |
| `workbench/api.py` | 205 | `retire(body, request)` |
| `workbench/api.py` | 211 | `assess(body, request)` |
| `workbench/api.py` | 213 | `identifier` |
| `workbench/api.py` | 217 | `report(identifier, request)` |
| `workbench/api.py` | 223 | `review(identifier, body, request)` |
| `workbench/api.py` | 229 | `export(identifier, request)` |
| `workbench/api.py` | 238 | `evidence(request)` |
| `workbench/api.py` | 247 | `index()` |
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
| `workbench/models.py` | 203 | `Review(class)` |
| `workbench/models.py` | 206 | `note` |
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
| `workbench/store.py` | 19 | `QUERIES` |
| `workbench/store.py` | 29 | `CAPACITY` |
| `workbench/store.py` | 41 | `canonical(value)` |
| `workbench/store.py` | 46 | `digest(value)` |
| `workbench/store.py` | 51 | `Store(class)` |
| `workbench/store.py` | 54 | `__init__(self, path)` |
| `workbench/store.py` | 58 | `db` |
| `workbench/store.py` | 62 | `connect(self, write)` |
| `workbench/store.py` | 64 | `db` |
| `workbench/store.py` | 76 | `state(self, db)` |
| `workbench/store.py` | 78 | `workspace` |
| `workbench/store.py` | 81 | `result` |
| `workbench/store.py` | 82 | `query` |
| `workbench/store.py` | 82 | `table` |
| `workbench/store.py` | 83 | `rows` |
| `workbench/store.py` | 84 | `record` |
| `workbench/store.py` | 85 | `value` |
| `workbench/store.py` | 87 | `content` |
| `workbench/store.py` | 92 | `value` |
| `workbench/store.py` | 99 | `verify(self, db, state)` |
| `workbench/store.py` | 101 | `generation` |
| `workbench/store.py` | 101 | `previous` |
| `workbench/store.py` | 102 | `last` |
| `workbench/store.py` | 103 | `row` |
| `workbench/store.py` | 104 | `value` |
| `workbench/store.py` | 105 | `checksum` |
| `workbench/store.py` | 112 | `generation` |
| `workbench/store.py` | 112 | `last` |
| `workbench/store.py` | 112 | `previous` |
| `workbench/store.py` | 121 | `seal(self, db, actor, event, detail)` |
| `workbench/store.py` | 123 | `state` |
| `workbench/store.py` | 124 | `row` |
| `workbench/store.py` | 125 | `value` |
| `workbench/store.py` | 136 | `initialize(self, examples)` |
| `workbench/store.py` | 138 | `db` |
| `workbench/store.py` | 144 | `records` |
| `workbench/store.py` | 145 | `table` |
| `workbench/store.py` | 146 | `value` |
| `workbench/store.py` | 148 | `item` |
| `workbench/store.py` | 152 | `item` |
| `workbench/store.py` | 156 | `item` |
| `workbench/store.py` | 162 | `insert_asset(self, db, table, value)` |
| `workbench/store.py` | 166 | `content` |
| `workbench/store.py` | 166 | `k` |
| `workbench/store.py` | 166 | `v` |
| `workbench/store.py` | 167 | `values` |
| `workbench/store.py` | 181 | `snapshot(self)` |
| `workbench/store.py` | 183 | `db` |
| `workbench/store.py` | 185 | `state` |
| `workbench/store.py` | 186 | `tip` |
| `workbench/store.py` | 190 | `change(self, expected, user, event, roles, detail)` |
| `workbench/store.py` | 194 | `db` |
| `workbench/store.py` | 195 | `state` |
| `workbench/store.py` | 207 | `entity(self, state, table, identifier)` |
| `workbench/store.py` | 209 | `item` |
| `workbench/store.py` | 209 | `result` |
| `workbench/store.py` | 214 | `create(self, body, user, table)` |
| `workbench/store.py` | 216 | `value` |
| `workbench/store.py` | 218 | `db` |
| `workbench/store.py` | 219 | `state` |
| `workbench/store.py` | 220 | `_` |
| `workbench/store.py` | 225 | `p` |
| `workbench/store.py` | 230 | `publish(self, body, user)` |
| `workbench/store.py` | 233 | `db` |
| `workbench/store.py` | 234 | `state` |
| `workbench/store.py` | 235 | `_` |
| `workbench/store.py` | 237 | `version` |
| `workbench/store.py` | 243 | `swap(self, body, user)` |
| `workbench/store.py` | 247 | `db` |
| `workbench/store.py` | 247 | `generation` |
| `workbench/store.py` | 247 | `state` |
| `workbench/store.py` | 248 | `aircraft` |
| `workbench/store.py` | 249 | `profile` |
| `workbench/store.py` | 250 | `p` |
| `workbench/store.py` | 252 | `s` |
| `workbench/store.py` | 252 | `slot` |
| `workbench/store.py` | 256 | `part` |
| `workbench/store.py` | 261 | `i` |
| `workbench/store.py` | 274 | `usage(self, body, user)` |
| `workbench/store.py` | 279 | `request_digest` |
| `workbench/store.py` | 280 | `db` |
| `workbench/store.py` | 281 | `state` |
| `workbench/store.py` | 283 | `previous` |
| `workbench/store.py` | 296 | `aircraft` |
| `workbench/store.py` | 297 | `parts` |
| `workbench/store.py` | 299 | `i` |
| `workbench/store.py` | 302 | `key` |
| `workbench/store.py` | 302 | `value` |
| `workbench/store.py` | 312 | `identifier` |
| `workbench/store.py` | 317 | `generation` |
| `workbench/store.py` | 319 | `cursor` |
| `workbench/store.py` | 337 | `inspect(self, body, user)` |
| `workbench/store.py` | 340 | `db` |
| `workbench/store.py` | 341 | `state` |
| `workbench/store.py` | 342 | `generation` |
| `workbench/store.py` | 344 | `part` |
| `workbench/store.py` | 351 | `now` |
| `workbench/store.py` | 373 | `defect(self, body, user)` |
| `workbench/store.py` | 377 | `_` |
| `workbench/store.py` | 377 | `db` |
| `workbench/store.py` | 377 | `state` |
| `workbench/store.py` | 386 | `complete_work(self, body, user)` |
| `workbench/store.py` | 389 | `db` |
| `workbench/store.py` | 390 | `state` |
| `workbench/store.py` | 391 | `generation` |
| `workbench/store.py` | 393 | `defect` |
| `workbench/store.py` | 394 | `w` |
| `workbench/store.py` | 401 | `verify_work(self, body, user)` |
| `workbench/store.py` | 405 | `db` |
| `workbench/store.py` | 405 | `generation` |
| `workbench/store.py` | 405 | `state` |
| `workbench/store.py` | 406 | `work` |
| `workbench/store.py` | 409 | `defect` |
| `workbench/store.py` | 410 | `part` |
| `workbench/store.py` | 411 | `_` |
| `workbench/store.py` | 411 | `inspections` |
| `workbench/store.py` | 412 | `inspection` |
| `workbench/store.py` | 421 | `policy` |
| `workbench/store.py` | 422 | `limit` |
| `workbench/store.py` | 422 | `p` |
| `workbench/store.py` | 425 | `result` |
| `workbench/store.py` | 445 | `retire(self, body, user)` |
| `workbench/store.py` | 449 | `_` |
| `workbench/store.py` | 449 | `db` |
| `workbench/store.py` | 449 | `state` |
| `workbench/store.py` | 450 | `part` |
| `workbench/store.py` | 453 | `i` |
| `workbench/store.py` | 458 | `assess(self, body, user)` |
| `workbench/store.py` | 460 | `db` |
| `workbench/store.py` | 461 | `state` |
| `workbench/store.py` | 462 | `tip` |
| `workbench/store.py` | 469 | `now` |
| `workbench/store.py` | 470 | `content` |
| `workbench/store.py` | 477 | `cursor` |
| `workbench/store.py` | 483 | `report(self, identifier, db)` |
| `workbench/store.py` | 486 | `connection` |
| `workbench/store.py` | 489 | `state` |
| `workbench/store.py` | 491 | `row` |
| `workbench/store.py` | 494 | `content` |
| `workbench/store.py` | 502 | `review` |
| `workbench/store.py` | 505 | `record` |
| `workbench/store.py` | 507 | `checksum` |
| `workbench/store.py` | 510 | `now` |
| `workbench/store.py` | 522 | `review(self, identifier, body, user)` |
| `workbench/store.py` | 526 | `db` |
| `workbench/store.py` | 527 | `report` |
| `workbench/store.py` | 532 | `record` |
| `workbench/store.py` | 540 | `dashboard(self)` |
| `workbench/store.py` | 542 | `db` |
| `workbench/store.py` | 544 | `state` |
| `workbench/store.py` | 545 | `tip` |
| `workbench/store.py` | 554 | `r` |
| `workbench/store.py` | 560 | `r` |
| `workbench/store.py` | 566 | `evidence(self)` |
| `workbench/store.py` | 568 | `db` |
| `workbench/store.py` | 570 | `state` |
| `workbench/store.py` | 571 | `tip` |
| `workbench/store.py` | 578 | `row` |
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
| `ui/src/main.ts` | 115 | `el` |
| `ui/src/main.ts` | 115 | `id` |
| `ui/src/main.ts` | 119 | `value` |
| `ui/src/main.ts` | 119 | `id` |
| `ui/src/main.ts` | 123 | `text` |
| `ui/src/main.ts` | 123 | `id` |
| `ui/src/main.ts` | 123 | `content` |
| `ui/src/main.ts` | 127 | `buttons` |
| `ui/src/main.ts` | 128 | `button` |
| `ui/src/main.ts` | 129 | `roles` |
| `ui/src/main.ts` | 137 | `api` |
| `ui/src/main.ts` | 137 | `path` |
| `ui/src/main.ts` | 137 | `body` |
| `ui/src/main.ts` | 138 | `generation` |
| `ui/src/main.ts` | 139 | `response` |
| `ui/src/main.ts` | 150 | `result` |
| `ui/src/main.ts` | 161 | `task` |
| `ui/src/main.ts` | 161 | `action` |
| `ui/src/main.ts` | 163 | `generation` |
| `ui/src/main.ts` | 171 | `error` |
| `ui/src/main.ts` | 179 | `reset` |
| `ui/src/main.ts` | 185 | `id` |
| `ui/src/main.ts` | 187 | `id` |
| `ui/src/main.ts` | 203 | `area` |
| `ui/src/main.ts` | 205 | `id` |
| `ui/src/main.ts` | 222 | `options` |
| `ui/src/main.ts` | 223 | `id` |
| `ui/src/main.ts` | 224 | `entries` |
| `ui/src/main.ts` | 225 | `selection` |
| `ui/src/main.ts` | 227 | `select` |
| `ui/src/main.ts` | 228 | `previous` |
| `ui/src/main.ts` | 230 | `[key, label]` |
| `ui/src/main.ts` | 231 | `option` |
| `ui/src/main.ts` | 236 | `[key]` |
| `ui/src/main.ts` | 239 | `findings` |
| `ui/src/main.ts` | 239 | `id` |
| `ui/src/main.ts` | 239 | `entries` |
| `ui/src/main.ts` | 240 | `root` |
| `ui/src/main.ts` | 242 | `finding` |
| `ui/src/main.ts` | 243 | `item` |
| `ui/src/main.ts` | 250 | `render` |
| `ui/src/main.ts` | 250 | `next` |
| `ui/src/main.ts` | 252 | `state` |
| `ui/src/main.ts` | 253 | `asset` |
| `ui/src/main.ts` | 255 | `part` |
| `ui/src/main.ts` | 257 | `metrics` |
| `ui/src/main.ts` | 259 | `status` |
| `ui/src/main.ts` | 265 | `div` |
| `ui/src/main.ts` | 267 | `count` |
| `ui/src/main.ts` | 269 | `asset` |
| `ui/src/main.ts` | 271 | `label` |
| `ui/src/main.ts` | 276 | `policy` |
| `ui/src/main.ts` | 277 | `record` |
| `ui/src/main.ts` | 322 | `part` |
| `ui/src/main.ts` | 327 | `part` |
| `ui/src/main.ts` | 336 | `d` |
| `ui/src/main.ts` | 336 | `work` |
| `ui/src/main.ts` | 338 | `d` |
| `ui/src/main.ts` | 346 | `work` |
| `ui/src/main.ts` | 347 | `work` |
| `ui/src/main.ts` | 356 | `record` |
| `ui/src/main.ts` | 365 | `defects` |
| `ui/src/main.ts` | 367 | `defect` |
| `ui/src/main.ts` | 367 | `entry` |
| `ui/src/main.ts` | 368 | `p` |
| `ui/src/main.ts` | 387 | `roster` |
| `ui/src/main.ts` | 388 | `root` |
| `ui/src/main.ts` | 391 | `asset` |
| `ui/src/main.ts` | 392 | `result` |
| `ui/src/main.ts` | 393 | `item` |
| `ui/src/main.ts` | 400 | `button` |
| `ui/src/main.ts` | 413 | `aircraftDesk` |
| `ui/src/main.ts` | 415 | `asset` |
| `ui/src/main.ts` | 416 | `item` |
| `ui/src/main.ts` | 418 | `result` |
| `ui/src/main.ts` | 419 | `item` |
| `ui/src/main.ts` | 436 | `policy` |
| `ui/src/main.ts` | 437 | `record` |
| `ui/src/main.ts` | 439 | `profile` |
| `ui/src/main.ts` | 439 | `entry` |
| `ui/src/main.ts` | 442 | `slot` |
| `ui/src/main.ts` | 448 | `slot` |
| `ui/src/main.ts` | 449 | `row` |
| `ui/src/main.ts` | 450 | `part` |
| `ui/src/main.ts` | 451 | `entry` |
| `ui/src/main.ts` | 453 | `status` |
| `ui/src/main.ts` | 454 | `entry` |
| `ui/src/main.ts` | 456 | `content` |
| `ui/src/main.ts` | 464 | `cell` |
| `ui/src/main.ts` | 473 | `componentDesk` |
| `ui/src/main.ts` | 475 | `part` |
| `ui/src/main.ts` | 476 | `entry` |
| `ui/src/main.ts` | 478 | `result` |
| `ui/src/main.ts` | 479 | `entry` |
| `ui/src/main.ts` | 491 | `cumulative` |
| `ui/src/main.ts` | 492 | `values` |
| `ui/src/main.ts` | 493 | `record` |
| `ui/src/main.ts` | 498 | `chart` |
| `ui/src/main.ts` | 500 | `line` |
| `ui/src/main.ts` | 511 | `refresh` |
| `ui/src/main.ts` | 517 | `mutate` |
| `ui/src/main.ts` | 518 | `path` |
| `ui/src/main.ts` | 519 | `fields` |
| `ui/src/main.ts` | 530 | `showReport` |
| `ui/src/main.ts` | 530 | `report` |
| `ui/src/main.ts` | 546 | `event` |
| `ui/src/main.ts` | 562 | `csrf` |
| `ui/src/main.ts` | 572 | `response` |
| `ui/src/main.ts` | 598 | `sendUsage` |
| `ui/src/main.ts` | 601 | `next` |
| `ui/src/main.ts` | 611 | `error` |
| `ui/src/main.ts` | 618 | `event` |
| `ui/src/main.ts` | 638 | `event` |
| `ui/src/main.ts` | 642 | `report` |
| `ui/src/main.ts` | 655 | `id` |
| `ui/src/main.ts` | 658 | `event` |
| `ui/src/main.ts` | 669 | `event` |
| `ui/src/main.ts` | 680 | `event` |
| `ui/src/main.ts` | 683 | `battery` |
| `ui/src/main.ts` | 684 | `part` |
| `ui/src/main.ts` | 699 | `event` |
| `ui/src/main.ts` | 709 | `event` |
| `ui/src/main.ts` | 718 | `event` |
| `ui/src/main.ts` | 736 | `event` |
| `ui/src/main.ts` | 742 | `event` |
| `ui/src/main.ts` | 748 | `event` |
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
| `tests/browser/workspace.spec.ts` | 22 | `{ page, }` |
| `tests/browser/workspace.spec.ts` | 35 | `route` |
| `tests/browser/workspace.spec.ts` | 36 | `response` |
| `tests/browser/workspace.spec.ts` | 57 | `workspace` |
| `tests/browser/workspace.spec.ts` | 61 | `p` |
| `tests/browser/workspace.spec.ts` | 66 | `download` |
| `tests/browser/workspace.spec.ts` | 68 | `report` |
| `tests/browser/workspace.spec.ts` | 87 | `{ page, }` |
| `tests/browser/workspace.spec.ts` | 126 | `workspace` |
| `tests/browser/workspace.spec.ts` | 128 | `d` |
| `tests/browser/workspace.spec.ts` | 132 | `a` |
| `tests/browser/workspace.spec.ts` | 136 | `{ page, }` |
| `tests/browser/workspace.spec.ts` | 142 | `policy` |
| `tests/browser/workspace.spec.ts` | 150 | `component` |
| `tests/browser/workspace.spec.ts` | 165 | `identity` |
| `tests/browser/workspace.spec.ts` | 166 | `state` |
| `tests/browser/workspace.spec.ts` | 167 | `changed` |
| `tests/browser/workspace.spec.ts` | 180 | `{ page, }` |
| `tests/browser/workspace.spec.ts` | 205 | `release` |
| `tests/browser/workspace.spec.ts` | 206 | `received` |
| `tests/browser/workspace.spec.ts` | 207 | `hold` |
| `tests/browser/workspace.spec.ts` | 207 | `resolve` |
| `tests/browser/workspace.spec.ts` | 210 | `responseReady` |
| `tests/browser/workspace.spec.ts` | 210 | `resolve` |
| `tests/browser/workspace.spec.ts` | 215 | `route` |
| `tests/browser/workspace.spec.ts` | 216 | `response` |
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
