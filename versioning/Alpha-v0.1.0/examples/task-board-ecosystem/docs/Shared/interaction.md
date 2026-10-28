# Interaction mappings — L4

This is the canonical channel projection for the **local demonstration**. Physical placement in `Shared/` does not change its L4 responsibility. The domain contracts and scenarios are referenced from [Minerva L2](../L2_MinervaBlueprints/blueprint.yaml); the companion Vulcan L3 documentation (`docs/L3_Vulcan/README.md` in that ecosystem) records how the concrete channels are composed and run.

| Stimulus / public operation | Prepared core case | Input representation | Channel result |
| --- | --- | --- | --- |
| Browser Create task / `POST /tasks` | `UC-TASK-001`, `UseCase_CreateTask.createTask` | JSON object containing only `title`; server-resolved actor context | HTTP 201 with task projection |
| Browser Refresh / `GET /tasks` | `UC-TASK-002`, `UseCase_ListTasks.listTasks` | No body; server-resolved actor context | HTTP 200 `{ "tasks": [...] }` |
| Browser Complete / `POST /tasks/{task_id}/complete` | `UC-TASK-003`, `UseCase_CompleteTask.completeTask` | Encoded path identifier and empty JSON object | HTTP 200 with task projection |
| CLI `create --title TEXT` | `UC-TASK-001` | Argument string and token resolved by composition | Task projection on stdout, exit 0 |
| CLI `list` | `UC-TASK-002` | Token resolved by composition | Tasks envelope on stdout, exit 0 |
| CLI `complete TASK_ID` | `UC-TASK-003` | Argument string and resolved context | Task projection on stdout, exit 0 |
| LegacyReports `GET /report` or `/` / CLI `report` | Existing `create_report` function, not an invented Vulcan case | Configured TaskBoard upstream URL and reader token | Counts: `total`, `completed`, `pending` |

A task projection has primitive fields `task_id` (string), `title` (string) and `completed` (boolean). The channel serializes an entity; it does not expose the value object, database connection, composition object or caller-supplied permissions. The browser code uses `textContent` for task titles and dispatches the listed HTTP operations. It never reads SQLite.

TaskBoard HTTP maps forbidden to 403, invalid body/domain input to 422, missing task or unknown route to 404, and caught storage access failure to 503. Request bodies must be JSON objects, at most 8192 bytes by the declared content length. Creation accepts exactly `title`; completion accepts no fields. Channel-shape validation may reject a malformed request before actor authorization; all domain effects still require the case's authorization. The scope is local development, with Python's standard-library HTTP server.

TaskBoard CLI domain outcomes use error JSON on stderr with exit 3 (forbidden), 2 (invalid data), 4 (missing) or 5 (storage failure). Parser/configuration errors may use conventional usage text with exit 2. LegacyReports reports `upstream_unavailable_or_invalid` as HTTP 502 or CLI exit 5; its CLI error JSON is on stdout to preserve the existing procedural interface.

`GET /health` is operational metadata, not a domain case. It returns app identity, a readiness boolean and launch instance identity. Browser page `GET /` on TaskBoard is presentation, not an extra domain identity. Legacy report endpoints are unauthenticated **local** aggregate endpoints using a configured read identity upstream; remote exposure needs a separately specified access policy.

Channel behavior is exercised by `Test_Boundaries`; serving/reading the HTML is covered, while browser clicking/rendering is not. This material does not claim a complete reusable OAL L4 model.
