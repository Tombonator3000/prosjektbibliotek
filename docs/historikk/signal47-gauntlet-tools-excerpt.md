# Historisk dokumentutdrag

Kilde: `/home/tombonator3000t/.codex/.chatgpt-projects/g-p-6aa25fc827e88191822a16151401213b/sources/SAMLET_DOKUMENTASJON.md`

Originale linjer 229–235; bevart 23. september 2026. Gauntlet04-kilden er fra prosjektets referansekopi ved 79c0742. Dette beskriver den daværende økten, ikke dagens verktøystatus.

---

## Stack and capability evidence

| Responsibility | Tool/version and reason | Input → output / handoff | Availability |
|---|---|---|---|
| Editable game source and scene | Unity 6000.3.22f1, URP 17.3.0, Input System 1.20.0; retain working native 3D stack | Unity scripts/assets → generated SARO_Prologue → Linux player | VERIFIED WORKING: editor CLI, project load, compile, scene/player and logs tested separately in prior passes |
| Editable geometry | Blender 4.5.13 LTS; existing reproducible source jobs | Blender source script/.blend → FBX/.meta → Unity import and runtime | VERIFIED WORKING CLI path; prior nine-family export and current lamp inspection documented in ART_PASS_01 and ASSET_PASS_03 |
| Optional Blender MCP | ahujasid/blender-mcp, third-party | Host MCP → addon → Blender scene | UNAVAILABLE in this session; current maintainer setup inspected. Executed scripts remain the selected alternative; no MCP connection is claimed |
