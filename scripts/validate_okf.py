import json
import os
import re
import sys
import urllib.parse

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def check_json_schemas():
    schema_dir = os.path.join(REPO_ROOT, "schema")
    errors = []
    count = 0
    for fname in sorted(os.listdir(schema_dir)):
        if not fname.endswith(".json"):
            continue
        count += 1
        fpath = os.path.join(schema_dir, fname)
        try:
            with open(fpath, "r", encoding="utf-8") as f:
                data = json.load(f)
            for req_key in ("$schema", "title", "type", "properties"):
                if req_key not in data:
                    errors.append(f"[SCHEMA] {fname}: falta clave obligatoria '{req_key}'")
        except Exception as e:
            errors.append(f"[SCHEMA] {fname}: JSON inválido ({e})")
    return count, errors


def check_skills():
    skills_dir = os.path.join(REPO_ROOT, ".agents", "skills")
    errors = []
    count = 0
    if not os.path.isdir(skills_dir):
        return 0, ["[SKILLS] No existe el directorio .agents/skills"]
    for entry in sorted(os.listdir(skills_dir)):
        skill_md = os.path.join(skills_dir, entry, "SKILL.md")
        if os.path.isfile(skill_md):
            count += 1
            with open(skill_md, "r", encoding="utf-8") as f:
                content = f.read()
            if not content.startswith("---"):
                errors.append(f"[SKILL] {entry}/SKILL.md: falta frontmatter YAML")
            if "name:" not in content or "description:" not in content:
                errors.append(f"[SKILL] {entry}/SKILL.md: falta 'name' o 'description' en frontmatter")
    return count, errors


def check_markdown_links():
    link_pattern = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
    errors = []
    checked_files = 0
    checked_links = 0

    for root, dirs, files in os.walk(REPO_ROOT):
        dirs[:] = [d for d in dirs if d not in (".git", "__pycache__", "venv", ".venv")]
        for fname in files:
            if not fname.endswith(".md"):
                continue
            checked_files += 1
            fpath = os.path.join(root, fname)
            with open(fpath, "r", encoding="utf-8") as f:
                content = f.read()
            # Ignorar bloques de código cercados para evitar falsos positivos en plantillas
            content_no_code = re.sub(r"```[\s\S]*?```", "", content)
            for match in link_pattern.finditer(content_no_code):
                target = match.group(1).strip()
                if (
                    target.startswith("http://")
                    or target.startswith("https://")
                    or target.startswith("#")
                    or target.startswith("mailto:")
                ):
                    continue
                target_path = urllib.parse.unquote(target.split("#")[0])
                if not target_path:
                    continue
                checked_links += 1
                resolved = os.path.normpath(os.path.join(root, target_path))
                if not os.path.exists(resolved):
                    rel_source = os.path.relpath(fpath, REPO_ROOT)
                    errors.append(f"[LINK ROTO] {rel_source} -> '{target}'")
    return checked_files, checked_links, errors


def check_plan_evalua_isolation():
    errors = []
    chk_path = os.path.join(
        REPO_ROOT, "docs", "checklists_supervision_programaciones_infantil_fp_ere.md"
    )
    if not os.path.isfile(chk_path):
        errors.append("[SUPERVISIÓN] Falta docs/checklists_supervision_programaciones_infantil_fp_ere.md")
    else:
        with open(chk_path, "r", encoding="utf-8") as f:
            text = f.read()
        for forbidden in ("PLAN EVALÚA FP", "PLAN EVALÚA ERE"):
            if forbidden in text.upper():
                errors.append(f"[AISLAMIENTO PLAN EVALÚA] Se encontró '{forbidden}' en el compendio de checklists")
    return errors


def main():
    print("=== AUDITORÍA AUTOMÁTICA DEL REPOSITORIO OPENDIDACTIA (OKF) ===")
    s_count, s_err = check_json_schemas()
    k_count, k_err = check_skills()
    m_files, m_links, m_err = check_markdown_links()
    p_err = check_plan_evalua_isolation()

    print(f"✔ Esquemas JSON validados:      {s_count}")
    print(f"✔ Habilidades de agente (.agents): {k_count}")
    print(f"✔ Archivos Markdown auditados:  {m_files} ({m_links} enlaces internos verificados)")
    print(f"✔ Aislamiento Plan Evalúa:      {'OK' if not p_err else 'ERROR'}")

    all_errors = s_err + k_err + m_err + p_err
    if all_errors:
        print("\n❌ INCIDENCIAS DETECTADAS:")
        for err in all_errors:
            print("  -", err)
        sys.exit(1)
    else:
        print("\n✅ ESTADO: 0 incidencias. El repositorio cumple íntegramente el estándar OKF.")


if __name__ == "__main__":
    main()
