# Historisk dokumentutdrag

Kilde: `/home/tombonator3000t/.codex/.chatgpt-projects/g-p-6aa25fc827e88191822a16151401213b/sources/OPPRINNELIG_SAMTALE.md`

Originale linjer 2587–2640; bevart 23. september 2026. Opplysningene nedenfor er historiske kildenotater, ikke en ny verifikasjon.

---

# Hva med faktisk direkte kontroll inne i Unity Editor?

Det finnes en enda mer direkte vei:

## Unity MCP

Det finnes flere aktive community-prosjekter som eksponerer Unity Editor gjennom MCP, blant annet:

[CoplayDev/unity-mcp](https://github.com/CoplayDev/unity-mcp?utm_source=chatgpt.com)

og

[CoderGamester/mcp-unity](https://github.com/CoderGamester/mcp-unity?utm_source=chatgpt.com)

Det betyr i prinsippet at en agent kan be Unity:

```text
create GameObject
move object
create material
assign material
open scene
save scene
enter play mode
read console
take screenshot
create prefab
modify component
```

uten at vi skriver en egen Unity Editor-scriptfil hver gang.

---

# Blender har det samme

Det finnes et ganske kjent Blender MCP-prosjekt:

[ahujasid/blender-mcp](https://github.com/ahujasid/blender-mcp?utm_source=chatgpt.com)

Det lar en agent styre Blender gjennom verktøykall:

```text
create mesh
modify mesh
set material
move camera
set lighting
render
inspect scene
import/export
run Python
```

