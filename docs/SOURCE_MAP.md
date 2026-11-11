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
| `tests/runtime_notice_cases.py` | 10 | `ROOT` |
| `tests/runtime_notice_cases.py` | 14 | `interpreter()` |
| `tests/runtime_notice_cases.py` | 16 | `root` |
| `tests/runtime_notice_cases.py` | 24 | `test_actual_tcl_notice_reader_preserves_bytes_and_missing_identity(tmp_path, interpreter)` |
| `tests/runtime_notice_cases.py` | 26 | `path` |
| `tests/runtime_notice_cases.py` | 27 | `raw` |
| `tests/runtime_notice_cases.py` | 34 | `raw` |
| `tests/runtime_notice_cases.py` | 42 | `test_exact_mac_version_uses_verbatim_upstream_notice_and_binds_digest(tmp_path, kind, interpreter)` |
| `tests/runtime_notice_cases.py` | 46 | `library` |
| `tests/runtime_notice_cases.py` | 47 | `file` |
| `tests/runtime_notice_cases.py` | 48 | `target` |
| `tests/runtime_notice_cases.py` | 51 | `raw` |
| `tests/runtime_notice_cases.py` | 51 | `source` |
| `tests/runtime_notice_cases.py` | 78 | `test_unreviewed_platform_version_or_library_cannot_substitute_notice(version, library, system, interpreter)` |
| `tests/runtime_notice_cases.py` | 87 | `test_ubuntu_uses_actual_runtime_package_copyright_not_guessed_script_file(tmp_path, monkeypatch, kind, interpreter)` |
| `tests/runtime_notice_cases.py` | 91 | `fixture` |
| `tests/runtime_notice_cases.py` | 93 | `actual` |
| `tests/runtime_notice_cases.py` | 94 | `calls` |
| `tests/runtime_notice_cases.py` | 95 | `library` |
| `tests/runtime_notice_cases.py` | 96 | `package_path` |
| `tests/runtime_notice_cases.py` | 98 | `installed(interpreter, path)` |
| `tests/runtime_notice_cases.py` | 105 | `raw` |
| `tests/runtime_notice_cases.py` | 105 | `source` |
| `tests/runtime_notice_cases.py` | 110 | `test_present_invalid_runtime_notice_never_falls_back_to_other_terms(tmp_path, interpreter)` |
| `tests/runtime_notice_cases.py` | 118 | `test_mac_pre905_terms_require_exact_psf_sdk_recipe(tmp_path, monkeypatch, interpreter, python_version, accepted)` |
| `tests/runtime_notice_cases.py` | 123 | `library` |
| `tests/runtime_notice_cases.py` | 124 | `name` |
| `tests/runtime_notice_cases.py` | 128 | `raw` |
| `tests/runtime_notice_cases.py` | 128 | `source` |
| `tests/runtime_notice_cases.py` | 136 | `test_mac_pre905_changed_notice_is_rejected(tmp_path, monkeypatch, interpreter)` |
| `tests/runtime_notice_cases.py` | 140 | `path` |
| `tests/runtime_notice_cases.py` | 142 | `library` |
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
| `tests/test_desktop_host.py` | 15 | `prepared(tmp_path)` |
| `tests/test_desktop_host.py` | 17 | `profile` |
| `tests/test_desktop_host.py` | 24 | `request(host, path)` |
| `tests/test_desktop_host.py` | 26 | `connection` |
| `tests/test_desktop_host.py` | 31 | `response` |
| `tests/test_desktop_host.py` | 37 | `test_actual_readiness_private_login_and_owned_stop(tmp_path)` |
| `tests/test_desktop_host.py` | 39 | `profile` |
| `tests/test_desktop_host.py` | 40 | `metadata` |
| `tests/test_desktop_host.py` | 41 | `host` |
| `tests/test_desktop_host.py` | 44 | `_` |
| `tests/test_desktop_host.py` | 44 | `code` |
| `tests/test_desktop_host.py` | 44 | `raw` |
| `tests/test_desktop_host.py` | 45 | `health` |
| `tests/test_desktop_host.py` | 50 | `login` |
| `tests/test_desktop_host.py` | 61 | `code` |
| `tests/test_desktop_host.py` | 61 | `headers` |
| `tests/test_desktop_host.py` | 61 | `raw` |
| `tests/test_desktop_host.py` | 69 | `cookie` |
| `tests/test_desktop_host.py` | 89 | `test_actual_partial_body_bounds_pre_shutdown_drain(tmp_path)` |
| `tests/test_desktop_host.py` | 91 | `profile` |
| `tests/test_desktop_host.py` | 92 | `host` |
| `tests/test_desktop_host.py` | 93 | `received` |
| `tests/test_desktop_host.py` | 95 | `ObserveRead(class)` |
| `tests/test_desktop_host.py` | 98 | `__init__(self, app)` |
| `tests/test_desktop_host.py` | 101 | `__call__(self, scope, receive, send)` |
| `tests/test_desktop_host.py` | 102 | `observed()` |
| `tests/test_desktop_host.py` | 103 | `message` |
| `tests/test_desktop_host.py` | 113 | `connection` |
| `tests/test_desktop_host.py` | 124 | `response` |
| `tests/test_desktop_host.py` | 140 | `test_startup_failure_is_never_reported_as_ready(tmp_path, monkeypatch, failure)` |
| `tests/test_desktop_host.py` | 142 | `profile` |
| `tests/test_desktop_host.py` | 143 | `host` |
| `tests/test_desktop_host.py` | 145 | `broken()` |
| `tests/test_desktop_host.py` | 163 | `test_two_actual_profiles_keep_sessions_in_one_host_scoped_cookie_jar(tmp_path)` |
| `tests/test_desktop_host.py` | 165 | `first` |
| `tests/test_desktop_host.py` | 166 | `second` |
| `tests/test_desktop_host.py` | 167 | `password` |
| `tests/test_desktop_host.py` | 171 | `hosts` |
| `tests/test_desktop_host.py` | 173 | `host` |
| `tests/test_desktop_host.py` | 175 | `client` |
| `tests/test_desktop_host.py` | 176 | `host` |
| `tests/test_desktop_host.py` | 176 | `name` |
| `tests/test_desktop_host.py` | 177 | `response` |
| `tests/test_desktop_host.py` | 183 | `cookie` |
| `tests/test_desktop_host.py` | 187 | `host` |
| `tests/test_desktop_host.py` | 187 | `users` |
| `tests/test_desktop_host.py` | 188 | `user` |
| `tests/test_desktop_host.py` | 189 | `foreign_cookie` |
| `tests/test_desktop_host.py` | 196 | `wrong_csrf` |
| `tests/test_desktop_host.py` | 213 | `host` |
| `tests/test_desktop_host.py` | 220 | `test_invalid_cookie_namespace_is_rejected_before_database_creation(tmp_path, invalid)` |
| `tests/test_desktop_host.py` | 224 | `database` |
| `tests/test_desktop_package.py` | 24 | `test_freeze_refuses_old_cached_or_prerelease_runtime(version, level, allowed)` |
| `tests/test_desktop_package.py` | 29 | `test_all_product_version_surfaces_agree()` |
| `tests/test_desktop_package.py` | 40 | `test_mismatched_version_or_identity_cannot_build(tmp_path, surface)` |
| `tests/test_desktop_package.py` | 42 | `root` |
| `tests/test_desktop_package.py` | 43 | `path` |
| `tests/test_desktop_package.py` | 44 | `output` |
| `tests/test_desktop_package.py` | 47 | `selected` |
| `tests/test_desktop_package.py` | 55 | `path` |
| `tests/test_desktop_package.py` | 59 | `value` |
| `tests/test_desktop_package.py` | 83 | `test_source_cleanliness_is_not_a_release_flag_waiver(monkeypatch, dirty, ci, override, sha, allowed)` |
| `tests/test_desktop_package.py` | 88 | `output(command)` |
| `tests/test_desktop_package.py` | 105 | `value` |
| `tests/test_desktop_package.py` | 109 | `test_archive_rejection_remains_active_with_optimized_python()` |
| `tests/test_desktop_package.py` | 111 | `result` |
| `tests/test_desktop_profile.py` | 13 | `test_provision_persist_login_and_existing_roles(tmp_path)` |
| `tests/test_desktop_profile.py` | 15 | `path` |
| `tests/test_desktop_profile.py` | 16 | `profile` |
| `tests/test_desktop_profile.py` | 24 | `original` |
| `tests/test_desktop_profile.py` | 25 | `namespace` |
| `tests/test_desktop_profile.py` | 26 | `marker_bytes` |
| `tests/test_desktop_profile.py` | 33 | `reopened` |
| `tests/test_desktop_profile.py` | 40 | `client` |
| `tests/test_desktop_profile.py` | 42 | `response` |
| `tests/test_desktop_profile.py` | 48 | `db` |
| `tests/test_desktop_profile.py` | 49 | `row` |
| `tests/test_desktop_profile.py` | 49 | `values` |
| `tests/test_desktop_profile.py` | 50 | `value` |
| `tests/test_desktop_profile.py` | 55 | `test_invalid_duplicate_and_first_role_do_not_create_account(tmp_path)` |
| `tests/test_desktop_profile.py` | 57 | `profile` |
| `tests/test_desktop_profile.py` | 59 | `args` |
| `tests/test_desktop_profile.py` | 68 | `db` |
| `tests/test_desktop_profile.py` | 69 | `original_hash` |
| `tests/test_desktop_profile.py` | 77 | `db` |
| `tests/test_desktop_profile.py` | 98 | `test_invalid_marker_never_adopts_unknown_profile(tmp_path, content)` |
| `tests/test_desktop_profile.py` | 100 | `folder` |
| `tests/test_desktop_profile.py` | 108 | `test_unknown_folder_and_wrong_product_are_preserved(tmp_path)` |
| `tests/test_desktop_profile.py` | 110 | `important` |
| `tests/test_desktop_profile.py` | 119 | `marker` |
| `tests/test_desktop_profile.py` | 127 | `test_default_directory_is_per_user_and_outside_source(monkeypatch, tmp_path)` |
| `tests/test_desktop_resources.py` | 13 | `test_source_mode_is_explicit_and_frozen_missing_identity_fails(tmp_path, monkeypatch)` |
| `tests/test_desktop_resources.py` | 36 | `test_each_wrong_frozen_identity_surface_is_rejected(tmp_path, field, value)` |
| `tests/test_desktop_resources.py` | 38 | `path` |
| `tests/test_desktop_resources.py` | 40 | `valid` |
| `tests/test_desktop_resources.py` | 55 | `test_resources_are_real_regular_nonempty_bounded_files(tmp_path)` |
| `tests/test_desktop_resources.py` | 57 | `path` |
| `tests/test_desktop_resources.py` | 60 | `raw` |
| `tests/test_desktop_resources.py` | 68 | `test_console_owner_uses_actual_saved_profile_and_quits_without_password_input(tmp_path, monkeypatch, capsys)` |
| `tests/test_desktop_resources.py` | 74 | `path` |
| `tests/test_desktop_resources.py` | 75 | `profile` |
| `tests/test_desktop_resources.py` | 82 | `output` |
| `tests/test_desktop_resources.py` | 85 | `reopened` |
| `tests/test_desktop_resources.py` | 92 | `test_console_cannot_create_preset_first_account(tmp_path)` |
| `tests/test_desktop_resources.py` | 96 | `path` |
| `tests/test_desktop_resources.py` | 99 | `profile` |
| `tests/test_desktop_resources.py` | 106 | `test_entrypoint_requires_explicit_console_mode_and_real_resources(tmp_path, monkeypatch, capsys)` |
| `tests/test_desktop_resources.py` | 110 | `error` |
| `tests/test_desktop_resources.py` | 121 | `test_normal_entrypoint_presents_native_controls(tmp_path, monkeypatch)` |
| `tests/test_desktop_resources.py` | 125 | `observed` |
| `tests/test_desktop_resources.py` | 127 | `close_after_construct(root, directory, metadata)` |
| `tests/test_desktop_resources.py` | 141 | `test_actual_loaded_tk_matches_package_and_runtime_info_opens_no_profile(tmp_path, monkeypatch, capsys)` |
| `tests/test_desktop_resources.py` | 147 | `root` |
| `tests/test_desktop_resources.py` | 150 | `versions` |
| `tests/test_desktop_resources.py` | 159 | `_` |
| `tests/test_desktop_resources.py` | 162 | `output` |
| `tests/test_desktop_resources.py` | 163 | `record` |
| `tests/test_desktop_resources.py` | 164 | `name` |
| `tests/test_desktop_resources.py` | 168 | `test_console_interrupt_drains_the_actual_owned_host_and_releases_profile(tmp_path, monkeypatch, capsys)` |
| `tests/test_desktop_resources.py` | 174 | `path` |
| `tests/test_desktop_resources.py` | 175 | `profile` |
| `tests/test_desktop_resources.py` | 180 | `actual_host` |
| `tests/test_desktop_resources.py` | 181 | `observed` |
| `tests/test_desktop_resources.py` | 183 | `remember()` |
| `tests/test_desktop_resources.py` | 184 | `host` |
| `tests/test_desktop_resources.py` | 188 | `Interrupted(class)` |
| `tests/test_desktop_resources.py` | 189 | `__iter__(self)` |
| `tests/test_desktop_resources.py` | 200 | `reopened` |
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
| `tests/test_owner_window.py` | 12 | `window(tmp_path)` |
| `tests/test_owner_window.py` | 14 | `root` |
| `tests/test_owner_window.py` | 16 | `view` |
| `tests/test_owner_window.py` | 33 | `credentials(view, name, password, confirmation)` |
| `tests/test_owner_window.py` | 35 | `password` |
| `tests/test_owner_window.py` | 41 | `test_actual_buttons_first_account_staff_and_no_password_retention(window, monkeypatch)` |
| `tests/test_owner_window.py` | 43 | `_` |
| `tests/test_owner_window.py` | 43 | `view` |
| `tests/test_owner_window.py` | 44 | `opened` |
| `tests/test_owner_window.py` | 63 | `original_host` |
| `tests/test_owner_window.py` | 78 | `test_folder_choice_and_unknown_existing_files_are_not_adopted(window, tmp_path, monkeypatch)` |
| `tests/test_owner_window.py` | 80 | `_` |
| `tests/test_owner_window.py` | 80 | `view` |
| `tests/test_owner_window.py` | 81 | `original` |
| `tests/test_owner_window.py` | 85 | `target` |
| `tests/test_owner_window.py` | 87 | `note` |
| `tests/test_owner_window.py` | 96 | `test_cancelled_or_busy_quit_retains_owner_until_actual_completion(window, monkeypatch)` |
| `tests/test_owner_window.py` | 98 | `root` |
| `tests/test_owner_window.py` | 98 | `view` |
| `tests/test_owner_window.py` | 107 | `busy()` |
| `tests/test_owner_window.py` | 110 | `change` |
| `tests/test_owner_window.py` | 120 | `test_identified_profile_automatically_reopens_without_reset(tmp_path, monkeypatch)` |
| `tests/test_owner_window.py` | 122 | `path` |
| `tests/test_owner_window.py` | 123 | `profile` |
| `tests/test_owner_window.py` | 127 | `before` |
| `tests/test_owner_window.py` | 129 | `opened` |
| `tests/test_owner_window.py` | 131 | `root` |
| `tests/test_owner_window.py` | 133 | `view` |
| `tests/test_owner_window.py` | 149 | `test_quit_after_real_startup_failure_releases_owner_and_retains_failure_exit(tmp_path, monkeypatch)` |
| `tests/test_owner_window.py` | 153 | `path` |
| `tests/test_owner_window.py` | 154 | `profile` |
| `tests/test_owner_window.py` | 159 | `actual_host` |
| `tests/test_owner_window.py` | 161 | `failed_host()` |
| `tests/test_owner_window.py` | 162 | `host` |
| `tests/test_owner_window.py` | 164 | `fail()` |
| `tests/test_owner_window.py` | 172 | `root` |
| `tests/test_owner_window.py` | 174 | `view` |
| `tests/test_owner_window.py` | 181 | `test_minimum_window_keeps_lifecycle_controls_visible_and_long_status_scrollable(window)` |
| `tests/test_owner_window.py` | 183 | `root` |
| `tests/test_owner_window.py` | 183 | `view` |
| `tests/test_owner_window.py` | 188 | `control` |
| `tests/test_owner_window.py` | 189 | `top` |
| `tests/test_portable_archive.py` | 17 | `APPLICATION` |
| `tests/test_portable_archive.py` | 21 | `test_roundtrip_keeps_one_application_root_and_metadata(tmp_path, suffix)` |
| `tests/test_portable_archive.py` | 23 | `bundle` |
| `tests/test_portable_archive.py` | 27 | `destination` |
| `tests/test_portable_archive.py` | 30 | `extracted` |
| `tests/test_portable_archive.py` | 38 | `test_posix_archive_keeps_relative_link_and_executable_mode(tmp_path)` |
| `tests/test_portable_archive.py` | 40 | `path` |
| `tests/test_portable_archive.py` | 41 | `output` |
| `tests/test_portable_archive.py` | 42 | `member` |
| `tests/test_portable_archive.py` | 45 | `link` |
| `tests/test_portable_archive.py` | 48 | `bundle` |
| `tests/test_portable_archive.py` | 68 | `test_member_escape_or_alias_is_rejected_before_writes(tmp_path, name)` |
| `tests/test_portable_archive.py` | 70 | `target` |
| `tests/test_portable_archive.py` | 71 | `output` |
| `tests/test_portable_archive.py` | 73 | `sentinel` |
| `tests/test_portable_archive.py` | 81 | `test_tar_link_escape_rejected_without_creating_links(tmp_path, target)` |
| `tests/test_portable_archive.py` | 83 | `path` |
| `tests/test_portable_archive.py` | 84 | `output` |
| `tests/test_portable_archive.py` | 85 | `member` |
| `tests/test_portable_archive.py` | 93 | `test_zip_symlink_and_duplicate_members_are_rejected(tmp_path)` |
| `tests/test_portable_archive.py` | 95 | `path` |
| `tests/test_portable_archive.py` | 96 | `output` |
| `tests/test_portable_archive.py` | 97 | `member` |
| `tests/test_portable_archive.py` | 102 | `path` |
| `tests/test_portable_archive.py` | 103 | `output` |
| `tests/test_portable_archive.py` | 104 | `_` |
| `tests/test_portable_archive.py` | 105 | `member` |
| `tests/test_portable_archive.py` | 111 | `test_member_content_and_metadata_budgets_are_checked(tmp_path, monkeypatch)` |
| `tests/test_portable_archive.py` | 113 | `path` |
| `tests/test_portable_archive.py` | 114 | `output` |
| `tests/test_portable_archive.py` | 120 | `path` |
| `tests/test_portable_archive.py` | 121 | `output` |
| `tests/test_profile_paths.py` | 12 | `files(directory)` |
| `tests/test_profile_paths.py` | 16 | `path` |
| `tests/test_profile_paths.py` | 21 | `junction_or_link(target, alias)` |
| `tests/test_profile_paths.py` | 34 | `test_actual_directory_alias_refused_before_target_or_parent_creation(tmp_path, ancestor)` |
| `tests/test_profile_paths.py` | 36 | `target` |
| `tests/test_profile_paths.py` | 38 | `alias` |
| `tests/test_profile_paths.py` | 40 | `chosen` |
| `tests/test_profile_paths.py` | 47 | `test_frozen_program_trees_refused_before_mkdir(tmp_path, monkeypatch, location)` |
| `tests/test_profile_paths.py` | 49 | `bundle` |
| `tests/test_profile_paths.py` | 50 | `executable` |
| `tests/test_profile_paths.py` | 51 | `internal` |
| `tests/test_profile_paths.py` | 58 | `parent` |
| `tests/test_profile_paths.py` | 63 | `chosen` |
| `tests/test_profile_paths.py` | 64 | `before` |
| `tests/test_profile_paths.py` | 68 | `outside` |
| `tests/test_profile_paths.py` | 83 | `test_real_hardlinked_member_refused_before_any_other_mutation(tmp_path, name)` |
| `tests/test_profile_paths.py` | 85 | `chosen` |
| `tests/test_profile_paths.py` | 86 | `profile` |
| `tests/test_profile_paths.py` | 88 | `destination` |
| `tests/test_profile_paths.py` | 89 | `target` |
| `tests/test_profile_paths.py` | 94 | `before` |
| `tests/test_profile_paths.py` | 100 | `test_bad_directory_kind_and_parent_traversal_are_not_created(tmp_path)` |
| `tests/test_profile_paths.py` | 102 | `ordinary` |
| `tests/test_profile_paths.py` | 111 | `test_read_only_missing_member_never_creates_it(tmp_path)` |
| `tests/test_profile_paths.py` | 113 | `path` |
| `tests/test_profile_paths.py` | 115 | `descriptor` |
| `tests/test_profile_paths.py` | 123 | `test_opened_identity_replacement_is_rejected_and_descriptor_closed(tmp_path, monkeypatch)` |
| `tests/test_profile_paths.py` | 125 | `path` |
| `tests/test_profile_paths.py` | 126 | `replacement` |
| `tests/test_profile_paths.py` | 129 | `original_open` |
| `tests/test_profile_paths.py` | 130 | `observed` |
| `tests/test_profile_paths.py` | 132 | `replace_then_open(candidate, flags, mode)` |
| `tests/test_profile_paths.py` | 134 | `descriptor` |
| `tests/test_profile_paths.py` | 140 | `descriptor` |
| `tests/test_profile_paths.py` | 150 | `test_existing_nonregular_identity_member_is_refused(tmp_path)` |
| `tests/test_profile_paths.py` | 152 | `chosen` |
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
| `tests/test_publication_text.py` | 78 | `test_active_parts_rejected_by_exact_publication_name(tmp_path, member)` |
| `tests/test_publication_text.py` | 80 | `path` |
| `tests/test_publication_text.py` | 81 | `package` |
| `tests/test_runtime_notices.py` | 13 | `test_all_thirteen_actual_notice_contracts_in_one_fresh_owned_interpreter()` |
| `tests/test_runtime_notices.py` | 15 | `root` |
| `tests/test_runtime_notices.py` | 16 | `cases` |
| `tests/test_runtime_notices.py` | 17 | `temporary` |
| `tests/test_runtime_notices.py` | 18 | `result_path` |
| `tests/test_runtime_notices.py` | 19 | `result` |
| `tests/test_runtime_notices.py` | 35 | `records` |
| `tests/test_runtime_notices.py` | 37 | `item` |
| `tests/test_runtime_notices.py` | 38 | `item` |
| `tests/test_runtime_notices.py` | 39 | `receipt` |
| `tests/test_runtime_notices.py` | 41 | `item` |
| `tests/test_runtime_notices.py` | 52 | `target` |
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
| `tools/docs_index.py` | 59 | `files()` |
| `tools/docs_index.py` | 61 | `result` |
| `tools/docs_index.py` | 62 | `children` |
| `tools/docs_index.py` | 62 | `directory` |
| `tools/docs_index.py` | 62 | `names` |
| `tools/docs_index.py` | 63 | `child` |
| `tools/docs_index.py` | 64 | `name` |
| `tools/docs_index.py` | 70 | `render()` |
| `tools/docs_index.py` | 72 | `catalog` |
| `tools/docs_index.py` | 80 | `source` |
| `tools/docs_index.py` | 89 | `path` |
| `tools/docs_index.py` | 90 | `relative` |
| `tools/docs_index.py` | 91 | `content` |
| `tools/docs_index.py` | 92 | `description` |
| `tools/docs_index.py` | 95 | `line` |
| `tools/docs_index.py` | 103 | `records` |
| `tools/docs_index.py` | 105 | `node` |
| `tools/docs_index.py` | 107 | `args` |
| `tools/docs_index.py` | 110 | `a` |
| `tools/docs_index.py` | 118 | `line` |
| `tools/docs_index.py` | 118 | `value` |
| `tools/docs_index.py` | 121 | `line` |
| `tools/docs_index.py` | 121 | `name` |
| `tools/docs_index.py` | 122 | `node` |
| `tools/docs_index.py` | 136 | `main()` |
| `tools/docs_index.py` | 138 | `content` |
| `tools/docs_index.py` | 138 | `relative` |
| `tools/docs_index.py` | 139 | `path` |
| `tools/package_app.py` | 28 | `ROOT` |
| `tools/package_app.py` | 29 | `APPLICATION` |
| `tools/package_app.py` | 30 | `PRODUCT` |
| `tools/package_app.py` | 33 | `build_python_supported(version, releaselevel)` |
| `tools/package_app.py` | 43 | `configuration(root)` |
| `tools/package_app.py` | 45 | `project` |
| `tools/package_app.py` | 46 | `package` |
| `tools/package_app.py` | 47 | `lock` |
| `tools/package_app.py` | 48 | `version` |
| `tools/package_app.py` | 62 | `source_metadata(version)` |
| `tools/package_app.py` | 68 | `command` |
| `tools/package_app.py` | 69 | `source` |
| `tools/package_app.py` | 70 | `changed` |
| `tools/package_app.py` | 92 | `main(argv)` |
| `tools/package_app.py` | 94 | `parser` |
| `tools/package_app.py` | 101 | `args` |
| `tools/package_app.py` | 121 | `version` |
| `tools/package_app.py` | 122 | `notices` |
| `tools/package_app.py` | 122 | `versions` |
| `tools/package_app.py` | 123 | `metadata` |
| `tools/package_app.py` | 125 | `generated` |
| `tools/package_app.py` | 127 | `identity_file` |
| `tools/package_app.py` | 129 | `notice_file` |
| `tools/package_app.py` | 131 | `pyinstaller` |
| `tools/package_app.py` | 132 | `licenses` |
| `tools/package_app.py` | 134 | `path` |
| `tools/package_app.py` | 138 | `build` |
| `tools/package_app.py` | 139 | `command` |
| `tools/package_app.py` | 156 | `destination` |
| `tools/package_app.py` | 156 | `source` |
| `tools/package_app.py` | 165 | `source_path` |
| `tools/package_app.py` | 167 | `source_path` |
| `tools/package_app.py` | 168 | `command` |
| `tools/package_app.py` | 169 | `hidden` |
| `tools/package_app.py` | 174 | `command` |
| `tools/package_app.py` | 175 | `command` |
| `tools/package_app.py` | 176 | `environment` |
| `tools/package_app.py` | 182 | `bundle` |
| `tools/package_app.py` | 184 | `suffix` |
| `tools/package_app.py` | 185 | `name` |
| `tools/package_app.py` | 186 | `output` |
| `tools/package_app.py` | 189 | `archive` |
| `tools/package_app.py` | 189 | `sidecar` |
| `tools/package_app.py` | 193 | `temporary` |
| `tools/package_app.py` | 194 | `extracted` |
| `tools/package_app.py` | 195 | `executable` |
| `tools/package_app.py` | 208 | `stream` |
| `tools/package_app.py` | 209 | `digest` |
| `tools/portable_archive.py` | 17 | `MAX_BYTES` |
| `tools/portable_archive.py` | 18 | `MAX_MEMBERS` |
| `tools/portable_archive.py` | 21 | `require(condition, message)` |
| `tools/portable_archive.py` | 27 | `safe_name(name, application)` |
| `tools/portable_archive.py` | 29 | `parts` |
| `tools/portable_archive.py` | 30 | `raw_parts` |
| `tools/portable_archive.py` | 38 | `part` |
| `tools/portable_archive.py` | 39 | `char` |
| `tools/portable_archive.py` | 44 | `safe_link(name, target, application)` |
| `tools/portable_archive.py` | 51 | `char` |
| `tools/portable_archive.py` | 54 | `resolved` |
| `tools/portable_archive.py` | 60 | `create_archive(bundle, archive)` |
| `tools/portable_archive.py` | 66 | `members` |
| `tools/portable_archive.py` | 68 | `total` |
| `tools/portable_archive.py` | 69 | `path` |
| `tools/portable_archive.py` | 78 | `total` |
| `tools/portable_archive.py` | 82 | `path` |
| `tools/portable_archive.py` | 84 | `target` |
| `tools/portable_archive.py` | 85 | `path` |
| `tools/portable_archive.py` | 88 | `target` |
| `tools/portable_archive.py` | 89 | `path` |
| `tools/portable_archive.py` | 97 | `inspected(archive, application)` |
| `tools/portable_archive.py` | 102 | `members` |
| `tools/portable_archive.py` | 103 | `total` |
| `tools/portable_archive.py` | 104 | `names` |
| `tools/portable_archive.py` | 106 | `source` |
| `tools/portable_archive.py` | 107 | `member` |
| `tools/portable_archive.py` | 111 | `total` |
| `tools/portable_archive.py` | 112 | `kind` |
| `tools/portable_archive.py` | 114 | `source` |
| `tools/portable_archive.py` | 115 | `member` |
| `tools/portable_archive.py` | 124 | `total` |
| `tools/portable_archive.py` | 129 | `kind` |
| `tools/portable_archive.py` | 136 | `member` |
| `tools/portable_archive.py` | 137 | `name` |
| `tools/portable_archive.py` | 143 | `archive_metadata(archive, application)` |
| `tools/portable_archive.py` | 145 | `kind` |
| `tools/portable_archive.py` | 145 | `members` |
| `tools/portable_archive.py` | 146 | `expected` |
| `tools/portable_archive.py` | 147 | `m` |
| `tools/portable_archive.py` | 147 | `selected` |
| `tools/portable_archive.py` | 149 | `member` |
| `tools/portable_archive.py` | 150 | `size` |
| `tools/portable_archive.py` | 155 | `source` |
| `tools/portable_archive.py` | 156 | `value` |
| `tools/portable_archive.py` | 158 | `source` |
| `tools/portable_archive.py` | 159 | `stream` |
| `tools/portable_archive.py` | 161 | `value` |
| `tools/portable_archive.py` | 166 | `extract_archive(archive, destination, application)` |
| `tools/portable_archive.py` | 168 | `kind` |
| `tools/portable_archive.py` | 168 | `members` |
| `tools/portable_archive.py` | 171 | `source` |
| `tools/portable_archive.py` | 172 | `member` |
| `tools/portable_archive.py` | 173 | `target` |
| `tools/portable_archive.py` | 178 | `total` |
| `tools/portable_archive.py` | 179 | `incoming` |
| `tools/portable_archive.py` | 179 | `outgoing` |
| `tools/portable_archive.py` | 180 | `chunk` |
| `tools/portable_archive.py` | 181 | `total` |
| `tools/portable_archive.py` | 186 | `source` |
| `tools/portable_archive.py` | 188 | `bundle` |
| `tools/portable_archive.py` | 190 | `path` |
| `tools/profile_admission_smoke.py` | 10 | `snapshot(root)` |
| `tools/profile_admission_smoke.py` | 14 | `path` |
| `tools/profile_admission_smoke.py` | 19 | `verify(executable, output, environment)` |
| `tools/profile_admission_smoke.py` | 21 | `fixture` |
| `tools/profile_admission_smoke.py` | 23 | `before_program` |
| `tools/profile_admission_smoke.py` | 24 | `selections` |
| `tools/profile_admission_smoke.py` | 28 | `label` |
| `tools/profile_admission_smoke.py` | 29 | `folder` |
| `tools/profile_admission_smoke.py` | 31 | `target` |
| `tools/profile_admission_smoke.py` | 33 | `alias` |
| `tools/profile_admission_smoke.py` | 43 | `results` |
| `tools/profile_admission_smoke.py` | 44 | `label` |
| `tools/profile_admission_smoke.py` | 44 | `selected` |
| `tools/profile_admission_smoke.py` | 45 | `result` |
| `tools/profile_admission_smoke.py` | 64 | `label` |
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
| `tools/publication_text.py` | 51 | `stream` |
| `tools/publication_text.py` | 52 | `payload` |
| `tools/runtime_notices.py` | 10 | `UPSTREAM_904` |
| `tools/runtime_notices.py` | 22 | `read_tcl_notice(interpreter, path)` |
| `tools/runtime_notices.py` | 27 | `channel` |
| `tools/runtime_notices.py` | 29 | `code` |
| `tools/runtime_notices.py` | 34 | `raw` |
| `tools/runtime_notices.py` | 37 | `raw` |
| `tools/runtime_notices.py` | 43 | `gui_notice(interpreter, root, kind, version, library, system)` |
| `tools/runtime_notices.py` | 45 | `system` |
| `tools/runtime_notices.py` | 58 | `path` |
| `tools/runtime_notices.py` | 60 | `framework` |
| `tools/runtime_notices.py` | 63 | `commit` |
| `tools/runtime_notices.py` | 63 | `expected` |
| `tools/runtime_notices.py` | 64 | `stream` |
| `tools/runtime_notices.py` | 65 | `raw` |
| `tools/runtime_notices.py` | 81 | `stream` |
| `tools/runtime_notices.py` | 82 | `raw` |
| `tools/runtime_notices.py` | 96 | `collect(root)` |
| `tools/runtime_notices.py` | 100 | `window` |
| `tools/runtime_notices.py` | 103 | `versions` |
| `tools/runtime_notices.py` | 107 | `value` |
| `tools/runtime_notices.py` | 109 | `blocks` |
| `tools/runtime_notices.py` | 110 | `kind` |
| `tools/runtime_notices.py` | 110 | `library` |
| `tools/runtime_notices.py` | 110 | `version` |
| `tools/runtime_notices.py` | 114 | `provenance` |
| `tools/runtime_notices.py` | 114 | `raw` |
| `tools/runtime_notices.py` | 120 | `names` |
| `tools/runtime_notices.py` | 123 | `name` |
| `tools/runtime_notices.py` | 124 | `info` |
| `tools/runtime_notices.py` | 125 | `files` |
| `tools/runtime_notices.py` | 127 | `path` |
| `tools/runtime_notices.py` | 133 | `path` |
| `tools/runtime_notices.py` | 134 | `stream` |
| `tools/runtime_notices.py` | 135 | `raw` |
| `tools/runtime_notices.py` | 139 | `raw` |
| `tools/runtime_notices.py` | 139 | `title` |
| `tools/smoke_app.py` | 22 | `ROOT` |
| `tools/smoke_app.py` | 26 | `require(condition, message)` |
| `tools/smoke_app.py` | 32 | `request(url, path)` |
| `tools/smoke_app.py` | 34 | `target` |
| `tools/smoke_app.py` | 43 | `connection` |
| `tools/smoke_app.py` | 46 | `response` |
| `tools/smoke_app.py` | 47 | `raw` |
| `tools/smoke_app.py` | 57 | `main(argv)` |
| `tools/smoke_app.py` | 62 | `parser` |
| `tools/smoke_app.py` | 65 | `args` |
| `tools/smoke_app.py` | 66 | `executable` |
| `tools/smoke_app.py` | 67 | `expected` |
| `tools/smoke_app.py` | 75 | `output` |
| `tools/smoke_app.py` | 77 | `node` |
| `tools/smoke_app.py` | 79 | `profile_directory` |
| `tools/smoke_app.py` | 80 | `password` |
| `tools/smoke_app.py` | 81 | `profile` |
| `tools/smoke_app.py` | 82 | `expected_cookie` |
| `tools/smoke_app.py` | 84 | `role` |
| `tools/smoke_app.py` | 88 | `allowed` |
| `tools/smoke_app.py` | 104 | `environment` |
| `tools/smoke_app.py` | 104 | `key` |
| `tools/smoke_app.py` | 104 | `value` |
| `tools/smoke_app.py` | 113 | `diagnostic` |
| `tools/smoke_app.py` | 122 | `lines` |
| `tools/smoke_app.py` | 123 | `line` |
| `tools/smoke_app.py` | 126 | `actual_runtime` |
| `tools/smoke_app.py` | 129 | `key` |
| `tools/smoke_app.py` | 136 | `process` |
| `tools/smoke_app.py` | 146 | `events` |
| `tools/smoke_app.py` | 147 | `log` |
| `tools/smoke_app.py` | 149 | `read_output()` |
| `tools/smoke_app.py` | 152 | `line` |
| `tools/smoke_app.py` | 158 | `reader` |
| `tools/smoke_app.py` | 160 | `actual_exit` |
| `tools/smoke_app.py` | 160 | `forced` |
| `tools/smoke_app.py` | 160 | `passed` |
| `tools/smoke_app.py` | 160 | `url` |
| `tools/smoke_app.py` | 162 | `deadline` |
| `tools/smoke_app.py` | 164 | `remaining` |
| `tools/smoke_app.py` | 166 | `line` |
| `tools/smoke_app.py` | 169 | `ready` |
| `tools/smoke_app.py` | 176 | `url` |
| `tools/smoke_app.py` | 177 | `code` |
| `tools/smoke_app.py` | 177 | `raw` |
| `tools/smoke_app.py` | 223 | `actual_exit` |
| `tools/smoke_app.py` | 229 | `target` |
| `tools/smoke_app.py` | 231 | `connection` |
| `tools/smoke_app.py` | 237 | `reopened` |
| `tools/smoke_app.py` | 246 | `line` |
| `tools/smoke_app.py` | 248 | `passed` |
| `tools/smoke_app.py` | 256 | `forced` |
| `workbench/__init__.py` | 3 | `__version__` |
| `workbench/__main__.py` | 14 | `main()` |
| `workbench/__main__.py` | 16 | `parser` |
| `workbench/__main__.py` | 18 | `commands` |
| `workbench/__main__.py` | 19 | `init` |
| `workbench/__main__.py` | 21 | `user` |
| `workbench/__main__.py` | 26 | `serve` |
| `workbench/__main__.py` | 28 | `args` |
| `workbench/__main__.py` | 29 | `store` |
| `workbench/__main__.py` | 36 | `password` |
| `workbench/api.py` | 37 | `ROOT` |
| `workbench/api.py` | 38 | `BODY_GATE` |
| `workbench/api.py` | 39 | `HEADERS` |
| `workbench/api.py` | 49 | `create_app(database, port)` |
| `workbench/api.py` | 55 | `authority` |
| `workbench/api.py` | 55 | `origin` |
| `workbench/api.py` | 56 | `app` |
| `workbench/api.py` | 59 | `store` |
| `workbench/api.py` | 63 | `boundary(request, call_next)` |
| `workbench/api.py` | 65 | `acquired` |
| `workbench/api.py` | 85 | `acquired` |
| `workbench/api.py` | 86 | `data` |
| `workbench/api.py` | 88 | `chunk` |
| `workbench/api.py` | 93 | `response` |
| `workbench/api.py` | 95 | `response` |
| `workbench/api.py` | 97 | `response` |
| `workbench/api.py` | 105 | `invalid(_request, error)` |
| `workbench/api.py` | 110 | `e` |
| `workbench/api.py` | 116 | `conflict(_request, _error)` |
| `workbench/api.py` | 123 | `health()` |
| `workbench/api.py` | 125 | `result` |
| `workbench/api.py` | 131 | `login(body, request)` |
| `workbench/api.py` | 133 | `token` |
| `workbench/api.py` | 133 | `user` |
| `workbench/api.py` | 134 | `response` |
| `workbench/api.py` | 139 | `me(request)` |
| `workbench/api.py` | 144 | `logout(request)` |
| `workbench/api.py` | 147 | `response` |
| `workbench/api.py` | 152 | `workspace(request)` |
| `workbench/api.py` | 158 | `aircraft(body, request)` |
| `workbench/api.py` | 164 | `component(body, request)` |
| `workbench/api.py` | 170 | `publish(body, request)` |
| `workbench/api.py` | 176 | `preview_policy(body, request)` |
| `workbench/api.py` | 181 | `swap(body, request)` |
| `workbench/api.py` | 187 | `usage(body, request)` |
| `workbench/api.py` | 189 | `result` |
| `workbench/api.py` | 193 | `inspect(body, request)` |
| `workbench/api.py` | 199 | `defect(body, request)` |
| `workbench/api.py` | 205 | `work(body, request)` |
| `workbench/api.py` | 211 | `verify(body, request)` |
| `workbench/api.py` | 217 | `retire(body, request)` |
| `workbench/api.py` | 223 | `assess(body, request)` |
| `workbench/api.py` | 225 | `identifier` |
| `workbench/api.py` | 229 | `report(identifier, request)` |
| `workbench/api.py` | 235 | `review(identifier, body, request)` |
| `workbench/api.py` | 241 | `export(identifier, request)` |
| `workbench/api.py` | 250 | `evidence(request)` |
| `workbench/api.py` | 259 | `index()` |
| `workbench/auth.py` | 17 | `HASHER` |
| `workbench/auth.py` | 18 | `DUMMY` |
| `workbench/auth.py` | 19 | `VERIFY_GATE` |
| `workbench/auth.py` | 22 | `session_cookie_name(request)` |
| `workbench/auth.py` | 27 | `add_user(store, username, password, role)` |
| `workbench/auth.py` | 40 | `hashed` |
| `workbench/auth.py` | 41 | `db` |
| `workbench/auth.py` | 45 | `sign_in(request, username, password)` |
| `workbench/auth.py` | 47 | `store` |
| `workbench/auth.py` | 48 | `now` |
| `workbench/auth.py` | 49 | `client` |
| `workbench/auth.py` | 52 | `db` |
| `workbench/auth.py` | 54 | `row` |
| `workbench/auth.py` | 63 | `user` |
| `workbench/auth.py` | 74 | `csrf` |
| `workbench/auth.py` | 74 | `token` |
| `workbench/auth.py` | 75 | `db` |
| `workbench/auth.py` | 88 | `identity(request)` |
| `workbench/auth.py` | 90 | `token` |
| `workbench/auth.py` | 93 | `db` |
| `workbench/auth.py` | 94 | `row` |
| `workbench/auth.py` | 103 | `authorize(request, role)` |
| `workbench/auth.py` | 105 | `user` |
| `workbench/auth.py` | 115 | `sign_out(request)` |
| `workbench/auth.py` | 118 | `db` |
| `workbench/desktop.py` | 21 | `ROOT` |
| `workbench/desktop.py` | 24 | `read_resource(path)` |
| `workbench/desktop.py` | 26 | `descriptor` |
| `workbench/desktop.py` | 29 | `stream` |
| `workbench/desktop.py` | 30 | `info` |
| `workbench/desktop.py` | 33 | `raw` |
| `workbench/desktop.py` | 39 | `identity(root)` |
| `workbench/desktop.py` | 42 | `value` |
| `workbench/desktop.py` | 61 | `console_session(directory, metadata)` |
| `workbench/desktop.py` | 63 | `profile` |
| `workbench/desktop.py` | 64 | `host` |
| `workbench/desktop.py` | 68 | `host` |
| `workbench/desktop.py` | 75 | `line` |
| `workbench/desktop.py` | 90 | `main(argv)` |
| `workbench/desktop.py` | 92 | `parser` |
| `workbench/desktop.py` | 109 | `args` |
| `workbench/desktop.py` | 113 | `metadata` |
| `workbench/desktop.py` | 118 | `root` |
| `workbench/desktop.py` | 121 | `versions` |
| `workbench/desktop.py` | 126 | `directory` |
| `workbench/desktop.py` | 134 | `root` |
| `workbench/desktop.py` | 135 | `window` |
| `workbench/desktop_host.py` | 18 | `OwnedServer(class)` |
| `workbench/desktop_host.py` | 21 | `__init__(self, config, ready, record)` |
| `workbench/desktop_host.py` | 27 | `startup(self, sockets)` |
| `workbench/desktop_host.py` | 36 | `Host(class)` |
| `workbench/desktop_host.py` | 39 | `__init__(self, profile, metadata)` |
| `workbench/desktop_host.py` | 54 | `app` |
| `workbench/desktop_host.py` | 56 | `config` |
| `workbench/desktop_host.py` | 76 | `_run(self)` |
| `workbench/desktop_host.py` | 89 | `start(self, timeout)` |
| `workbench/desktop_host.py` | 97 | `stop(self, timeout)` |
| `workbench/desktop_profile.py` | 18 | `PRODUCT` |
| `workbench/desktop_profile.py` | 19 | `ROLES` |
| `workbench/desktop_profile.py` | 20 | `FIRST_ROLE` |
| `workbench/desktop_profile.py` | 23 | `default_directory()` |
| `workbench/desktop_profile.py` | 26 | `base` |
| `workbench/desktop_profile.py` | 28 | `base` |
| `workbench/desktop_profile.py` | 30 | `base` |
| `workbench/desktop_profile.py` | 36 | `read_marker(path)` |
| `workbench/desktop_profile.py` | 38 | `descriptor` |
| `workbench/desktop_profile.py` | 39 | `stream` |
| `workbench/desktop_profile.py` | 40 | `info` |
| `workbench/desktop_profile.py` | 43 | `raw` |
| `workbench/desktop_profile.py` | 46 | `value` |
| `workbench/desktop_profile.py` | 59 | `Profile(class)` |
| `workbench/desktop_profile.py` | 62 | `__init__(self, directory)` |
| `workbench/desktop_profile.py` | 64 | `directory` |
| `workbench/desktop_profile.py` | 68 | `marker` |
| `workbench/desktop_profile.py` | 74 | `stream` |
| `workbench/desktop_profile.py` | 76 | `metadata` |
| `workbench/desktop_profile.py` | 78 | `namespace` |
| `workbench/desktop_profile.py` | 80 | `lock` |
| `workbench/desktop_profile.py` | 96 | `database` |
| `workbench/desktop_profile.py` | 106 | `count_users(self)` |
| `workbench/desktop_profile.py` | 108 | `database` |
| `workbench/desktop_profile.py` | 111 | `create_account(self, username, password, confirmation, role)` |
| `workbench/desktop_profile.py` | 121 | `close(self)` |
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
| `workbench/owner_window.py` | 19 | `OwnerWindow(class)` |
| `workbench/owner_window.py` | 22 | `__init__(self, root, directory, metadata)` |
| `workbench/owner_window.py` | 42 | `shell` |
| `workbench/owner_window.py` | 45 | `actions` |
| `workbench/owner_window.py` | 53 | `content` |
| `workbench/owner_window.py` | 56 | `scrollbar` |
| `workbench/owner_window.py` | 60 | `body` |
| `workbench/owner_window.py` | 61 | `item` |
| `workbench/owner_window.py` | 82 | `location` |
| `workbench/owner_window.py` | 100 | `account` |
| `workbench/owner_window.py` | 110 | `caption` |
| `workbench/owner_window.py` | 110 | `index` |
| `workbench/owner_window.py` | 110 | `secret` |
| `workbench/owner_window.py` | 110 | `variable` |
| `workbench/owner_window.py` | 119 | `entry` |
| `workbench/owner_window.py` | 142 | `choose_directory(self)` |
| `workbench/owner_window.py` | 144 | `selected` |
| `workbench/owner_window.py` | 150 | `open_profile(self)` |
| `workbench/owner_window.py` | 156 | `control` |
| `workbench/owner_window.py` | 173 | `create_account(self)` |
| `workbench/owner_window.py` | 195 | `start_host(self)` |
| `workbench/owner_window.py` | 207 | `open_browser(self)` |
| `workbench/owner_window.py` | 212 | `quit(self)` |
| `workbench/owner_window.py` | 222 | `stop(self)` |
| `workbench/profile_paths.py` | 13 | `alias(info)` |
| `workbench/profile_paths.py` | 20 | `member(path)` |
| `workbench/profile_paths.py` | 23 | `info` |
| `workbench/profile_paths.py` | 26 | `expected` |
| `workbench/profile_paths.py` | 32 | `admitted_directory(path)` |
| `workbench/profile_paths.py` | 34 | `path` |
| `workbench/profile_paths.py` | 37 | `ancestor` |
| `workbench/profile_paths.py` | 40 | `executable_root` |
| `workbench/profile_paths.py` | 41 | `roots` |
| `workbench/profile_paths.py` | 42 | `parent` |
| `workbench/profile_paths.py` | 43 | `root` |
| `workbench/profile_paths.py` | 48 | `workspace_members(directory)` |
| `workbench/profile_paths.py` | 50 | `name` |
| `workbench/profile_paths.py` | 63 | `open_member(path, flags)` |
| `workbench/profile_paths.py` | 65 | `prior` |
| `workbench/profile_paths.py` | 66 | `flags` |
| `workbench/profile_paths.py` | 72 | `flags` |
| `workbench/profile_paths.py` | 73 | `descriptor` |
| `workbench/profile_paths.py` | 75 | `opened` |
| `workbench/runtime_gui.py` | 7 | `inspect_tk(root, metadata)` |
| `workbench/runtime_gui.py` | 9 | `versions` |
| `workbench/runtime_gui.py` | 13 | `value` |
| `workbench/runtime_gui.py` | 16 | `name` |
| `workbench/runtime_gui.py` | 16 | `value` |
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
| `ui/src/env.d.ts` | 2 | `__APP_VERSION__` |
| `ui/src/import_file.test.ts` | 11 | `value` |
| `ui/src/import_file.test.ts` | 23 | `text` |
| `ui/src/import_file.test.ts` | 34 | `incorrectMetadata` |
| `ui/src/import_file.ts` | 2 | `MAX_IMPORT_BYTES` |
| `ui/src/import_file.ts` | 5 | `objectFromText` |
| `ui/src/import_file.ts` | 5 | `text` |
| `ui/src/import_file.ts` | 8 | `value` |
| `ui/src/import_file.ts` | 11 | `stack` |
| `ui/src/import_file.ts` | 12 | `visited` |
| `ui/src/import_file.ts` | 15 | `[node, depth]` |
| `ui/src/import_file.ts` | 21 | `child` |
| `ui/src/import_file.ts` | 27 | `readObjectFile` |
| `ui/src/import_file.ts` | 28 | `file` |
| `ui/src/import_file.ts` | 32 | `bytes` |
| `ui/src/main.ts` | 11 | `User` |
| `ui/src/main.ts` | 16 | `Finding` |
| `ui/src/main.ts` | 21 | `Asset` |
| `ui/src/main.ts` | 32 | `PartResult` |
| `ui/src/main.ts` | 41 | `AircraftResult` |
| `ui/src/main.ts` | 47 | `Policy` |
| `ui/src/main.ts` | 51 | `State` |
| `ui/src/main.ts` | 79 | `Dashboard` |
| `ui/src/main.ts` | 86 | `Report` |
| `ui/src/main.ts` | 98 | `ApiError` |
| `ui/src/main.ts` | 100 | `message` |
| `ui/src/main.ts` | 101 | `status` |
| `ui/src/main.ts` | 106 | `user` |
| `ui/src/main.ts` | 107 | `dashboard` |
| `ui/src/main.ts` | 108 | `assessment` |
| `ui/src/main.ts` | 109 | `selectedAircraft` |
| `ui/src/main.ts` | 110 | `selectedComponent` |
| `ui/src/main.ts` | 111 | `epoch` |
| `ui/src/main.ts` | 112 | `busy` |
| `ui/src/main.ts` | 113 | `logoutPending` |
| `ui/src/main.ts` | 114 | `pendingUsage` |
| `ui/src/main.ts` | 115 | `Impact` |
| `ui/src/main.ts` | 134 | `impact` |
| `ui/src/main.ts` | 135 | `impactRevision` |
| `ui/src/main.ts` | 136 | `previewPolicy` |
| `ui/src/main.ts` | 140 | `downloadImpact` |
| `ui/src/main.ts` | 145 | `impactOutput` |
| `ui/src/main.ts` | 154 | `clearImpact` |
| `ui/src/main.ts` | 160 | `id` |
| `ui/src/main.ts` | 169 | `importPolicy` |
| `ui/src/main.ts` | 169 | `file` |
| `ui/src/main.ts` | 172 | `requested` |
| `ui/src/main.ts` | 173 | `generation` |
| `ui/src/main.ts` | 176 | `policy` |
| `ui/src/main.ts` | 185 | `formatted` |
| `ui/src/main.ts` | 193 | `error` |
| `ui/src/main.ts` | 201 | `event` |
| `ui/src/main.ts` | 202 | `input` |
| `ui/src/main.ts` | 203 | `file` |
| `ui/src/main.ts` | 211 | `policy` |
| `ui/src/main.ts` | 212 | `url` |
| `ui/src/main.ts` | 215 | `link` |
| `ui/src/main.ts` | 220 | `error` |
| `ui/src/main.ts` | 232 | `requested` |
| `ui/src/main.ts` | 233 | `result` |
| `ui/src/main.ts` | 246 | `heading` |
| `ui/src/main.ts` | 248 | `notice` |
| `ui/src/main.ts` | 251 | `list` |
| `ui/src/main.ts` | 252 | `row` |
| `ui/src/main.ts` | 253 | `item` |
| `ui/src/main.ts` | 257 | `row` |
| `ui/src/main.ts` | 258 | `item` |
| `ui/src/main.ts` | 259 | `finding` |
| `ui/src/main.ts` | 266 | `url` |
| `ui/src/main.ts` | 269 | `link` |
| `ui/src/main.ts` | 276 | `el` |
| `ui/src/main.ts` | 276 | `id` |
| `ui/src/main.ts` | 280 | `value` |
| `ui/src/main.ts` | 280 | `id` |
| `ui/src/main.ts` | 284 | `text` |
| `ui/src/main.ts` | 284 | `id` |
| `ui/src/main.ts` | 284 | `content` |
| `ui/src/main.ts` | 288 | `buttons` |
| `ui/src/main.ts` | 290 | `id` |
| `ui/src/main.ts` | 292 | `button` |
| `ui/src/main.ts` | 293 | `roles` |
| `ui/src/main.ts` | 302 | `api` |
| `ui/src/main.ts` | 302 | `path` |
| `ui/src/main.ts` | 302 | `body` |
| `ui/src/main.ts` | 303 | `generation` |
| `ui/src/main.ts` | 304 | `response` |
| `ui/src/main.ts` | 315 | `result` |
| `ui/src/main.ts` | 326 | `task` |
| `ui/src/main.ts` | 326 | `action` |
| `ui/src/main.ts` | 328 | `generation` |
| `ui/src/main.ts` | 336 | `error` |
| `ui/src/main.ts` | 344 | `reset` |
| `ui/src/main.ts` | 351 | `id` |
| `ui/src/main.ts` | 353 | `id` |
| `ui/src/main.ts` | 369 | `area` |
| `ui/src/main.ts` | 371 | `id` |
| `ui/src/main.ts` | 388 | `options` |
| `ui/src/main.ts` | 389 | `id` |
| `ui/src/main.ts` | 390 | `entries` |
| `ui/src/main.ts` | 391 | `selection` |
| `ui/src/main.ts` | 393 | `select` |
| `ui/src/main.ts` | 394 | `previous` |
| `ui/src/main.ts` | 396 | `[key, label]` |
| `ui/src/main.ts` | 397 | `option` |
| `ui/src/main.ts` | 402 | `[key]` |
| `ui/src/main.ts` | 405 | `findings` |
| `ui/src/main.ts` | 405 | `id` |
| `ui/src/main.ts` | 405 | `entries` |
| `ui/src/main.ts` | 406 | `root` |
| `ui/src/main.ts` | 408 | `finding` |
| `ui/src/main.ts` | 409 | `item` |
| `ui/src/main.ts` | 416 | `render` |
| `ui/src/main.ts` | 416 | `next` |
| `ui/src/main.ts` | 419 | `state` |
| `ui/src/main.ts` | 420 | `asset` |
| `ui/src/main.ts` | 422 | `part` |
| `ui/src/main.ts` | 424 | `metrics` |
| `ui/src/main.ts` | 426 | `status` |
| `ui/src/main.ts` | 432 | `div` |
| `ui/src/main.ts` | 434 | `count` |
| `ui/src/main.ts` | 436 | `asset` |
| `ui/src/main.ts` | 438 | `label` |
| `ui/src/main.ts` | 443 | `policy` |
| `ui/src/main.ts` | 444 | `record` |
| `ui/src/main.ts` | 489 | `part` |
| `ui/src/main.ts` | 494 | `part` |
| `ui/src/main.ts` | 503 | `d` |
| `ui/src/main.ts` | 503 | `work` |
| `ui/src/main.ts` | 505 | `d` |
| `ui/src/main.ts` | 513 | `work` |
| `ui/src/main.ts` | 514 | `work` |
| `ui/src/main.ts` | 523 | `record` |
| `ui/src/main.ts` | 532 | `defects` |
| `ui/src/main.ts` | 534 | `defect` |
| `ui/src/main.ts` | 534 | `entry` |
| `ui/src/main.ts` | 535 | `p` |
| `ui/src/main.ts` | 542 | `notice` |
| `ui/src/main.ts` | 560 | `roster` |
| `ui/src/main.ts` | 561 | `root` |
| `ui/src/main.ts` | 564 | `asset` |
| `ui/src/main.ts` | 565 | `result` |
| `ui/src/main.ts` | 566 | `item` |
| `ui/src/main.ts` | 573 | `button` |
| `ui/src/main.ts` | 586 | `aircraftDesk` |
| `ui/src/main.ts` | 588 | `asset` |
| `ui/src/main.ts` | 589 | `item` |
| `ui/src/main.ts` | 591 | `result` |
| `ui/src/main.ts` | 592 | `item` |
| `ui/src/main.ts` | 609 | `policy` |
| `ui/src/main.ts` | 610 | `record` |
| `ui/src/main.ts` | 612 | `profile` |
| `ui/src/main.ts` | 612 | `entry` |
| `ui/src/main.ts` | 615 | `slot` |
| `ui/src/main.ts` | 621 | `slot` |
| `ui/src/main.ts` | 622 | `row` |
| `ui/src/main.ts` | 623 | `part` |
| `ui/src/main.ts` | 624 | `entry` |
| `ui/src/main.ts` | 626 | `status` |
| `ui/src/main.ts` | 627 | `entry` |
| `ui/src/main.ts` | 629 | `content` |
| `ui/src/main.ts` | 637 | `cell` |
| `ui/src/main.ts` | 646 | `componentDesk` |
| `ui/src/main.ts` | 648 | `part` |
| `ui/src/main.ts` | 649 | `entry` |
| `ui/src/main.ts` | 651 | `result` |
| `ui/src/main.ts` | 652 | `entry` |
| `ui/src/main.ts` | 664 | `cumulative` |
| `ui/src/main.ts` | 665 | `values` |
| `ui/src/main.ts` | 666 | `record` |
| `ui/src/main.ts` | 671 | `chart` |
| `ui/src/main.ts` | 673 | `line` |
| `ui/src/main.ts` | 684 | `refresh` |
| `ui/src/main.ts` | 690 | `mutate` |
| `ui/src/main.ts` | 691 | `path` |
| `ui/src/main.ts` | 692 | `fields` |
| `ui/src/main.ts` | 703 | `showReport` |
| `ui/src/main.ts` | 703 | `report` |
| `ui/src/main.ts` | 719 | `event` |
| `ui/src/main.ts` | 735 | `csrf` |
| `ui/src/main.ts` | 745 | `response` |
| `ui/src/main.ts` | 771 | `sendUsage` |
| `ui/src/main.ts` | 774 | `next` |
| `ui/src/main.ts` | 784 | `error` |
| `ui/src/main.ts` | 791 | `event` |
| `ui/src/main.ts` | 811 | `event` |
| `ui/src/main.ts` | 815 | `report` |
| `ui/src/main.ts` | 828 | `id` |
| `ui/src/main.ts` | 831 | `event` |
| `ui/src/main.ts` | 842 | `event` |
| `ui/src/main.ts` | 853 | `event` |
| `ui/src/main.ts` | 856 | `battery` |
| `ui/src/main.ts` | 857 | `part` |
| `ui/src/main.ts` | 872 | `event` |
| `ui/src/main.ts` | 882 | `event` |
| `ui/src/main.ts` | 891 | `event` |
| `ui/src/main.ts` | 909 | `event` |
| `ui/src/main.ts` | 915 | `event` |
| `ui/src/main.ts` | 921 | `event` |
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
| `tests/browser/import.spec.ts` | 7 | `Window` |
| `tests/browser/import.spec.ts` | 14 | `login` |
| `tests/browser/import.spec.ts` | 14 | `page` |
| `tests/browser/import.spec.ts` | 14 | `role` |
| `tests/browser/import.spec.ts` | 15 | `directory` |
| `tests/browser/import.spec.ts` | 18 | `account` |
| `tests/browser/import.spec.ts` | 29 | `{ page, }` |
| `tests/browser/import.spec.ts` | 33 | `original` |
| `tests/browser/import.spec.ts` | 35 | `draft` |
| `tests/browser/import.spec.ts` | 52 | `after` |
| `tests/browser/import.spec.ts` | 53 | `key` |
| `tests/browser/import.spec.ts` | 55 | `pending` |
| `tests/browser/import.spec.ts` | 57 | `file` |
| `tests/browser/import.spec.ts` | 60 | `retained` |
| `tests/browser/import.spec.ts` | 61 | `buffer` |
| `tests/browser/import.spec.ts` | 80 | `{ page, }` |
| `tests/browser/import.spec.ts` | 86 | `original` |
| `tests/browser/import.spec.ts` | 90 | `resolve` |
| `tests/browser/import.spec.ts` | 90 | `reject` |
| `tests/browser/import.spec.ts` | 97 | `before` |
| `tests/browser/import.spec.ts` | 98 | `older` |
| `tests/browser/import.spec.ts` | 99 | `newer` |
| `tests/browser/import.spec.ts` | 100 | `input` |
| `tests/browser/import.spec.ts` | 101 | `hold` |
| `tests/browser/import.spec.ts` | 138 | `{ page, }` |
| `tests/browser/import.spec.ts` | 142 | `original` |
| `tests/browser/import.spec.ts` | 143 | `retained` |
| `tests/browser/import.spec.ts` | 153 | `after` |
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
| `tests/browser/workspace.spec.ts` | 304 | `{ page, }` |
| `tests/browser/workspace.spec.ts` | 307 | `release` |
| `tests/browser/workspace.spec.ts` | 308 | `observed` |
| `tests/browser/workspace.spec.ts` | 309 | `hold` |
| `tests/browser/workspace.spec.ts` | 309 | `resolve` |
| `tests/browser/workspace.spec.ts` | 312 | `responseReady` |
| `tests/browser/workspace.spec.ts` | 312 | `resolve` |
| `tests/browser/workspace.spec.ts` | 315 | `route` |
| `tests/browser/workspace.spec.ts` | 316 | `response` |
| `tools/browser_checks.mjs` | 8 | `project` |
| `tools/browser_checks.mjs` | 9 | `result` |
| `tools/native_feature_smoke.mjs` | 9 | `[base, output]` |
| `tools/native_feature_smoke.mjs` | 11 | `origin` |
| `tools/native_feature_smoke.mjs` | 12 | `browser` |
| `tools/native_feature_smoke.mjs` | 13 | `context` |
| `tools/native_feature_smoke.mjs` | 18 | `page` |
| `tools/native_feature_smoke.mjs` | 19 | `errors` |
| `tools/native_feature_smoke.mjs` | 20 | `external` |
| `tools/native_feature_smoke.mjs` | 21 | `error` |
| `tools/native_feature_smoke.mjs` | 22 | `request` |
| `tools/native_feature_smoke.mjs` | 31 | `login` |
| `tools/native_feature_smoke.mjs` | 31 | `role` |
| `tools/native_feature_smoke.mjs` | 43 | `ready` |
| `tools/native_feature_smoke.mjs` | 48 | `signOut` |
| `tools/native_feature_smoke.mjs` | 49 | `response` |
| `tools/native_feature_smoke.mjs` | 50 | `response` |
| `tools/native_feature_smoke.mjs` | 62 | `download` |
| `tools/native_feature_smoke.mjs` | 62 | `locator` |
| `tools/native_feature_smoke.mjs` | 63 | `pending` |
| `tools/native_feature_smoke.mjs` | 65 | `file` |
| `tools/native_feature_smoke.mjs` | 71 | `canonical` |
| `tools/native_feature_smoke.mjs` | 71 | `value` |
| `tools/native_feature_smoke.mjs` | 78 | `key` |
| `tools/native_feature_smoke.mjs` | 86 | `canonicalPolicy` |
| `tools/native_feature_smoke.mjs` | 86 | `value` |
| `tools/native_feature_smoke.mjs` | 87 | `floatFields` |
| `tools/native_feature_smoke.mjs` | 95 | `key` |
| `tools/native_feature_smoke.mjs` | 96 | `item` |
| `tools/native_feature_smoke.mjs` | 97 | `encoded` |
| `tools/native_feature_smoke.mjs` | 113 | `original` |
| `tools/native_feature_smoke.mjs` | 119 | `draft` |
| `tools/native_feature_smoke.mjs` | 121 | `battery` |
| `tools/native_feature_smoke.mjs` | 121 | `limit` |
| `tools/native_feature_smoke.mjs` | 140 | `impact` |
| `tools/native_feature_smoke.mjs` | 161 | `change` |
| `tools/native_feature_smoke.mjs` | 162 | `row` |
| `tools/native_feature_smoke.mjs` | 169 | `finding` |
| `tools/native_feature_smoke.mjs` | 175 | `after` |
| `tools/native_feature_smoke.mjs` | 178 | `key` |
| `tools/native_feature_smoke.mjs` | 191 | `beforeInvalid` |
| `tools/native_feature_smoke.mjs` | 213 | `used` |
| `tools/native_feature_smoke.mjs` | 218 | `part` |
| `tools/native_feature_smoke.mjs` | 223 | `report` |
| `tools/native_feature_smoke.mjs` | 248 | `repaired` |
| `tools/native_feature_smoke.mjs` | 252 | `defect` |
| `tools/native_feature_smoke.mjs` | 269 | `defect` |
| `tools/native_feature_smoke.mjs` | 273 | `asset` |
| `tools/native_feature_smoke.mjs` | 278 | `part` |
| `tools/native_feature_smoke.mjs` | 312 | `cookies` |
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
| `vite.config.ts` | 4 | `version` |
| `playwright.config.ts` | 5 | `directory` |
| `playwright.config.ts` | 8 | `local` |
| `playwright.config.ts` | 12 | `python` |
